@echo off
cd /d "%~dp0"

:: Check for Admin privileges
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

:: If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto :runAsAdmin )

:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"
del "%temp%\getadmin.vbs"
exit /b

:runAsAdmin
echo Wait ...

setlocal

:: Set the description for the restore point
set DESCRIPTION="Pixel_backup"

:: Store the original registry value
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v SystemRestorePointCreationFrequency > nul 2>&1
if %ERRORLEVEL% == 0 (
    for /F "tokens=3" %%A in ('reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v SystemRestorePointCreationFrequency') do set ORIGINAL_FREQUENCY=%%A
) else (
    set ORIGINAL_FREQUENCY=1440
)

:: Set the registry to allow immediate restore point creation
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v SystemRestorePointCreationFrequency /t REG_DWORD /d 0 /f

:: Create the restore point using PowerShell
powershell.exe -Command "Checkpoint-Computer -Description %DESCRIPTION% -RestorePointType 'Modify_Settings'"

:: Log the state of services (running and stopped)
powershell.exe -Command "Get-Service | Select-Object Name, Status | Out-File -FilePath 'C:\ServiceStatus.txt'"

:: Log the list of deleted files and programs
powershell.exe -Command "Get-EventLog -LogName 'Application' -Newest 1000 | Where-Object { $_.EventID -eq 4104 } | Select-Object TimeGenerated, EntryType, Source, Message | Out-File -FilePath 'C:\DeletedItemsLog.txt'"

:: Restore the original registry value
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v SystemRestorePointCreationFrequency /t REG_DWORD /d %ORIGINAL_FREQUENCY% /f

endlocal

exit

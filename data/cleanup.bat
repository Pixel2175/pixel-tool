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

RD /S /Q %temp%
MKDIR %temp%
takeown /f "%temp%" /r /d y
takeown /f "C:\Windows\Temp" /r /d y
RD /S /Q C:\Windows\Temp
MKDIR C:\Windows\Temp
takeown /f "C:\Windows\Temp" /r /d y
takeown /f %temp% /r /d y

echo Cleaning user-specific TEMP files...
del /s /q %UserProfile%\AppData\Local\Temp\*.*
del *.log /a /s /q /f

net stop wuauserv
net stop UsoSvc
rd /s /q C:\Windows\SoftwareDistribution
md C:\Windows\SoftwareDistribution

echo Clearing Windows event logs...
for /f "tokens=*" %%G in ('wevtutil.exe el') do wevtutil.exe cl "%%G"

echo Cleaning Windows Error Reporting files...
del /s /q C:\ProgramData\Microsoft\Windows\WER\*.*

echo Cleaning system memory dump files...
del /s /q C:\Windows\MEMORY.DMP

echo Cleaning temporary internet files for all users...
for /d %%x in (C:\Users\*) do del /s /q "%%x\AppData\Local\Microsoft\Windows\INetCache\*.*"

echo Cleaning thumbnail cache...
del /s /q %UserProfile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_*.db

echo Cleaning font cache...
del /s /q %WinDir%\ServiceProfiles\LocalService\AppData\Local\FontCache\*.*

echo Cleaning DirectX shader cache...
del /s /q %LocalAppData%\D3DSCache\*.*

echo Cleaning Windows upgrade log files...
del /s /q C:\$Windows.~BT\Sources\Panther\*.*

echo Cleaning Microsoft Edge temporary files...
del /s /q "%LocalAppData%\Microsoft\Edge\User Data\Default\Code Cache\*.*"

echo Cleaning Windows Defender cache...
del /s /q "%ProgramData%\Microsoft\Windows Defender\Scans\History\Store\*.*"

echo Cleaning Windows Delivery Optimization files...
del /s /q C:\Windows\SoftwareDistribution\DeliveryOptimization\*.*

echo Cleaning Windows prefetch files...
del /s /q C:\Windows\Prefetch\*.*

echo Cleaning all user recent files...
for /d %%x in (C:\Users\*) do del /s /q "%%x\AppData\Roaming\Microsoft\Windows\Recent\*.*"

echo Cleaning Spotify cache...
del /s /q %LocalAppData%\Spotify\Storage\*.*

echo Cleaning temporary installation files...
del /s /q %UserProfile%\AppData\Local\Temp\*.tmp

echo Cleaning Windows Installer cache...
del /s /q %windir%\Installer\$PatchCache$\*.*

echo Cleaning IIS log files...
del /s /q C:\inetpub\logs\LogFiles\*.*

echo Cleaning Java cache...
del /s /q %LocalAppData%\Sun\Java\Deployment\cache\*.*

echo Cleaning OneDrive cache...
del /s /q %LocalAppData%\Microsoft\OneDrive\*.* /s /q

echo Cleaning TEMP files...
del /s /q %temp%\*.*

echo Cleaning Windows TEMP files...
del /s /q C:\Windows\Temp\*.*

echo Cleaning Prefetch files...
del /s /q C:\Windows\Prefetch\*.*

echo Cleaning browser cache files...
del /s /q "%LocalAppData%\Google\Chrome\User Data\Default\Cache\*.*"
del /s /q "%LocalAppData%\Mozilla\Firefox\Profiles\*.default-release\cache2\entries\*.*"

echo Cleaning update logs...
del /s /q C:\Windows\SoftwareDistribution\Download\*.*

echo Cleaning Recycle Bin files...
rd /s /q C:\$Recycle.Bin

echo Cleaning error report files...
del /s /q C:\ProgramData\Microsoft\Windows\WER\ReportQueue\*.*

echo Cleaning temporary update files...
del /s /q C:\Windows\Logs\WindowsUpdate\*.*

echo Cleaning temporary log files...
del /s /q C:\Windows\Temp\*.log

echo Cleaning system temporary files...
vssadmin delete shadows /for=c: /all /quiet
del /s /q C:\Windows\System32\LogFiles\WMI\*.*

echo Cleaning temporary internet files...
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8

echo Cleaning DNS cache...
ipconfig /flushdns

echo Cleaning clipboard...
echo off | clip

echo Cleaning virtual memory files...
del /s /q %systemdrive%\pagefile.sys

echo Cleaning recent files...
del /s /q %AppData%\Microsoft\Windows\Recent\*.*

echo Cleaning browser recycle bin files...
del /s /q "%LocalAppData%\Microsoft\Edge\User Data\Default\Cache\*.*"
del /s /q "%LocalAppData%\Opera Software\Opera Stable\Cache\*.*"

echo Cleaning TEMP files for installed programs...
del /s /q "%LocalAppData%\Temp\*.*"

echo Cleaning Downloads folder...
del /s /q %UserProfile%\Downloads\*.*

echo Cleaning previous update files...
dism /online /cleanup-image /startcomponentcleanup

echo Cleaning other system temporary files...
for /d %%x in (%systemroot%\Installer\$PatchCache$\*) do rd /s /q "%%x"

echo Cleaning process completed.
start "" "DiskCleaner.lnk"

exit


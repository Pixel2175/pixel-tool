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
echo Uninstalling 3D Builder...
wmic product where "Name='3D Builder'" call uninstall /nointeractive

echo Uninstalling Calculator...
wmic product where "Name='Calculator'" call uninstall /nointeractive

echo Uninstalling Cortana...
wmic product where "Name='Cortana'" call uninstall /nointeractive

echo Uninstalling Groove Music...
wmic product where "Name='Groove Music'" call uninstall /nointeractive

echo Uninstalling Mixed Reality Portal...
wmic product where "Name='Mixed Reality Portal'" call uninstall /nointeractive

echo Uninstalling Movies & TV...
wmic product where "Name='Movies & TV'" call uninstall /nointeractive

echo Uninstalling OneNote...
wmic product where "Name='OneNote'" call uninstall /nointeractive

echo Uninstalling Calendar and Mail...
wmic product where "Name='Calendar and Mail'" call uninstall /nointeractive

echo Uninstalling Feedback Hub...
wmic product where "Name='Feedback Hub'" call uninstall /nointeractive

echo Uninstalling Maps...
wmic product where "Name='Maps'" call uninstall /nointeractive

echo Uninstalling Mobile Plans...
wmic product where "Name='Mobile Plans'" call uninstall /nointeractive

echo Uninstalling News...
wmic product where "Name='News'" call uninstall /nointeractive

echo Uninstalling Paint 3D...
wmic product where "Name='Paint 3D'" call uninstall /nointeractive

echo Uninstalling Print 3D...
wmic product where "Name='Print 3D'" call uninstall /nointeractive

echo Uninstalling Solitaire...
wmic product where "Name='Solitaire'" call uninstall /nointeractive

echo Uninstalling Sticky Notes...
wmic product where "Name='Sticky Notes'" call uninstall /nointeractive

echo Uninstalling Voice Recorder...
wmic product where "Name='Voice Recorder'" call uninstall /nointeractive

echo Uninstalling Translator...
wmic product where "Name='Translator'" call uninstall /nointeractive

echo Uninstalling 3D Viewer...
wmic product where "Name='3D Viewer'" call uninstall /nointeractive

echo Uninstalling Alarms & Clock...
wmic product where "Name='Alarms & Clock'" call uninstall /nointeractive

echo Uninstalling Get Help...
wmic product where "Name='Get Help'" call uninstall /nointeractive

echo Uninstalling Messaging...
wmic product where "Name='Messaging'" call uninstall /nointeractive

echo Uninstalling Money...
wmic product where "Name='Money'" call uninstall /nointeractive

echo Uninstalling People...
wmic product where "Name='People'" call uninstall /nointeractive

echo Uninstalling Skype...
wmic product where "Name='Skype'" call uninstall /nointeractive

echo Uninstalling Sports...
wmic product where "Name='Sports'" call uninstall /nointeractive

echo Uninstalling Tips...
wmic product where "Name='Tips'" call uninstall /nointeractive

echo Uninstalling Weather...
wmic product where "Name='Weather'" call uninstall /nointeractive

echo Uninstalling Your Phone...
wmic product where "Name='Your Phone'" call uninstall /nointeractive

echo Uninstalling Camera...
wmic product where "Name='Camera'" call uninstall /nointeractive


echo Uninstallation complete.
pause

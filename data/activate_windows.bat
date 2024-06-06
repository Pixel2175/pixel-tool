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
echo Activating Windows...

slmgr /ipk VK7JG-NPHTM-C97JM-9MPGT-3V66T

slmgr /skms kms8.msguides.com

slmgr /ato


set "keys=TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 PVMJN-6DFY6-9CCP6-7BKTT-D3WVR 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH 3KHY7-WNT83-DGQKR-F7HPR-844BM W269N-WFGWX-YVC9B-4J6C9-T83GX MH37W-N47XK-V7XM9-C7227-GCQG9 NPPR9-FWDCX-D2C8J-H872K-2YT43 DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ WNMTR-4C88C-JK8YV-HQ7T2-76DF9 2F77B-TNFGY-69QQF-B8YKP-D69TJ DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ QFFDN-GRT3P-VKWWX-X7T3R-8B639 MNXKQ-WY2CT-JWBJ2-T68TQ-YBH2V 7TNX7-H36JG-QFF42-K4JYV-YY482 D3M8K-4YN49-89KYG-4F3DR-TVJW3 VPMWD-PVNRR-79WJ9-VVJQC-3YH2G D6RD9-D4N8T-RT9QX-YW6YT-FCWWJ 84NGF-MHBT6-FXBX8-QWJK7-DRR8H YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY VK7JG-NPHTM-C97JM-9MPGT-3V66T 2B87N-8KFHP-DKV6R-Y2C8J-PKCKT DXG7C-N36C4-C4HTG-X4T3X-2YV77 WYPNQ-8C467-V2W6J-TX4WX-WT2RQ 3NF4D-GF9GY-63VKH-QRC3V-7QW8P GJTYN-HDMQY-FRR76-HVGC7-QPF8P XGVPP-NMH47-7TTHJ-W3FW7-8HV2C NK96Y-D9CD8-W44CQ-R8YTK-DYJWX WGGHN-J84D6-QYCPR-T7PJ7-X766F"

for %%k in (%keys%) do (
    cscript //nologo %windir%\system32\slmgr.vbs /ipk %%k >nul 2>&1
    cscript //nologo %windir%\system32\slmgr.vbs /ato >nul 2>&1
    cscript //nologo %windir%\system32\slmgr.vbs /xpr >nul 2>&1
    if %errorlevel%==0 (
        echo Windows activation successful!
        exit
    )
)

echo Windows is not activated.
exit

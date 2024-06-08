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
:: Disable Making Touch Easier
reg add "HKEY_CURRENT_USER\Software\Microsoft\Wisp\Touch" /v "TouchMode_hold" /t REG_DWORD /d 0 /f

:: Disable Warning Sounds
reg add "HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default" /v "EmptyTrash" /t REG_SZ /d "" /f

:: Debloat Send To
reg add "HKEY_CLASSES_ROOT\*\shellex\ContextMenuHandlers\SendTo" /f

:: Disable Check Boxed
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "AutoCheckSelect" /t REG_DWORD /d 0 /f

:: Disable Gallery
reg add "HKEY_CLASSES_ROOT\SystemFileAssociations\image\ShellEx\ContextMenuHandlers" /f

:: Disable Network Navigation Pane
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "LaunchTo" /t REG_DWORD /d 0 /f

:: Disable Sharing Wizard
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "HideFileExt" /t REG_DWORD /d 0 /f

:: Disable Remote Assistance
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Remote Assistance" /v "fAllowToGetHelp" /t REG_DWORD /d 0 /f

:: Disable UAC Secure Desktop
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "PromptOnSecureDesktop" /t REG_DWORD /d 0 /f

:: Disable Aero Shake
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DisallowShaking" /t REG_DWORD /d 1 /f

:: Disable Low Disk Warning
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoLowDiskSpaceChecks" /t REG_DWORD /d 1 /f

:: Disable Menu Delay
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d 0 /f

:: Disable Nearby Sharing
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Sharing" /v "DisableAnimations" /t REG_DWORD /d 1 /f

:: Disable Network Location Wizard
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /v "NetworkLocationWizard" /t REG_SZ /d "rundll32 netplwiz.dll,LaunchWizardEx" /f

:: Disable Edge Swipe
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ImmersiveShell\EdgeUI" /v "DisableTLcorner" /t REG_DWORD /d 1 /f

:: Disable Startup Delay
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v "Startupdelayinmsec" /t REG_DWORD /d 0 /f

:: Disable WPBT
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "EnableFirstLogonAnimation" /t REG_DWORD /d 0 /f

:: Disable Cloud OptimizedContent
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

:: Disable Copilot
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

:: Disable Desktop Peek
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DisablePreviewDesktop" /t REG_DWORD /d 1 /f

:: Disable News and Interests
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Feeds" /v "ShellFeedsTaskbarViewMode" /t REG_DWORD /d 2 /f

:: Disable Table Mode
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ImmersiveShell" /v "TabletMode" /t REG_DWORD /d 0 /f

:: Disable Windows Chat
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ImmersiveShell" /v "Chat" /t REG_DWORD /d 0 /f

:: Disable Auto Reboot
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "NoAutoRebootWithLoggedOnUsers" /t REG_DWORD /d 1 /f

:: Disable Auto Updates
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "AUOptions" /t REG_DWORD /d 1 /f

:: Disable Delivery Optimization
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" /v "DODownloadMode" /t REG_DWORD /d 0 /f

:: Disable Feature Updates
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "DeferFeatureUpdates" /t REG_DWORD /d 1 /f

:: Disable Insider
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\PreviewBuilds" /v "AllowBuildPreview" /t REG_DWORD /d 0 /f

:: Disable MSRT Telemetry
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\MpEngine" /v "MpCloudBlockLevel" /t REG_DWORD /d 0 /f

:: Disable Nagging
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SilentInstalledAppsEnabled" /t REG_DWORD /d 0 /f

:: Disable Background Auto Login
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\UserSwitch" /v "Enabled" /t REG_DWORD /d 0 /f

:: Disable Mouse Acceleration
reg add "HKEY_CURRENT_USER\Control Panel\Mouse" /v "MouseSpeed" /t REG_SZ /d 0 /f

:: Disable Setting Tips
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

:: Disable Spell Checking
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DisableSpellchecking" /t REG_DWORD /d 1 /f

:: Disable Store Auto Updates
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore" /v "AutoDownload" /t REG_DWORD /d 2 /f

:: Disable Tips
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SystemPaneSuggestionsEnabled" /t REG_DWORD /d 0 /f

:: Disable Touch Keyboard Features
reg add "HKEY_CURRENT_USER\Software\Microsoft\TabletTip\1.7" /v "EnableSpringboard" /t REG_DWORD /d 0 /f

:: Disable Touch Visual Feedback
reg add "HKEY_CURRENT_USER\Software\Microsoft\Wisp\Touch" /v "ContactVisualFeedback" /t REG_DWORD /d 0 /f

:: Disable USB Issues Notifications
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\UsbFlags" /v "DisableOnSoftRemove" /t REG_DWORD /d 1 /f

:: Disable Win11 Setting Banner
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ShowInitialActivationDialog" /t REG_DWORD /d 0 /f

:: Disable Windows Feedback
reg add "HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules" /v "NumberOfSIUFInPeriod" /t REG_DWORD /d 0 /f

:: Disable Windows Spotlight
reg add "HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

:: Disable Activation Telemetry
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsActivationClient" /v "DisableWindowsActivationClient" /t REG_DWORD /d 1 /f

:: Disable CEIP
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CEIP" /v "Participation" /t REG_DWORD /d 0 /f

:: Disable Diagnostic Tracing
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f

:: Disable Dotnet Tracing
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetryDotnet" /t REG_DWORD /d 0 /f

:: Disable Input Telemetry
reg add "HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization" /v "RestrictImplicitInkCollection" /t REG_DWORD /d 1 /f

:: Disable Data Collection
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Privacy" /v "TailoredExperiencesWithDiagnosticDataEnabled" /t REG_DWORD /d 0 /f

:: Disable Suggest Ways to Finish Setup
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

:: Disable Message Cloud Sync
reg add "HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\SettingSync" /v "SyncOnlyWithAutoUpload" /t REG_DWORD /d 0 /f

:: Disable Advertising Info
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d 0 /f

:: Disable Bluetooth
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\bluetooth" /v "Value" /t REG_DWORD /d 0 /f

:: Disable Sync Provider Notifications
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\SyncHost" /v "EnableWNSNotifications" /t REG_DWORD /d 0 /f

:: Disable User Tracking
reg add "HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization" /v "RestrictImplicitTextCollection" /t REG_DWORD /d 1 /f

:: Disable Web Language List Access
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Languages" /v "PreferExternalManifest" /t REG_DWORD /d 1 /f

:: Disable Windows Error Reporting
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" /v "Disabled" /t REG_DWORD /d 1 /f

:: Disable MS Activity Upload
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync" /v "SyncOnlyWithAutoUpload" /t REG_DWORD /d 0 /f

:: Disable Activity Feed
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Feeds" /v "ShellFeedsTaskbarViewMode" /t REG_DWORD /d 2 /f

:: Disable Device Monitoring
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses" /v "Deny_All" /t REG_DWORD /d 1 /f

:: Disable Experimentation
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowExperimentation" /t REG_DWORD /d 0 /f

:: Disable Location Tracking
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" /v "DisableLocation" /t REG_DWORD /d 1 /f

:: Disable Lockscreen Camera
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Personalization" /v "NoLockScreenCamera" /t REG_DWORD /d 1 /f

:: Disable Online Speech Recognition
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Speech" /v "AllowOnlineSpeechRecognition" /t REG_DWORD /d 0 /f

:: Disable PCA
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Personalization" /v "NoAutoTrayNotify" /t REG_DWORD /d 1 /f

:: Disable Perf Track
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowPerfTrack" /t REG_DWORD /d 0 /f

:: Disable Privacy Experience
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Privacy" /v "EnablePrivacyTracking" /t REG_DWORD /d 0 /f

:: Disable RSOP Logging
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" /v "LoggingDisabled" /t REG_DWORD /d 1 /f

:: Disable Speech Auto Updates
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Speech_OneCore" /v "DataCollection" /t REG_DWORD /d 0 /f

:: Disable Tailored Experiences
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

:: Disable Paging
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "DisablePagingExecutive" /t REG_DWORD /d 1 /f

:: Disable Services Host Split
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "EnableSplit" /t REG_DWORD /d 0 /f

:: Disable Auto Folder Discovery
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Start_TrackProgs" /t REG_DWORD /d 0 /f

:: Disable Background Apps
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d 1 /f

:: Disable FTH
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\FTH" /v "Enabled" /t REG_DWORD /d 0 /f

:: Disable Game Bar
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\GameDVR" /v "AppCaptureEnabled" /t REG_DWORD /d 0 /f

:: Disable Reserved Storage
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ReserveManager" /v "ShippedWithReserves" /t REG_DWORD /d 0 /f

:: Disable Scheduled Tasks
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Schedule" /v "Start" /t REG_DWORD /d 4 /f

:: Disable Sleep Study
powercfg /h off

echo Uninstalling Meet Now...
start /wait powershell.exe -Command "Get-AppxPackage -Name Microsoft.MeetNow | Remove-AppxPackage -AllUsers"
echo Meet Now has been uninstalled.

rem Allow publishing of user Activities
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d 0 /f

rem Allow upload of user Activities
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d 0 /f

rem Enables activity Feed
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d 0 /f

rem Sync your settings
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync" /v "DisableSettingSync" /t REG_DWORD /d 1 /f

rem Use OneDrive for file storage
reg add "HKLM\Software\Policies\Microsoft\Windows\OneDrive" /v "DisableFileSync" /t REG_DWORD /d 1 /f

rem User data access
reg add "HKLM\Software\Policies\Microsoft\Windows\AppPrivacy" /v "LetAppsAccessAccountInfo" /t REG_DWORD /d 2 /f

rem User data storage
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "EnableDataCollection" /t REG_DWORD /d 0 /f

rem Messaging Services
reg add "HKLM\Software\Policies\Microsoft\Messaging" /v "AllowMessaging" /t REG_DWORD /d 0 /f

rem Windows Customer Experience Improvement program
reg add "HKLM\Software\Policies\Microsoft\SQMClient\Windows" /v "CEIPEnable" /t REG_DWORD /d 0 /f

rem Internet Explorer Customer Experience Improvement program
reg add "HKLM\Software\Policies\Microsoft\Internet Explorer\SQM" /v "Disable" /t REG_DWORD /d 1 /f

rem Windows Messenger Customer Experience Improvement program
reg add "HKLM\Software\Policies\Microsoft\Messenger" /v "CEIP" /t REG_DWORD /d 0 /f

rem Windows Error Reporting
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Error Reporting" /v "Disabled" /t REG_DWORD /d 1 /f

rem Steps Recorder
reg add "HKLM\Software\Policies\Microsoft\Windows\AppCompat" /v "DisableUAR" /t REG_DWORD /d 1 /f

rem Inventory Collector
reg add "HKLM\Software\Policies\Microsoft\Windows\Inventory" /v "Collect" /t REG_DWORD /d 0 /f

rem Telemetry
reg add "HKLM\Software\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f

rem Handwriting automatic learning
reg add "HKLM\Software\Policies\Microsoft\Windows\TabletPC" /v "PreventHandwritingDataSharing" /t REG_DWORD /d 1 /f

rem Allow users to enable online speech recognition services
reg add "HKLM\Software\Policies\Microsoft\Speech" /v "AllowSpeechModelUpdate" /t REG_DWORD /d 0 /f

rem Improve inking and typing recognition
reg add "HKLM\Software\Policies\Microsoft\InputPersonalization" /v "RestrictImplicitTextCollection" /t REG_DWORD /d 1 /f

rem PerfTrack
reg add "HKLM\Software\Policies\Microsoft\Windows\DataCollection" /v "DisablePerfTrack" /t REG_DWORD /d 1 /f

rem Microsoft Support Diagnostic tool
reg add "HKLM\Software\Policies\Microsoft\Windows\ScriptedDiagnosticsProvider\Policy" /v "DisableQueryRemoteServer" /t REG_DWORD /d 1 /f

rem Advertising ID
reg add "HKLM\Software\Policies\Microsoft\Windows\AdvertisingInfo" /v "Disabled" /t REG_DWORD /d 1 /f

rem Microsoft consumer experiences
reg add "HKLM\Software\Policies\Microsoft\Windows\CloudContent" /v "DisableConsumerFeatures" /t REG_DWORD /d 1 /f

rem Block Windows telemetry
reg add "HKLM\Software\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f

rem Disable telemetry
reg add "HKLM\Software\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f

rem Disable compatibility telemetry
schtasks /change /tn "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /disable

rem Disable advertising ID for relevant ads
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d 0 /f
reg add "HKLM\Software\Policies\Microsoft\Windows\AdvertisingInfo" /v "Disabled" /t REG_DWORD /d 1 /f

rem Disable WiFi Sense
reg add "HKLM\Software\Microsoft\WcmSvc\wifinetworkmanager\config" /v "AutoConnectAllowedOEM" /t REG_DWORD /d 0 /f
reg add "HKLM\Software\Microsoft\WcmSvc\wifinetworkmanager\config" /v "AutoConnectAllowed" /t REG_DWORD /d 0 /f

rem Prevent using diagnostic data
reg add "HKLM\Software\Policies\Microsoft\Windows\DataCollection" /v "LimitDiagnosticLogCollection" /t REG_DWORD /d 1 /f

rem Prevent using handwriting data
reg add "HKLM\Software\Policies\Microsoft\Windows\TabletPC" /v "PreventHandwritingDataSharing" /t REG_DWORD /d 1 /f

rem Disable Windows Hello biometrics
reg add "HKLM\Software\Policies\Microsoft\Biometrics" /v "Enabled" /t REG_DWORD /d 0 /f

rem Disable timeline feature
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d 0 /f
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d 0 /f
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d 0 /f

rem Disable location tracking
reg add "HKLM\Software\Policies\Microsoft\Windows\LocationAndSensors" /v "DisableLocation" /t REG_DWORD /d 1 /f

rem Do not show feedback notifications
reg add "HKCU\Software\Microsoft\Siuf\Rules" /v "NumberOfSIUFInPeriod" /t REG_DWORD /d 0 /f
reg add "HKCU\Software\Microsoft\Siuf\Rules" /v "PeriodInNanoSeconds" /t REG_QWORD /d 0 /f

rem Disable ads and links on lock screen
reg add "HKLM\Software\Policies\Microsoft\Windows\CloudContent" /v "DisableWindowsConsumerFeatures" /t REG_DWORD /d 1 /f

rem Block automatic install apps
reg add "HKLM\Software\Policies\Microsoft\Windows\CloudContent" /v "DisableSoftLanding" /t REG_DWORD /d 1 /f

rem Block suggested apps in Start
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SystemPaneSuggestionsEnabled" /t REG_DWORD /d 0 /f

rem Block suggested content in setting experimentation
reg add "HKLM\Software\Microsoft\PolicyManager\current\device\System" /v "AllowExperimentation" /t REG_DWORD /d 0 /f

rem Disable Inventory Collector
schtasks /change /tn "\Microsoft\Windows\Inventory\InventoryCollector" /disable

rem Disable "Get even more out of Windows"
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\UserProfileEngagement" /v "ScoobeSystemSettingEnabled" /t REG_DWORD /d 0 /f

rem Disable Cortana
reg add "HKLM\Software\Policies\Microsoft\Windows\Windows Search" /v "AllowCortana" /t REG_DWORD /d 0 /f

rem Disable Bing in Windows Search
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v "BingSearchEnabled" /t REG_DWORD /d 0 /f

rem Uninstall Cortana
powershell -Command "Get-AppxPackage *Microsoft.549981C3F5F10* | Remove-AppxPackage"

rem Remove pre-installed bloatware apps only
powershell -Command "Get-AppxPackage -AllUsers | Where-Object { $_.Name -like '*Microsoft.ZuneMusic*' -or $_.Name -like '*Microsoft.Music.Preview*' -or $_.Name -like '*Microsoft.XboxApp*' -or $_.Name -like '*Microsoft.SkypeApp*' } | Remove-AppxPackage"

rem Disable forced Windows Update
reg add "HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "NoAutoUpdate" /t REG_DWORD /d 1 /f

rem Disable Windows Update sharing
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config" /v "DODownloadMode" /t REG_DWORD /d 0 /f

rem Block major Windows Update
reg add "HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate" /v "TargetReleaseVersion" /t REG_DWORD /d 1 /f
reg add "HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate" /v "TargetReleaseVersionInfo" /t REG_SZ /d "2004" /f

rem Disable safeguards of Windows Updates
reg add "HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate" /v "DisableWUfBSafeguards" /t REG_DWORD /d 1 /f

rem Disable Game Bar
reg add "HKLM\Software\Policies\Microsoft\Windows\GameDVR" /v "AllowGameDVR" /t REG_DWORD /d 0 /f

rem Disable SmartScreen for Store Apps
reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "EnableSmartScreen" /t REG_DWORD /d 0 /f

rem Disable autofill from credit cards
reg add "HKCU\Software\Microsoft\Edge\Autofill" /v "CreditCardEnabled" /t REG_DWORD /d 0 /f

rem Prevent Edge running in background
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d 1 /f

rem Disable synchronization of data
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync" /v "SyncPolicy" /t REG_DWORD /d 1 /f

rem Block installation of new Microsoft Edge
reg add "HKLM\Software\Microsoft\EdgeUpdate" /v "DoNotUpdateToEdgeWithChromium" /t REG_DWORD /d 1 /f

rem Disable password reveal button
reg add "HKLM\Software\Policies\Microsoft\Windows\CredUI" /v "DisablePasswordReveal" /t REG_DWORD /d 1 /f

rem Disable DRM in Windows Media Player
reg add "HKLM\Software\Policies\Microsoft\WindowsMediaPlayer" /v "DisableDRM" /t REG_DWORD /d 1 /f



echo All policies have been disabled.

rem Block Windows Update
sc stop wuauserv
sc config wuauserv start= disabled

rem Connected User Experiences and telemetry
sc stop DiagTrack
sc config DiagTrack start= disabled

rem Microsoft Diagnostics Hub Standard Collector Service
sc stop diagnosticshub.standardcollector.service
sc config diagnosticshub.standardcollector.service start= disabled

rem Device Management Wireless Application Protocol (WAP) Push message Routing Service
sc stop dmwappushservice
sc config dmwappushservice start= disabled

rem Windows Media Player Network Sharing Service
sc stop WMPNetworkSvc
sc config WMPNetworkSvc start= disabled

rem Consolidator
sc stop PerfHost
sc config PerfHost start= disabled

rem Microsoft Compatibility Appraiser
schtasks /change /tn "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /disable

rem Device Census
schtasks /change /tn "\Microsoft\Windows\Device Information\Device" /disable

echo All specified services have been disabled.

powershell -File "%~dp0ps\Debloater.ps1"

taskkill /f /im explorer.exe
start explorer.exe

exit
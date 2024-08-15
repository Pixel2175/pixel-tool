import os
import subprocess as sub 
import urllib.parse as parse




  ####################################tweak_main###############################################################################################################################################
def run_command(command):
    sub.run(["powershell", "-Command", command], capture_output=True, text=True)



def disable_windows_search():
    run_command(" Get-Service -Name WSearch | Set-Service -StartupType Disabled")

def enable_windows_search():
    run_command(" Get-Service -Name WSearch | Set-Service -StartupType Automatic")

def disable_superfetch():
    run_command(" Get-Service -Name SysMain | Set-Service -StartupType Disabled")

def enable_superfetch():
    run_command(" Get-Service -Name SysMain | Set-Service -StartupType Automatic")

def disable_print_spooler():
    run_command(" Get-Service -Name Spooler | Set-Service -StartupType Disabled")

def enable_print_spooler():
    run_command(" Get-Service -Name Spooler | Set-Service -StartupType Automatic")

def disable_xbox_live_networking():
    run_command(" Get-Service -Name XboxNetApiSvc | Set-Service -StartupType Disabled")

def enable_xbox_live_networking():
    run_command(" Get-Service -Name XboxNetApiSvc | Set-Service -StartupType Manual")

def disable_wmp_network_sharing():
    run_command(" Get-Service -Name WMPNetworkSvc | Set-Service -StartupType Disabled")

def enable_wmp_network_sharing():
    run_command(" Get-Service -Name WMPNetworkSvc | Set-Service -StartupType Manual")

def disable_remote_registry():
    run_command(" Get-Service -Name RemoteRegistry | Set-Service -StartupType Disabled")

def enable_remote_registry():
    run_command(" Get-Service -Name RemoteRegistry | Set-Service -StartupType Manual")

def disable_diagnostic_policy():
    run_command(" Get-Service -Name DPS | Set-Service -StartupType Disabled")

def enable_diagnostic_policy():
    run_command(" Get-Service -Name DPS | Set-Service -StartupType Automatic")

def disable_error_reporting():
    run_command(" Get-Service -Name WerSvc | Set-Service -StartupType Disabled")

def enable_error_reporting():
    run_command(" Get-Service -Name WerSvc | Set-Service -StartupType Manual")

def disable_connected_user_experiences():
    run_command(" Get-Service -Name DiagTrack | Set-Service -StartupType Disabled")

def enable_connected_user_experiences():
    run_command(" Get-Service -Name DiagTrack | Set-Service -StartupType Automatic")

def disable_bluetooth_support():
    run_command(" Get-Service -Name bthserv | Set-Service -StartupType Disabled")

def enable_bluetooth_support():
    run_command(" Get-Service -Name bthserv | Set-Service -StartupType Manual")

def disable_fax():
    run_command(" Get-Service -Name Fax | Set-Service -StartupType Disabled")

def enable_fax():
    run_command(" Get-Service -Name Fax | Set-Service -StartupType Manual")

def disable_windows_insider():
    run_command(" Get-Service -Name wisvc | Set-Service -StartupType Disabled")

def enable_windows_insider():
    run_command(" Get-Service -Name wisvc | Set-Service -StartupType Manual")

def disable_mobile_hotspot():
    run_command(" Get-Service -Name icssvc | Set-Service -StartupType Disabled")

def enable_mobile_hotspot():
    run_command(" Get-Service -Name icssvc | Set-Service -StartupType Manual")

def disable_windows_defender():
    run_command(" Get-Service -Name WinDefend | Set-Service -StartupType Disabled")

def enable_windows_defender():
    run_command(" Get-Service -Name WinDefend | Set-Service -StartupType Automatic")

def disable_ms_account_signin():
    run_command(" Get-Service -Name wlidsvc | Set-Service -StartupType Disabled")

def enable_ms_account_signin():
    run_command(" Get-Service -Name wlidsvc | Set-Service -StartupType Manual")

def disable_windows_update():
    run_command(" Get-Service -Name wuauserv | Set-Service -StartupType Disabled")

def enable_windows_update():
    run_command(" Get-Service -Name wuauserv | Set-Service -StartupType Automatic")

def disable_windows_update_medic():
    run_command(" Get-Service -Name WaaSMedicSvc | Set-Service -StartupType Disabled")

def enable_windows_update_medic():
    run_command(" Get-Service -Name WaaSMedicSvc | Set-Service -StartupType Manual")

def disable_ceip():
    run_command(" Get-Service -Name CEIPSvc | Set-Service -StartupType Disabled")

def enable_ceip():
    run_command(" Get-Service -Name CEIPSvc | Set-Service -StartupType Automatic")

def disable_program_compatibility():
    run_command(" Get-Service -Name PcaSvc | Set-Service -StartupType Disabled")

def enable_program_compatibility():
    run_command(" Get-Service -Name PcaSvc | Set-Service -StartupType Automatic")


def disable_biometric_service():
    run_command(" Get-Service -Name WbioSrvc | Set-Service -StartupType Disabled")

def enable_biometric_service():
    run_command(" Get-Service -Name WbioSrvc | Set-Service -StartupType Manual")

def disable_touch_keyboard():
    run_command(" Get-Service -Name TabletInputService | Set-Service -StartupType Disabled")

def enable_touch_keyboard():
    run_command(" Get-Service -Name TabletInputService | Set-Service -StartupType Manual")

def disable_distributed_link_tracking():
    run_command(" Get-Service -Name TrkWks | Set-Service -StartupType Disabled")

def enable_distributed_link_tracking():
    run_command(" Get-Service -Name TrkWks | Set-Service -StartupType Automatic")

def disable_downloaded_maps_manager():
    run_command(" Get-Service -Name MapsBroker | Set-Service -StartupType Disabled")

def enable_downloaded_maps_manager():
    run_command(" Get-Service -Name MapsBroker | Set-Service -StartupType Automatic")

def disable_geolocation():
    run_command(" Get-Service -Name lfsvc | Set-Service -StartupType Disabled")

def enable_geolocation():
    run_command(" Get-Service -Name lfsvc | Set-Service -StartupType Manual")

def disable_offline_files():
    run_command(" Get-Service -Name CscService | Set-Service -StartupType Disabled")

def enable_offline_files():
    run_command(" Get-Service -Name CscService | Set-Service -StartupType Manual")

def disable_retail_demo():
    run_command(" Get-Service -Name RetailDemo | Set-Service -StartupType Disabled")

def enable_retail_demo():
    run_command(" Get-Service -Name RetailDemo | Set-Service -StartupType Manual")

def disable_smart_card():
    run_command(" Get-Service -Name SCardSvr | Set-Service -StartupType Disabled")

def enable_smart_card():
    run_command(" Get-Service -Name SCardSvr | Set-Service -StartupType Manual")

def disable_smart_card_device_enumeration():
    run_command(" Get-Service -Name ScDeviceEnum | Set-Service -StartupType Disabled")

def enable_smart_card_device_enumeration():
    run_command(" Get-Service -Name ScDeviceEnum | Set-Service -StartupType Manual")

def disable_windows_camera_frame_server():
    run_command(" Get-Service -Name FrameServer | Set-Service -StartupType Disabled")

def enable_windows_camera_frame_server():
    run_command(" Get-Service -Name FrameServer | Set-Service -StartupType Manual")

def disable_windows_image_acquisition():
    run_command(" Get-Service -Name stisvc | Set-Service -StartupType Disabled")

def enable_windows_image_acquisition():
    run_command(" Get-Service -Name stisvc | Set-Service -StartupType Manual")

def disable_windows_push_notifications():
    run_command(" Get-Service -Name WpnService | Set-Service -StartupType Disabled")

def enable_windows_push_notifications():
    run_command(" Get-Service -Name WpnService | Set-Service -StartupType Automatic")

def disable_alljoyn_router():
    run_command(" Get-Service -Name AJRouter | Set-Service -StartupType Disabled")

def enable_alljoyn_router():
    run_command(" Get-Service -Name AJRouter | Set-Service -StartupType Manual")

def disable_problem_reports():
    run_command(" Get-Service -Name wercplsupport | Set-Service -StartupType Disabled")

def enable_problem_reports():
    run_command(" Get-Service -Name wercplsupport | Set-Service -StartupType Manual")

def disable_remote_desktop_config():
    run_command(" Get-Service -Name SessionEnv | Set-Service -StartupType Disabled")

def enable_remote_desktop_config():
    run_command(" Get-Service -Name SessionEnv | Set-Service -StartupType Manual")

def disable_remote_desktop_services():
    run_command(" Get-Service -Name TermService | Set-Service -StartupType Disabled")

def enable_remote_desktop_services():
    run_command(" Get-Service -Name TermService | Set-Service -StartupType Manual")

def disable_hyperv_services():
    run_command(" Get-Service -Name vmms, vmcompute | Set-Service -StartupType Disabled")

def enable_hyperv_services():
    run_command(" Get-Service -Name vmms, vmcompute | Set-Service -StartupType Automatic")

def disable_ip_helper():
    run_command(" Get-Service -Name iphlpsvc | Set-Service -StartupType Disabled")

def enable_ip_helper():
    run_command(" Get-Service -Name iphlpsvc | Set-Service -StartupType Automatic")

def disable_parental_controls():
    run_command(" Get-Service -Name WpcMonSvc | Set-Service -StartupType Disabled")

def enable_parental_controls():
    run_command(" Get-Service -Name WpcMonSvc | Set-Service -StartupType Manual")

def disable_secondary_logon():
    run_command(" Get-Service -Name seclogon | Set-Service -StartupType Disabled")

def enable_secondary_logon():
    run_command(" Get-Service -Name seclogon | Set-Service -StartupType Manual")

def disable_sensor_data():
    run_command(" Get-Service -Name SensorDataService | Set-Service -StartupType Disabled")

def enable_sensor_data():
    run_command(" Get-Service -Name SensorDataService | Set-Service -StartupType Manual")

def disable_sensor_monitoring():
    run_command(" Get-Service -Name SensrSvc | Set-Service -StartupType Disabled")

def enable_sensor_monitoring():
    run_command(" Get-Service -Name SensrSvc | Set-Service -StartupType Manual")

def disable_sensor_service():
    run_command(" Get-Service -Name SensorService | Set-Service -StartupType Disabled")

def enable_sensor_service():
    run_command(" Get-Service -Name SensorService | Set-Service -StartupType Manual")

def disable_shared_pc_account_manager():
    run_command(" Get-Service -Name shpamsvc | Set-Service -StartupType Disabled")

def enable_shared_pc_account_manager():
    run_command(" Get-Service -Name shpamsvc | Set-Service -StartupType Manual")

def disable_shell_hardware_detection():
    run_command(" Get-Service -Name ShellHWDetection | Set-Service -StartupType Disabled")

def enable_shell_hardware_detection():
    run_command(" Get-Service -Name ShellHWDetection | Set-Service -StartupType Automatic")

def disable_snmp_trap():
    run_command(" Get-Service -Name SNMPTRAP | Set-Service -StartupType Disabled")

def enable_snmp_trap():
    run_command(" Get-Service -Name SNMPTRAP | Set-Service -StartupType Manual")

def disable_web_account_manager():
    run_command(" Get-Service -Name TokenBroker | Set-Service -StartupType Disabled")

def enable_web_account_manager():
    run_command(" Get-Service -Name TokenBroker | Set-Service -StartupType Manual")

def disable_windows_audio():
    run_command(" Get-Service -Name Audiosrv | Set-Service -StartupType Disabled")

def enable_windows_audio():
    run_command(" Get-Service -Name Audiosrv | Set-Service -StartupType Automatic")

def disable_windows_audio_endpoint_builder():
    run_command(" Get-Service -Name AudioEndpointBuilder | Set-Service -StartupType Disabled")

def enable_windows_audio_endpoint_builder():
    run_command(" Get-Service -Name AudioEndpointBuilder | Set-Service -StartupType Automatic")

def disable_windows_event_log():
    run_command(" Get-Service -Name EventLog | Set-Service -StartupType Disabled")

def enable_windows_event_log():
    run_command(" Get-Service -Name EventLog | Set-Service -StartupType Automatic")

def disable_application_experience():
    run_command(" Get-Service -Name AeLookupSvc | Set-Service -StartupType Disabled")

def enable_application_experience():
    run_command(" Get-Service -Name AeLookupSvc | Set-Service -StartupType Manual")

def disable_application_identity():
    run_command(" Get-Service -Name AppIDSvc | Set-Service -StartupType Disabled")

def enable_application_identity():
    run_command(" Get-Service -Name AppIDSvc | Set-Service -StartupType Manual")

def disable_bits():
    run_command(" Get-Service -Name BITS | Set-Service -StartupType Disabled")

def enable_bits():
    run_command(" Get-Service -Name BITS | Set-Service -StartupType Manual")

def disable_bitlocker():
    run_command(" Get-Service -Name BDESVC | Set-Service -StartupType Disabled")

def enable_bitlocker():
    run_command(" Get-Service -Name BDESVC | Set-Service -StartupType Manual")

def disable_certificate_propagation():
    run_command(" Get-Service -Name CertPropSvc | Set-Service -StartupType Disabled")

def enable_certificate_propagation():
    run_command(" Get-Service -Name CertPropSvc | Set-Service -StartupType Manual")

def disable_clipsvc():
    run_command(" Get-Service -Name ClipSVC | Set-Service -StartupType Disabled")

def enable_clipsvc():
    run_command(" Get-Service -Name ClipSVC | Set-Service -StartupType Manual")

def disable_computer_browser():
    run_command(" Get-Service -Name Browser | Set-Service -StartupType Disabled")

def enable_computer_browser():
    run_command(" Get-Service -Name Browser | Set-Service -StartupType Manual")

def disable_credential_manager():
    run_command(" Get-Service -Name VaultSvc | Set-Service -StartupType Disabled")

def enable_credential_manager():
    run_command(" Get-Service -Name VaultSvc | Set-Service -StartupType Manual")

def disable_cryptographic_services():
    run_command(" Get-Service -Name CryptSvc | Set-Service -StartupType Disabled")

def enable_cryptographic_services():
    run_command(" Get-Service -Name CryptSvc | Set-Service -StartupType Automatic")

def disable_dcom_server_process_launcher():
    run_command(" Get-Service -Name DcomLaunch | Set-Service -StartupType Disabled")

def enable_dcom_server_process_launcher():
    run_command(" Get-Service -Name DcomLaunch | Set-Service -StartupType Automatic")

def disable_delivery_optimization():
    run_command(" Get-Service -Name DoSvc | Set-Service -StartupType Disabled")

def enable_delivery_optimization():
    run_command(" Get-Service -Name DoSvc | Set-Service -StartupType Automatic")

def disable_wap_push_message_routing():
    run_command(" Get-Service -Name dmwappushservice | Set-Service -StartupType Disabled")

def enable_wap_push_message_routing():
    run_command(" Get-Service -Name dmwappushservice | Set-Service -StartupType Manual")

def disable_dhcp_client():
    run_command(" Get-Service -Name Dhcp | Set-Service -StartupType Disabled")

def enable_dhcp_client():
    run_command(" Get-Service -Name Dhcp | Set-Service -StartupType Automatic")

def disable_diagnostic_service_host():
    run_command(" Get-Service -Name WdiServiceHost | Set-Service -StartupType Disabled")

def enable_diagnostic_service_host():
    run_command(" Get-Service -Name WdiServiceHost | Set-Service -StartupType Manual")

def disable_distributed_transaction_coordinator():
    run_command(" Get-Service -Name MSDTC | Set-Service -StartupType Disabled")

def enable_distributed_transaction_coordinator():
    run_command(" Get-Service -Name MSDTC | Set-Service -StartupType Manual")

def disable_dns_client():
    run_command(" Get-Service -Name Dnscache | Set-Service -StartupType Disabled")

def enable_dns_client():
    run_command(" Get-Service -Name Dnscache | Set-Service -StartupType Automatic")

def disable_encrypting_file_system():
    run_command(" Get-Service -Name EFS | Set-Service -StartupType Disabled")

def enable_encrypting_file_system():
    run_command(" Get-Service -Name EFS | Set-Service -StartupType Manual")

def disable_extensible_authentication_protocol():
    run_command(" Get-Service -Name Eaphost | Set-Service -StartupType Disabled")

def enable_extensible_authentication_protocol():
    run_command(" Get-Service -Name Eaphost | Set-Service -StartupType Manual")

def disable_function_discovery_provider_host():
    run_command(" Get-Service -Name fdPHost | Set-Service -StartupType Disabled")

def enable_function_discovery_provider_host():
    run_command(" Get-Service -Name fdPHost | Set-Service -StartupType Manual")

def disable_function_discovery_resource_publication():
    run_command(" Get-Service -Name FDResPub | Set-Service -StartupType Disabled")

def enable_function_discovery_resource_publication():
    run_command(" Get-Service -Name FDResPub | Set-Service -StartupType Manual")

def disable_human_interface_device():
    run_command(" Get-Service -Name hidserv | Set-Service -StartupType Disabled")

def enable_human_interface_device():
    run_command(" Get-Service -Name hidserv | Set-Service -StartupType Manual")

def disable_ike_authip_ipsecc_keying_modules():
    run_command(" Get-Service -Name IKEEXT | Set-Service -StartupType Disabled")

def enable_ike_authip_ipsecc_keying_modules():
    run_command(" Get-Service -Name IKEEXT | Set-Service -StartupType Manual")

def disable_interactive_services_detection():
    run_command(" Get-Service -Name UI0Detect | Set-Service -StartupType Disabled")

def enable_interactive_services_detection():
    run_command(" Get-Service -Name UI0Detect | Set-Service -StartupType Manual")

def disable_internet_connection_sharing():
    run_command(" Get-Service -Name SharedAccess | Set-Service -StartupType Disabled")

def enable_internet_connection_sharing():
    run_command(" Get-Service -Name SharedAccess | Set-Service -StartupType Manual")

def disable_link_layer_topology_discovery_mapper():
    run_command(" Get-Service -Name lltdsvc | Set-Service -StartupType Disabled")

def enable_link_layer_topology_discovery_mapper():
    run_command(" Get-Service -Name lltdsvc | Set-Service -StartupType Manual")

def disable_microsoft_iscsi_initiator():
    run_command(" Get-Service -Name MSiSCSI | Set-Service -StartupType Disabled")

def enable_microsoft_iscsi_initiator():
    run_command(" Get-Service -Name MSiSCSI | Set-Service -StartupType Manual")

def disable_microsoft_software_shadow_copy_provider():
    run_command(" Get-Service -Name swprv | Set-Service -StartupType Disabled")

def enable_microsoft_software_shadow_copy_provider():
    run_command(" Get-Service -Name swprv | Set-Service -StartupType Manual")

def disable_netlogon():
    run_command(" Get-Service -Name Netlogon | Set-Service -StartupType Disabled")

def enable_netlogon():
    run_command(" Get-Service -Name Netlogon | Set-Service -StartupType Manual")

def disable_network_connection_broker():
    run_command(" Get-Service -Name NcbService | Set-Service -StartupType Disabled")

def enable_network_connection_broker():
    run_command(" Get-Service -Name NcbService | Set-Service -StartupType Manual")

def disable_network_connections():
    run_command(" Get-Service -Name Netman | Set-Service -StartupType Disabled")

def enable_network_connections():
    run_command(" Get-Service -Name Netman | Set-Service -StartupType Manual")

def disable_network_list_service():
    run_command(" Get-Service -Name netprofm | Set-Service -StartupType Disabled")

def enable_network_list_service():
    run_command(" Get-Service -Name netprofm | Set-Service -StartupType Automatic")

def disable_network_location_awareness():
    run_command(" Get-Service -Name NlaSvc | Set-Service -StartupType Disabled")

def enable_network_location_awareness():
    run_command(" Get-Service -Name NlaSvc | Set-Service -StartupType Automatic")

def disable_network_store_interface_service():
    run_command(" Get-Service -Name nsi | Set-Service -StartupType Disabled")

def enable_network_store_interface_service():
    run_command(" Get-Service -Name nsi | Set-Service -StartupType Automatic")

def disable_peer_name_resolution_protocol():
    run_command(" Get-Service -Name PNRPsvc | Set-Service -StartupType Disabled")

def enable_peer_name_resolution_protocol():
    run_command(" Get-Service -Name PNRPsvc | Set-Service -StartupType Manual")

def disable_peer_networking_grouping():
    run_command(" Get-Service -Name p2psvc | Set-Service -StartupType Disabled")

def enable_peer_networking_grouping():
    run_command(" Get-Service -Name p2psvc | Set-Service -StartupType Manual")

def disable_peer_networking_identity_manager():
    run_command(" Get-Service -Name p2pimsvc | Set-Service -StartupType Disabled")

def enable_peer_networking_identity_manager():
    run_command(" Get-Service -Name p2pimsvc | Set-Service -StartupType Manual")

def disable_performance_counter_dll_host():
    run_command(" Get-Service -Name PerfHost | Set-Service -StartupType Disabled")

def enable_performance_counter_dll_host():
    run_command(" Get-Service -Name PerfHost | Set-Service -StartupType Manual")

def disable_performance_logs_alerts():
    run_command(" Get-Service -Name pla | Set-Service -StartupType Disabled")

def enable_performance_logs_alerts():
    run_command(" Get-Service -Name pla | Set-Service -StartupType Manual")

def disable_phone_service():
    run_command(" Get-Service -Name PhoneSvc | Set-Service -StartupType Disabled")

def enable_phone_service():
    run_command(" Get-Service -Name PhoneSvc | Set-Service -StartupType Manual")

def disable_plug_and_play():
    run_command(" Get-Service -Name PlugPlay | Set-Service -StartupType Disabled")

def enable_plug_and_play():
    run_command(" Get-Service -Name PlugPlay | Set-Service -StartupType Automatic")

def disable_portable_device_enumerator():
    run_command(" Get-Service -Name WPDBusEnum | Set-Service -StartupType Disabled")

def enable_portable_device_enumerator():
    run_command(" Get-Service -Name WPDBusEnum | Set-Service -StartupType Manual")

def disable_qwave():
    run_command(" Get-Service -Name QWAVE | Set-Service -StartupType Disabled")

def enable_qwave():
    run_command(" Get-Service -Name QWAVE | Set-Service -StartupType Manual")

def disable_radio_management_service():
    run_command(" Get-Service -Name RmSvc | Set-Service -StartupType Disabled")

def enable_radio_management_service():
    run_command(" Get-Service -Name RmSvc | Set-Service -StartupType Manual")

def disable_remote_access_auto_connection_manager():
    run_command(" Get-Service -Name RasAuto | Set-Service -StartupType Disabled")

def enable_remote_access_auto_connection_manager():
    run_command(" Get-Service -Name RasAuto | Set-Service -StartupType Manual")

def disable_remote_access_connection_manager():
    run_command(" Get-Service -Name RasMan | Set-Service -StartupType Disabled")

def enable_remote_access_connection_manager():
    run_command(" Get-Service -Name RasMan | Set-Service -StartupType Manual")

def disable_rpc_locator():
    run_command(" Get-Service -Name RpcLocator | Set-Service -StartupType Disabled")

def enable_rpc_locator():
    run_command(" Get-Service -Name RpcLocator | Set-Service -StartupType Manual")

def disable_routing_and_remote_access():
    run_command(" Get-Service -Name RemoteAccess | Set-Service -StartupType Disabled")

def enable_routing_and_remote_access():
    run_command(" Get-Service -Name RemoteAccess | Set-Service -StartupType Manual")

def disable_server():
    run_command(" Get-Service -Name LanmanServer | Set-Service -StartupType Disabled")

def enable_server():
    run_command(" Get-Service -Name LanmanServer | Set-Service -StartupType Automatic")

def disable_still_image_acquisition_events():
    run_command(" Get-Service -Name WiaRpc | Set-Service -StartupType Disabled")

def enable_still_image_acquisition_events():
    run_command(" Get-Service -Name WiaRpc | Set-Service -StartupType Manual")

def disable_volume_shadow_copy():
    run_command(" Get-Service -Name VSS | Set-Service -StartupType Disabled")

def enable_volume_shadow_copy():
    run_command(" Get-Service -Name VSS | Set-Service -StartupType Manual")


####################################debloat_main########################################################################################################################################################################################################################

def remove_command(command):
    os.system(f'PowerShell -Command "{command}"')
def builder_3d():
    remove_command("Get-AppxPackage *3dbuilder* | Remove-AppxPackage")
def viewer_3d():
    remove_command("Get-AppxPackage *3dviewer* | Remove-AppxPackage")
def alarms_and_clock():
    remove_command("Get-AppxPackage *windowsalarms* | Remove-AppxPackage")
def calculator():
    remove_command("Get-AppxPackage *windowscalculator* | Remove-AppxPackage")
def calendar_and_mail():
    remove_command("Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage")
def camera():
    remove_command("Get-AppxPackage *windowscamera* | Remove-AppxPackage")
def cortana():
    remove_command("Get-AppxPackage *Microsoft.549981C3F5F10* | Remove-AppxPackage")
def feedback_hub():
    remove_command("Get-AppxPackage *windowsfeedbackhub* | Remove-AppxPackage")
def get_help():
    remove_command("Get-AppxPackage *Microsoft.GetHelp* | Remove-AppxPackage")
def groove_music():
    remove_command("Get-AppxPackage *zunemusic* | Remove-AppxPackage")
def maps():
    remove_command("Get-AppxPackage *windowsmaps* | Remove-AppxPackage")
def messaging():
    remove_command("Get-AppxPackage *messaging* | Remove-AppxPackage")
def mixed_reality_portal():
    remove_command("Get-AppxPackage *Microsoft.MixedReality.Portal* | Remove-AppxPackage")
def mobile_plans():
    remove_command("Get-AppxPackage *oneconnect* | Remove-AppxPackage")
def money():
    remove_command("Get-AppxPackage *bingfinance* | Remove-AppxPackage")
def movies_and_tv():
    remove_command("Get-AppxPackage *zunevideo* | Remove-AppxPackage")
def news():
    remove_command("Get-AppxPackage *bingnews* | Remove-AppxPackage")
def office():
    remove_command("Get-AppxPackage *officehub* | Remove-AppxPackage")
def onenote():
    remove_command("Get-AppxPackage *onenote* | Remove-AppxPackage")
def paint_3d():
    remove_command("Get-AppxPackage *mspaint* | Remove-AppxPackage")
def people():
    remove_command("Get-AppxPackage *people* | Remove-AppxPackage")
def photos():
    remove_command("Get-AppxPackage *photos* | Remove-AppxPackage")
def print_3d():
    remove_command("Get-AppxPackage *print3d* | Remove-AppxPackage")
def skype():
    remove_command("Get-AppxPackage *skypeapp* | Remove-AppxPackage")
def snip_and_sketch():
    remove_command("Get-AppxPackage *ScreenSketch* | Remove-AppxPackage")
def solitaire():
    remove_command("Get-AppxPackage *solitairecollection* | Remove-AppxPackage")
def sports():
    remove_command("Get-AppxPackage *bingsports* | Remove-AppxPackage")
def spotify():
    remove_command("Get-AppxPackage *SpotifyAB.SpotifyMusic* | Remove-AppxPackage")
def sticky_notes():
    remove_command("Get-AppxPackage *MicrosoftStickyNotes* | Remove-AppxPackage")
def tips():
    remove_command("Get-AppxPackage *getstarted* | Remove-AppxPackage")
def translator():
    remove_command("Get-AppxPackage *translator* | Remove-AppxPackage")
def voice_recorder():
    remove_command("Get-AppxPackage *soundrecorder* | Remove-AppxPackage")
def weather():
    remove_command("Get-AppxPackage *bingweather* | Remove-AppxPackage")
def xbox():
    remove_command("Get-AppxPackage *xboxapp* | Remove-AppxPackage")
def xbox_game_bar():
    remove_command("Get-AppxPackage *Xbox.TCUI* | Remove-AppxPackage")
def your_phone():
    remove_command("Get-AppxPackage *yourphone* | Remove-AppxPackage")
def zune():
    remove_command("Get-AppxPackage *zune* | Remove-AppxPackage")
def bing():
    remove_command("Get-AppxPackage *bing* | Remove-AppxPackage")
def candy_crush():
    remove_command("Get-AppxPackage *candycrush* | Remove-AppxPackage")
def netflix():
    remove_command("Get-AppxPackage *netflix* | Remove-AppxPackage")
def dolby():
    remove_command("Get-AppxPackage *dolby* | Remove-AppxPackage")
def fitbit():
    remove_command("Get-AppxPackage *fitbit* | Remove-AppxPackage")
def connectivity_store():
    remove_command("Get-AppxPackage *ConnectivityStore* | Remove-AppxPackage")
def xbox_gaming_overlay():
    remove_command("Get-AppxPackage *Microsoft.XboxGamingOverlay* | Remove-AppxPackage")
def xbox_speech_to_text():
    remove_command("Get-AppxPackage *Microsoft.XboxSpeechToTextOverlay* | Remove-AppxPackage")
def webp_image_extension():
    remove_command("Get-AppxPackage *Microsoft.WebpImageExtension* | Remove-AppxPackage")
def web_media_extensions():
    remove_command("Get-AppxPackage *Microsoft.WebMediaExtensions* | Remove-AppxPackage")
def xbox_identity_provider():
    remove_command("Get-AppxPackage *Microsoft.XboxIdentityProvider* | Remove-AppxPackage")
def paint():
    remove_command("Get-AppxPackage *paint* | Remove-AppxPackage")

######################################### tools ###############################################################




#tweak

tweak_name=[
    "Windows Search",
    "Superfetch (SysMain)",
    "Print Spooler",
    "Xbox Live Networking ",
    "Media Player Sharing",
    "Remote Registry",
    "Diagnostic Policy Service",
    "Windows Error Reporting",
    "User Experiences and Telemetry",
    "Bluetooth Support Service",
    "Disable Fax",
    "Windows Insider Service",
    "Windows Mobile Hotspot ",
    "Windows Defender Antivirus ",
    "Microsoft Account Sign-in",
    "Windows Update",
    "Windows Update Medic ",
    "Experience Improvement",
    "Compatibility Assistant ",
    "Windows Biometric ",
    "Touch Keyboard & Handwriting ",
    "Distributed Link Tracking ",
    "Downloaded Maps Manager",
    "Geolocation Service",
    "Offline Files",
    "Retail Demo Service",
    "Smart Card",
    "Smart Card Device",
    "Windows Camera Frame ",
    "Windows Image Acquisition",
    "Push Notifications System ",
    "AllJoyn Router Service",
    "Problem Reports and Solutions",
    "Remote Desktop Configuration",
    "Remote Desktop Services",
    "Hyper-V services",
    "Disable IP Helper",
    "Parental Controls",
    "Secondary Logon",
    "Sensor Data Service",
    "Sensor Monitoring Service",
    "Sensor Service",
    "Shared PC Account Manager",
    "Shell Hardware Detection",
    "Disable SNMP Trap",
    "Web Account Manager",
    "Windows Audio",
    "Windows Audio Endpoint Builder",
    "Windows Event Log",
    "Application Experience",
    "Application Identity",
    "Background Intelligent Transfer ",
    "BitLocker Drive Encryption ",
    "Certificate Propagation",
    "ClipSVC (Client License Service)",
    "Computer Browser",
    "Credential Manager",
    "Cryptographic Services",
    "DCOM Server Process Launcher",
    "Delivery Optimization",
    "Wireless Application Protocol",
    "DHCP Client",
    "Diagnostic Service Host",
    "Distributed Transaction Coordinator",
    "DNS Client",
    "Encrypting File System",
    "Extensible Authentication",
    "Discovery Provider Host",
    "Discovery Resource Publication",
    "Human Interface Device ",
    "IKE and AuthIP IPsec Keying",
    "Interactive Services Detection",
    "Internet Connection Sharing",
    "Link-Layer Topology Discovery",
    "Microsoft iSCSI Initiator",
    "Software Shadow Copy Provider",
    "Disable Netlogon",
    "Network Connection Broker",
    "Network Connections",
    "Network List Service",
    "Network Location Awareness",
    "Network Store Interface Service",
    "Peer Name Resolution Protocol",
    "Peer Networking Grouping",
    "Peer Networking Identity Manager",
    "Performance Counter DLL Host",
    "Performance Logs & Alerts",
    "Phone Service",
    "Plug and Play",
    "Portable Device Enumerator ",
    "Quality Windows Audio Video",
    "Radio Management",
    "Remote Access Auto Connection",
    "Remote Access Connection ",
    "Remote Procedure Call",
    "Routing and Remote Access",
    "Disable Server",
    "Still Image Acquisition",
    "Volume Shadow Copy", 
]

on_value = [
    disable_windows_search,
    disable_superfetch,
    disable_print_spooler,
    disable_xbox_live_networking,
    disable_wmp_network_sharing,
    disable_remote_registry,
    disable_diagnostic_policy,
    disable_error_reporting,
    disable_connected_user_experiences,
    disable_bluetooth_support,
    disable_fax,
    disable_windows_insider,
    disable_mobile_hotspot,
    disable_windows_defender,
    disable_ms_account_signin,
    disable_windows_update,
    disable_windows_update_medic,
    disable_ceip,
    disable_program_compatibility,
    disable_biometric_service,
    disable_touch_keyboard,
    disable_distributed_link_tracking,
    disable_downloaded_maps_manager,
    disable_geolocation,
    disable_offline_files,
    disable_retail_demo,
    disable_smart_card,
    disable_smart_card_device_enumeration,
    disable_windows_camera_frame_server,
    disable_windows_image_acquisition,
    disable_windows_push_notifications,
    disable_alljoyn_router,
    disable_problem_reports,
    disable_remote_desktop_config,
    disable_remote_desktop_services,
    disable_hyperv_services,
    disable_ip_helper,
    disable_parental_controls,
    disable_secondary_logon,
    disable_sensor_data,
    disable_sensor_monitoring,
    disable_sensor_service,
    disable_shared_pc_account_manager,
    disable_shell_hardware_detection,
    disable_snmp_trap,
    disable_web_account_manager,
    disable_windows_audio,
    disable_windows_audio_endpoint_builder,
    disable_windows_event_log,
    disable_application_experience,
    disable_application_identity,
    disable_bits,
    disable_bitlocker,
    disable_certificate_propagation,
    disable_clipsvc,
    disable_computer_browser,
    disable_credential_manager,
    disable_cryptographic_services,
    disable_dcom_server_process_launcher,
    disable_delivery_optimization,
    disable_wap_push_message_routing,
    disable_dhcp_client,
    disable_diagnostic_service_host,
    disable_distributed_transaction_coordinator,
    disable_dns_client,
    disable_encrypting_file_system,
    disable_extensible_authentication_protocol,
    disable_function_discovery_provider_host,
    disable_function_discovery_resource_publication,
    disable_human_interface_device,
    disable_ike_authip_ipsecc_keying_modules,
    disable_interactive_services_detection,
    disable_internet_connection_sharing,
    disable_link_layer_topology_discovery_mapper,
    disable_microsoft_iscsi_initiator,
    disable_microsoft_software_shadow_copy_provider,
    disable_netlogon,
    disable_network_connection_broker,
    disable_network_connections,
    disable_network_list_service,
    disable_network_location_awareness,
    disable_network_store_interface_service,
    disable_peer_name_resolution_protocol,
    disable_peer_networking_grouping,
    disable_peer_networking_identity_manager,
    disable_performance_counter_dll_host,
    disable_performance_logs_alerts,
    disable_phone_service,
    disable_plug_and_play,
    disable_portable_device_enumerator,
    disable_qwave,
    disable_radio_management_service,
    disable_remote_access_auto_connection_manager,
    disable_remote_access_connection_manager,
    disable_rpc_locator,
    disable_routing_and_remote_access,
    disable_server,
    disable_still_image_acquisition_events,
    disable_volume_shadow_copy,
]


off_value =[
    enable_windows_search,
    enable_superfetch,
    enable_print_spooler,
    enable_xbox_live_networking,
    enable_wmp_network_sharing,
    enable_remote_registry,
    enable_diagnostic_policy,
    enable_error_reporting,
    enable_connected_user_experiences,
    enable_bluetooth_support,
    enable_fax,
    enable_windows_insider,
    enable_mobile_hotspot,
    enable_windows_defender,
    enable_ms_account_signin,
    enable_windows_update,
    enable_windows_update_medic,
    enable_ceip,
    enable_program_compatibility,
    enable_biometric_service,
    enable_touch_keyboard,
    enable_distributed_link_tracking,
    enable_downloaded_maps_manager,
    enable_geolocation,
    enable_offline_files,
    enable_retail_demo,
    enable_smart_card,
    enable_smart_card_device_enumeration,
    enable_windows_camera_frame_server,
    enable_windows_image_acquisition,
    enable_windows_push_notifications,
    enable_alljoyn_router,
    enable_problem_reports,
    enable_remote_desktop_config,
    enable_remote_desktop_services,
    enable_hyperv_services,
    enable_ip_helper,
    enable_parental_controls,
    enable_secondary_logon,
    enable_sensor_data,
    enable_sensor_monitoring,
    enable_sensor_service,
    enable_shared_pc_account_manager,
    enable_shell_hardware_detection,
    enable_snmp_trap,
    enable_web_account_manager,
    enable_windows_audio,
    enable_windows_audio_endpoint_builder,
    enable_windows_event_log,
    enable_application_experience,
    enable_application_identity,
    enable_bits,
    enable_bitlocker,
    enable_certificate_propagation,
    enable_clipsvc,
    enable_computer_browser,
    enable_credential_manager,
    enable_cryptographic_services,
    enable_dcom_server_process_launcher,
    enable_delivery_optimization,
    enable_wap_push_message_routing,
    enable_dhcp_client,
    enable_diagnostic_service_host,
    enable_distributed_transaction_coordinator,
    enable_dns_client,
    enable_encrypting_file_system,
    enable_extensible_authentication_protocol,
    enable_function_discovery_provider_host,
    enable_function_discovery_resource_publication,
    enable_human_interface_device,
    enable_ike_authip_ipsecc_keying_modules,
    enable_interactive_services_detection,
    enable_internet_connection_sharing,
    enable_link_layer_topology_discovery_mapper,
    enable_microsoft_iscsi_initiator,
    enable_microsoft_software_shadow_copy_provider,
    enable_netlogon,
    enable_network_connection_broker,
    enable_network_connections,
    enable_network_list_service,
    enable_network_location_awareness,
    enable_network_store_interface_service,
    enable_peer_name_resolution_protocol,
    enable_peer_networking_grouping,
    enable_peer_networking_identity_manager,
    enable_performance_counter_dll_host,
    enable_performance_logs_alerts,
    enable_phone_service,
    enable_plug_and_play,
    enable_portable_device_enumerator,
    enable_qwave,
    enable_radio_management_service,
    enable_remote_access_auto_connection_manager,
    enable_remote_access_connection_manager,
    enable_rpc_locator,
    enable_routing_and_remote_access,
    enable_server,
    enable_still_image_acquisition_events,
    enable_volume_shadow_copy,

]

#debloat


debloat_name=[
    "3D Builder ",
    "3D Viewer",
    "Alarms and Clock",
    "Calculator",
    "Calendar and Mail",
    "Camera",
    "Cortana",
    "Feedback Hub",
    "Get Help",
    "Groove Music",
    "Maps",
    "Messaging",
    "Mixed Reality Portal",
    "Mobile Plans",
    "Money",
    "Movies and TV",
    "News",
    "Office",
    "Onenote",
    "Paint 3D",
    "People",
    "Photos",
    "Print 3D",
    "Skype",
    "Snip and Sketch",
    "Solitaire",
    "Sports",
    "Spotify",
    "Sticky Notes",
    "Windows Tips",
    "Translator",
    "Voice Recorder",
    "Weather",
    "Xbox",
    "Xbox Game Bar",
    "Connectivity Store",
    "Xbox Gaming Overlay",
    "Xbox Speech to Text",
    "WEBP Image Extension",
    "WEB Media Extensions",
    "Xbox Identity Provider",
    "Paint",
    "Your Phone",
    "Microsoft Zune",
    "Microsoft Bing",
    "Candy Crush",
    "Netflix",
    "Dolby",
    "Fitbit",
]
    


remove_app=[
    builder_3d,
    viewer_3d,
    alarms_and_clock,
    calculator,
    calendar_and_mail,
    camera,
    cortana,
    feedback_hub,
    get_help,
    groove_music,
    maps,
    messaging,
    mixed_reality_portal,
    mobile_plans,
    money,
    movies_and_tv,
    news,
    office,
    onenote,
    paint_3d,
    people,
    photos,
    print_3d,
    skype,
    snip_and_sketch,
    solitaire,
    sports,
    spotify,
    sticky_notes,
    tips,
    translator,
    voice_recorder,
    weather,
    xbox,
    xbox_game_bar,
    connectivity_store,
    xbox_gaming_overlay,
    xbox_speech_to_text,
    webp_image_extension,
    web_media_extensions,
    xbox_identity_provider,
    paint,
    your_phone,
    zune,
    bing,
    candy_crush,
    netflix,
    dolby,
    fitbit,
]

delete_selected=[]





#####################[tools main]##################################################################################################################################################################################################################

download_selected=[]

download_apps_name=['Echo X','Hone','ShutUp10','Optimizer','QuickBoost','PrivateZilla','ZusierAIO','WPD','Real','MLW App','Chromium','Brave','Malware Bytes','XToolBox','Mem Reduct','7-Zip','Runtime Drivers','Optmizer','ADW Cleaner','Winrar','Revo Uninstaller']
download_apps_name_path=['EchoX.bat','HoneInstaller.exe','ShutUp10.exe','Optimizer.exe','QuickBoost.exe','PrivateZilla.zip','ZusierAIO.bat','latest.zip','Real.exe','MLWapp.zip','Winaero_Tweaker_v1.40.0.0.zip','chromium_installer.exe','BraveBrowserSetup.exe','MBSetup.exe','XTBox.exe','memreduct-3.4-setup.exe','7z2407-x64.exe','Visual-C-Runtimes-All-in-One-May-2024.zip','Optimizer-16.6.exe','adwcleaner.exe','winrar-x64-701.exe','revosetup.exe']
download_apps_url=[
        'https://github.com/UnLovedCookie/EchoX/releases/latest/download/EchoX.bat',
        'https://download.overwolf.com/installer/prod/cfbc7eeb79ab95eb3f553c4344a186ee/Hone%20-%20Installer.exe',
        'https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe',
        'https://github.com/hellzerg/optimizer/releases/download/16.2/Optimizer-16.2.exe',
        'https://github.com/SanGraphic/QuickBoost/releases/latest/download/QuickBoost.exe',
        'https://github.com/builtbybel/privatezilla/releases/latest/download/privatezilla.zip',
        'https://raw.githubusercontent.com/Zusier/Zusiers-optimization-Batch/master/Zusier%20AIO.bat',
        'https://wpd.app/get/latest.zip',
        'https://cdn.discordapp.com/attachments/1148712576495124580/1149004164983173141/REAL.exe?ex=66ae4d84&is=66acfc04&hm=8f29e562699deb2fc1145672827f0dba26bd2f758b207007919090c6bd28de85&',
        'https://mylivewallpapers.com/download/mlwapp-version-2-6/?wpdmdl=44746&refresh=66ad236ec7bad1722622830',
        'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/1336632/mini_installer.exe',
        'https://laptop-updates.brave.com/latest/winx64',
        'https://downloads.malwarebytes.com/file/mb-windows',
        'https://github.com/nyxiereal/XToolbox/releases/download/v4.2/XTBox.exe',
        'https://github.com/henrypp/memreduct/releases/download/v.3.4/memreduct-3.4-setup.exe',
        'https://7-zip.org/a/7z2407-x64.exe',
        'https://us1-dl.techpowerup.com/files/aN_EscRstR8HcgAGz998kQ/1722686084/Visual-C-Runtimes-All-in-One-May-2024.zip',
        'https://github.com/hellzerg/optimizer/releases/download/16.6/Optimizer-16.6.exe',
        'https://adwcleaner.malwarebytes.com/adwcleaner?channel=release&_gl=1*1keufi7*_gcl_aw*R0NMLjE3MjI2MjQyMjguQ2owS0NRandoN0sxQmhDWkFSSXNBS09yVnFIbUpDN25uQ0lVN3I1SnE0aUw0UWxEbTFrZWJkc3lBeHlrOXJESU5aZXNFbzVOcy01Xzhod2FBaHJpRUFMd193Y0I.*_gcl_au*MjA1OTMwODk0OC4xNzIyNjI0MjI4*_ga*MjA1ODY3MTM3My4xNzIyNjI0MjI5*_ga_K8KCHE3KSC*MTcyMjYyNDIyOS4xLjEuMTcyMjY0MzA0Ni41MS4wLjA.&_ga=2.11172660.1851557141.1722643038-2058671373.1722624229',
        'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-701.exe',
        'https://download.revouninstaller.com/download/revosetup.exe',
]

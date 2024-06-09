import os
import sys
import subprocess as sub
from colorama import Fore
import win32api
import colorama
from art import text2art
import webbrowser as web
import setwallpaper as wallp

def set_size(columns, rows):
    os.system(f'mode con: cols={columns} lines={rows}')

def swt(title):
    win32api.SetConsoleTitle(title)   

set_size(90,24)
os.system("cls")
restore_point_bat = os.path.join(os.path.dirname(__file__), 'data', 'restore_point.bat')

os.system("cls")

def restart():
    path=sys.executable
    os.execl(path, path, *sys.argv)

print("")
colorama.init()
title = text2art("        Restore   Point")
print(Fore.BLUE + title + Fore.RESET)
colorama.deinit()
print("")
print("")
print("      ####################[Do You Want To Create Resor Point]####################")
print("      #                                                                         #")
print("      #                                                                         #")
print("      #          \033[1;31;40m[1]\033[0m- YES                                  \033[1;31;40m[2]\033[0m- no              #")
print("      #                                                                         #")
print("      #                                                                         #")
print("      ###########################################################################")
print("")
print("")
print("")
loppa = input("   [*]-Enter 1 OR 2 :  ")
if loppa == "1":
    print("")
    sub.run([restore_point_bat])
elif loppa == "2":
    pass
else:
    restart()

services_bat = os.path.join(os.path.dirname(__file__), 'data', 'services.bat')
cleanup_bat = os.path.join(os.path.dirname(__file__), 'data', 'cleanup.bat')
remove_app_bat = os.path.join(os.path.dirname(__file__), 'data', 'windows_remover.bat')
activate_windows_bat = os.path.join(os.path.dirname(__file__), 'data', 'activate_windows.bat')
runtime_bat = os.path.join(os.path.dirname(__file__), 'runtime', 'install.bat')
wallpaper = os.path.join(os.path.dirname(__file__), 'wallpapers', 'pixel_1.png')
amd_bat= os.path.join(os.path.dirname(__file__), 'data', 'gpu', 'amd.bat' )
nvidia_bat= os.path.join(os.path.dirname(__file__), 'data', 'gpu', 'nvidia.bat' )

def menu():
    set_size(90,24)
    os.system("cls")
    print("")
    colorama.init()
    title = text2art("                    Pixel Tool")
    print(Fore.BLUE + title + Fore.RESET)
    colorama.deinit()
    print("")
    print("   #####################################################################################")
    print("   #                                                                                   #")
    print("   #  \033[1;31;40m[1]\033[0m- Full Tweak           \033[1;31;40m[2]\033[0m- Windows Apps Remover        \033[1;31;40m[3]\033[0m- Disk Cleaner     #")
    print("   #                                                                                   #")
    print("   #  \033[1;31;40m[4]\033[0m- Runtime Install      \033[1;31;40m[5]\033[0m- Windows Activator           \033[1;31;40m[6]\033[0m- Gpu Tweaks       #")             
    print("   #                                                                                   #")
    print("   #  \033[1;31;40m[7]\033[0m- About                                                                       #")
    print("   #                                                                                   #")
    print("   #####################################################################################")
    print("")
    print("")
    print("")

    while True :
        inp = input("  [*]- Enter what you want : ")
        if inp == "1" or inp == "2" or inp == "3" or inp == "4" or inp == "5" or inp == "6" or inp =="7":
            inp =  int(inp)
            break

        else:
            menu()


    lop = 0

    while lop ==0:

        # ____________________________________________[Disable Tweaks]___________________________________________________


        if inp == 1 :
            print("")
            warning = input("[?]- are you sure you want use\033[1;31;40m Disable Services Tweak \033[0m (yes/no): ")
            print("")
            if warning == "yes" or warning == "Yes" or warning == "y" or warning == "Y":
                wallp.set_wallpaper(wallpaper)
                sub.run([services_bat])
                menu()
                
            elif warning == "no" or warning == "No" or warning == "n" or warning == "N":
                warning_1 = input("do you wanna exit? (yes/no) : ")
                if warning_1 == "yes" or warning_1 == "Yes" or warning_1 == "y" or warning_1 == "Y":

                    sys.exit()
                elif warning_1 == "no" or warning_1 == "No" or warning_1 == "n" or warning_1 == "N":
                    print()
                    
                    menu()
            else:
                print("")
                
                menu()
                    
        #____________________________________________[Disk Cleaner]_________________________________________________

        if inp == 3 :
            print("")
            warning = input("  [?]- are you sure you want \033[1;31;40mCleanUp Your Disk and Ram?\033[0m (yes/no): ")
            print("")

            if warning == "yes" or warning == "Yes" or warning == "y" or warning == "Y":
                sub.run([cleanup_bat])
                menu()
                
            elif warning == "no" or warning == "No" or warning == "n" or warning == "N":
                warning_1 = input("do you wanna exit? (yes/no) : ")
                if warning_1 == "yes" or warning_1 == "Yes" or warning_1 == "y" or warning_1 == "Y":

                    sys.exit()
                elif warning_1 == "no" or warning_1 == "No" or warning_1 == "n" or warning_1 == "N":
                    print()
                    
                    menu()
            else:
                print("")
                menu()
                
                




        if inp == 6:
            os.system("cls")
            print("")
            print("")
            colorama.init()
            spptitle = text2art("                                GPU  ")
            print(Fore.RED + spptitle + Fore.RESET)
            colorama.deinit()
            print("""
          ##########################[GPU Optmizer]###########################
          #                                                                 #
          #                                                                 #
          #            \033[1;31;40m[1]\033[0m- Nvidia                   \033[1;31;40m[2]\033[0m- AMD               #
          #                                                                 #
          #                           \033[1;31;40m[3]\033[0m- Back                             #
          #                                                                 #
          ###################################################################
""")
            print("")
            lool= input("   [*]- Whats Your Gpu : ")
            if lool =="1":
                print("")
                sub.run([nvidia_bat])
            elif lool == "2":
                sub.run([amd_bat])
            elif lool == "3":
                menu() 


        #_________________________________________________[AppRemover]__________________________________________




        if inp == 2 :
            set_size(90,39)
            os.system("cls")
            print("")
            colorama.init()
            title = text2art("     Windows Apps")
            print(Fore.BLUE + title + Fore.RESET)
            colorama.deinit()
            print("       ###################################[Apps]##################################")
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- Print 3D           \033[1;31;40m[*]\033[0m- 3D Viewer          \033[1;31;40m[*]\033[0m- Zune              #")
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- Windows Maps       \033[1;31;40m[*]\033[0m- Bing               \033[1;31;40m[*]\033[0m- Skype             #")                                                                       
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- Solitare           \033[1;31;40m[*]\033[0m- CandyCruch         \033[1;31;40m[*]\033[0m- Netflix           #")
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- Onenote            \033[1;31;40m[*]\033[0m- Dolby              \033[1;31;40m[*]\033[0m- Fitbit            #")                                                 
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- FeedBack           \033[1;31;40m[*]\033[0m- YourPhone          \033[1;31;40m[*]\033[0m- Photos            #")
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- One Drive          \033[1;31;40m[*]\033[0m- Massaging          \033[1;31;40m[*]\033[0m- Camera            #")                                                        
            print("       #                                                                         #")                                                        
            print("       #  \033[1;31;40m[*]\033[0m- Office Hub         \033[1;31;40m[*]\033[0m- Getstarted         \033[1;31;40m[*]\033[0m- Sounde Recording  #")
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- Xbox (All)         \033[1;31;40m[*]\033[0m- Alarms             \033[1;31;40m[*]\033[0m- Screen Sketch     #")                                                                    
            print("       #                                                                         #")                                                                                                                                                        
            print("       #  \033[1;31;40m[*]\033[0m- StickyNotes        \033[1;31;40m[*]\033[0m- Get Help           \033[1;31;40m[*]\033[0m- Paint             #")
            print("       #                                                                         #")
            print("       #  \033[1;31;40m[*]\033[0m- Edge               \033[1;31;40m[*]\033[0m- One Drive          \033[1;31;40m[*]\033[0m- MixedReality      #")                                                                                                                                                  
            print("       #                                                                         #")
            print("       #                                                                         #")
            print("       #                                                                         #")
            print("       #                          \033[1;31;40m[B]\033[0m- Back To Menu                              #")
            print("       ###########################################################################")                    
            print("")
            print("")
            warning = input("  [?]- are you sure you want \033[1;31;40mRemove Windows Apps? \033[0m (yes/no/b): ")
            print("")
            if warning == "yes" or warning == "Yes" or warning == "y" or warning == "Y":
                sub.run([remove_app_bat])
                wallp.set_wallpaper(wallpaper)
                menu()
            elif warning == "b" or warning == "B":
                menu() 
                                           
            elif warning == "no" or warning == "No" or warning == "n" or warning == "N":
                warning_1 = input("do you wanna exit? (yes/no) : ")
                if warning_1 == "yes" or warning_1 == "Yes" or warning_1 == "y" or warning_1 == "Y":
                    sys.exit()
                elif warning_1 == "no" or warning_1 == "No" or warning_1 == "n" or warning_1 == "N":
                    os.system("clear")
                    menu()
            else:
                os.system("clear")
                menu()

        #_________________________________________________[RunTime]__________________________________________

        if inp == 4 :
            print("")
            warning = input("  [?]- are you sure you want \033[1;31;40minstall Runtime Drivers? \033[0m (yes/no): ")
            if warning == "yes" or warning == "Yes" or warning == "y" or warning == "Y":
                print("")
                sub.run([runtime_bat])
                wallp.set_wallpaper(wallpaper)
                menu()
    
            elif warning == "no" or warning == "No" or warning == "n" or warning == "N":
                warning_1 = input("do you wanna exit? (yes/no) : ")
                if warning_1 == "yes" or warning_1 == "Yes" or warning_1 == "y" or warning_1 == "Y":
                    os.system("clear")
                    sys.exit()
                elif warning_1 == "no" or warning_1 == "No" or warning_1 == "n" or warning_1 == "N":
                    print()
                    os.system("clear")
                    menu()

            else:
                os.system("clear")
                menu()

        if inp == 5 :
            print("")
            warning = input("  [?]- are you sure you want \033[1;31;40mActivate Windows ? \033[0m (yes/no): ")
            if warning == "yes" or warning == "Yes" or warning == "y" or warning == "Y":
                print("")
                sub.run([activate_windows_bat])
                wallp.set_wallpaper(wallpaper)
                menu()
    
            elif warning == "no" or warning == "No" or warning == "n" or warning == "N":
                warning_1 = input("do you wanna exit? (yes/no) : ")
                if warning_1 == "yes" or warning_1 == "Yes" or warning_1 == "y" or warning_1 == "Y":
                    os.system("clear")
                    sys.exit()
                elif warning_1 == "no" or warning_1 == "No" or warning_1 == "n" or warning_1 == "N":
                    print()
                    os.system("clear")
                    menu()

            else:
                os.system("clear")
                menu()
        #_____________________________________________________[support]____________________________________________ 
        if inp == 7 :
            os.system("cls")
            print("")
            print("")
            colorama.init()
            spptitle = text2art("                      About  ")
            print(Fore.RED + spptitle + Fore.RESET)
            colorama.deinit()
            print("""
      ####################################################################
      #                                                                  #
      #      \033[1;31;40m[1]\033[0m- GitHub         \033[1;31;40m[2]\033[0m- Discord         \033[1;31;40m[3]\033[0m- Website       #
      #                                                                  #
      #                                                                  #
      #         \033[1;31;40m[4]\033[0m- TikTok(Pixel)            \033[1;31;40m[5]\033[0m- TikTok(7Tech)         #
      #                                                                  #
      ####################################################################
""")
            print("")

            chs = input("  [*]- Which will you choose first? : ")
            if chs == "1":
                web.open("https://github.com/pixel2175")
            elif chs == "2":
                web.open("https://discord.gg/tQV6NS2sUR")
            elif chs == "4":
                web.open("https://www.tiktok.com/@pixel2715")
            elif chs == "3":
                web.open("https://pixel31.github.io/")
            elif chs == "5":
                web.open("https://www.tiktok.com/@_tech7_")

menu()

if __name__ == "__main__":
    swt("Pixel Tool")
    sys.stdout.write("\x1b]2;Pixel Tool\x07")
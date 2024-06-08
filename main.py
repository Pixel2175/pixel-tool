import os
import sys
import subprocess as sub
from colorama import Fore
import colorama
from art import text2art
import webbrowser as web
import setwallpaper as wallp

def set_size(columns, rows):
    os.system(f'mode con: cols={columns} lines={rows}')


set_size(80,25)
os.system("cls")
restore_point_bat = os.path.join(os.path.dirname(__file__), 'data', 'restore_point.bat')

os.system("cls")
print("")
colorama.init()
title = text2art("  Restore   Point")
print(Fore.BLUE + title + Fore.RESET)
colorama.deinit()
print("")
print("")
loppa = input("[*]-First Do You Want To Create \033[1;31;40mRestore Point\033[0m?? (yes/no): ")
if loppa == "yes" or loppa == "Yes" or loppa == "y" or loppa == "Y":
    print("   Create Restore Poite")
    print("   Please wait...")
    print("")
    sub.run([restore_point_bat])
else:
    pass





services_bat = os.path.join(os.path.dirname(__file__), 'data', 'services.bat')
cleanup_bat = os.path.join(os.path.dirname(__file__), 'data', 'cleanup.bat')
remove_app_bat = os.path.join(os.path.dirname(__file__), 'data', 'windows_remover.bat')
activate_windows_bat = os.path.join(os.path.dirname(__file__), 'data', 'activate_windows.bat')
runtime_bat = os.path.join(os.path.dirname(__file__), 'runtime', 'install.bat')
wallpaper = os.path.join(os.path.dirname(__file__), 'wallpapers', 'pixel_1.png')

def restart():
    path=sys.executable
    os.execl(path, path, *sys.argv)




def menu():
    os.system("cls")
    print("")
    colorama.init()
    title = text2art("              Pixel Tool")
    print(Fore.BLUE + title + Fore.RESET)
    colorama.deinit()
    print("  ###########################################################################")
    print("  #                                                                         #")
    print("  #    \033[1;31;40m[1]\033[0m- Disable Services                    \033[1;31;40m[2]\033[0m- Windows App Remover    #")
    print("  #                                                                         #")
    print("  #    \033[1;31;40m[3]\033[0m- Disk Cleaner                        \033[1;31;40m[4]\033[0m- Runtime Drivers        #")
    print("  #                                                                         #")
    print("  #    \033[1;31;40m[5]\033[0m- Windows Activator                   \033[1;31;40m[6]\033[0m- Support me             #")
    print("  #                                                                         #")
    print("  ###########################################################################")
    print("")
    print("")
    print("")

    while True :
        inp = input("  [*]- Enter what you want : ")
        if inp == "1" or inp == "2" or inp == "3" or inp == "4" or inp == "5" or inp == "6":
            inp =  int(inp)
            break

        elif inp == "0":
        	menu()

        else:
            print("go fuck your self :3 ")
            input("press enter to relaunch: ")
            print("")
            print("")


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
                
                


        #_________________________________________________[AppRemover]__________________________________________

        if inp == 2 :
            print("")
            print("")
            warning = input("  [?]- are you sure you want \033[1;31;40mRemove Windows Apps? \033[0m (yes/no): ")
            print("")
            if warning == "yes" or warning == "Yes" or warning == "y" or warning == "Y":
                sub.run([remove_app_bat])
                wallp.set_wallpaper(wallpaper)
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
        if inp == 6:
            os.system("cls")
            print("")
            print("")
            colorama.init()
            spptitle = text2art("                 Support")
            print(Fore.RED + spptitle + Fore.RESET)
            colorama.deinit()
            print("""
      ####################################################################
      #                                                                  #
      #      [1]- GitHub         [2]- Discord         [3]- Website       #
      #                                                                  #
      #                                                                  #
      #         [4]- TikTok(Pixel)            [5]- TikTok(7Tech)         #
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
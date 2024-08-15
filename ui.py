import customtkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser as web
import data
import os
import requests as req
tk.set_appearance_mode('dark')
tk.set_default_color_theme('theme/purpel.json')

class Update(tk.CTkToplevel):
    def __init__(self,main):
        super().__init__(main)
        self.title('Check Update')
        self.geometry('275x350')
        self.resizable(False, False)

        self.version='V0.9'
        self.url='https://github.com/Pixel2175/pixel-tool/releases/tag/V1.4'
        
        self.uptodate_logo=ImageTk.PhotoImage(Image.open('images/update_done.png').resize((115,115)))
        self.update_wait_logo=ImageTk.PhotoImage(Image.open('images/update_wait.png').resize((115,115)))

        self.update_massage=tk.CTkLabel(self,text="Latest Version !!",font=tk.CTkFont('poppins',24,'bold'),text_color='#afafaf')
        self.update_massage.place(x=45,y=180)

        self.version_label=tk.CTkLabel(self,text=self.version,font=tk.CTkFont('poppins',13,'normal'))
        self.version_label.place(x=235,y=320)

        self.update_btn=tk.CTkButton(self,text='Download',font=tk.CTkFont('poppins',18,'normal'))
        self.update_btn.place(x=70,y=260)

        self.logo_update=tk.CTkLabel(self,text='',font=tk.CTkFont('',20),image=self.update_wait_logo)
        self.logo_update.place(x=80,y=30)

        if req.get(self.url).status_code==200:
            self.update_massage.configure(text='Version Available!!')
            self.update_massage.place(x=30,y=180)
            self.logo_update.configure(image=self.update_wait_logo)
            self.update_btn.configure(text='Download',command=lambda: web.open(self.url))
            self.close_btn=tk.CTkButton(self,text='Close',font=tk.CTkFont('poppins',18,'normal'),command=self.destroy)
            self.close_btn.place(x=70,y=300)
        else:
            self.update_massage.configure(text='Latest Version')
            self.logo_update.configure(image=self.uptodate_logo)
            self.update_btn.configure(text='Close',command=self.destroy)

class Win(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("901x490")
        self.resizable(False,False)
        self.title("Pixel Tool")

        # Header
        self.header=tk.CTkFrame(self,height=56,width=880,corner_radius=20)
        self.header.pack(pady=11,padx=10,fill='y')
        self.logo=tk.CTkButton(self.header,text='',image=ImageTk.PhotoImage(Image.open('images/icon.png').resize((36,35))),height=35,width=35,fg_color="transparent",hover_color="#2c074f")
        self.logo.place(x=13,y=6)
        self.titlee = tk.CTkLabel(self.header,text="PIXEL TOOL",font=tk.CTkFont('poppins',23,"bold"))
        self.titlee.place(x=71,y=11)
        self.github_logo = tk.CTkButton(self.header,
                                        text="",
                                        image=ImageTk.PhotoImage(Image.open("images/github.png").resize((31,30))),
                                        height=31,width=30,
                                        fg_color="transparent",hover_color="#2c074f",
                                        command=self.github_link)
        self.github_logo.place(x=771,y=9)
        self.discord_logo= tk.CTkButton(self.header,
                                        text="",
                                        image=ImageTk.PhotoImage(Image.open("images/discord.png").resize((31,30))),
                                        height=31,width=30,
                                        fg_color="transparent",hover_color="#2c074f",
                                        command=self.discord_link)
        self.discord_logo.place(x=721,y=10)
    

        self.update_logo=tk.CTkButton(self.header,
                                      text='',
                                      image=ImageTk.PhotoImage(Image.open('images/update.png').resize((36,36))),
                                      height=36,width=36,
                                      fg_color='transparent',hover_color='#2c074f',
                                      command=self.check_update_btn)
        self.update_logo.place(x=821,y=8)


        self.menu=tk.CTkFrame(self,width=181,corner_radius=20)
        self.menu.pack(pady=11,padx=15,side="left",fill="y")
        self.menu.pack_propagate(False)
   
        self.menubuttons_font = tk.CTkFont('poppins',19,'bold')
        
        self.home=tk.CTkButton(self.menu,
                               text=" Home",
                               width=0,
                               bg_color="#2c074f",
                               hover_color="#2c074f",fg_color="transparent",
                               image=ImageTk.PhotoImage(Image.open("images/home.png").resize((27,27))),
                               text_color="#b4b4b4",font=self.menubuttons_font,
                               command=self.home_btn)
        self.home.place(x=25,y=35)

        self.tweak=tk.CTkButton(self.menu,
                               text=" Tweak",
                               width=0,
                               bg_color="#2c074f",
                               hover_color="#2c074f",fg_color="transparent",
                               image=ImageTk.PhotoImage(Image.open("images/tweak.png").resize((30,30))),
                               text_color="#b4b4b4",font=self.menubuttons_font,
                                command=self.tweak_btn)
        self.tweak.place(x=23,y=95)

        self.debloat=tk.CTkButton(self.menu,
                               text=" Debloat",
                               width=0,
                               bg_color="#2c074f",
                               hover_color="#2c074f",fg_color="transparent",
                               image=ImageTk.PhotoImage(Image.open("images/debloat.png").resize((30,30))),
                               text_color="#b4b4b4",font=self.menubuttons_font,
                               command=self.debloat_btn)
        self.debloat.place(x=23,y=155)

        self.tools=tk.CTkButton(self.menu,
                               text=" Tools",
                               width=0,
                               bg_color="#2c074f",
                               hover_color="#2c074f",fg_color="transparent",
                               image=ImageTk.PhotoImage(Image.open("images/toolbox.png").resize((33,33))),
                               text_color="#b4b4b4",font=self.menubuttons_font,
                               command=self.tools_btn)
        self.tools.place(x=23,y=215)

        self.interp=tk.CTkLabel(self.menu,text='',bg_color="#b4b4b4",width=3,height=32)
        self.interp.place(x=20,y=36)

        self.rikka_icon=tk.CTkLabel(self.menu,text="",image=ImageTk.PhotoImage(Image.open("images/rikka.png").resize((136,128))))
        self.rikka_icon.place(x=25,y=270)

        self.main=tk.CTkFrame(self,corner_radius=21,height=3000)
        self.main.pack(pady=11,padx=15,anchor='s',fill="both",expand=True)

        #all mains buttons ################################################################################
        self.home_main=tk.CTkFrame(self.main,width=647,height=377,fg_color="#2c074f")
        self.home_main.place(x=7,y=7)
        self.tweak_main=tk.CTkFrame(self.main,width=647,height=377,fg_color="#2c074f")
        self.debloat_main=tk.CTkFrame(self.main,width=647,height=377,fg_color="#2c074f")
        self.tools_main=tk.CTkFrame(self.main,width=647,height=377,fg_color="#2c074f")


        # ################################## home main widget ##################################
        self.warning_title=tk.CTkLabel(self.home_main,
                                       text="Warning",
                                       font=tk.CTkFont('poppins',48,'bold'),)
        self.warning_title.place(x=215,y=23)
        self.warning_text=tk.CTkLabel(self.home_main,
                                      text="this tool will modify your windows that will stop services\n on your windows and disable telemetry that means this tool \nwill not work on all PCs and will maybe impact your system stability\n and could break windows features ,Please before using it\n you need to understand all changes and accept all risks\n and you need to create a full system backup",
                                      font=tk.CTkFont('poppins',16,'normal'))
        self.warning_text.place(x=58,y=110)
        
        self.restore=tk.CTkButton(self.home_main,
                                  text="Create BackUp",
                                  width=110,height=50,corner_radius=20,
                                  font=tk.CTkFont('poppins',20,'normal'),
                                  command=self.open_restore)
        self.restore.place(x=90,y=290)
        self.restore_how=tk.CTkButton(self.home_main,
                                   text="How To Create BackUp",
                                   width=110,height=50,corner_radius=20,
                                   font=tk.CTkFont('poppins',20,'normal'),
                                   command=self.how_to_restore)
        self.restore_how.place(x=330,y=290)
       
        # ################################## tweak main ##################################          
        self.tweak_btns_main=tk.CTkCanvas(self.tweak_main,bg='#2c074f',height=320,width=3230,highlightthickness=0)
        self.tweak_btns_main.place(x=0,y=0)

        self.bo_x=37 
        self.bo_y=15 

        for i in data.tweak_name:
            btn=tk.CTkSwitch(self.tweak_btns_main,text=i,font=tk.CTkFont('poppins',14,'normal'))
            btn.configure(command=lambda a=btn, b=i: self.bobo(a, b))
            btn.place(x=self.bo_x,y=self.bo_y)
            if self.bo_y >=270:
                self.bo_y =15 
                self.bo_x+=310
            else:
                self.bo_y+=30
    
        self.next_btn_tweak=tk.CTkButton(self.tweak_main,text='',
                                         image=ImageTk.PhotoImage(Image.open('images/next.png').resize((36,48))),
                                         hover_color='#2c074f',fg_color='#2c074f',width=30,height=40,command=self.next_tweak)
        self.next_btn_tweak.place(x=590,y=320)
        
        self.back_btn_tweak=tk.CTkButton(self.tweak_main,text='',
                                         image=ImageTk.PhotoImage(Image.open('images/back.png').resize((36,48))),
                                         hover_color='#2c074f',fg_color="#2c074f",width=30,height=40,command=self.back_tweak)
        self.back_btn_tweak.place(x=480,y=320)
        self.tweak_page_num=tk.CTkLabel(self.tweak_main,text_color='#b4b4b4',text='1/5',font=tk.CTkFont('poppins',36,'bold'))
        self.tweak_page_num.place(x=532,y=320)
        # ################################## debloat main ##################################
        self.btns_main=tk.CTkCanvas(self.debloat_main,width=1292,height=320,bg="#2c074f",highlightthickness=0)
        self.btns_main.place(x=0,y=0)
        
        self.debloat_next_page=tk.CTkButton(self.debloat_main,image=ImageTk.PhotoImage(Image.open('images/next.png').resize((36,48))),fg_color='#2c074f',hover_color='#2c074f',width=30,height=40,text='',command=self.debloat_next_btn)
        self.debloat_next_page.place(x=590,y=320)

        self.debloat_back_page=tk.CTkButton(self.debloat_main,image=ImageTk.PhotoImage(Image.open('images/back.png').resize((36,48))),fg_color='#2c074f',hover_color='#2c074f',width=30,height=40,text='',command=self.debloat_back_btn)
        self.debloat_back_page.place(x=480,y=320)

        self.debloat_page_num=tk.CTkLabel(self.debloat_main,text_color='#b4b4b4',text='1/2',font=tk.CTkFont('poppins',36,'bold'))
        self.debloat_page_num.place(x=535,y=320)
        
        self.select_all=tk.CTkButton(self.debloat_main,text='Select All',font=tk.CTkFont('poppins',24,'normal'),corner_radius=20,command=self.select_al)
        self.select_all.place(x=35,y=330)
        
        self.delete_select=tk.CTkButton(self.debloat_main,text='Delete Selected',font=tk.CTkFont('poppins',24,'normal'),corner_radius=20,command=self.delete_btn)
        self.delete_select.place(x=215,y=330)

        self.btn_y=30 
        self.btn_x=50 
        for index,i in enumerate(data.debloat_name):
            btn=tk.CTkCheckBox(self.btns_main,text=i,font=tk.CTkFont('poppins',14,'normal'))
            btn.configure(command=lambda a=btn,b=index : self.btn_add_index(a,b))
            btn.place(x=self.btn_x,y=self.btn_y)
            if self.btn_y==270:
                self.btn_y=30
                self.btn_x+=220
            else:
                self.btn_y +=30

        self.chk_ = 0
        

        #  ################################## Tools main ##################################
        self.tools_btns_main=tk.CTkCanvas(self.tools_main,bg='#2c074f',height=300,width=1292,highlightthickness=0)
        self.tools_btns_main.place(x=0,y=0)
        
        self.path=tk.StringVar()
        self.path.set('C:\Program Files (x86)\\')
        self.entry_path=tk.CTkEntry(self.tools_main,width=300,textvariable=self.path,font=tk.CTkFont('poppins',13,'normal'))
        self.entry_path.place(x=20,y=337)
        
        self.open_dialog_btn=tk.CTkButton(self.tools_main,text="Open",image=ImageTk.PhotoImage(Image.open('images/open.png').resize((20,20))),font=tk.CTkFont('poppins',18,'normal'),width=110,command=self.open_dialog)
        self.open_dialog_btn.place(x=330,y=335)

        self.app_station=tk.CTkLabel(self.tools_main,text='',font=tk.CTkFont('poppins',20,'bold'))
        self.app_station.place(x=15,y=300)


        self.download_btn=tk.CTkButton(self.tools_main,text='Download',image=ImageTk.PhotoImage(Image.open('images/download.png').resize((20,20))),font=tk.CTkFont('poppins',18,'normal'),command=self.download_apps)
        self.download_btn.place(x=455,y=335)


        self.btn_x=30 
        self.btn_y=20 
        for index, app in enumerate(data.download_apps_name):
            btn=tk.CTkCheckBox(self.tools_btns_main,text=app,font=tk.CTkFont('poppins',14,'normal'))
            btn.configure(command=lambda a=index , b= app , c= btn: self.app_index(a,b,c))
            btn.place(x=self.btn_x,y=self.btn_y)
            if self.btn_y>=240:
                self.btn_y=20 
                self.btn_x+=150
            else:
                self.btn_y+=40 



    def next_tweak(self):
        if self.tweak_btns_main.winfo_x() == 0:
            self.tweak_btns_main.place(x= -620 )
            self.tweak_page_num.configure(text='2/5')
        elif self.tweak_btns_main.winfo_x() == -620 :
            self.tweak_btns_main.place(x= -1240 )
            self.tweak_page_num.configure(text='3/5')
        elif self.tweak_btns_main.winfo_x() == -1240:
            self.tweak_btns_main.place(x= -1860)
            self.tweak_page_num.configure(text='4/5')
        elif self.tweak_btns_main.winfo_x() == -1860:
            self.tweak_btns_main.place(x= -2480)
            self.tweak_page_num.configure(text='5/5')

    def back_tweak(self):
        if self.tweak_btns_main.winfo_x() == -2480:
            self.tweak_btns_main.place(x= -1860 )
            self.tweak_page_num.configure(text='4/5')
        elif self.tweak_btns_main.winfo_x() == -1860 :
            self.tweak_btns_main.place(x= -1240 )
            self.tweak_page_num.configure(text='3/5')
        elif self.tweak_btns_main.winfo_x() == -1240:
            self.tweak_btns_main.place(x= -620)
            self.tweak_page_num.configure(text='2/5')
        elif self.tweak_btns_main.winfo_x() == -620:
            self.tweak_btns_main.place(x= -0)
            self.tweak_page_num.configure(text='1/5')


    def download_apps(self):
        self.app_station.configure(text='')
        origin_path = os.getcwd()
        path = self.path.get()
        if os.path.exists(path):
            os.chdir(path)
            for i in data.download_selected:
                self.app_station.configure(text=f'Downloading {data.download_apps_name[i]} ...')
                self.app_station.update()
                get = req.get(data.download_apps_url[i])
                size = len(get.content)
                file_name = data.download_apps_name_path[i]
                with open(file_name, 'wb') as f:
                    f.write(get.content)

            self.app_station.configure(text='Done')
            os.chdir(origin_path)
        else:
            self.app_station.configure(text='Wrong Path')
                


    def app_index(self, index, app, btn):
        if btn.get():
            data.download_selected.append(index)
        else:
            data.download_selected.remove(index)
        print(data.download_selected)
        

    def how_to_restore(self):
        web.open('https://support.kaspersky.com/common/windows/15104')


    def open_restore(self):
        os.system('systempropertiesprotection')


    def open_dialog(self):
         path = filedialog.askdirectory(title="Add Folder")
         if path:
            self.path.set(path)


    def delete_btn(self):
        for i, value in enumerate(data.delete_selected):
            data.remove_app[value]()


    def btn_add_index(self,btn,index):
        if btn.get():
            if not index in data.delete_selected:
                data.delete_selected.append(index)
        else:
            if index in data.delete_selected:
                data.delete_selected.remove(index)

    def select_al(self):
        if self.chk_ ==0:
            for btn in self.btns_main.winfo_children():
                if isinstance(btn, tk.CTkCheckBox):
                    btn.select()
                    self.select_all.configure(text='Deselect All')
                    data.delete_selected.clear() 
                    for i in range(49):
                        data.delete_selected.append(i)
                    self.chk_=1 
        elif self.chk_ ==1:
            for btn in self.btns_main.winfo_children():
                if isinstance(btn, tk.CTkCheckBox):
                    btn.deselect()
                    data.delete_selected.clear()
                    self.select_all.configure(text='Select All')
                    self.chk_= 0

    def debloat_next_btn(self):
        if self.btns_main.winfo_x()==0:
            self.btns_main.place(x= -660)
            self.debloat_page_num.configure(text='2/2')
    def debloat_back_btn(self):
        if self.btns_main.winfo_x()== -660:
            self.btns_main.place(x=0)
            self.debloat_page_num.configure(text='1/2')


    def bobo(self,btn,var):
        index=data.tweak_name.index(var)
        if btn.get():
            data.on_value[index]()
        else:
            data.off_value[index]()
            print(data.off_value[index])


    def interp_changer(self,my_y):
        if self.interp.winfo_y() > my_y: 
            self.interp.place(y=self.interp.winfo_y() - 1)
            self.after(2,lambda: self.interp_changer(my_y))
        elif self.interp.winfo_y() < my_y:
            self.interp.place(y=self.interp.winfo_y() + 1)
            self.after(2,lambda: self.interp_changer(my_y) )

    def home_btn(self):
        self.interp_changer(35)
        self.home_main.place(x=7,y=7)
        self.tweak_main.place_forget()
        self.debloat_main.place_forget()
        self.tools_main.place_forget()

    def tweak_btn(self):
        self.interp_changer(95)
        self.tweak_main.place(x=7,y=7)
        self.home_main.place_forget() 
        self.debloat_main.place_forget()
        self.tools_main.place_forget()

    def debloat_btn(self):
        self.interp_changer(155)
        self.debloat_main.place(x=7,y=7)
        self.home_main.place_forget()
        self.tweak_main.place_forget()
        self.tools_main.place_forget()
    def tools_btn(self):
        self.interp_changer(215)
        self.tools_main.place(x=7,y=7)
        self.home_main.place_forget()
        self.debloat_main.place_forget()
        self.tweak_main.place_forget()

    def github_link(self):
        web.open("https://github.com/pixel2175")
    def discord_link(self):
        web.open("https://discord.gg/k7MckM2f3V")

    def check_update_btn(self):
        Update(main=self)

if __name__=='__main__':
    root = Win()
    root.mainloop()

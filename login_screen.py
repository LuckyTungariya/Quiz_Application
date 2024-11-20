import customtkinter as ctk 
import tkinter as tk
from datetime import *
from quiz_screen import quiz_class
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk
import pymysql as psql

class login_class(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()        
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,0,0))

        self.frames = {}

        self.container_frame = ctk.CTkFrame(self)
        self.container_frame.pack(fill = "both",expand = True)
    
        self.title("LOGIN PAGE")

        self.login_frame = ctk.CTkFrame(self.container_frame)
        self.login_frame.pack(fill = "both",expand = "True")

        self.add_frames("login",self.login_frame)

        self.bgimage = ctk.CTkImage(dark_image=Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\quizbg.jpg"),size=(self.width, self.height))
        self.bglabel = ctk.CTkLabel(self.login_frame,image = self.bgimage,text = "")
        self.bglabel.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

        self.bind("<f>",self.toggle_fullscreen)

        self.bind("<Escape>",self.escape_fullscreen)

        self.login_page()

        self.mycon = psql.connect(host = "localhost",user = "root",password = "root",port = 3307,charset = 'utf8',db = 'projects')
        self.cur = self.mycon.cursor()
        print("connected")

    def add_frames(self,name,frame_object):
        self.frames[name] = frame_object

    def navigate_between_frames(self,old_frame,new_frame):
        if old_frame:
            self.frames[old_frame].pack_forget()
        render_frame =  self.frames[new_frame]
        render_frame.pack(fill = "both",expand = True)

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)
        #self.attributes("-fullscreen",True)

    def escape_fullscreen(self,event = None):
        self.overrideredirect(False)

    def login_page(self):
        self.background_frame = ctk.CTkFrame(self.login_frame,corner_radius=20,border_width=1,border_color="#000000",fg_color="#29B6F6",width=600)
        self.background_frame.pack(anchor = "n",padx = 50,pady = (50,20),fill = "y")

        self.login_background_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\login_background.webp"),size = (500,500))
        self.login_label = ctk.CTkLabel(self.background_frame,image = self.login_background_image,text = "")
        self.login_label.pack()

        self.option_lbl = ctk.CTkLabel(self.background_frame,text = "LOGIN OR REGISTER",text_color="#000000",font = ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.option_lbl.place(x = 120,y = 20)

        self.usr_lbl = ctk.CTkLabel(self.background_frame,text = "USERNAME",fg_color="#ffffff",corner_radius=10,text_color="#000000",font = ctk.CTkFont(family = "Garamond",size = 15,weight = "bold"))
        self.usr_lbl.place(x = 120,y = 100)
        
        self.name_of_user = ctk.StringVar()
        self.name_of_user.set("Enter your username:")
        self.username_entry = ctk.CTkEntry(self.background_frame,height = 35,textvariable=self.name_of_user,fg_color = "#ffffff",text_color = "#000000",placeholder_text_color = "#000000",placeholder_text="Enter Username:")
        self.username_entry.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
        self.username_entry.bind("<FocusIn>",self.usr_focus_in)
        self.username_entry.bind("<FocusOut>",self.usr_focus_out)
        
        self.pss_lbl = ctk.CTkLabel(self.background_frame,text = "PASSWORD",fg_color="#ffffff",corner_radius=10,text_color="#000000",font = ctk.CTkFont(family = "Garamond",size = 15,weight = "bold"))
        self.pss_lbl.place(x = 120,y = 250)

        self.pass_of_user = ctk.StringVar()
        self.pass_of_user.set("Enter your password:")
        self.password_entry = ctk.CTkEntry(self.background_frame,height = 35,textvariable=self.pass_of_user,fg_color = "#ffffff",text_color = "#000000",placeholder_text_color = "#000000",placeholder_text="Enter Password:")
        self.password_entry.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
        self.password_entry.bind("<FocusIn>",self.psr_focus_in)
        self.password_entry.bind("<FocusOut>",self.psr_focus_out)

        self.login_button = ctk.CTkButton(self.background_frame,text = "LOGIN",text_color = "#000000",font = ctk.CTkFont(family = " Consolas",size = 20),fg_color = "#F5F5F5",hover_color = "darkgray",command = self.check_login)
        self.login_button.place(relx = 0.15,rely = 0.8,relwidth = 0.3)

        self.register_button = ctk.CTkButton(self.background_frame,text = "REGISTER",text_color = "#000000",font = ctk.CTkFont(family = " Consolas",size = 20),fg_color = "#F5F5F5",hover_color = "darkgray",command = self.register)
        self.register_button.place(relx = 0.55,rely = 0.8,relwidth = 0.3)

    def usr_focus_in(self,event):
        if self.username_entry.get() == "Enter your username:":
            self.username_entry.delete(0,ctk.END)

    def usr_focus_out(self,event):
        if self.username_entry.get() == "":
            self.username_entry.insert(0,"Enter your username:")

    def psr_focus_in(self,event):
        if self.password_entry.get() == "Enter your password:":
            self.password_entry.delete(0,ctk.END)

    def psr_focus_out(self,event):
         if self.password_entry.get() == "":
            self.password_entry.insert(0,"Enter your password:")
        
    def register(self):
        if self.name_of_user.get() == "" or self.name_of_user.get() == "Enter your username:":
            messagebox.showerror(title = "Error",message = "Input your username:")
        if self.pass_of_user.get() == "" or self.pass_of_user.get() == "Enter your password:":
            messagebox.showerror(title = "Error",message = "Input your password:")
        else:
            self.usr_register = self.name_of_user.get()
            pss_register = self.pass_of_user.get()
            check_user_query = f'select * from user_details where username = %s and password = %s'
            self.cur.execute(check_user_query,(self.usr_register,pss_register))
            affected_rows = self.cur.rowcount
            if affected_rows!=0:
                messagebox.showerror(title="Already exist..!!",message="User already exists..please login")
                self.username_entry.delete(0,ctk.END)
                self.password_entry.delete(0,ctk.END)
            else:
                check_username_query = f'select * from user_details where username = %s'
                self.cur.execute(check_username_query,(self.usr_register))
                row_affected = self.cur.rowcount
                if row_affected!=0:
                    messagebox.showerror(title="Change username",message="Please change username..")
                else:
                    qstring1 = f"insert into user_details(username,password) values (%s,%s)"
                    self.cur.execute(qstring1,(self.usr_register,pss_register))
                    self.mycon.commit()
                    messagebox.showinfo(title = "Registered successfully",message = "Registered Successfully")
                    user_username = self.usr_register
                    user_password = pss_register
                    returned_fetched_id = self.fetch_id(user_username)
                    quiz_class_object = quiz_class(self.container_frame,user_username,user_password,returned_fetched_id,self.cur,self.mycon,self.add_frames,self.navigate_between_frames)
                    add_frame = quiz_class_object.homescreen_frame
                    #self.add_frames("homescreen",add_frame)
                    self.navigate_between_frames("login","homescreen")
                    self.title("QUIZ HOMESCREEN")

    def check_login(self):
        usr_login = self.name_of_user.get()
        pss_login = self.pass_of_user.get()
        qstring2 = f"select * from user_details where username = %s and password = %s"
        self.cur.execute(qstring2,(usr_login,pss_login))
        if self.cur.rowcount > 0:
            messagebox.showinfo(title = "Login Successfull",message = "Logged in Successfully")
            user_username = usr_login
            user_password = pss_login
            returned_fetched_id = self.fetch_id(usr_login)
            quiz_class_object = quiz_class(self.container_frame,user_username,user_password,returned_fetched_id,self.cur,self.mycon,self.add_frames,self.navigate_between_frames)
            add_frame = quiz_class_object.homescreen_frame
            #.add_frames("homescreen",add_frame)
            self.navigate_between_frames("login","homescreen")
            self.title("QUIZ HOMESCREEN")
        else:
            messagebox.showerror(title = "Login Denied",message = "Please register first..!!")
            self.username_entry.delete(0,ctk.END)
            self.username_entry.insert(0,"Enter your username:")
            self.password_entry.delete(0,ctk.END)
            self.password_entry.insert(0,"Enter your password:")

    def fetch_id(self,usr):
        qstring2 = f'select userid from user_details where username = %s'
        self.cur.execute(qstring2,(usr))
        fetched_id = self.cur.fetchall()
        return fetched_id

if __name__ == "__main__":
    quiz_app = login_class()
    quiz_app.mainloop()



import customtkinter as ctk
import tkinter as tk
from datetime import *
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk

class user_profile(ctk.CTk):
    def __init__(self,parent_frame,current_username,current_password,cur,con,add_frame_method,navigate_method):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame_method
        self.navigate_method = navigate_method
        self.cur = cur
        self.mycon = con
        self.current_usr = current_username
        self.current_psr = current_password

        self.user_profile_frame = ctk.CTkFrame(self.parent_frame,fg_color="#3DC8D8")
        self.user_profile_frame.pack(fill = "both",expand = True)

        self.add_frame_method("userprofile",self.user_profile_frame)

        self.bind("<f>",self.toggle_fullscreen)

        self.bind("<Escape>",self.escape_fullscreen)

        self.user_profile()

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def escape_fullscreen(self,event = None):
        self.overrideredirect(False)

    def user_profile(self):
        back_image = ctk.CTkImage(dark_image=Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\back (1).png"),size = (25,25))

        back_button = ctk.CTkButton(self.user_profile_frame,text="Back",text_color="#000000",fg_color="#ffffff",image=back_image,hover_color="lightgray",height = 50,corner_radius=15,font=ctk.CTkFont(family="Helvetica",weight = "bold",size = 20),command = self.return_to_home)
        back_button.pack(anchor = "nw",padx = 50,pady = (10,0))

        self.main_frame = ctk.CTkFrame(self.user_profile_frame,border_width = 1,border_color = "#000000",fg_color = "#ffffff",corner_radius=25)
        self.main_frame.pack(side = "top",fill = "both",expand = True,padx = 50,pady = (5,30))

        user_image = ctk.CTkImage(dark_image=Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\user.png"),size = (50,50))
        user_img_label = ctk.CTkLabel(self.main_frame,text = "",image=user_image,height=100,width=50,corner_radius=50,fg_color="lightgray")
        user_img_label.pack(side = "top",pady = (10,0))

        self.username_label = ctk.CTkLabel(self.main_frame,fg_color = "#ffffff",text = "Username:",text_color = "#000000",corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 30))
        self.username_label.pack(anchor = "nw",padx = 10,pady = (20,0))
        
        self.current_username = self.current_usr
        self.show_username = ctk.CTkEntry(self.main_frame,height = 50,corner_radius = 10,fg_color = "#ffffff",font = ctk.CTkFont(family = "Arial",size = 20,weight = "bold"))
        self.show_username.insert(0,self.current_username)
        self.show_username.configure(state = "disabled")
        self.show_username.pack(anchor = "nw",padx = (15,250),fill = "x",pady = 5)

        self.password_label = ctk.CTkLabel(self.main_frame,fg_color = "#ffffff",text = "Password:",text_color = "#000000",corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 30,weight = "normal"))
        self.password_label.pack(anchor = "nw",padx = 10,pady = (50,0))

        self.outer_frame = ctk.CTkFrame(self.main_frame,height=50,corner_radius=10,fg_color="#ffffff")
        self.outer_frame.pack(fill = "x",padx = 5,pady = 5)

        self.current_password = self.current_psr
        self.len_of_pass = len(self.current_password)
        answer = "*" * self.len_of_pass
        
        self.show_password = ctk.CTkEntry(self.outer_frame,height = 50,width=700,corner_radius = 10,fg_color = "#ffffff",font = ctk.CTkFont(family = "Arial",size = 20,weight = "bold"))
        self.show_password.insert(0,answer)
        self.show_password.configure(state = "disabled")
        self.show_password.pack(side = "left",pady = 5,padx = (5,0))

        self.hide_button = ctk.CTkButton(self.outer_frame,text = "Show",height=50,corner_radius=10,text_color="#000000",fg_color="#3DC8D8",font=ctk.CTkFont(family="Helvetica",size = 30,weight="normal"),command = self.hide)
        self.hide_button.pack(side = "right",padx = (5,300),pady = 5)

        self.option_label = ctk.CTkLabel(self.main_frame,text = "DO YOU WANT TO CHANGE CREDENTIAL?",text_color="#000000",fg_color="#ffffff",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25))
        self.option_label.pack(anchor = "nw",padx = 15,pady = (50,0))

        self.change_credential_button = ctk.CTkButton(self.main_frame,text = "Change Credential",height=45,text_color="#000000",fg_color="#3DC8D8",corner_radius=15,font = ctk.CTkFont(family="Helvetica",weight = "bold",size = 25),command=self.change)
        self.change_credential_button.pack(anchor = "nw",padx = 15,pady = 5)
        
        self.edit_button_frame = ctk.CTkFrame(self.main_frame,fg_color="#ffffff",height = 50,corner_radius=5)
        self.edit_button_frame.pack(fill = "x",padx = 5,pady = (15,0))

        self.new_username = ctk.CTkButton(self.edit_button_frame,text = "Edit Username",text_color="#000000",height=50,hover_color="lightgray",fg_color="#3DC8D8",corner_radius=15,font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 20),command = self.new_usr)
        self.new_username.pack_forget()

        self.new_password = ctk.CTkButton(self.edit_button_frame,text = "Edit Password",text_color="#000000",height=50,hover_color="lightgray",fg_color="#3DC8D8",corner_radius=15,font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 20),command = self.new_psr)
        self.new_password.pack_forget()

    def return_to_home(self,):
        self.navigate_method("userprofile","homescreen")

    def change(self):
        self.new_username.pack(side = "left",padx = 10,pady = 3)
        self.new_password.pack(side = "right",padx = 10,pady = 3)

    def new_usr(self):
        new_usr = ctk.CTkInputDialog(text = "Enter new username:",title="Edit username",fg_color="gray",button_fg_color="#3DC8D8",button_hover_color="lightgray",button_text_color="#000000",entry_fg_color="#ffffff",entry_border_color="#000000",entry_text_color="#000000",font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"))
        new_usr_value = new_usr.get_input()
        if new_usr_value:
            update_query = f'update user_details set username = %s where username = %s'
            self.cur.execute(update_query,(new_usr_value,self.current_username))
            self.mycon.commit()
            self.show_username.configure(state = "normal")
            self.show_username.delete(0,"end")
            self.show_username.insert(0,new_usr_value)
            self.current_username = new_usr_value

    def new_psr(self):
        new_psr = ctk.CTkInputDialog(text = "Enter new password:",title="Edit password",fg_color="gray",button_fg_color="#3DC8D8",button_hover_color="lightgray",button_text_color="#000000",entry_fg_color="#ffffff",entry_border_color="#000000",entry_text_color="#000000",font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"))
        new_psr_value = new_psr.get_input()
        if new_psr_value:
            updated_answer = "*"*len(self.new_psr_value)
            update_query = f'update user_details set password = %s where password = %s'
            self.cur.execute(update_query,(new_psr_value,self.current_password))
            self.current_password = new_psr_value
            self.mycon.commit()
            self.show_password.configure(state = "normal")
            self.show_password.delete(0,"end")
            self.show_password.insert(0,updated_answer)

    def hide(self):
        if self.hide_button.cget("text") == "Hide":
            answer = "*" * self.len_of_pass
            self.show_password.configure(state = "normal")
            self.show_password.delete(0,"end")
            self.show_password.insert(0,answer)
            self.show_password.configure(state = "disabled")
            self.hide_button.configure(text = "Show")
        else:
            self.show_password.configure(state = "normal")
            self.show_password.delete(0,"end")
            self.show_password.insert(0,self.current_password)
            self.show_password.configure(state = "disabled")
            self.hide_button.configure(text = "Hide")

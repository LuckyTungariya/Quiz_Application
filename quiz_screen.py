import customtkinter as ctk
import tkinter as tk
from datetime import *
from user_profile_screen import user_profile
from user_choice_screen import user_choice
from responses_screen import saved_responses
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk

class quiz_class(ctk.CTk):
    def __init__(self,parent_frame,username,password,id,cur,mycon,add_frame_method,navigate_method):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame_method
        self.navigate_frame_method = navigate_method

        self.homescreen_frame = ctk.CTkFrame(self.parent_frame)
        self.homescreen_frame.pack(fill = "both",expand = "True")

        self.add_frame_method("homescreen",self.homescreen_frame)

        self.cur = cur
        self.mycon = mycon
        self.name = username
        self.pass_details = password
        self.id = id

        self.create_quiz_screen()

        self.current_question_index = 0
        self.score = 0
        self.answerkey_result = []
        self.user_responses = [None]*10
        self.user_responses_int = []

        self.bind("<f>",self.toggle_fullscreen)

        self.bind("<Escape>",self.escape_fullscreen)

        self.user_profile_object = user_profile(self.parent_frame,self.name,self.pass_details,self.cur,self.mycon,self.add_frame_method,self.navigate_frame_method)

    def create_quiz_screen(self):
        self.right_frame = ctk.CTkFrame(self.homescreen_frame,fg_color = "#ffffff",width = 500)
        self.right_frame.pack(side = "right",fill = "x")

        self.quiz_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\quiz_photo.webp"),size = (500,350))
        self.quiz_image_label = ctk.CTkLabel(self.right_frame,text = "",image = self.quiz_image)
        self.quiz_image_label.pack(side = "top")

        self.question_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\ques.jpg"),size = (500,350))
        self.question_image_label = ctk.CTkLabel(self.right_frame,text = "",image = self.question_image)
        self.question_image_label.pack(side = "bottom")

        self.left_frame = ctk.CTkFrame(self.homescreen_frame,fg_color = "#44dfc4")
        self.left_frame.pack(side = "left",fill = "both",expand = True)

        self.top_label = ctk.CTkLabel(self.left_frame,height = 100,fg_color = "#939393",corner_radius = 20,text = "SIMPLE PROGRAMMING QUIZ",font = ctk.CTkFont(family = "Verdana",size = 30,weight = "bold"))
        self.top_label.pack(side = "top",fill = "x",padx = 10,pady = 10)
        
        self.welcome_label = ctk.CTkLabel(self.left_frame,height = 40,text_color = "#000000",fg_color = "#ffffff",corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"))
        self.welcome_label.configure(text = "WELCOME"+" "+ self.name.upper())
        self.welcome_label.pack(pady = 20)

        self.message_label = ctk.CTkLabel(self.left_frame,text = "START WITH A NEW QUIZ NOW..!!",text_color = "#000000",fg_color = "#44dfc4",font = ctk.CTkFont(family = "ARIAL",size = 30,weight = "normal"))
        self.message_label.pack(padx = 10,pady = 20)

        self.profile_and_view_frame = ctk.CTkFrame(self.left_frame,height = 100,fg_color = "#44dfc4")
        self.profile_and_view_frame.pack(fill = "x",padx = 5,pady = 10)
        
        self.profile_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\avatar.png"),size = (35,35))
        self.see_profile_button = ctk.CTkButton(self.profile_and_view_frame,image = self.profile_image,text = "My Profile",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 200,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.user_profile)
        self.see_profile_button.pack(side = "left",padx = 20)
        
        self.history_image =  ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\sourcing.png"),size = (35,35))
        self.view_history = ctk.CTkButton(self.profile_and_view_frame,image = self.history_image,text = "Quiz History",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 150,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.view)
        self.view_history.pack(side = "right",padx = (0,30))
        
        self.start_and_signout_frame = ctk.CTkFrame(self.left_frame,height = 100,fg_color = "#44dfc4")
        self.start_and_signout_frame.pack(fill = "x",padx = 5,pady = 30)

        self.start_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\explorer.png"),size = (35,35))
        self.start_quiz_button = ctk.CTkButton(self.start_and_signout_frame,image = self.start_image,text = "Start Quiz",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 150,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.selection)
        self.start_quiz_button.pack(side = "left",padx = 20)

        self.signout_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\logout.png"),size = (35,35))
        self.signout_button = ctk.CTkButton(self.start_and_signout_frame,image = self.signout_image,text = "Sign Out",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 190,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.user_signout)
        self.signout_button.pack(side = "right",padx = (0,60))

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def escape_fullscreen(self,event = None):
        self.overrideredirect(False)

    def user_profile(self):
        self.navigate_frame_method("homescreen","userprofile")

    def user_signout(self):
        response = messagebox.askyesno(title = "Confirm Signout",message = "Are You Sure You Want To Sign Out?")
        if response:
            self.navigate_frame_method("homescreen","login")

            messagebox.showinfo(title = "Signout Successful",message = "Successfully Signed out")
        else:
            print("Not Signed Out..")

    def selection(self):
        user_choice_object = user_choice(self.parent_frame,self.cur,self.mycon,self.id,self.add_frame_method,self.navigate_frame_method)
        self.navigate_frame_method("homescreen","userchoice")

    def view(self):
        saved_responses_object = saved_responses(self.parent_frame,self.cur,self.id,self.add_frame_method,self.navigate_frame_method)
        self.navigate_frame_method("homescreen","response")

import customtkinter as ctk
import tkinter as tk
from datetime import *
from tkinter import messagebox,PhotoImage
from questions_screen import question_screen
from PIL import Image,ImageTk

class user_choice(ctk.CTk):
    def __init__(self,parent_frame,cur,mycon,id,add_frame_method,navigate_method):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame_method
        self.navigate_method = navigate_method

        self.user_choice_frame = ctk.CTkFrame(self.parent_frame,fg_color="#3DC8D8")
        self.user_choice_frame.pack(fill = "both",expand = True)

        self.add_frame_method("userchoice",self.user_choice_frame)

        self.title("Select preferred domain")
        self.cur = cur
        self.mycon = mycon
        self.id = id

        self.bind("<f>",self.toggle_fullscreen)

        self.bind("<Escape>",self.escape_fullscreen)

        self.selection()

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def escape_fullscreen(self,event = None):
        self.overrideredirect(False)

    def selection(self):
        self.top_frame = ctk.CTkFrame(self.user_choice_frame,fg_color = "#ffffff")
        self.top_frame.pack(side = "top",fill = "x",padx = 20,pady = 5)
        
        back_image = ctk.CTkImage(dark_image=Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\back (1).png"),size = (25,25))
        self.back_button = ctk.CTkButton(self.top_frame,corner_radius = 15,image=back_image,fg_color = "#29B6F6",text = "Back",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 30),command = self.homescreen)
        self.back_button.pack(side = "left",padx = 20,pady = 10)

        self.select_label = ctk.CTkLabel(self.top_frame,corner_radius = 15,fg_color = "#ffffff",text = "SELECT PREFERRED DOMAIN",text_color = "#000000",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 30))
        self.select_label.pack(side = "right",padx = (0,350),pady = 10)

        self.choice_frame1 = ctk.CTkFrame(self.user_choice_frame,height = 200,corner_radius = 15,fg_color = "#ffffff",border_color = "#000000",border_width = 1)
        self.choice_frame1.pack(fill = "both",expand = True,padx = 30,pady = (5,70))

        self.python_button = ctk.CTkButton(self.choice_frame1,text = "PYTHON",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.python_quiz)
        self.python_button.pack(side = "top",padx = 100,pady = 30)

        self.c_button = ctk.CTkButton(self.choice_frame1,text = "C++",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.c_quiz)
        self.c_button.pack(side = "top",padx = 100,pady = 30)

        self.java_button = ctk.CTkButton(self.choice_frame1,text = "JAVA",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.java_quiz)
        self.java_button.pack(side = "top",padx = 100,pady = 30)

        self.sql_button = ctk.CTkButton(self.choice_frame1,text = "SQL",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.sql_quiz)
        self.sql_button.pack(side = "top",padx = 100,pady = 30)

    def homescreen(self):
        self.navigate_method("userchoice","homescreen")

    def python_quiz(self):
        response = messagebox.askyesno(title = "Ask",message="Do you want to start quiz in python?")
        if response:
            self.current_question_index = 0
            self.score = 0
            qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from python_questions"
            self.cur.execute(qstring3)
            self.qstring3_result = self.cur.fetchall()
            button_text = self.python_button.cget("text")

            answerkey = f'select correct_option from python_questions'
            self.cur.execute(answerkey)
            self.answerkey_result_tuple = self.cur.fetchall()
            self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]

            question_screen_obj = question_screen(self.parent_frame,self.id,self.mycon,self.cur,self.qstring3_result,self.answerkey_result,button_text,self.add_frame_method,self.navigate_method)
            self.navigate_method("userchoice","questions")
        

    def c_quiz(self):
        response = messagebox.askyesno(title = "Ask",message="Do you want to start quiz in c++?")
        if response:
            self.current_question_index = 0
            self.score = 0
            qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from c_questions"
            self.cur.execute(qstring3)
            self.qstring3_result = self.cur.fetchall()
            button_text = self.c_button.cget("text")

            answerkey = f'select correct_option from c_questions'
            self.cur.execute(answerkey)
            self.answerkey_result_tuple = self.cur.fetchall()
            self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]
            #print(self.answerkey_result)
            question_screen_obj = question_screen(self.parent_frame,self.id,self.mycon,self.cur,self.qstring3_result,self.answerkey_result,button_text,self.add_frame_method,self.navigate_method)
            self.navigate_method("userchoice","questions")

    def java_quiz(self):
        response = messagebox.askyesno(title = "Ask",message="Do you want to start quiz in java?")
        if response:
            self.current_question_index = 0
            self.score = 0
            qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from java_questions"
            self.cur.execute(qstring3)
            self.qstring3_result = self.cur.fetchall()
            button_text = self.java_button.cget("text")

            answerkey = f'select correct_option from java_questions'
            self.cur.execute(answerkey)
            self.answerkey_result_tuple = self.cur.fetchall()
            self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]
            
            question_screen_obj = question_screen(self.parent_frame,self.id,self.mycon,self.cur,self.qstring3_result,self.answerkey_result,button_text,self.add_frame_method,self.navigate_method)
            self.navigate_method("userchoice","questions")

    def sql_quiz(self):
        response = messagebox.askyesno(title = "Ask",message="Do you want to start quiz in sql?")
        if response:
            self.current_question_index = 0
            self.score = 0
            qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from sql_questions"
            self.cur.execute(qstring3)
            self.qstring3_result = self.cur.fetchall()
            button_text = self.sql_button.cget("text")

            answerkey = f'select correct_option from sql_questions'
            self.cur.execute(answerkey)
            self.answerkey_result_tuple = self.cur.fetchall()
            self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]

            question_screen_obj = question_screen(self.parent_frame,self.id,self.mycon,self.cur,self.qstring3_result,self.answerkey_result,button_text,self.add_frame_method,self.navigate_method)
            self.navigate_method("userchoice","questions")

import customtkinter as ctk 
import tkinter as tk
from datetime import *
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk
import pymysql as psql

class login_class:
    def __init__(self):
        self.login_page()

        self.mycon = psql.connect(host = "localhost",user = "root",password = "root",port = 3307,charset = 'utf8',db = 'projects')
        self.cur = self.mycon.cursor()
        print("connected")

    def login_page(self):
        self.login_screen = ctk.CTk()
        self.login_screen.geometry("500x500")
        self.login_screen.resizable(False,False)
        self.login_screen.configure(fg_color = "lightgray")
        self.login_screen.title("LOGIN PAGE")
        self.login_background_image = ctk.CTkImage(dark_image = Image.open("C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\Quiz Application\\login_background.webp"),size = (500,500))
        self.login_label = ctk.CTkLabel(self.login_screen,image = self.login_background_image,text = "")
        self.login_label.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
        
        self.name_of_user = ctk.StringVar()
        self.name_of_user.set("Enter your username:")
        self.username_entry = ctk.CTkEntry(self.login_screen,height = 35,textvariable=self.name_of_user,fg_color = "#ffffff",text_color = "#000000",placeholder_text_color = "#000000",placeholder_text="Enter Username:")
        self.username_entry.place(relx = 0.5,rely = 0.3,relwidth = 0.7,anchor = "center")
      
        self.pass_of_user = ctk.StringVar()
        self.pass_of_user.set("Enter your password:")
        self.password_entry = ctk.CTkEntry(self.login_screen,height = 35,textvariable=self.pass_of_user,fg_color = "#ffffff",text_color = "#000000",placeholder_text_color = "#000000",placeholder_text="Enter Password:")
        self.password_entry.place(relx = 0.5,rely = 0.5,relwidth = 0.7,anchor = "center")

        self.login_button = ctk.CTkButton(self.login_screen,text = "LOGIN",text_color = "#000000",font = ctk.CTkFont(family = " Consolas",size = 20),fg_color = "#F5F5F5",hover_color = "darkgray",command = self.check_login)
        self.login_button.place(relx = 0.15,rely = 0.68,relwidth = 0.3)

        self.register_button = ctk.CTkButton(self.login_screen,text = "REGISTER",text_color = "#000000",font = ctk.CTkFont(family = " Consolas",size = 20),fg_color = "#F5F5F5",hover_color = "darkgray",command = self.register)
        self.register_button.place(relx = 0.55,rely = 0.68,relwidth = 0.3)

    def register(self):
        if self.name_of_user.get() == "":
            messagebox.showerror(title = "Error",message = "Input your username:")
        if self.pass_of_user.get() == "":
            messagebox.showerror(title = "Error",message = "Input your password:")
        else:
            usr_register = self.name_of_user.get()
            pss_register = self.pass_of_user.get()
            check_user_query = f'select * from user_details where username = %s and password = %s'
            self.cur.execute(check_user_query,(usr_register,pss_register))
            affected_rows = self.cur.rowcount
            if affected_rows!=0:
                messagebox.showerror(title="Already exist..!!",message="User already exists..please login")
            else:
                check_username_query = f'select * from user_details where username = %s'
                self.cur.execute(check_username_query,(usr_register))
                row_affected = self.cur.rowcount
                if row_affected!=0:
                    messagebox.showerror(title="Change username",message="Please change username..")
                else:
                    qstring1 = f"insert into user_details(username,password) values (%s,%s)"
                    self.cur.execute(qstring1,(usr_register,pss_register))
                    self.mycon.commit()
                    messagebox.showinfo(title = "Registered successfully",message = "Registered Successfully")
                    self.login_screen.destroy()
                    user_username = usr_register
                    user_password = pss_register
                    quiz_class_object = quiz_class(user_username,user_password,self.cur,self.mycon)
                    quiz_class_object.quiz_screen.mainloop()

    def check_login(self):
        usr_login = self.name_of_user.get()
        pss_login = self.pass_of_user.get()
        qstring2 = f"select * from user_details where username = %s and password = %s"
        self.cur.execute(qstring2,(usr_login,pss_login))
        if self.cur.rowcount > 0:
            messagebox.showinfo(title = "Login Successfull",message = "Logged in Successfully")
            self.login_screen.destroy()
            user_username = usr_login
            user_password = pss_login
            quiz_class_object = quiz_class(user_username,user_password,self.cur,self.mycon)
            quiz_class_object.quiz_screen.mainloop()
        else:
            messagebox.showerror(title = "Login Denied",message = "Please register first..!!")
            self.username_entry.delete(0,tk.END)
            self.username_entry.insert(0,"Enter Username:")
            self.password_entry.delete(0,tk.END)
            self.password_entry.insert(0,"Enter Password:")

class quiz_class():
    def __init__(self,username,password,cur,mycon):
        self.cur = cur
        self.mycon = mycon
        self.name = username
        self.pass_details = password

        self.create_quiz_screen()

    def create_quiz_screen(self):
        self.quiz_screen = ctk.CTk()
        #self.back_image = tk.PhotoImage(file = "C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\Quiz Application\\back (1).png")
        self.width = self.quiz_screen.winfo_screenwidth()
        self.height = self.quiz_screen.winfo_screenheight()
        #self.quiz_screen.geometry("800x800")
        self.quiz_screen.geometry('{}x{}+{}+{}'.format(self.width,self.height,0,0))
        self.quiz_screen.configure(fg_color = "#ffffff")
        self.quiz_screen.title("QUIZ HOMESCREEN")

        self.current_question_index = 0
        self.score = 0
        self.answerkey_result = []
        self.user_responses = [None]*10
       # print(self.user_responses)
        self.user_responses_int = []

        self.right_frame = ctk.CTkFrame(self.quiz_screen,fg_color = "#ffffff",width = 500)
        self.right_frame.pack(side = "right",fill = "x")

        self.quiz_image = ctk.CTkImage(dark_image = Image.open("C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\Quiz Application\\quiz_photo.webp"),size = (500,350))
        self.quiz_image_label = ctk.CTkLabel(self.right_frame,text = "",image = self.quiz_image)
        self.quiz_image_label.pack(side = "top")

        self.question_image = ctk.CTkImage(dark_image = Image.open("C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\Quiz Application\\ques.jpg"),size = (500,350))
        self.question_image_label = ctk.CTkLabel(self.right_frame,text = "",image = self.question_image)
        self.question_image_label.pack(side = "bottom")

        self.left_frame = ctk.CTkFrame(self.quiz_screen,fg_color = "#44dfc4")
        self.left_frame.pack(side = "left",fill = "both",expand = True)

        self.top_label = ctk.CTkLabel(self.left_frame,height = 100,fg_color = "#939393",corner_radius = 20,text = "SIMPLE PROGRAMMING QUIZ",font = ctk.CTkFont(family = "Verdana",size = 30,weight = "bold"))
        self.top_label.pack(side = "top",fill = "x",padx = 10,pady = 10)
        
        self.welcome_label = ctk.CTkLabel(self.left_frame,height = 40,text_color = "#000000",fg_color = "#ffffff",corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"))
        self.welcome_label.configure(text = "WELCOME"+" "+self.name.upper())
        self.welcome_label.pack(pady = 20)

        self.message_label = ctk.CTkLabel(self.left_frame,text = "START WITH A NEW QUIZ NOW..!!",text_color = "#000000",fg_color = "#44dfc4",font = ctk.CTkFont(family = "ARIAL",size = 30,weight = "normal"))
        self.message_label.pack(padx = 10,pady = 20)

        self.profile_and_view_frame = ctk.CTkFrame(self.left_frame,height = 100,fg_color = "#44dfc4")
        self.profile_and_view_frame.pack(fill = "x",padx = 5,pady = 10)
        
        self.profile_image = ctk.CTkImage(dark_image = Image.open(r"C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\Quiz Application\\avatar.png"),size = (35,35))
        self.see_profile_button = ctk.CTkButton(self.profile_and_view_frame,image = self.profile_image,text = "My Profile",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 200,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.user_profile)
        self.see_profile_button.pack(side = "left",padx = 20)
        
        self.history_image =  ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\sourcing.png"),size = (35,35))
        self.view_history = ctk.CTkButton(self.profile_and_view_frame,image = self.history_image,text = "Quiz History",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 150,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"))
        self.view_history.pack(side = "right",padx = (0,30))
        
        self.start_and_signout_frame = ctk.CTkFrame(self.left_frame,height = 100,fg_color = "#44dfc4")
        self.start_and_signout_frame.pack(fill = "x",padx = 5,pady = 30)

        self.start_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\explorer.png"),size = (35,35))
        self.start_quiz_button = ctk.CTkButton(self.start_and_signout_frame,image = self.start_image,text = "Start Quiz",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 150,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.selection)
        self.start_quiz_button.pack(side = "left",padx = 20)

        self.signout_image = ctk.CTkImage(dark_image = Image.open(r"C:\\Users\\lucky\\OneDrive\\Desktop\\SYCS SEM3\\Quiz Application\\logout.png"),size = (35,35))
        self.signout_button = ctk.CTkButton(self.start_and_signout_frame,image = self.signout_image,text = "Sign Out",text_color = "#000000",fg_color = "#29B6F6",height = 60,width = 190,corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 25,weight = "bold"),command = self.user_signout)
        self.signout_button.pack(side = "right",padx = (0,60))

    def user_profile(self):
        self.user_profile_screen = ctk.CTk()
        self.user_profile_screen.title("MY PROFILE")
        self.user_profile_screen.geometry('{}x{}+{}+{}'.format(self.width,self.height,-1,-1))
        self.user_profile_screen.resizable(False,False)
        self.user_profile_screen.configure(fg_color = "#3DC8D8")

        back_button = ctk.CTkButton(self.user_profile_screen,text="Back",text_color="#000000",fg_color="#ffffff",hover_color="lightgray",height = 50,corner_radius=15,font=ctk.CTkFont(family="Helvetica",weight = "bold",size = 20),command = self.return_to_home)
        back_button.pack(anchor = "nw",padx = 50,pady = (10,0))

        self.main_frame = ctk.CTkFrame(self.user_profile_screen,border_width = 1,border_color = "#000000",fg_color = "#ffffff",corner_radius=25)
        self.main_frame.pack(side = "top",fill = "both",expand = True,padx = 50,pady = (5,30))

        self.username_label = ctk.CTkLabel(self.main_frame,fg_color = "#ffffff",text = "Username:",text_color = "#000000",corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 30))
        self.username_label.pack(anchor = "nw",padx = 10,pady = (50,0))
        
        self.current_username = self.name
        self.show_username = ctk.CTkEntry(self.main_frame,height = 50,corner_radius = 10,fg_color = "#ffffff",font = ctk.CTkFont(family = "Arial",size = 20,weight = "bold"))
        self.show_username.insert(0,self.current_username)
        self.show_username.configure(state = "disabled")
        self.show_username.pack(anchor = "nw",padx = (15,250),fill = "x",pady = 5)

        self.password_label = ctk.CTkLabel(self.main_frame,fg_color = "#ffffff",text = "Password:",text_color = "#000000",corner_radius = 20,font = ctk.CTkFont(family = "Helvetica",size = 30,weight = "normal"))
        self.password_label.pack(anchor = "nw",padx = 10,pady = (70,0))

        self.outer_frame = ctk.CTkFrame(self.main_frame,height=50,corner_radius=10,fg_color="#ffffff")
        self.outer_frame.pack(fill = "x",padx = 5,pady = 5)

        self.current_password = self.pass_details
        self.len_of_pass = len(self.current_password)
        answer = "*" * self.len_of_pass
        
        self.show_password = ctk.CTkEntry(self.outer_frame,height = 50,width=700,corner_radius = 10,fg_color = "#ffffff",font = ctk.CTkFont(family = "Arial",size = 20,weight = "bold"))
        self.show_password.insert(0,answer)
        self.show_password.configure(state = "disabled")
        self.show_password.pack(side = "left",pady = 5,padx = (5,0))

        self.hide_button = ctk.CTkButton(self.outer_frame,text = "Show",height=50,corner_radius=10,text_color="#000000",fg_color="#3DC8D8",font=ctk.CTkFont(family="Helvetica",size = 30,weight="normal"),command = self.hide)
        self.hide_button.pack(side = "right",padx = (5,300),pady = 5)

        self.option_label = ctk.CTkLabel(self.main_frame,text = "DO YOU WANT TO CHANGE CREDENTIAL?",text_color="#000000",fg_color="#ffffff",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25))
        self.option_label.pack(anchor = "nw",padx = 15,pady = (60,0))

        self.change_credential_button = ctk.CTkButton(self.main_frame,text = "Change Credential",height=45,text_color="#000000",fg_color="#3DC8D8",corner_radius=15,font = ctk.CTkFont(family="Helvetica",weight = "bold",size = 25),command=self.change)
        self.change_credential_button.pack(anchor = "nw",padx = 15,pady = 5)
        
        self.edit_button_frame = ctk.CTkFrame(self.main_frame,fg_color="#ffffff",height = 100,corner_radius=5)
        self.edit_button_frame.pack(fill = "x",padx = 5,pady = (25,0))

        self.new_username = ctk.CTkButton(self.edit_button_frame,text = "Edit Username",text_color="#000000",height=50,hover_color="lightgray",fg_color="#3DC8D8",corner_radius=15,font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 20),command = self.new_usr)
        self.new_username.pack_forget()

        self.new_password = ctk.CTkButton(self.edit_button_frame,text = "Edit Password",text_color="#000000",height=50,hover_color="lightgray",fg_color="#3DC8D8",corner_radius=15,font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 20),command = self.new_psr)
        self.new_password.pack_forget()

        self.user_profile_screen.mainloop()

    def return_to_home(self):
        if self.user_profile_screen and self.user_profile_screen.winfo_exists():
            self.user_profile_screen.destroy()

    def change(self):
        self.new_username.pack(side = "left",padx = 10,pady = 3)
        self.new_password.pack(side = "right",padx = 10,pady = 3)

    def new_usr(self):
        new_usr = ctk.CTkInputDialog(text = "Enter new username:",title="Edit username",fg_color="gray",button_fg_color="#3DC8D8",button_hover_color="lightgray",button_text_color="#000000",entry_fg_color="#ffffff",entry_border_color="#000000",entry_text_color="#000000",font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"))
        self.new_usr_value = new_usr.get_input()
        update_query = f'update user_details set username = %s where username = %s'
        self.cur.execute(update_query,(self.new_usr_value,self.current_username))
        self.mycon.commit()
        self.show_username.configure(state = "normal")
        self.show_username.delete(0,"end")
        self.show_username.insert(0,self.new_usr_value)

    def new_psr(self):
        new_psr = ctk.CTkInputDialog(text = "Enter new password:",title="Edit password",fg_color="gray",button_fg_color="#3DC8D8",button_hover_color="lightgray",button_text_color="#000000",entry_fg_color="#ffffff",entry_border_color="#000000",entry_text_color="#000000",font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"))
        self.new_psr_value = new_psr.get_input()
        updated_answer = "*"*len(self.new_psr_value)
        update_query = f'update user_details set password = %s where password = %s'
        self.cur.execute(update_query,(self.new_psr_value,self.current_password))
        self.current_password = self.new_psr_value
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

    def user_signout(self):
        response = messagebox.askyesno(title = "Confirm Signout",message = "Are You Sure You Want To Sign Out?")
        if response:
            self.quiz_screen.destroy()
            messagebox.showinfo(title = "Signout Successful",message = "Successfully Signed out")
           # login_class_object = login_class()
           # login_class_object.login_page()
        else:
            print("Not Signed Out..")

    def selection(self):
        self.user_choice = ctk.CTk()
        width = self.user_choice.winfo_screenwidth()
        height = self.user_choice.winfo_screenheight()
        self.user_choice.geometry('{}x{}+{}+{}'.format(width,height,0,0))
        self.user_choice.configure(fg_color = "#3DC8D8")
        self.user_choice.title("Select preferred domain")

        self.top_frame = ctk.CTkFrame(self.user_choice,fg_color = "#ffffff")
        self.top_frame.pack(side = "top",fill = "x",padx = 20,pady = 5)

        self.back_button = ctk.CTkButton(self.top_frame,corner_radius = 15,fg_color = "#29B6F6",text = "Back",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 30),command = self.homescreen)
        self.back_button.pack(side = "left",padx = 20,pady = 10)

        self.select_label = ctk.CTkLabel(self.top_frame,corner_radius = 15,fg_color = "#ffffff",text = "SELECT PREFERRED DOMAIN",text_color = "#000000",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 30))
        self.select_label.pack(side = "right",padx = (0,350),pady = 10)

        self.choice_frame1 = ctk.CTkFrame(self.user_choice,height = 200,corner_radius = 15,fg_color = "#ffffff",border_color = "#000000",border_width = 1)
        self.choice_frame1.pack(fill = "both",expand = True,padx = 30,pady = (5,70))

        self.python_button = ctk.CTkButton(self.choice_frame1,text = "PYTHON",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.python_quiz)
        self.python_button.pack(side = "top",padx = 100,pady = 30)

        self.c_button = ctk.CTkButton(self.choice_frame1,text = "C++",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.c_quiz)
        self.c_button.pack(side = "top",padx = 100,pady = 30)

        self.java_button = ctk.CTkButton(self.choice_frame1,text = "JAVA",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.java_quiz)
        self.java_button.pack(side = "top",padx = 100,pady = 30)

        self.sql_button = ctk.CTkButton(self.choice_frame1,text = "SQL",text_color = "#000000",height = 60,width = 150,fg_color = "#29B6F6",corner_radius = 15,font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 25),command = self.sql_quiz)
        self.sql_button.pack(side = "top",padx = 100,pady = 30)
        
        self.user_choice.mainloop()

    def homescreen(self):
        self.user_choice.destroy()

    def python_quiz(self):
        self.current_question_index = 0
        self.score = 0
        python_qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from python_questions"
        self.cur.execute(python_qstring3)
        self.qstring3_result = self.cur.fetchall()

        python_answerkey = f'select correct_option from python_questions'
        self.cur.execute(python_answerkey)
        self.answerkey_result_tuple = self.cur.fetchall()
        self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]
       # print(self.answerkey_result)

        self.start_quiz()
        

    def c_quiz(self):
        self.current_question_index = 0
        self.score = 0
        c_qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from c_questions"
        self.cur.execute(c_qstring3)
        self.qstring3_result = self.cur.fetchall()

        c_answerkey = f'select correct_option from c_questions'
        self.cur.execute(c_answerkey)
        self.answerkey_result_tuple = self.cur.fetchall()
        self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]
        #print(self.answerkey_result)

        self.start_quiz()

    def java_quiz(self):
        self.current_question_index = 0
        self.score = 0
        c_qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from java_questions"
        self.cur.execute(c_qstring3)
        self.qstring3_result = self.cur.fetchall()

        c_answerkey = f'select correct_option from java_questions'
        self.cur.execute(c_answerkey)
        self.answerkey_result_tuple = self.cur.fetchall()
        self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]

        self.start_quiz()

    def sql_quiz(self):
        self.current_question_index = 0
        self.score = 0
        c_qstring3 = f"select Srno,question,option1,option2,option3,option4,correct_option from sql_questions"
        self.cur.execute(c_qstring3)
        self.qstring3_result = self.cur.fetchall()

        c_answerkey = f'select correct_option from sql_questions'
        self.cur.execute(c_answerkey)
        self.answerkey_result_tuple = self.cur.fetchall()
        self.answerkey_result = [item[0] for item in self.answerkey_result_tuple]

        self.start_quiz() 

    def start_quiz(self):
        self.questions_screen = ctk.CTk()
        self.questions_screen.configure(fg_color = "#3DC8D8")
        width = self.questions_screen.winfo_screenwidth()
        height = self.questions_screen.winfo_screenheight()
        self.questions_screen.geometry('{}x{}+{}+{}'.format(width,height,0,0))
        # self.questions_screen.geometry("700x700")
        self.questions_screen.title("Questions")

        self.timer_label = ctk.CTkLabel(self.questions_screen,fg_color = "#ffffff",height = 30,width = 80,text = "Timer :"+ str(60),text_color = "#000000",corner_radius = 20,font = ('Trebuchet MS',25,"bold"))
        self.timer_label.pack(anchor = "ne",padx = (0,30),pady = 40)

        self.question_frame = ctk.CTkFrame(self.questions_screen,border_width = 1,border_color = "#959595",corner_radius = 20,fg_color = "#ffffff")
        self.question_frame.pack(fill = "both",expand = True,padx = 30,pady = 20)

        self.time_left = 60
        self.update_timer()

        self.top_question_frame = ctk.CTkFrame(self.question_frame,height = 70,fg_color = "#ffffff",corner_radius = 10)
        self.top_question_frame.pack(side = "top",fill = "x",padx = 5,pady = 10)

        self.mcq_label = ctk.CTkLabel(self.top_question_frame,text_color = "#000000",font = ctk.CTkFont(family = "Garamold",size = 16,weight = "bold"))
        self.mcq_label.pack(side = "left",pady = 10,padx = 40)

        self.quit_button = ctk.CTkButton(self.top_question_frame,height = 50,width = 100,corner_radius = 20,border_width = 1,border_color = "#000000",border_spacing = 2,fg_color = "#FF5B5D",text = "Quit",text_color = "#000000",command = self.quit_page) 
        self.quit_button.pack(side = "right",pady = 10,padx = 40)
        
        self.radiobutton_value = ctk.StringVar()
        self.radiobutton_a = ctk.CTkRadioButton(self.question_frame,variable=self.radiobutton_value,height = 50,width = 80,radiobutton_height = 20,radiobutton_width = 20,corner_radius = 16,border_color = "#000000",fg_color = "#939393",text_color = "#000000",hover_color = "darkgray",value = 1,font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "bold"))
        self.radiobutton_a.pack(anchor = "nw",padx = 35,pady = 25)
        
        self.radiobutton_b = ctk.CTkRadioButton(self.question_frame,variable = self.radiobutton_value,height = 50,width = 80,radiobutton_height = 20,radiobutton_width = 20,corner_radius = 15,border_color = "#000000",fg_color = "#939393",text_color = "#000000",hover_color = "darkgray",value = 2,font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "bold"))
        self.radiobutton_b.pack(anchor = "nw",padx = 35,pady = 10)
        
        self.radiobutton_c = ctk.CTkRadioButton(self.question_frame,variable = self.radiobutton_value,height = 50,width = 80,radiobutton_height = 20,radiobutton_width = 20,corner_radius = 18,border_color = "#000000",fg_color = "#939393",text_color = "#000000",hover_color = "darkgray",value = 3,font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "bold"))
        self.radiobutton_c.pack(anchor = "nw",padx = 35,pady = 10)
        
        self.radiobutton_d = ctk.CTkRadioButton(self.question_frame,variable = self.radiobutton_value,height = 50,width = 80,radiobutton_height = 20,radiobutton_width = 20,corner_radius = 18,border_color = "#000000",fg_color = "#939393",text_color = "#000000",hover_color = "darkgray",value = 4,font = ctk.CTkFont(family = "Helvetica",size = 20,weight = "bold"))
        self.radiobutton_d.pack(anchor = "nw",padx = 35,pady = 10)
        
        self.navigation_frame = ctk.CTkFrame(self.question_frame,fg_color = "#ffffff")
        self.navigation_frame.pack(anchor = "n",pady=5)

        self.prev_button = ctk.CTkButton(self.navigation_frame, height=40, width=150, corner_radius=10, fg_color="#FF5B5D",text_color="#000000", text="Previous",font=ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"),command=self.show_previous_question)
        self.prev_button.pack(side="left", padx=20)

        self.next_button = ctk.CTkButton(self.navigation_frame, height=40, width=150, corner_radius=10, fg_color="#FF5B5D",text_color="#000000", text="Next",font=ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"),command=self.show_next_question)
        self.next_button.pack(side="right", padx=(190,0))

        self.down_navigation_frame = ctk.CTkFrame(self.question_frame,fg_color = "#ffffff")
        self.down_navigation_frame.pack(anchor = "n",pady=5)

        self.submit_button = ctk.CTkButton(self.down_navigation_frame, height=40, width=150, corner_radius=10, fg_color="#FF5B5D",text_color="#000000",text="Submit",font=ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"),command=self.submit)
        self.submit_button.pack_forget()

        self.view_score_button = ctk.CTkButton(self.down_navigation_frame, height=40, width=150, corner_radius=10, fg_color="#FF5B5D", text="View Score",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 20,weight = "normal"),command=self.calculate_score)
        self.view_score_button.pack_forget()

        self.show_question(self.current_question_index)   #Function Call

        self.questions_screen.mainloop()

    def show_question(self,index):
        question_data = self.qstring3_result[index]
        question_text = question_data[1]
        option_a = question_data[2]
        option_b = question_data[3]
        option_c = question_data[4]
        option_d = question_data[5]
        #self.correct_option = question_data[6]

        self.mcq_label.configure(text=question_text)
        self.radiobutton_a.configure(text=option_a)
        self.radiobutton_b.configure(text=option_b)
        self.radiobutton_c.configure(text=option_c)
        self.radiobutton_d.configure(text=option_d)

    def show_next_question(self):
        self.save_user_response()
        if self.current_question_index < len(self.qstring3_result)-1:
            self.current_question_index = self.current_question_index + 1
            self.show_question(self.current_question_index)
        if self.current_question_index == len(self.qstring3_result)-1:
            self.submit_button.pack(side="left", padx=27)

    def show_previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index = self.current_question_index - 1
            self.show_question(self.current_question_index)

    def save_user_response(self):
        user_response = self.radiobutton_value.get()
        if user_response:
            self.user_responses[self.current_question_index] = user_response
        else:
            self.user_responses[self.current_question_index] = None
        
        if self.current_question_index<len(self.qstring3_result)-1:
            self.radiobutton_a.deselect()
            self.radiobutton_b.deselect()
            self.radiobutton_c.deselect()
            self.radiobutton_d.deselect()

    def convert_to_int(self):
        for i in self.user_responses:
            if i not in [None,"Null"]:
                converted_int_value = int(i)
                self.user_responses_int.append(converted_int_value)
            else:
                self.user_responses_int.append(None)
        return self.user_responses_int

    def submit(self):
        user_response = self.radiobutton_value.get()
        if user_response:
            self.user_responses[self.current_question_index] = user_response
        else:
            self.user_responses[self.current_question_index] = None

        top_level_window = ctk.CTkToplevel()
        top_level_window.title("Success message")
        top_level_window.geometry("250x80")
        top_level_window.resizable(False,False)
        top_label = ctk.CTkLabel(top_level_window,30,50,corner_radius=5,text="Data submitted successfully",text_color="#000000")
        top_label.pack(side = "top",pady = 5)
        
        self.view_score_button.pack(side="right", padx=(180,0))


    def calculate_score(self):
        self.questions_screen.destroy()
        self.user_choice.destroy()
        returned_values = [None]*10
        returned_values = self.convert_to_int()
        print(returned_values)
        for response,value in zip(returned_values,self.answerkey_result):
            #correct_answer = self.qstring3_result[index][6]
            if response == value:
                self.score = self.score+1

        total_marks = len(self.answerkey_result)
        messagebox.showinfo(title = "Score",message = "Your Total Score Is:"+ " "+str(self.score)+ "/" + str(total_marks))
        messagebox.askyesno(title = "Choice to save",message = "Do you want to save your past result? You can view it in your history.")
        returned_values.clear()

    def quit_page(self):
        self.questions_screen.destroy()
        
    def update_timer(self):
        if self.time_left>=0:
            self.timer_label.configure(text = "Timer :"+str(self.time_left))
            self.time_left = self.time_left-1
            self.timer_label.after(1000,self.update_timer)
        else:
            self.timer_label.configure(text = "Timer :"+"Time Up..!!")

if __name__ == "__main__":
    login_class_object = login_class()
    login_class_object.login_screen.mainloop()

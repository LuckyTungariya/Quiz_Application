import customtkinter as ctk 
import tkinter as tk
import datetime
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk
import pymysql as psql

class question_screen(ctk.CTk):
    def __init__(self,parent_frame,id,mycon,cur,question,answer,button_value,add_frame_method,navigate_method):
        super().__init__()
        self.parent_frame = parent_frame

        self.add_frame_method = add_frame_method
        self.navigate_frame = navigate_method

        self.questions_frame = ctk.CTkFrame(self.parent_frame,fg_color="#3DC8D8")
        self.questions_frame.pack(fill = "both",expand = True)

        self.add_frame_method("questions",self.questions_frame)

        self.configure(fg_color = "#3DC8D8")
        self.title("Questions")
        self.id = id
        self.mycon = mycon
        self.cur = cur
        self.qstring3_result = question
        self.answerkey_result = answer
        self.button_text = button_value
        self.current_question_index = 0
        self.score = 0
        self.user_responses = [None]*10
        self.user_responses_int = []

        self.bind("<f>",self.toggle_fullscreen)

        self.bind("<Escape>",self.escape_fullscreen)

        self.timer_id = None

        self.timer_label = ctk.CTkLabel(self.questions_frame,fg_color = "#ffffff",height = 30,width = 80,text = "Timer :"+ str(60),text_color = "#000000",corner_radius = 20,font = ('Trebuchet MS',25,"bold"))
        self.timer_label.pack(anchor = "ne",padx = (0,30),pady = 40)

        self.time_left = 60
        self.update_timer()

        self.start_quiz()

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def escape_fullscreen(self,event = None):
        self.overrideredirect(False)

    def start_quiz(self):

        self.question_frame = ctk.CTkFrame(self.questions_frame,border_width = 1,border_color = "#959595",corner_radius = 20,fg_color = "#ffffff")
        self.question_frame.pack(fill = "both",expand = True,padx = 30,pady = 20)

        self.top_question_frame = ctk.CTkFrame(self.question_frame,height = 70,fg_color = "#ffffff",corner_radius = 10)
        self.top_question_frame.pack(side = "top",fill = "x",padx = 5,pady = 10)

        self.mcq_label = ctk.CTkLabel(self.top_question_frame,text_color = "#000000",font = ctk.CTkFont(family = "Garamold",size = 16,weight = "bold"))
        self.mcq_label.pack(side = "left",pady = 10,padx = 40)

        self.quit_button = ctk.CTkButton(self.top_question_frame,height = 50,width = 100,corner_radius = 20,border_width = 1,border_color = "#000000",border_spacing = 2,fg_color = "#FF5B5D",text = "Quit",font = ctk.CTkFont(family="Helvetica",size = 15,weight = "bold"),text_color = "#000000",command = self.quit_page) 
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
        if self.timer_id:
            self.timer_label.after_cancel(self.timer_id)
            self.timer_id = None
        user_response = self.radiobutton_value.get()
        if user_response:
            self.user_responses[self.current_question_index] = user_response
        else:
            self.user_responses[self.current_question_index] = None
        
        messagebox.showinfo(title = "Success",message="Data Submitted successfully")
        self.view_score_button.pack(side="right", padx=(180,0))

    def calculate_score(self):
        returned_values = [None]*10
        returned_values = self.convert_to_int()
        print(returned_values)
        for response,value in zip(returned_values,self.answerkey_result):
            if response == value:
                self.score = self.score+1

        total_marks = len(self.answerkey_result)
        messagebox.showinfo(title = "Score",message = "Your Total Score Is:"+ " "+str(self.score)+ "/" + str(total_marks))
        value = messagebox.askyesno(title = "Choice to save",message = "Do you want to save your past result? You can view it in your history.")
        if value:
           self.save_response()
           messagebox.showinfo(title="Success",message="Your response saved successfully")
        self.navigate_frame("questions","userchoice")
        returned_values.clear()

    def save_response(self):
        current_datetime = datetime.datetime.now()
        button_value = self.button_text
        current_date = current_datetime.strftime("%d/%m/%y")
        current_time = current_datetime.strftime("%I:%M:%S %p")
        current_score = str(self.score)
        current_id = self.id
        query1 = f'insert into responses (domain,played_date,played_time,score,userid) values(%s,%s,%s,%s,%s)'
        self.cur.execute(query1,(button_value,current_date,current_time,current_score,current_id))
        self.mycon.commit() 

    def quit_page(self):
        response = messagebox.askyesno(title = "Confirm",message = "Are you sure you want to exit?")
        if response:
            self.navigate_frame("questions","userchoice")
            self.timer_label.after_cancel(self.timer_id)
            self.timer_id = None

        
    def update_timer(self):
        if self.time_left>=0:
            self.timer_label.configure(text = "Timer :"+str(self.time_left))
            self.time_left = self.time_left-1
            self.timer_id =  self.timer_label.after(1000,self.update_timer)
        else:
            self.timer_label.configure(text = "Timer :"+"Time Up..!!")
            messagebox.showinfo(title="Time Up..!!",message="Your time is upp..!!")
            self.calculate_score()




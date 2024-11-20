import customtkinter as ctk 
import tkinter as tk
from datetime import *
from tkinter import messagebox,PhotoImage
from questions_screen import question_screen
from PIL import Image,ImageTk
import pymysql as psql

class saved_responses(ctk.CTk):
    def __init__(self,parent_frame,cur,id,add_frame_method,navigate_method):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame_method
        self.navigate_method = navigate_method

        self.responses_screen = ctk.CTkFrame(self.parent_frame,fg_color="#29B6F6")
        self.responses_screen.pack(fill = "both",expand = True)

        self.add_frame_method("response",self.responses_screen)

        self.title("Saved Responses")

        self.cur = cur
        self.userid = id

        self.bind("<f>",self.toggle_fullscreen)

        self.bind("<Escape>",self.escape_fullscreen)

        self.main_frame = ctk.CTkScrollableFrame(self.responses_screen,corner_radius=20,border_width=1,border_color="#000000",fg_color="#ffffff",scrollbar_fg_color="lightgray",scrollbar_button_hover_color="gray",orientation="vertical")
        self.main_frame.pack(fill = "both",expand = True,padx = (25,25),pady = (35,60))

        self.button_frame = ctk.CTkFrame(self.main_frame,height = 50,fg_color="#ffffff")
        self.button_frame.pack(fill = "x",anchor = "nw",padx = 50,pady = (10,0))
        
        back_image = ctk.CTkImage(dark_image=Image.open(r"C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\Quiz Application\pics\back (1).png"),size = (25,25))
        self.back_button = ctk.CTkButton(self.button_frame,corner_radius = 15,image=back_image,fg_color = "#29B6F6",text = "Back",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "bold",size = 30),command = self.previous_page)
        self.back_button.pack(side = "left",padx = 0,pady = (0,0))

        self.saved_lbl = ctk.CTkLabel(self.button_frame,text = "SAVED RESPONSES",text_color="#000000",fg_color="#ffffff",font = ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.saved_lbl.pack(side = "left",padx = (300,0))

        self.check_render()

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def escape_fullscreen(self,event = None):
        self.overrideredirect(False)

    def create_screen(self):
        self.text_frame = ctk.CTkFrame(self.main_frame,fg_color="#ffffff")
        self.text_frame.pack(fill = "x",padx = (25,25),pady = (10,0))

        self.domain_lbl = ctk.CTkLabel(self.text_frame,text="DOMAIN",text_color="#000000",font=ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.domain_lbl.pack(side = "left",padx = (40,0))

        self.date_lbl = ctk.CTkLabel(self.text_frame,text="PLAYED DATE",text_color="#000000",font=ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.date_lbl.pack(side = "left",padx = (200,0))

        self.time_lbl = ctk.CTkLabel(self.text_frame,text="PLAYED TIME",text_color="#000000",font=ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.time_lbl.pack(side = "left",padx = (160,0))

        self.scored = ctk.CTkLabel(self.text_frame,text="SCORE",text_color="#000000",font=ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.scored.pack(side = "left",padx = (150,10))

    def show_none(self):
        self.created_lbl = ctk.CTkLabel(self.main_frame,text = "No Saved Responses Yet.",corner_radius=20,fg_color="#ebf0ee",height = 100,text_color="#000000",font = ctk.CTkFont(family = "Impact",size = 35,weight = "normal"))
        self.created_lbl.pack(fill = "x",padx = (15,15),pady = (200,0))

    def previous_page(self):
        self.navigate_method("response","homescreen")

    def check_render(self):
        query = f'select * from responses where userid = %s'
        self.cur.execute(query,(self.userid))
        affected_rows = self.cur.rowcount
        if affected_rows == 0:
            self.show_none()
        else:
            self.create_screen()
            self.fetch_records()

    def fetch_records(self):
        query = f'select * from responses where userid = %s'
        self.cur.execute(query,(self.userid))
        returned_records = self.cur.fetchall()
        for record in returned_records:
            value_frame = ctk.CTkFrame(self.main_frame,height = 50,fg_color="#ffffff",corner_radius = 20)
            value_frame.pack(fill = "x",padx = (15,15),pady = 10)

            domain_value_lbl = ctk.CTkLabel(value_frame,text = record[0] ,height = 50,corner_radius = 20,fg_color="#ebf0ee",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 20,weight = "normal"))
            domain_value_lbl.pack(side = "left",padx = (10,10),expand = True,fill = "both")

            date_value_lbl = ctk.CTkLabel(value_frame,text = record[1],height = 50,corner_radius = 20,fg_color="#ebf0ee",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 20,weight = "normal"))
            date_value_lbl.pack(side="left", padx=(10, 10), expand=True, fill="both")

            time_value_lbl = ctk.CTkLabel(value_frame,text = record[2],height = 50,corner_radius = 20,fg_color="#ebf0ee",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 20,weight = "normal"))
            time_value_lbl.pack(side="left", padx=(10, 10), expand=True, fill="both")

            score_value_lbl = ctk.CTkLabel(value_frame,text = record[3],height = 50,corner_radius = 20,fg_color="#ebf0ee",text_color = "#000000",font = ctk.CTkFont(family = "Impact",size = 20,weight = "normal"))
            score_value_lbl.pack(side="left", padx=(10, 10), expand=True, fill="both")




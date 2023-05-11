import tkinter as tk
import requests
from tkinter import messagebox
import customtkinter
import DataBase.dbManager as db
from PIL import Image,ImageTk
from Screens.Update import *
from Screens.Sensor_info import *
from Screens.Details import *
from Screens.Profile import *


class Landing_screen():
    def __init__(self) -> None:
        self.frame_landing =tk.Frame(width=1920, height=1080)
        self.frame_landing.place(x=0,y=0)
        
        customtkinter.CTkLabel(master=self.frame_landing ,width=1920,height=100,bg_color='Gray',text='').place(x=0,y=0)
        customtkinter.CTkLabel(master=self.frame_landing,text='PyFlora posuda  > Biljke ',bg_color='Gray',text_color='white',font=('Arial',30)).place(x=250,y=25)


        profile_button=customtkinter.CTkButton(master=self.frame_landing,width=100,height=35,border_width=1,border_color='black',bg_color='gray',text='Profili',command=self.profiles)
        profile_button.place(x=1100,y=25)
        sync_button=customtkinter.CTkButton(master=self.frame_landing,width=100,height=35,border_width=1,border_color='black',bg_color='gray',text='Sync', command=self.synchronise)
        sync_button.place(x=650,y=25)

    def synchronise(self):
        syncronisation=Sensor_info()
        syncronisation.Sync_data()
        messagebox.showinfo('Update','Molimo osviježite stranicu na REFRESH gumb.')

    def profiles(self):
        korisnici=Profile()

    def details_general_action(self):
        details=Details()
     

    def PyFloraBoxes(self):
        db_connection =db.create_connection('baza.db')
        sql_querry = 'SELECT * FROM Posude'
        data=db.select_all_records(db_connection,sql_querry)

        db_connection1 =db.create_connection('baza.db')
        sql_querry1 = 'SELECT * FROM Biljke'
        data_biljke=db.select_all_records(db_connection1,sql_querry1)
        
       
            
        row = 0
        col = 0
        self.frame_main_data= tk.Frame(borderwidth=2,highlightcolor='red')
        self.frame_main_data.place(x=100,y=100)


        
        
        for i, row_data in enumerate(data):
            frame = tk.Frame(self.frame_main_data, borderwidth=2, relief="groove")
            self.status_biljke = row_data[3]
            self.status_svijetlo=row_data[8]
            self.status_vlaga=row_data[4]
            self.status_ph=row_data[9]        

            for i in data_biljke:
                self.pic_url = i[2]
                self.naziv_biljke =i[1]

                if self.naziv_biljke == row_data[2]:

                    label_pot_name=tk.Label(master=frame,text=f'IME POSUDE  : {row_data[1]}',font=('Calibri',16,'bold','underline'))
                    label_pot_name.grid(row=0,column=0)

                    image= Image.open(requests.get(self.pic_url,stream=True).raw).resize((250,175))
                    photo=ImageTk.PhotoImage(image)
                    label_image = tk.Label(frame, image=photo)
                    label_image.photo = photo
                    label_image.grid(row=1, column=0,rowspan=3,padx=0,pady=0)

                    label_plantname_raw=tk.Label(master=frame,text=f'BILJKA  :\n{row_data[2]}',font=('Calibri',16,'bold'))
                    label_plantname_raw.grid(row=0,column=1,columnspan=3,padx=10,pady=10)          

                    label_status_raw=tk.Label(master=frame,text=f'__STATUS__ : \n Svijelta: {self.status_svijetlo}\n Vlage u zraku: {self.status_vlaga} % \n Tla:{self.status_ph} ({row_data[6]}pH)')
                    label_status_raw.grid(row=3,column=1,columnspan=3,padx=10,pady=10)


                        
            frame.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1


            
            self.addnew_button=customtkinter.CTkButton(master=self.frame_landing,width=100,height=35,border_width=1,border_color='black',text='Update/Add pots',bg_color='gray',command=self.add_new)
            self.addnew_button.place(x=875,y=25)

            self.details_general=customtkinter.CTkButton(master=self.frame_landing,width=100,height=35,border_width=1,border_color='black',text='Details',bg_color='gray',command=self.details_general_action)
            self.details_general.place(x=990,y=25)     

            self.refreshbutton=customtkinter.CTkButton(master=self.frame_landing,width=100,height=35,border_width=1,bg_color='gray',border_color='black',text='Refresh',command=self.refresh)
            self.refreshbutton.place(x=755,y=25)

    def refresh(self):
        self.frame_landing.destroy()
        new_screen=Landing_screen()
        new_screen.PyFloraBoxes()

    def add_new(self):
        newScreen=Update()
        newScreen.Update_scr()       
        
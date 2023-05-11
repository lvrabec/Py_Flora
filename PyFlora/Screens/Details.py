import tkinter as tk
import customtkinter
import DataBase.dbManager as db
from PIL import Image,ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import requests

class Details():
    def __init__(self) -> None:
       self.dialog=tk.Toplevel()
       self.dialog.title('Novi prozor- Details')
       self.dialog.geometry("1200x750")
       self.dialog.focus_set()
       self.frm = tk.Frame(self.dialog,width=1200, height=750, highlightbackground='black',highlightthickness=2)
       self.frm.place(x=0,y=0)
       #______ HEADER ________# 
       self.frm_header=tk.Frame(self.dialog,width=1200, height=75)
       self.frm_header.place(x=0,y=0)
       self.gray_label_header=customtkinter.CTkLabel(master=self.frm_header,bg_color='gray',fg_color='gray',text='',height=75,width=1200)
       self.gray_label_header.place(x=0,y=0)
       details_button_plant=customtkinter.CTkButton(self.frm_header,text='Plant Details',bg_color='gray',command=self.call_details_plants)
       details_button_plant.place(x=10,y=25)
       details_button_pot=customtkinter.CTkButton(self.frm_header,text='Pot Details',bg_color='gray',command=self.call_details_pot)
       details_button_pot.place(x=195,y=25)


       self.operational_variable_ID=tk.StringVar()
       self.operational_variable_NAME=tk.StringVar()
       self.operational_variable_URL=tk.StringVar()
       self.operational_variable_URL_POTS=tk.StringVar()
       self.current_option=tk.StringVar()

       self.current_option_pots=tk.StringVar()

       self.operational_frame_plant_exists_variable=tk.IntVar()
       self.operational_frame_plant_exists_variable.set(0)
    

    def refresh_button(self):
        
        value=int(self.current_option.get())               
        # print('print iz baze ',self.data_biljke[value])       
        url=self.data_biljke[value][2]
        self.operational_variable_URL.set(url)
        # print('operational variable : ',self.operational_variable_URL.get())

        self.plant_name_label_CONTENT.configure(text=self.data_biljke[value][1])

        self.image=Image.open(requests.get(self.operational_variable_URL.get(),stream=True).raw).resize((430,323))
        self.photo=ImageTk.PhotoImage(self.image)
        self.label_image=tk.Label(self.master_frame_content_plants,image=self.photo)
        self.label_image.photo=self.photo
        self.label_image.place(x=650,y=165)

        self.plant_care_label_CONTENT.configure(text=str(self.data_biljke[value][3]))
        self.plant_care_label_CONTENT1.configure(text=str(self.data_biljke[value][4]))
        self.plant_care_label_CONTENT2.configure(text=str(self.data_biljke[value][5]))


        
        db_connection1 =db.create_connection('baza.db')
        sql_querry2 = 'SELECT * FROM Posude'
        self.data_posude=db.select_all_records(db_connection1,sql_querry2)


        
    

    def refresh_button_pots(self):
        value_current_pot_id=int(self.current_option_pots.get())
        # print('trenutni odabir  : ',self.data_posude[value_current_pot_id])

        self.sensor_CONTENT_POTS.configure(text=f"Status svijetla : {str(self.data_posude[value_current_pot_id][8])}")
        self.sensor_CONTENT1_POTS.configure(text=f"PH Vrijednost tla je : {str(self.data_posude[value_current_pot_id][9])}")
        self.sensor_CONTENT2_POTS.configure(text=f"Trenutna vlaga zraka je : {str(self.data_posude[value_current_pot_id][4])} %")
        self.pot_name_label_CONTENT_POTS.configure(text=f"{str(self.data_posude[value_current_pot_id][1])}")
        self.plant_poted_label_CONTENT_POTS.configure(text=f"{str(self.data_posude[value_current_pot_id][2])}")
        self.id_posude.configure(text=f"ID trenutne posude : {str(self.current_option_pots.get())}")

        imena_biljaka=[]
        imena_biljaka.append(self.data_posude[value_current_pot_id][2])
        # print(imena_biljaka)
        # print(self.data_biljke)
        
        for i in self.data_biljke:
            # print(i[1])
            if i[1]==imena_biljaka[0]:
                # print('match!')
                url=i[2]
                # print(url)
                self.operational_variable_URL_POTS.set(url)


               
        self.image=Image.open(requests.get(self.operational_variable_URL_POTS.get(),stream=True).raw).resize((430,323))
        self.photo=ImageTk.PhotoImage(self.image)
        self.label_image=tk.Label(self.master_frame_content_pots,image=self.photo)
        self.label_image.photo=self.photo
        self.label_image.place(x=650,y=165)
        self.pot_graph()

  
        




    def call_details_plants(self): 

        if self.operational_frame_plant_exists_variable.get()==1:
            self.master_frame_content_plants.destroy()
            self.operational_frame_plant_exists_variable.set(0)

        
        self.master_frame_content_plants=tk.Frame(self.frm,width=1200,height=675)
        self.master_frame_content_plants.place(x=0,y=75)
        self.operational_frame_plant_exists_variable.set(1)
        # print('NAKON pokretanja funkcije : ',self.operational_frame_plant_exists_variable.get())

        self.refresh_button=customtkinter.CTkButton(master=self.master_frame_content_plants,text='REFRESH',command=self.refresh_button)
        self.refresh_button.place(x=990,y=15)

        self.plant_name_label=customtkinter.CTkLabel(master=self.master_frame_content_plants,font=('Arial',32,'bold','underline'),text='Naziv biljke:')
        self.plant_name_label.place(x=50,y=45)

        self.plant_name_label_CONTENT=customtkinter.CTkLabel(master=self.master_frame_content_plants,text='Ovdje ide ime iz baze',font=('Calibri',28))
        self.plant_name_label_CONTENT.place(x=50,y=85)

        self.plant_care_label=customtkinter.CTkLabel(master=self.master_frame_content_plants,text='Napomene za brigu o biljci :',font=('Calibri',20))
        self.plant_care_label.place(x=50, y=135)

        self.plant_care_label_CONTENT=customtkinter.CTkLabel(master=self.master_frame_content_plants,text='',font=('Calibri',16))
        self.plant_care_label_CONTENT.place(x=50, y=165)
        
        self.plant_care_label_CONTENT1=customtkinter.CTkLabel(master=self.master_frame_content_plants,text='',font=('Calibri',16))
        self.plant_care_label_CONTENT1.place(x=50, y=195)
        self.plant_care_label_CONTENT2=customtkinter.CTkLabel(master=self.master_frame_content_plants,text='',font=('Calibri',16))
        self.plant_care_label_CONTENT2.place(x=50, y=220)


        self.drop_down_menu_label=customtkinter.CTkLabel(master=self.master_frame_content_plants,text='Chose the plant ID:',font=('Calibri',24))
        self.drop_down_menu_label.place(x=650,y=55)


        url_default = 'https://img.icons8.com/?size=512&id=119755&format=png'
        self.operational_variable_URL.set(url_default)

       
        self.image=Image.open(requests.get(self.operational_variable_URL.get(),stream=True).raw).resize((430,323))
        self.photo=ImageTk.PhotoImage(self.image)
        self.label_image=tk.Label(self.master_frame_content_plants,image=self.photo)
        self.label_image.photo=self.photo
        self.label_image.place(x=650,y=165)


        db_connection1 =db.create_connection('baza.db')
        sql_querry1 = 'SELECT * FROM Biljke'
        self.data_biljke=db.select_all_records(db_connection1,sql_querry1)
        
        self.options_list=[]

        for i in self.data_biljke:
            self.options_list.append(i[0])
            self.id_biljke=i[0]
            self.ime_biljke=i[1]
            self.slika_url=i[2]        
               
        self.drop_down_menu=customtkinter.CTkOptionMenu(master=self.master_frame_content_plants,variable=self.current_option,values=self.options_list)
        self.drop_down_menu.place(x=650,y=85)
    


    def call_details_pot(self):

        if self.operational_frame_plant_exists_variable.get()==1:
            self.master_frame_content_plants.destroy()
            self.operational_frame_plant_exists_variable.set(0)
        

        self.master_frame_content_pots=tk.Frame(self.frm,width=1200,height=675)
        self.master_frame_content_pots.place(x=0,y=75)

        
        self.refresh_button_btn_pots=customtkinter.CTkButton(master=self.master_frame_content_pots,text='REFRESH',command=self.refresh_button_pots)
        self.refresh_button_btn_pots.place(x=990,y=45)

        self.naziv_posude_label=customtkinter.CTkLabel(master=self.master_frame_content_pots,text='Naziv Posude:',font=('Arial',32,'bold','underline'))
        self.naziv_posude_label.place(x=50,y=45)
        self.id_posude=customtkinter.CTkLabel(master=self.master_frame_content_pots,text=f'Izaberide id posude:',font=('Arial',32,'bold','underline'))
        self.id_posude.place(x=50 , y=0)

        self.pot_name_label_CONTENT_POTS=customtkinter.CTkLabel(master=self.master_frame_content_pots,text='',font=('Calibri',28))
        self.pot_name_label_CONTENT_POTS.place(x=50,y=85)

        self.plant_poted_label_CONTENT_POTS=customtkinter.CTkLabel(master=self.master_frame_content_pots,text='',font=('Calibri',24))
        self.plant_poted_label_CONTENT_POTS.place(x=50,y=125)
 
        self.sensor_CONTENT_POTS=customtkinter.CTkLabel(master=self.master_frame_content_pots,text='',font=('Calibri',16))
        self.sensor_CONTENT_POTS.place(x=50, y=165)
        
        self.sensor_CONTENT1_POTS=customtkinter.CTkLabel(master=self.master_frame_content_pots,text='',font=('Calibri',16))
        self.sensor_CONTENT1_POTS.place(x=50, y=195)
        self.sensor_CONTENT2_POTS=customtkinter.CTkLabel(master=self.master_frame_content_pots,text='',font=('Calibri',16))
        self.sensor_CONTENT2_POTS.place(x=50, y=220)



        db_connection1 =db.create_connection('baza.db')
        sql_querry1 = 'SELECT * FROM Biljke'
        self.data_biljke=db.select_all_records(db_connection1,sql_querry1)


        db_connection2 =db.create_connection('baza.db')
        sql_querry2 = 'SELECT * FROM Posude'
        self.data_posude=db.select_all_records(db_connection2,sql_querry2)    


        self.lista_posude=[]
        for i in self.data_posude:
            self.lista_posude.append(i[0])
            # print(self.lista_posude)
              
        
        self.drop_down_menu=customtkinter.CTkOptionMenu(master=self.master_frame_content_pots,variable=self.current_option_pots,values=self.lista_posude)
        self.drop_down_menu.place(x=990,y=85)




   
    def pot_graph(self):
            print('funkcija pot graph je pokrenuta')
            print('trenutno je odabrano ',self.current_option_pots.get())
         
    

            self.frame_za_graf=tk.Frame(master=self.master_frame_content_pots,width=580,height=450)
            self.frame_za_graf.place(x=50,y=250)




            self.svi_podaci_df=pd.read_csv('./SensorData/Sensor_Data_table.csv')
            self.filtered_id_data = self.svi_podaci_df.loc[self.svi_podaci_df['id'].eq(int(self.current_option_pots.get()))]

            y1=self.filtered_id_data['vlaga'].tolist()
            y2=self.filtered_id_data['svijetlo'].tolist()
            y3=self.filtered_id_data['ph'].tolist()

            fig=Figure(figsize=(5.5,4.05),dpi=100)
            plot1=fig.add_subplot()
            x=list(range(len(y1))) 
            plot1.plot(x,y1,label='Vlaga')
            plot1.plot(x,y2,label='Svijetlo')
            plot1.plot(x,y3,label='ph')
            plot1.set_xlabel('Vrijeme')
            plot1.set_ylabel('Vrijednosti')
            plot1.legend()
            

            canvas= FigureCanvasTkAgg(fig,self.frame_za_graf)
            canvas.get_tk_widget().place(x=0,y=0)
            
            
            print(y1)
            print(y2)
            print(y3)
                       
                

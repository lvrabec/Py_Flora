import random
import requests
import tkinter as tk
import DataBase.dbManager as db
from tkinter import messagebox


class Sensor_info():    

    def __init__(self) -> None:
        self.grad='varaždin'        
        self.myApiKey= 'bb953d86a376e58dbfb65740c08a2fb2'
        self.base_URL= 'http://api.openweathermap.org/data/2.5/weather?'
        self.complete_URL=self.base_URL+"appid="+self.myApiKey+"&q="+self.grad


        self.humidity_VAR = tk.StringVar()
        self.humidity_VAR_STATUS_TEXT=tk.StringVar() 

    def Sync_data(self):

        db_connection =db.create_connection('baza.db')
        sql_querry = 'SELECT * FROM Posude'
        data_baza=db.select_all_records(db_connection,sql_querry)
        



        for i in data_baza :

            try:
                self.response= requests.get(self.complete_URL)
                self.data=self.response.json()
                self.y=self.data['main']
            except:
                self.error_msg=messagebox.showerror("ERROR",'Something went wrong , try again')


            self.current_humidity=str(self.y["humidity"])
            self.humidity_VAR.set(self.current_humidity)

            
            db_connection =db.create_connection('baza.db')
            sql_query1 = "UPDATE Posude SET statusvlaga = '" + self.humidity_VAR.get() + "'"
            db.update_record(db_connection,sql_query1)
            db.close_connection(db_connection)






        db_connection = db.create_connection('baza.db')
        for row in data_baza:
                ph_number = random.randint(1, 14)
                sql_query_random = f"UPDATE Posude SET statusph = {ph_number} WHERE id = {row[0]}"
                db.update_record(db_connection, sql_query_random)

        self.Sync_text_ph()
                     
    
  
    def Sync_text_ph(self):
        db_connection =db.create_connection('baza.db')
        sql_querry = 'SELECT * FROM Posude'
        data_baza=db.select_all_records(db_connection,sql_querry)


        for i in data_baza:


            if i[6] == 7:
                db_connection = db.create_connection('baza.db')
                ph_txt="PH je ok."
                sql_querry_ph_normal=f"UPDATE Posude SET phtxt = '{ph_txt}' WHERE id = {i[0]}"
                db.update_record(db_connection, sql_querry_ph_normal)
                db.close_connection(db_connection)
                
            if i[6] in range(1,7):
                db_connection = db.create_connection('baza.db')
                ph_txt_acidic="Tlo je kiselo"
                sql_querry_ph_acidic=f"UPDATE Posude SET phtxt = '{ph_txt_acidic}' WHERE id = {i[0]}"
                db.update_record(db_connection, sql_querry_ph_acidic)
                db.close_connection(db_connection)
               
            if i[6] in range(8,15):
                db_connection = db.create_connection('baza.db')
                ph_txt_alkine="Tlo je lužnato"
                sql_querry_ph_alkine=f"UPDATE Posude SET phtxt = '{ph_txt_alkine}' WHERE id = {i[0]}"
                db.update_record(db_connection, sql_querry_ph_alkine)
                db.close_connection(db_connection)
        
        
        
     
     
        for row in data_baza:
                db_connection =db.create_connection('baza.db')
                svijetlo_number = random.randint(0, 1)
                sql_query_svijetlo = f"UPDATE Posude SET statussvijetlo = '{svijetlo_number}' WHERE id = {row[0]}"
                db.update_record(db_connection, sql_query_svijetlo)
                db.close_connection(db_connection)




        self.Sync_light()

    def Sync_light(self):
        print('fukcija je pozvana') 

        db_connection =db.create_connection('baza.db')
        sql_querry = 'SELECT * FROM Posude'
        data_baza=db.select_all_records(db_connection,sql_querry)



        for i in data_baza:                
            if i[5]==1:
                db_connection = db.create_connection('baza.db')
                svijetlo_status_dovoljno='svijetla je dovoljno'
                sql_query_svijetlo_txt=f"UPDATE Posude SET svijetlotxt = '{svijetlo_status_dovoljno}' WHERE id = {i[0]}"
                db.update_record(db_connection, sql_query_svijetlo_txt)
                db.close_connection(db_connection)
            if i[5]!=1:
                db_connection = db.create_connection('baza.db')
                svijetlo_status_nedovoljno='Nedovoljno svijetla'
                sql_query_svijetlo_txt1=f"UPDATE Posude SET svijetlotxt = '{svijetlo_status_nedovoljno}' WHERE id = {i[0]}"
                db.update_record(db_connection, sql_query_svijetlo_txt1)
                db.close_connection(db_connection)

        self.log_data()
                 
    def log_data(self):
        db_connection =db.create_connection('baza.db')
        sql_querry = 'SELECT * FROM Posude'
        data=db.select_all_records(db_connection,sql_querry)


        for i in data :

            self.id_variable =i[0]
            self.vlaga_variable=i[4]
            self.svijetlo_variable=i[5]
            self.ph_variable=i[6]

            print('----POČETAK-----')
            print('ID ',self.id_variable)
            print('vlaga ',self.vlaga_variable)
            print('svijetlo ',self.svijetlo_variable)
            print('PH ',self.ph_variable)
        

            try:
                with open("./SensorData/Sensor_Data_table.csv","a") as file_writer:
                    file_writer.write(f"\n{self.id_variable},{self.vlaga_variable},{self.svijetlo_variable},{self.ph_variable}")
                    print('----POČETAK-----')
                    print('ID ',self.id_variable)
                    print('vlaga ',self.vlaga_variable)
                    print('svijetlo ',self.svijetlo_variable)
                    print('PH ',self.ph_variable)
                
            
            except Exception as e:
                print(f"greška: {e}")

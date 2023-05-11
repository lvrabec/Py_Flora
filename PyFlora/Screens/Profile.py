import tkinter as tk
from tkinter import ttk
import customtkinter
import DataBase.dbManager as db






class Profile():
    def __init__(self) -> None:
        self.dialog=tk.Toplevel()
        self.dialog.title('novi Prozor - Profili korisnika')
        self.dialog.geometry("1200x750")
        self.dialog.focus_set()
        self.frame=tk.Frame(master=self.dialog,width=1200,height=750)
        self.frame.place(x=0,y=0)
        self.label_header=customtkinter.CTkLabel(master=self.frame,width=1200,height=75,fg_color='gray',bg_color='gray',text='')
        self.label_header.place(x=0,y=0)


        self.combobox_operational_VAR=tk.StringVar()
        self.ID_operational_VAR=tk.StringVar()
        self.ime_operational_VAR=tk.StringVar()
        self.prezime_operational_VAR=tk.StringVar()
        self.korime_operational_VAR=tk.StringVar()
        self.pass_operational_VAR=tk.StringVar()




        self.profili()

    def clear_data(self):
        self.ID_operational_VAR.set('')
        self.ime_operational_VAR.set('')
        self.prezime_operational_VAR.set('')
        self.korime_operational_VAR.set('')
        self.pass_operational_VAR.set('')
        

    def read_korisnik(self):
        db_connection = db.create_connection('baza.db')
        sql_query = 'SELECT * FROM Korisnici WHERE korime = "'+self.combobox_operational_VAR.get()+'"'
        self.data_selected_korisnik = db.select_record_by_id(db_connection, sql_query)
        print(self.data_selected_korisnik)
        return self.data_selected_korisnik 
        
    def create_new_in_DB(self):
        db_connection = db.create_connection('baza.db')
        sql_query = 'INSERT INTO Korisnici(id,ime,prezime,korime,lozinka) VALUES ("' + self.ID_operational_VAR.get() + '","' + self.ime_operational_VAR.get() + '","' + self.prezime_operational_VAR.get() + '","' + self.korime_operational_VAR.get() + '","' + self.pass_operational_VAR.get() + '")'
        db.create_record(db_connection, sql_query)
        db.close_connection(db_connection)
        self.clear_data()
        self.frame.destroy()
        self.dialog.destroy()
        Profile()



    def update(self):
        db_connection = db.create_connection('baza.db')
        # sql_query = 'UPDATE Korisnici SET (ime,prezime,korime,lozinka) VALUES("' + self.ime_operational_VAR.get() +'","' + self.pass_operational_VAR.get() +'","' + self.korime_operational_VAR.get() +'","' + self.pass_operational_VAR.get() +'") WHERE id = "' + self.ID_operational_VAR.get() + '"'
        
        sql_query = 'UPDATE Korisnici SET ime = "' + self.ime_operational_VAR.get() + '", prezime = "' + self.prezime_operational_VAR.get() + '", korime = "' + self.korime_operational_VAR.get() + '", lozinka = "' + self.pass_operational_VAR.get() + '" WHERE id = "' + self.ID_operational_VAR.get() + '"'
        db.update_record(db_connection,sql_query)
        db.close_connection(db_connection)
        self.clear_data()
        self.frame.destroy()
        self.dialog.destroy()
        Profile()
        
    

    def delete(self):
        db_connection = db.create_connection('baza.db')
        sql_query = 'DELETE FROM Korisnici WHERE id = "' + self.ID_operational_VAR.get() + '"'
        db.delete_record(db_connection, sql_query)
        db.close_connection(db_connection)
        self.clear_data()
        self.frame.destroy()
        self.dialog.destroy()
        Profile()      




    def read(self):

        self.read_korisnik()
        self.ID_operational_VAR.set(self.data_selected_korisnik[0])
        self.ime_operational_VAR.set(self.data_selected_korisnik[1])
        self.prezime_operational_VAR.set(self.data_selected_korisnik[2])
        self.korime_operational_VAR.set(self.data_selected_korisnik[3])
        self.pass_operational_VAR.set(self.data_selected_korisnik[4])

     

        print(self.ID_operational_VAR.get())
        print(self.ime_operational_VAR.get())
        print(self.prezime_operational_VAR.get())
        print(self.korime_operational_VAR.get())
        print(self.pass_operational_VAR.get())




    def profili(self):

        self.label_naziv_forme=customtkinter.CTkLabel(master=self.frame,text='Administracija Korisnika',font=('Arial',32,'bold','underline'))
        self.label_naziv_forme.place(x=50,y=150)

        self.korisnici_db=[]
        
        db_connection =db.create_connection('baza.db')
        sql_querry = 'SELECT * FROM Korisnici'
        self.data_korisnici=db.select_all_records(db_connection,sql_querry)
                
        for i in self.data_korisnici:
            self.korisnici_db.append(i[3])       

        self.combobox=ttk.Combobox(master=self.frame,values=self.korisnici_db,textvariable=self.combobox_operational_VAR)
        self.combobox.place(x=50,y=195)
       
     

        self.id_labela_text=customtkinter.CTkLabel(master=self.frame,text='ID korisnika:',font=('Calibri',18,'bold'))
        self.id_labela_text.place(x=50,y=240)

        self.id_labela_VALUE=tk.Entry(master=self.frame,text='',textvariable=self.ID_operational_VAR)
        self.id_labela_VALUE.place(x=50,y=275)

        ime_labela_text=customtkinter.CTkLabel(master=self.frame,text='Ime korisnika:',font=('Calibri',18,'bold')).place(x=50,y=300)

        self.ime_labela_VALUE=tk.Entry(master=self.frame,text='',textvariable=self.ime_operational_VAR)
        self.ime_labela_VALUE.place(x=50,y=335)
        
        
        prezime_labela_text=customtkinter.CTkLabel(master=self.frame,text='Prezime korisnika:',font=('Calibri',18,'bold')).place(x=50,y=360)

        self.prezime_labela_VALUE=tk.Entry(master=self.frame,textvariable=self.prezime_operational_VAR)
        self.prezime_labela_VALUE.place(x=50,y=395)
        
        
        korime_labela_text=customtkinter.CTkLabel(master=self.frame,text='Username:',font=('Calibri',18,'bold')).place(x=50,y=420)

        self.korime_labela_VALUE=tk.Entry(master=self.frame,textvariable=self.korime_operational_VAR)
        self.korime_labela_VALUE.place(x=50,y=455)
       
        pass_labela_text=customtkinter.CTkLabel(master=self.frame,text='Password:',font=('Calibri',18,'bold')).place(x=50,y=480)

        self.pass_labela_VALUE=tk.Entry(master=self.frame,textvariable=self.pass_operational_VAR)
        self.pass_labela_VALUE.place(x=50,y=515)

        #_________ BUTTONS _____________#

        self.button_create=customtkinter.CTkButton(master=self.frame,text='Create',command=self.create_new_in_DB)
        self.button_create.place(x=430,y=195)

        self.button_read=customtkinter.CTkButton(master=self.frame,text='Read',command=self.read)
        self.button_read.place(x=580,y=195)

        self.button_update=customtkinter.CTkButton(master=self.frame,text='Update',command=self.update)
        self.button_update.place(x=735,y=195)


        self.button_delete=customtkinter.CTkButton(master=self.frame,text='Delete',fg_color='red',text_color='Black',font=('Arial',16,'bold'),border_color='black',border_width=2,command=self.delete)
        self.button_delete.place(x=900,y=195)





           

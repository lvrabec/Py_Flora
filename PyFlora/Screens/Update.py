import tkinter as tk
from tkinter import ttk
import customtkinter
import DataBase.dbManager as db
from tkinter import messagebox



class Update():
    def __init__(self) -> None:
       self.dialog=tk.Toplevel()
       self.dialog.title('Novi prozor- Update PyPots')
       self.dialog.geometry("600x450")
       self.dialog.focus_set()
       self.frm = tk.Frame(self.dialog,width=600, height=450)
       self.frm.grid(row=1,column=0)

       self.clicked=tk.StringVar()
       self.ime_var=tk.StringVar()
       self.var_id=tk.StringVar() 
        

       
    def Close(self):
        self.frm.destroy()
        self.dialog.destroy()
        

    
    def read_id(self):
        db_connection = db.create_connection('baza.db')
        sql_query = 'SELECT * FROM Posude'
        data = db.select_all_records(db_connection, sql_query)
        self.id_posude_combobox['values'] = [i[0] for i in data]



    def cleardata(self):
        self.var_id.set('')
        self.ime_var.set('')




    def Update_scr(self):

        headerlabel=customtkinter.CTkLabel(master=self.frm,height=75,width=600,bg_color='gray',text='').place(x=0,y=0)
        headerlabeltext=customtkinter.CTkLabel(master=self.frm,text='Upravljanje posudama:',font=('Arial black',32,'bold'),bg_color='gray',fg_color='gray').place(x=115,y=20)


        
        buttonclose=customtkinter.CTkButton(master=self.frm,height=2,width=2,text='CANCEL', command=self.Close)
        buttonclose.place(x=500,y=385) 

        buttoncreate=customtkinter.CTkButton(master=self.frm,height=2,width=2,text='Create',command=self.create)
        buttoncreate.place(x=10,y=385)

        buttonread=customtkinter.CTkButton(master=self.frm,height=2,width=2,text='Read', command=self.read)
        buttonread.place(x=60,y=385)

        buttonupdate=customtkinter.CTkButton(master=self.frm,height=2,width=2,text='Update',command=self.update)
        buttonupdate.place(x=105,y=385)

        buttondelete=customtkinter.CTkButton(master=self.frm,height=2,width=2,text='Delete',fg_color='red',text_color='black',command=self.delete)
        buttondelete.place(x=155,y=385)

        
        db_connection1 =db.create_connection('baza.db')
        sql_querry1 = 'SELECT * FROM Biljke'
        data_biljke=db.select_all_records(db_connection1,sql_querry1)

        db_connection2 =db.create_connection('baza.db')
        sql_querry2 = 'SELECT * FROM Posude'
        data_posude=db.select_all_records(db_connection2,sql_querry2)
        
        
        self.lista=[]
        for i in data_biljke :  
            self.lista.append(i[1])
        
        
        self.clicked.set(self.lista[0])
        
        
        self.lista_posude_id=[]
        for i in data_posude:
            self.lista_posude_id.append(i[0])
        self.var_id.set(self.lista_posude_id)


        self.drop_label=customtkinter.CTkLabel(master=self.frm,text='Biljka: ')
        self.drop_label.place(x=10,y=155)

        self.drop=tk.OptionMenu(self.frm,self.clicked,*self.lista)
        self.drop.place(x=10,y=185)
        # print(self.clicked.get())

    

        self.ime_posude_label=customtkinter.CTkLabel(master=self.frm,text='Ime posude: ')
        self.ime_posude_label.place(x=10,y=90)

        self.ime_posude_entry=customtkinter.CTkEntry(master=self.frm,placeholder_text='name',textvariable=self.ime_var)
        self.ime_posude_entry.place(x=8,y=115)

        self.id_posude_label=customtkinter.CTkLabel(master=self.frm,text='Id posude:')
        self.id_posude_label.place(x=200,y=90)

        self.id_posude_combobox=ttk.Combobox(master=self.frm,textvariable=self.var_id)
        self.id_posude_combobox.place(x=200,y=120)
        self.id_posude_combobox.set(1)

        self.read_id()
    


    def create(self):
        if int(self.var_id.get()) in self.lista_posude_id:
            messagebox.showwarning("Error" , " You can`t create 2 or more identical pot boxes with the same ID. Try again !")
        db_connection = db.create_connection('baza.db')
        sql_query = 'INSERT INTO Posude(id,naziv,biljka) VALUES ("' + self.var_id.get() + '","' + self.ime_var.get() + '","' + self.clicked.get() + '")'
        db.create_record(db_connection, sql_query)
        db.close_connection(db_connection)
        self.cleardata()
        self.read_id()
        messagebox.showinfo("INFO","Pot sucessfuly CREATED , please refresh the main page to see your pots\n Dont Forget to Sync the sensors before you refresh!")

    def update(self):
        db_connection = db.create_connection('baza.db')
        sql_query = "UPDATE Posude SET Naziv = '" + self.ime_var.get() + "', biljka = '" + self.clicked.get() + "' WHERE id = '" + self.var_id.get() + "'"
        db.update_record(db_connection,sql_query)
        db.close_connection(db_connection)
        self.cleardata()
        self.read_id()
        messagebox.showinfo("INFO","Pot sucessfuly UPDATED , please refresh the main page to see your pots\n Dont Forget to Sync the sensors before you refresh!")


    def read (self):
        db_connection = db.create_connection('baza.db')
        sql_query = 'SELECT * FROM Posude WHERE id = "' + self.var_id.get() + '"'
        data = db.select_record_by_id(db_connection, sql_query)
        self.ime_var.set(data[1])

    def delete(self):
        db_connection = db.create_connection('baza.db')
        sql_query = 'DELETE FROM Posude WHERE id = "' + self.var_id.get() + '"'
        db.delete_record(db_connection, sql_query)
        db.close_connection(db_connection)
        self.cleardata()
        self.read_id()
        messagebox.showwarning("INFO","Pot DELETED! , please refresh the main page to see your pots")
from tkinter import *
from tkinter import messagebox
import customtkinter
import DataBase.dbManager as db
from Screens.Landing_screen import *


class Login_screen():

    def __init__(self) -> None:
        self.frame_login = Frame(width=1920, height=1080,highlightthickness=2)
        self.frame_login.place(x=0,y=0)

        customtkinter.CTkLabel(master=self.frame_login ,text='PyFlora Posuda',width=1920,height=200,bg_color='Gray',text_color='white',font=('Arial',30)).place(x=0,y=0)
        
        customtkinter.CTkLabel(master=self.frame_login ,text='Prijava',width=150,height=20,font=('Arial',30)).place(x=885,y=380)

    


    def check_info(self):
        user=self.entry_bar_user_name.get()
        password = self.entry_bar_user_password.get()
        print('Upisani user je :',user)
        print('Upisani password je :', password)


        if user =='' or password=='':
            messagebox.showwarning("Error" , " Polja su prazna")
        else:
            db_connection = db.create_connection('baza.db')
            sql_query = 'SELECT * FROM Korisnici'
            data = db.select_all_records(db_connection, sql_query)

            for i in data:
                if i[3]==user and i[4]== password:
                    print('User uspješno nađen')
                    self.frame_login.destroy()
                    new_screen=Landing_screen()
                    new_screen.PyFloraBoxes()
                    break

                else :
                    print('Error in finding the user')
                    messagebox.showerror('Error',"Korisničko ime ili lozinka su neispravni .\nPokušajte ponovno.")
                    break




    def login_check(self):
        self.user_name_var_content = StringVar()
        self.user_pass_var_content = StringVar()

        self.entry_bar_user_name = customtkinter.CTkEntry(master=self.frame_login,
                                                        placeholder_text='User',
                                                        width=200,
                                                        height=25                                                          
                                                          )
        self.entry_bar_user_name.place(x=850,y=450)
        self.entry_bar_user_name_label = customtkinter.CTkLabel(master=self.frame_login,                                   
                                            text='User Name:')
        self.entry_bar_user_name_label.place(x=850,y=420)



        self.entry_bar_user_password = customtkinter.CTkEntry(master=self.frame_login,
                                                              placeholder_text='Enter Password',
                                                              show='*',                                                                                    width=200,
                                                              height=25
                                                              )
        self.entry_bar_user_password.place(x=850,y=530)
        self.entry_bar_user_password_label= customtkinter.CTkLabel(master=self.frame_login,
                                            text='Password',
                                            text_color='Black',
                                                                   )
        self.entry_bar_user_password_label.place(x=850,y=500)

        self.submit_button=customtkinter.CTkButton(master=self.frame_login,
                                                   text='Prijava',
                                                   command=self.check_info
        )

        self.submit_button.place(x=850,y=750)
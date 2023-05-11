from tkinter import *
from Screens.Login_screen import *




if __name__ == '__main__':

    root= Tk()
    root.title('MyPyFlora aplication - Vrabec Luka')
    root.geometry('1920x1080')


    def Login_scr():
        login=Login_screen()
        login.login_check()



    
    
    Login_scr()
    root.mainloop()
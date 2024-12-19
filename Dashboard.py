from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Pengelolaan Keuangan')
        self.window.geometry('1366x768')
       
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        icon = PhotoImage(file='assets\\img\\people.png')
        self.window.iconphoto(True, icon)
        
        #======================Header==========
        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)
        
        self.logout_text = Button(self.window, text='logout', bg='#32cff8', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e')  # Perbaikan warna di sini
        self.logout_text.place(x=950, y=15)
        
        #===============Sidebar========
        self.sidebar = Frame(self.window, bg='#ffffff')  # Perbaikan Self.windows menjadi self.window
        self.sidebar.place(x=0, y=0, width=300, height=750)
        
        #=========Body===========
        

def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()
    
if __name__== '__main__':
    win()

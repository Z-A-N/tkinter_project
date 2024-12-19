import tkinter as tk 
from tkinter import ttk 
from tkinter import PhotoImage

# jendela utama
root = tk.Tk()
root.title("Aplikasi Pengelolaan Keuangan")
root.geometry("600x400")
root.resizable(True, True)
mode_dark= True
# fungsi - fungsi
def toggle_mode():
    global mode_dark
    if mode_dark:
        root.config(bg="white")
        mode_dark = False
    else:
        root.config(bg="black")
        mode_dark = True


toggle_button = tk.Button(root, text="Toggle Mode", command=toggle_mode)
toggle_button.pack()


# #isi navbar



root.mainloop()



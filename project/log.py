import tkinter as tk
from tkinter import messagebox

#fungsi login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Username dan Password harus diisi!") #harus diisi
    else:
        messagebox.showinfo("Login", f"Login berhasil!\nUsername: {username}") #kalo berhasil

window = tk.Tk()
window.title("Login Form")#judul
window.geometry("400x300") #ukuran
window.configure(bg="#D6EFFF")  #warna

#buat frame
frame = tk.Frame(window, bg="white", padx=20, pady=20)
frame.pack(expand=True, fill="both", padx=10, pady=10)

#judul
title_label = tk.Label(frame, text="Login", font=("Arial", 18, "bold"), bg="white", fg="#333")
title_label.pack(pady=(10, 20))

#username
username_label = tk.Label(frame, text="Username", font=("Arial", 10), bg="white", fg="#555")
username_label.pack(anchor="w")
username_entry = tk.Entry(frame, font=("Arial", 12), bg="#F0F0F0", relief="flat")
username_entry.pack(fill="x", pady=(0, 10))

#password
password_label = tk.Label(frame, text="Password", font=("Arial", 10), bg="white", fg="#555")
password_label.pack(anchor="w") #w itu west (biar ke kiri)
password_entry = tk.Entry(frame, font=("Arial", 12), show="*", bg="#F0F0F0", relief="flat")
password_entry.pack(fill="x", pady=(0, 10))

# tombol forgot password
forgot_password_btn = tk.Button(
    frame, text="Forgot Password?", font=("Arial", 9, "italic"), bg="white", fg="#0078D7", relief="flat",
    bd=0, cursor="hand2"
)
forgot_password_btn.pack(anchor="e", pady=(0, 20))

#tombol log
login_btn = tk.Button(
    frame, text="Login", font=("Arial", 12), bg="#0078D7", fg="white", relief="flat", command=login
)
login_btn.pack(fill="x", pady=(10, 0))

window.mainloop()

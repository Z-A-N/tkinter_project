import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

# Fungsi untuk melakukan registrasi
def register():
    full_name = full_name_entry.get()  # Mengambil input nama lengkap
    email = email_entry.get()  # Mengambil input email
    password = password_entry.get()  # Mengambil input password
    
    # Validasi jika semua kolom harus diisi
    if full_name == "" or email == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill out all fields.")  # Peringatan jika ada kolom kosong
    else:
        messagebox.showinfo("Registration", "Registration successful!")  # Notifikasi sukses registrasi

# Fungsi untuk registrasi via platform sosial media
def register_via_social(platform):
    if platform == "Google":
        webbrowser.open("https://accounts.google.com/signup")  # Membuka link registrasi Google
    elif platform == "Facebook":
        webbrowser.open("https://www.facebook.com/signup")  # Membuka link registrasi Facebook
    else:
        messagebox.showerror("Error", f"Unknown platform: {platform}")  # Menampilkan error jika platform tidak dikenal

# Fungsi untuk membuka halaman login
def open_login():
    try:
        os.system("python login-nblzzz.py")  # Menjalankan file login lain dengan command sistem
    except Exception as e:
        messagebox.showerror("Error", f"Could not open login page: {e}")  # Menampilkan error jika file gagal dijalankan

# Membuat jendela utama
root = tk.Tk()
root.title("Join Us")  # Judul jendela
root.geometry("1024x768")  # Ukuran awal jendela
root.resizable(True, True)  # Mengizinkan jendela untuk diubah ukurannya

# Background gradien menggunakan Canvas
canvas = tk.Canvas(root, width=1024, height=768, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Membuat gradien (dari biru ke biru muda)
canvas.create_rectangle(0, 0, 1024, 768, fill="#0072ff", outline="")
canvas.create_rectangle(0, 0, 1024, 768, fill="#00c6ff", outline="", stipple="gray50")

# Membuat frame untuk form registrasi
card_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
card_frame.place(relx=0.5, rely=0.5, anchor="center")  # Posisi frame di tengah

# Membuat grid dalam frame untuk tata letak yang rapi
card_frame.grid_rowconfigure(0, weight=1)
card_frame.grid_columnconfigure(0, weight=1)

# Frame kanan untuk form input
right_frame = tk.Frame(card_frame, bg="#f5f5f5")
right_frame.grid(row=0, column=0, padx=20, pady=20)

# Judul pada frame kanan
title_label = tk.Label(right_frame, text="Welcome Back", font=("Arial", 24), bg="#f5f5f5")
title_label.pack(pady=20)

# Input nama lengkap
full_name_label = tk.Label(right_frame, text="Full Name", font=("Arial", 12), bg="#f5f5f5")
full_name_label.pack(anchor="w", padx=10)
full_name_entry = tk.Entry(right_frame, font=("Arial", 12))
full_name_entry.pack(fill="x", padx=10, pady=5)

# Input email
email_label = tk.Label(right_frame, text="Email", font=("Arial", 12), bg="#f5f5f5")
email_label.pack(anchor="w", padx=10)
email_entry = tk.Entry(right_frame, font=("Arial", 12))
email_entry.pack(fill="x", padx=10, pady=5)

# Input password
password_label = tk.Label(right_frame, text="Password", font=("Arial", 12), bg="#f5f5f5")
password_label.pack(anchor="w", padx=10)
password_entry = tk.Entry(right_frame, font=("Arial", 12), show="*")
password_entry.pack(fill="x", padx=10, pady=5)

# Tombol untuk registrasi via Google dan Facebook
social_buttons_frame = tk.Frame(right_frame, bg="#f5f5f5")
social_buttons_frame.pack(pady=20)

google_button = tk.Button(
    social_buttons_frame, 
    text="Google", 
    font=("Arial", 12), 
    fg="#ffffff", 
    bg="#4285F4", 
    width=15, 
    command=lambda: register_via_social("Google")  # Memanggil fungsi register via Google
)
google_button.pack(side="left", padx=10)

facebook_button = tk.Button(
    social_buttons_frame, 
    text="Facebook", 
    font=("Arial", 12), 
    fg="#ffffff", 
    bg="#3b5998", 
    width=15, 
    command=lambda: register_via_social("Facebook")  # Memanggil fungsi register via Facebook
)
facebook_button.pack(side="left", padx=10)

# Label untuk teks "OR"
or_label = tk.Label(right_frame, text="OR", font=("Arial", 14), bg="#f5f5f5")
or_label.pack(pady=10)

# Tombol registrasi
register_button = tk.Button(right_frame, text="Register", font=("Arial", 14), bg="#0072ff", fg="white", command=register)

# Efek hover pada tombol registrasi
def on_enter(event):
    register_button['background'] = '#005bb5'  # Warna tombol saat hover

def on_leave(event):
    register_button['background'] = '#0072ff'  # Warna tombol saat tidak hover

register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)

register_button.pack(pady=20)

# Tautan ke halaman login
login_link = tk.Label(right_frame, text="Have an account? Login", font=("Arial", 10), bg="#f5f5f5", fg="#0072ff", cursor="hand2")
login_link.pack(pady=10)
login_link.bind("<Button-1>", lambda e: open_login())  # Mengarahkan ke halaman login

# Fungsi untuk membuat elemen tetap responsif
def resize_elements(event):
    canvas.config(width=event.width, height=event.height)
    card_frame.place(relx=0.5, rely=0.5, anchor="center")

root.bind("<Configure>", resize_elements)  # Memanggil fungsi saat ukuran jendela berubah

# Menjalankan loop Tkinter
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import bcrypt

# Membuat koneksi ke database MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',       # Ubah sesuai dengan host database Anda
        user='root',            # Ubah dengan username MySQL Anda
        password='',            # Ubah dengan password MySQL Anda
        database='keuangan_db'  # Pastikan nama database benar
    )
    if conn.is_connected():
        cursor = conn.cursor()
        print("Connected to MySQL Database")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# Fungsi untuk melakukan registrasi
def register():
    full_name = username_entry.get()  # Memperbaiki penulisan variabel
    email = email_entry.get()
    password = password_entry.get()
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Menambahkan waktu registrasi
    
    # Validasi input
    if full_name == "" or email == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill out all fields.")
    else:
        # Mengecek apakah email sudah terdaftar
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            messagebox.showerror("Error", "Email already registered!")
        else:
            # Hash password menggunakan bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            try:
                # Menyimpan data ke tabel `users` dengan password yang sudah di-hash
                cursor.execute("""
                    INSERT INTO users (username, email, password, created_at)
                    VALUES (%s, %s, %s, %s)
                """, (full_name, email, hashed_password, created_at))
                conn.commit()
                messagebox.showinfo("Registration", "Registration successful!")
                
                # Menutup jendela registrasi dan membuka halaman login
                root.quit()  # Menutup window registrasi
                os.system("python login-nblzzz.py")  # Membuka halaman login
            except mysql.connector.IntegrityError as e:
                messagebox.showerror("Error", f"Registration failed: {e}")

# Fungsi untuk registrasi via platform sosial media
def register_via_social(platform):
    if platform == "Google":
        webbrowser.open("https://accounts.google.com/signup")
    elif platform == "Facebook":
        webbrowser.open("https://www.facebook.com/signup")
    else:
        messagebox.showerror("Error", f"Unknown platform: {platform}")

# Fungsi untuk membuka halaman login
def open_login():
    try:
        os.system("python login-nblzzz.py")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open login page: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Join Us")
root.geometry("1024x768")
root.resizable(True, True)

# Background gradien menggunakan Canvas
canvas = tk.Canvas(root, width=1024, height=768, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Membuat frame untuk form registrasi
card_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
card_frame.place(relx=0.5, rely=0.5, anchor="center")

# Frame kanan untuk form input
right_frame = tk.Frame(card_frame, bg="#f5f5f5")
right_frame.grid(row=0, column=0, padx=20, pady=20)

# Judul pada frame kanan
title_label = tk.Label(right_frame, text="Welcome Back", font=("Arial", 24), bg="#f5f5f5")
title_label.pack(pady=20)

# Input nama lengkap
username_label = tk.Label(right_frame, text="Username", font=("Arial", 12), bg="#f5f5f5")  # Memperbaiki penulisan variabel
username_label.pack(anchor="w", padx=10)
username_entry = tk.Entry(right_frame, font=("Arial", 12))  # Memperbaiki penulisan variabel
username_entry.pack(fill="x", padx=10, pady=5)

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
    command=lambda: register_via_social("Google")
)
google_button.pack(side="left", padx=10)

facebook_button = tk.Button(
    social_buttons_frame,
    text="Facebook",
    font=("Arial", 12),
    fg="#ffffff",
    bg="#3b5998",
    width=15,
    command=lambda: register_via_social("Facebook")
)
facebook_button.pack(side="left", padx=10)

# Label untuk teks "OR"
or_label = tk.Label(right_frame, text="OR", font=("Arial", 14), bg="#f5f5f5")
or_label.pack(pady=10)

# Tombol registrasi
register_button = tk.Button(right_frame, text="Register", font=("Arial", 14), bg="#0072ff", fg="white", command=register)

def on_enter(event):
    register_button['background'] = '#005bb5'

def on_leave(event):
    register_button['background'] = '#0072ff'

register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)

register_button.pack(pady=20)

# Tautan ke halaman login
login_link = tk.Label(right_frame, text="Have an account? Login", font=("Arial", 10), bg="#f5f5f5", fg="#0072ff", cursor="hand2")
login_link.pack(pady=10)
login_link.bind("<Button-1>", lambda e: open_login())

# Fungsi untuk membuat elemen tetap responsif
def resize_elements(event):
    canvas.config(width=event.width, height=event.height)
    card_frame.place(relx=0.5, rely=0.5, anchor="center")

root.bind("<Configure>", resize_elements)

root.mainloop()

# Menutup koneksi database saat program berakhir
conn.close()

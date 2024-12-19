import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from hashlib import sha256

# Fungsi untuk koneksi ke database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Host (localhost untuk phpMyAdmin)
            user="root",       # Username MySQL
            password="",       # Password MySQL (kosong jika tidak ada password)
            database="keuangan_db"  # Nama database
        )
        return conn
    except Error as e:
        messagebox.showerror("Koneksi Gagal", f"Terjadi kesalahan: {e}")
        return None

# Fungsi untuk registrasi pengguna
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    # Validasi input
    if not username or not password or not email:
        messagebox.showwarning("Input Tidak Lengkap", "Harap lengkapi semua field.")
        return
    
    # Hash password
    hashed_password = sha256(password.encode()).hexdigest()

    # Cek apakah username sudah ada
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            messagebox.showwarning("Username Sudah Terdaftar", "Username sudah terdaftar.")
        else:
            # Menyimpan data user baru ke database
            cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                           (username, hashed_password, email))
            conn.commit()
            messagebox.showinfo("Registrasi Sukses", "Akun berhasil dibuat!")
            # Setelah registrasi berhasil, langsung login
            show_login()
        
        cursor.close()
        conn.close()

# Fungsi untuk login pengguna
def login_user():
    username = username_login_entry.get()
    password = password_login_entry.get()

    # Validasi input
    if not username or not password:
        messagebox.showwarning("Input Tidak Lengkap", "Harap lengkapi semua field.")
        return

    # Hash password untuk mencocokkan
    hashed_password = sha256(password.encode()).hexdigest()

    # Cek apakah username dan password cocok
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, hashed_password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Sukses", f"Selamat datang, {username}!")
            # Alihkan ke halaman utama setelah login sukses
            root.quit()  # Keluar dari jendela login dan lanjut ke aplikasi utama
            open_dashboard()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")
        
        cursor.close()
        conn.close()

# ======= Tampilan Registrasi =======
def show_registration():
    register_window = tk.Toplevel(root)  # Membuka jendela baru untuk registrasi
    register_window.title("Registrasi Pengguna")
    register_window.geometry("300x300")

    global username_entry, password_entry, email_entry

    username_label = tk.Label(register_window, text="Username")
    username_label.pack(pady=5)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    password_label = tk.Label(register_window, text="Password")
    password_label.pack(pady=5)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack(pady=5)

    email_label = tk.Label(register_window, text="Email")
    email_label.pack(pady=5)
    email_entry = tk.Entry(register_window)
    email_entry.pack(pady=5)

    register_button = tk.Button(register_window, text="Register", command=register_user)
    register_button.pack(pady=10)

# ======= Tampilan Login =======
def show_login():
    login_window = tk.Toplevel(root)  # Membuka jendela baru untuk login
    login_window.title("Login Pengguna")
    login_window.geometry("300x300")

    global username_login_entry, password_login_entry

    username_login_label = tk.Label(login_window, text="Username")
    username_login_label.pack(pady=5)
    username_login_entry = tk.Entry(login_window)
    username_login_entry.pack(pady=5)

    password_login_label = tk.Label(login_window, text="Password")
    password_login_label.pack(pady=5)
    password_login_entry = tk.Entry(login_window, show="*")
    password_login_entry.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", command=login_user)
    login_button.pack(pady=10)

# ======= Dashboard Setelah Login =======
def open_dashboard():
    dashboard_window = tk.Tk()
    dashboard_window.title("Dashboard Aplikasi Keuangan")
    dashboard_window.geometry("800x600")

    # Menambahkan label di dashboard
    dashboard_label = tk.Label(dashboard_window, text="Selamat datang di Dashboard!", font=("Arial", 20))
    dashboard_label.pack(pady=50)

    # Tombol Logout
    logout_button = tk.Button(dashboard_window, text="Logout", command=dashboard_window.quit)
    logout_button.pack(pady=10)

    dashboard_window.mainloop()

# ======= Setup Jendela Utama =======
root = tk.Tk()
root.title("Aplikasi Pengelolaan Keuangan")
root.geometry("400x300")

# Tombol untuk buka registrasi dan login
register_button = tk.Button(root, text="Register", command=show_registration)
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=show_login)
login_button.pack(pady=10)

root.mainloop()

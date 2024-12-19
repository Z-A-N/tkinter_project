import tkinter as tk
from tkinter import messagebox
from hashlib import sha256
import mysql.connector
from mysql.connector import Error

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

def login_user(username, password):
    hashed_password = sha256(password.encode()).hexdigest()

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, hashed_password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Sukses", f"Selamat datang, {username}!")
            conn.close()
            return True  # Menandakan login berhasil
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")
        
        cursor.close()
        conn.close()
    return False

def show_login(root):
    login_window = tk.Toplevel(root)
    login_window.title("Login Pengguna")
    login_window.geometry("300x300")

    username_label = tk.Label(login_window, text="Username")
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    password_label = tk.Label(login_window, text="Password")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    def on_login():
        username = username_entry.get()
        password = password_entry.get()

        if login_user(username, password):
            login_window.destroy()  # Menutup jendela login
            import dashboard  # Import dashboard setelah login berhasil
            dashboard.show_dashboard(root)

    login_button = tk.Button(login_window, text="Login", command=on_login)
    login_button.pack(pady=10)

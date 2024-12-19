import tkinter as tk
from tkinter import messagebox
from hashlib import sha256
import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="keuangan_db"
        )
        return conn
    except Error as e:
        messagebox.showerror("Koneksi Gagal", f"Terjadi kesalahan: {e}")
        return None

def register_user(username, password, email):
    hashed_password = sha256(password.encode()).hexdigest()

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showwarning("Username Sudah Terdaftar", "Username sudah terdaftar.")
        else:
            cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                           (username, hashed_password, email))
            conn.commit()
            messagebox.showinfo("Registrasi Sukses", "Akun berhasil dibuat!")
        
        cursor.close()
        conn.close()

def show_register(root):
    register_window = tk.Toplevel(root)
    register_window.title("Registrasi Pengguna")
    register_window.geometry("300x300")

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

    def on_register():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()

        if username and password and email:
            register_user(username, password, email)
            register_window.destroy()  # Tutup jendela setelah registrasi
        else:
            messagebox.showwarning("Input Tidak Lengkap", "Harap lengkapi semua field.")

    register_button = tk.Button(register_window, text="Register", command=on_register)
    register_button.pack(pady=10)

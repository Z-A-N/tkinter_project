# Import library Tkinter untuk membuat GUI dan library tambahan
import tkinter as tk  # Digunakan untuk membuat elemen GUI
from tkinter import messagebox  # Untuk menampilkan kotak pesan (message box)
import os  # Digunakan untuk menjalankan perintah sistem
import webbrowser  # Untuk membuka URL di browser

# Fungsi untuk menangani aksi login
def login():
    """
    Memvalidasi apakah email dan password telah diisi.
    Jika kosong, menampilkan peringatan.
    Jika terisi, menampilkan pesan berhasil login.
    """
    email = email_entry.get()  # Mengambil input email dari pengguna
    password = password_entry.get()  # Mengambil input password dari pengguna
    
    if email == "" or password == "":  # Mengecek jika email atau password kosong
        messagebox.showwarning("Input Error", "Please enter both email and password.")  # Menampilkan peringatan
    else:
        messagebox.showinfo("Login", "Logged in successfully!")  # Menampilkan pesan sukses

# Fungsi untuk membuka link login Google
def open_google():
    """
    Membuka halaman login Google di browser default.
    """
    webbrowser.open("https://accounts.google.com/signin")  # URL halaman login Google

# Fungsi untuk membuka link login Facebook
def open_facebook():
    """
    Membuka halaman login Facebook di browser default.
    """
    webbrowser.open("https://www.facebook.com/login")  # URL halaman login Facebook

# Fungsi untuk membuka halaman register (file Python lain)
def open_register():
    """
    Membuka file register-nblzzz.py untuk proses registrasi.
    Jika terjadi error, menampilkan pesan kesalahan.
    """
    try:
        os.system("python register-nblzzz.py")  # Menjalankan file Python lain
    except Exception as e:
        messagebox.showerror("Error", f"Could not open register page: {e}")  # Menampilkan error jika file tidak ditemukan

# Membuat jendela utama aplikasi
root = tk.Tk()  # Membuat window utama
root.title("Login Page")  # Memberi judul pada window
root.geometry("600x400")  # Mengatur ukuran window (lebar x tinggi)

# Mengatur warna latar belakang window
root.config(bg="#a8e6cf")  # Warna latar hijau muda

# Membuat frame untuk menampung elemen login
login_frame = tk.Frame(root, bg="#f0f8ff", padx=20, pady=20)  # Frame dengan padding
login_frame.pack(expand=True, fill="both", padx=20, pady=20)  # Frame dipusatkan dan memenuhi ruang

# Menambahkan teks sambutan
welcome_label = tk.Label(login_frame, text="Welcome Back", font=("Arial", 24), bg="#f0f8ff")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")  # Teks ditempatkan di atas tengah

# Tombol login menggunakan Google
google_button = tk.Button(
    login_frame, text="Google", font=("Arial", 12), bg="#00d4ff", fg="white", width=20, command=open_google
)
google_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew")  # Tombol di baris pertama, kolom kiri

# Tombol login menggunakan Facebook
facebook_button = tk.Button(
    login_frame, text="Facebook", font=("Arial", 12), bg="#007bff", fg="white", width=20, command=open_facebook
)
facebook_button.grid(row=1, column=1, pady=10, padx=10, sticky="ew")  # Tombol di baris pertama, kolom kanan

# Menambahkan teks "OR" sebagai pemisah
or_label = tk.Label(login_frame, text="OR", font=("Arial", 12), bg="#f0f8ff")
or_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")  # Teks pemisah di tengah

# Input untuk email
email_label = tk.Label(login_frame, text="Email", font=("Arial", 12), bg="#f0f8ff")
email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")  # Label email di kolom kiri
email_entry = tk.Entry(login_frame, font=("Arial", 12))
email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")  # Input email di kolom kanan

# Input untuk password
password_label = tk.Label(login_frame, text="Password", font=("Arial", 12), bg="#f0f8ff")
password_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")  # Label password di kolom kiri
password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*")  # Input password disembunyikan dengan tanda "*"
password_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")  # Input password di kolom kanan

# Tombol untuk login
login_button = tk.Button(
    login_frame, text="Login", font=("Arial", 14), bg="#007bff", fg="white", command=login
)
login_button.grid(row=5, column=0, columnspan=2, pady=20, sticky="ew")  # Tombol login di bawah input

# Link untuk membuka halaman register
signup_label = tk.Label(
    login_frame, text="Don't have an account? Sign up", font=("Arial", 10), bg="#f0f8ff", fg="#007bff", cursor="hand2"
)
signup_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")  # Label link register di bawah tombol login
signup_label.bind("<Button-1>", lambda e: open_register())  # Membuka halaman register saat diklik

# Membuat tata letak responsif
for i in range(7):  # Menyesuaikan jumlah baris pada grid
    login_frame.grid_rowconfigure(i, weight=1)  # Setiap baris memiliki proporsi tinggi yang sama
login_frame.grid_columnconfigure(0, weight=1)  # Kolom kiri responsif
login_frame.grid_columnconfigure(1, weight=1)  # Kolom kanan responsif

# Menjalankan event loop Tkinter untuk aplikasi GUI
root.mainloop()  # Loop utama yang membuat aplikasi tetap berjalan

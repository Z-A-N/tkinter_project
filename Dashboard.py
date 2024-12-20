import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from mysql.connector import Error
from tkcalendar import DateEntry


# Membuat koneksi ke database MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',       # Ubah sesuai dengan host database Anda
        user='root',            # Ubah dengan username MySQL Anda
        password='',    # Ubah dengan password MySQL Anda
        database='keuangan_db'  # Pastikan nama database benar
    )
    if conn.is_connected():
        cursor = conn.cursor()
        print("Connected to MySQL Database")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# ======= Setup Jendela Utama =======
root = tk.Tk()
root.iconbitmap("assets/img/logo.ico")  # Gunakan logo .ico
root.title("Aplikasi Pengelolaan Keuangan")  # Judul aplikasi
root.geometry("800x600")  # Ukuran jendela
root.resizable(True, True)  # Membuat jendela bisa diubah ukurannya

# ======= Fungsi untuk mengganti konten =======

def change_content(page_name):
    # Hapus semua widget yang ada di content_frame (selain saldo)
    for widget in content_frame.winfo_children():
        widget.destroy()
        
    # Menampilkan konten sesuai pilihan
    if page_name == "Home":
        display_home()
    elif page_name == "Transaksi":
        display_transactions()
    elif page_name == "Laporan":
        display_report()
    elif page_name == "Pengaturan":
        display_settings()
    elif page_name == "Logout":
        content_label = tk.Label(content_frame, text="Anda telah Logout.", font=("Arial", 14))
        content_label.pack(pady=50)
    else:
        content_label = tk.Label(content_frame, text=f"Anda Memilih {page_name}", font=("Arial", 14))
        content_label.pack(pady=50)
# Fungsi untuk menghitung saldo
def hitung_saldo(cursor):
    # Mengambil total pemasukan dari database
    cursor.execute("SELECT SUM(nominal) FROM transaksi WHERE jenis_transaksi = 'Pemasukan'")
    total_pemasukan = cursor.fetchone()[0] or 0
    
    # Mengambil total pengeluaran dari database
    cursor.execute("SELECT SUM(nominal) FROM transaksi WHERE jenis_transaksi = 'Pengeluaran'")
    total_pengeluaran = cursor.fetchone()[0] or 0
    
    # Menghitung saldo keseluruhan
    saldo_keseluruhan = total_pemasukan - total_pengeluaran

    return total_pemasukan, total_pengeluaran, saldo_keseluruhan

# Fungsi untuk mengambil username berdasarkan user_id dari database
def get_username(user_id):
    try:
        # Mengambil username dari database berdasarkan user_id
        cursor.execute("SELECT username FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return "User Not Found"
    except mysql.connector.Error as e:
        print(f"Error fetching username: {e}")
        return "Error"

# Fungsi untuk update profile (misalnya membuka form update)
def update_profile():
    messagebox.showinfo("Update Profile", "Open profile update form here.")


# Menambahkan tombol logout pada dashboard (misalnya)
def logout():
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response:
        root.destroy()  # Menutup aplikasi saat logout
        os.system("python login-nblzzz.py")  # Kembali ke halaman login
        
def open_dashboard():
    root.withdraw()  # Sembunyikan jendela login
    # Buka dashboard di sini
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("1024x768")
    # Setup tampilan dashboard di sini
    dashboard_window.protocol("WM_DELETE_WINDOW", logout)  # Tambahkan logout ketika menutup


# ======= Menampilkan Halaman Home =======
def display_home():
    # Mengambil total pemasukan, pengeluaran dan saldo keseluruhan
    total_pemasukan, total_pengeluaran, saldo_keseluruhan = hitung_saldo(cursor)

    # Frame untuk Label Selamat datang
    content_label = tk.Label(content_frame, text="Selamat datang di Aplikasi Pengelolaan Keuangan!", font=("Arial", 16, "bold"), bg="#ECF0F1")
    content_label.pack(pady=30)

    # Frame untuk Menampilkan Saldo dengan Card Style
    saldo_frame = tk.Frame(content_frame, bg="#FFFFFF", relief="solid", borderwidth=1, padx=30, pady=20)
    saldo_frame.pack(fill="x", pady=20)

    saldo_label = tk.Label(saldo_frame, text="Saldo Keseluruhan", font=("Arial", 18, "bold"), bg="#FFFFFF")
    saldo_label.pack(side="top", pady=5)

    # Menampilkan saldo secara dinamis
    saldo_masuk_label = tk.Label(saldo_frame, text=f"Total Pemasukan: Rp {total_pemasukan}", font=("Arial", 14), bg="#FFFFFF")
    saldo_masuk_label.pack(side="left", padx=20)

    saldo_keluar_label = tk.Label(saldo_frame, text=f"Total Pengeluaran: Rp {total_pengeluaran}", font=("Arial", 14), bg="#FFFFFF")
    saldo_keluar_label.pack(side="left", padx=20)

    saldo_keseluruhan_label = tk.Label(saldo_frame, text=f"Sisa Saldo: Rp {saldo_keseluruhan}", font=("Arial", 14), bg="#FFFFFF")
    saldo_keseluruhan_label.pack(side="left", padx=20)

    # Tabel Data Terbaru (Card Style)
    update_label = tk.Label(content_frame, text="Data Transaksi Terbaru", font=("Arial", 16, "bold"), bg="#ECF0F1")
    update_label.pack(pady=20)

    # Frame untuk tabel
    table_frame = tk.Frame(content_frame, bg="#FFFFFF", relief="solid", borderwidth=1, padx=10, pady=10)
    table_frame.pack(fill="both", pady=20)

    # Header tabel
    headers = ["ID", "Jenis Transaksi", "Nominal", "Tanggal", "Deskripsi", "Username"]
    for col, header in enumerate(headers):
        tk.Label(table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=10, pady=5)

    # Mengambil dan menampilkan data transaksi dari database dengan Username
    try:
        # Query untuk mengambil data transaksi dan username
        cursor.execute("""
            SELECT t.id, t.jenis_transaksi, t.nominal, t.tanggal_transaksi, t.deskripsi, u.username
            FROM transaksi t
            JOIN users u ON t.user_id = u.id
            ORDER BY t.tanggal_transaksi DESC
        """)
        transactions = cursor.fetchall()
        
        # Menampilkan data transaksi di tabel
        for i, transaction in enumerate(transactions, start=1):
            for j, value in enumerate(transaction):
                tk.Label(table_frame, text=value, font=("Arial", 12)).grid(row=i, column=j, padx=10, pady=5)
    except Error as e:
        tk.Label(table_frame, text=f"Error: {e}", font=("Arial", 12, "italic"), fg="red").grid(row=1, column=0, columnspan=6)

def display_transactions():
    content_label = tk.Label(content_frame, text="Catatan Transaksi", font=("Arial", 14))
    content_label.pack(pady=50)

    # Frame untuk Form Transaksi
    form_frame = tk.Frame(content_frame, bg="white")
    form_frame.pack(pady=20)

    # Pilih Jenis Transaksi (Pemasukan atau Pengeluaran)
    transaksi_type_label = tk.Label(form_frame, text="Jenis Transaksi", font=("Arial", 12))
    transaksi_type_label.grid(row=0, column=0, padx=10, pady=10)

    transaksi_type_var = tk.StringVar()
    transaksi_type_var.set("Pemasukan")  # Default value
    pemasukan_radio = tk.Radiobutton(form_frame, text="Pemasukan", variable=transaksi_type_var, value="Pemasukan", font=("Arial", 12))
    pengeluaran_radio = tk.Radiobutton(form_frame, text="Pengeluaran", variable=transaksi_type_var, value="Pengeluaran", font=("Arial", 12))
    pemasukan_radio.grid(row=0, column=1, padx=10, pady=10)
    pengeluaran_radio.grid(row=0, column=2, padx=10, pady=10)

    # Nominal Transaksi
    nominal_label = tk.Label(form_frame, text="Nominal", font=("Arial", 12))
    nominal_label.grid(row=1, column=0, padx=10, pady=10)

    nominal_entry = tk.Entry(form_frame, font=("Arial", 12))
    nominal_entry.grid(row=1, column=1, padx=10, pady=10)

    # Tanggal Transaksi
    form_frame.grid_columnconfigure(1, weight=1)  # Memberikan bobot agar kolom 1 bisa melebar
    form_frame.grid_columnconfigure(2, weight=1)  # Memberikan bobot pada kolom lainnya

    tanggal_label = tk.Label(form_frame, text="Tanggal Transaksi", font=("Arial", 12))
    tanggal_label.grid(row=2, column=0, padx=10, pady=10)

    tanggal_entry = DateEntry(form_frame, font=("Arial", 12), width=20, background="darkblue", foreground="white", borderwidth=2)
    tanggal_entry.grid(row=2, column=1, padx=10, pady=10)


    # Deskripsi Transaksi
    deskripsi_label = tk.Label(form_frame, text="Deskripsi", font=("Arial", 12))
    deskripsi_label.grid(row=3, column=0, padx=10, pady=10)

    deskripsi_entry = tk.Entry(form_frame, font=("Arial", 12))
    deskripsi_entry.grid(row=3, column=1, padx=10, pady=10)

    # List to hold transactions (you may use a database in a real scenario)
    transactions = []
    
    # Fungsi untuk mendapatkan tanggal yang dipilih
    def get_selected_date():
        selected_date = tanggal_entry.get_date()  # Mendapatkan tanggal yang dipilih
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Format tanggal ke format yang sesuai
        return formatted_date

    # Function to save transaction
    def save_transaction():
        jenis_transaksi = transaksi_type_var.get()
        nominal = nominal_entry.get()
        tanggal = get_selected_date()  # Mengambil tanggal yang telah diformat
        deskripsi = deskripsi_entry.get()
        user_id = 1  # Misalnya user_id statis

        # Validasi Input
        try:
            # Validasi nominal (harus angka)
            nominal = float(nominal)
            if nominal <= 0:
                raise ValueError("Nominal harus lebih besar dari 0.")
        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")
            return

        if not deskripsi:
            messagebox.showwarning("Peringatan", "Deskripsi tidak boleh kosong!")
            return

        # Simpan ke database
        try:
            cursor.execute(
                "INSERT INTO transaksi (jenis_transaksi, nominal, tanggal_transaksi, deskripsi, user_id) VALUES (%s, %s, %s, %s, %s)",
                (jenis_transaksi, nominal, tanggal, deskripsi, user_id)
            )
            conn.commit()
            messagebox.showinfo("Sukses", "Transaksi berhasil disimpan!")
            nominal_entry.delete(0, tk.END)
            deskripsi_entry.delete(0, tk.END)
            display_transaction_table()
        except Error as e:
            messagebox.showerror("Error", f"Gagal menyimpan transaksi: {e}")

    # Tombol Simpan Transaksi
    simpan_button = tk.Button(form_frame, text="Simpan Transaksi", font=("Arial", 12), bg="#1ABC9C", fg="white", command=save_transaction)
    simpan_button.grid(row=4, column=0, columnspan=3, pady=20)

    # Function to display the transaction table
    def display_transaction_table():
        # Remove existing transaction table if any
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Header tabel
        headers = ["ID", "Jenis Transaksi", "Nominal", "Tanggal", "Deskripsi", "User ID"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=10, pady=5)

        # Display transactions
        try:
            cursor.execute("SELECT id, jenis_transaksi, nominal, tanggal_transaksi, deskripsi, user_id FROM transaksi ORDER BY tanggal_transaksi DESC")
            transactions = cursor.fetchall()
            for i, transaction in enumerate(transactions, start=1):
                for j, value in enumerate(transaction):
                    tk.Label(table_frame, text=value, font=("Arial", 12)).grid(row=i, column=j, padx=10, pady=5)
        except Error as e:
            tk.Label(table_frame, text=f"Error: {e}", font=("Arial", 12, "italic"), fg="red").grid(row=1, column=0, columnspan=6)

    # Tabel Data Transaksi
    update_label = tk.Label(content_frame, text="Data Transaksi Terbaru", font=("Arial", 14, "bold"))
    update_label.pack(pady=20)

    # Frame untuk tabel transaksi
    table_frame = tk.Frame(content_frame, bg="white", padx=10, pady=10)
    table_frame.pack(fill="x", pady=10)

    # Initial call to display an empty table
    display_transaction_table()

def display_report():
    content_label = tk.Label(content_frame, text="Laporan Keuangan", font=("Arial", 14))
    content_label.pack(pady=50)

def display_settings():
    content_label = tk.Label(content_frame, text="Halaman Pengaturan", font=("Arial", 14))
    content_label.pack(pady=50)

# ======= Tampilan Saldo =======
def display_saldo():
    # Menampilkan saldo di bagian atas content_frame
    saldo_frame = tk.Frame(content_frame, bg="white")
    saldo_frame.pack(fill="x", pady=10)

    saldo_label = tk.Label(saldo_frame, text="Saldo Keseluruhan", font=("Arial", 16, "bold"))
    saldo_label.pack(side="top", pady=5)

    # Misalnya saldo masuk dan keluar
    saldo_masuk = 5000
    saldo_keluar = 3000
    saldo_keseluruhan = saldo_masuk - saldo_keluar

    saldo_masuk_label = tk.Label(saldo_frame, text=f"Saldo Masuk: Rp {saldo_masuk}", font=("Arial", 12))
    saldo_masuk_label.pack(side="left", padx=20)

    saldo_keluar_label = tk.Label(saldo_frame, text=f"Saldo Keluar: Rp {saldo_keluar}", font=("Arial", 12))
    saldo_keluar_label.pack(side="left", padx=20)

    saldo_keseluruhan_label = tk.Label(saldo_frame, text=f"Saldo Keseluruhan: Rp {saldo_keseluruhan}", font=("Arial", 12))
    saldo_keseluruhan_label.pack(side="left", padx=20)

# ======= Navbar =======
navbar = tk.Frame(root, bg="#2C3E50", height=50)  # Navbar dengan warna biru tua
navbar.pack(side="top", fill="x")  # Navbar hanya mengisi lebar

# Menambahkan label di navbar dengan efek hover
def on_enter(e):
    e.widget['background'] = "#1ABC9C"  # Warna ketika hover
    e.widget['foreground'] = "white"

def on_leave(e):
    e.widget['background'] = "#2C3E50"  # Warna ketika tidak hover
    e.widget['foreground'] = "white"

# Menambahkan label dengan ikon dan efek hover
navbar_label = tk.Label(navbar, text="Aplikasi Pengelolaan Keuangan", fg="white", font=("Arial", 16, "bold"), bg="#2C3E50")
navbar_label.pack(pady=10)

navbar_label.bind("<Enter>", on_enter)
navbar_label.bind("<Leave>", on_leave)

# ======= Sidebar =======
sidebar_width = 200  # Lebar sidebar
sidebar = tk.Frame(root, width=sidebar_width, bg="#34495E", height=600, relief="sunken")  # Warna biru gelap
sidebar.pack(side="left", fill="y")

# Dashboard frame
dashboard_frame = tk.Frame(root, bg="#f0f8ff")
dashboard_frame.pack(side="right", fill="both", expand=True)

# Simulasi user_id (biasanya ini akan diambil setelah login)
user_id = 1  # Misalnya, setelah login, kita tahu user_id = 1

# Menampilkan profile di sidebar
def display_profile(user_id):
    username = get_username(user_id)  # Mengambil username berdasarkan user_id
    profile_frame = tk.Frame(sidebar, bg="#2C3E50", pady=20)  # Frame untuk profile dengan background gelap
    profile_frame.pack(fill="x")  # Menempatkan frame secara horizontal (full width)

    profile_label = tk.Label(
        profile_frame,
        text=f"👤 {username}",  # Menampilkan username
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#2C3E50"
    )
    profile_label.pack()  # Menampilkan label di dalam frame
    
    # Tombol update profile
    update_profile_button = tk.Button(
        profile_frame,
        text="Update Profile",  # Teks pada tombol
        font=("Arial", 14),
        bg="#4CAF50",
        fg="white",
        command=update_profile  # Mengarah ke fungsi update profile
    )
    update_profile_button.pack(pady=20)  # Menempatkan tombol dengan sedikit padding

# Panggil fungsi untuk menampilkan profile setelah login
display_profile(user_id)


divider = tk.Frame(sidebar, bg="white", height=2)  # Pembatas
divider.pack(fill="x", pady=5)

# Fungsi untuk efek hover
def on_enter(e):
    e.widget['background'] = "#1ABC9C"  # Hijau muda
    e.widget['foreground'] = "white"

def on_leave(e):
    e.widget['background'] = "#34495E"  # Warna asli
    e.widget['foreground'] = "white"

# Tombol Sidebar dengan Hover Effect
def create_sidebar_button(text, icon, command):
    btn = tk.Button(
        sidebar,
        text=text,
        image=icon,
        compound="left",
        font=("Arial", 12),
        bg="#34495E",
        fg="white",
        activebackground="#1ABC9C",
        activeforeground="white",
        bd=0,
        command=command,
        pady=10
    )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(fill="x", pady=5)
    return btn

# Tombol Sidebar dengan fungsionalitas untuk ganti konten
home_image = Image.open("assets/img/bx-home.ico")  # Ganti dengan path ke gambar .ico Anda
home_image = home_image.resize((20, 20))  # Menyesuaikan ukuran gambar jika perlu
home_icon = ImageTk.PhotoImage(home_image)
create_sidebar_button("Home", home_icon, lambda: change_content("Home"))

transactions_image = Image.open("assets/img/bx-transaksi.ico")  # Ganti dengan path ke gambar .ico Anda
transactions_image = transactions_image.resize((20, 20))  # Menyesuaikan ukuran gambar jika perlu
transactions_icon = ImageTk.PhotoImage(transactions_image)
create_sidebar_button("Transaksi", transactions_icon, lambda: change_content("Transaksi"))

report_image = Image.open("assets/img/bx-laporan.ico")
report_image = report_image.resize((20, 20))
report_icon = ImageTk.PhotoImage(report_image)
create_sidebar_button("Laporan", report_icon, lambda: change_content("Laporan"))

settings_image = Image.open("assets/img/settings.ico")
settings_image = settings_image.resize((20,20))
settings_icon = ImageTk.PhotoImage(settings_image)
create_sidebar_button("Pengaturan", settings_icon, lambda: change_content("Pengaturan"))

# Memuat gambar ikon logout
logout_image = Image.open("assets/img/logout.ico")  # Pastikan path file benar
logout_image = logout_image.resize((20, 20))  # Resize gambar sesuai ukuran yang diinginkan
logout_icon = ImageTk.PhotoImage(logout_image)  # Mengonversi gambar menjadi format yang bisa digunakan Tkinter
create_sidebar_button("Logout", logout_icon, logout)
# ======= Main Content Area =======
main_frame = tk.Frame(root, bg="white", height=600)  # Area utama untuk konten
main_frame.pack(side="right", fill="both", expand=True)

# Menampilkan saldo di atas konten utama
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(fill="both", expand=True)

# Menampilkan halaman Home pertama kali
display_home()


# Menjalankan aplikasi
root.mainloop()

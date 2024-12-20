import tkinter as tk
from PIL import Image, ImageTk

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

# ======= Menampilkan Halaman Home =======
def display_home():
    # Label Selamat datang
    content_label = tk.Label(content_frame, text="Selamat datang di Aplikasi Pengelolaan Keuangan!", font=("Arial", 16, "bold"), bg="#ECF0F1")
    content_label.pack(pady=30)

    # Frame untuk Menampilkan Saldo dengan Card Style
    saldo_frame = tk.Frame(content_frame, bg="#FFFFFF", relief="solid", borderwidth=1, padx=30, pady=20)
    saldo_frame.pack(fill="x", pady=20)

    saldo_label = tk.Label(saldo_frame, text="Saldo Keseluruhan", font=("Arial", 18, "bold"), bg="#FFFFFF")
    saldo_label.pack(side="top", pady=5)

    # Data Saldo (Misalnya)
    saldo_masuk = 5000  # Pemasukan
    saldo_keluar = 3000  # Pengeluaran
    saldo_keseluruhan = saldo_masuk - saldo_keluar

    # Tampilan saldo dalam bentuk card
    saldo_masuk_label = tk.Label(saldo_frame, text=f"Total Pemasukan: Rp {saldo_masuk}", font=("Arial", 14), bg="#FFFFFF")
    saldo_masuk_label.pack(side="left", padx=20)

    saldo_keluar_label = tk.Label(saldo_frame, text=f"Total Pengeluaran: Rp {saldo_keluar}", font=("Arial", 14), bg="#FFFFFF")
    saldo_keluar_label.pack(side="left", padx=20)

    saldo_keseluruhan_label = tk.Label(saldo_frame, text=f"Sisa Saldo: Rp {saldo_keseluruhan}", font=("Arial", 14), bg="#FFFFFF")
    saldo_keseluruhan_label.pack(side="left", padx=20)

    # Tabel Data Terbaru (Card Style)
    update_label = tk.Label(content_frame, text="Data Transaksi Terbaru", font=("Arial", 16, "bold"), bg="#ECF0F1")
    update_label.pack(pady=20)

    # Frame untuk tabel
    table_frame = tk.Frame(content_frame, bg="#FFFFFF", relief="solid", borderwidth=1, padx=10, pady=10)
    table_frame.pack(fill="both", pady=20)

    # Judul Kolom Tabel dengan desain lebih menarik
    col_headers = ["Jenis Transaksi", "Nominal", "Tanggal", "Deskripsi"]
    header_style = {"font": ("Arial", 12, "bold"), "bg": "#3498DB", "fg": "white", "padx": 10, "pady": 5}
    for col, header in enumerate(col_headers):
        col_label = tk.Label(table_frame, text=header, **header_style)
        col_label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")

    # Data Dummy untuk Tabel (contoh)
    transactions = [
        ("Pemasukan", 5000, "2024-12-19", "Gaji"),
        ("Pengeluaran", 1000, "2024-12-18", "Belanja"),
        ("Pemasukan", 2000, "2024-12-17", "Proyek"),
    ]

    # Menampilkan data transaksi dengan desain yang lebih menarik
    for i, transaction in enumerate(transactions):
        for j, value in enumerate(transaction):
            data_label = tk.Label(table_frame, text=value, font=("Arial", 12), padx=10, pady=5)
            data_label.grid(row=i+1, column=j, padx=10, pady=5)
    # Label Selamat datang
    content_label = tk.Label(content_frame, text="Selamat datang di Aplikasi Pengelolaan Keuangan!", font=("Arial", 16, "bold"), bg="#ECF0F1")
    content_label.pack(pady=30)

    # Frame untuk Menampilkan Saldo dengan Card Style
    saldo_frame = tk.Frame(content_frame, bg="#FFFFFF", relief="solid", borderwidth=1, padx=30, pady=20)
    saldo_frame.pack(fill="x", pady=20)

    saldo_label = tk.Label(saldo_frame, text="Saldo Keseluruhan", font=("Arial", 18, "bold"), bg="#FFFFFF")
    saldo_label.pack(side="top", pady=5)

    # Data Saldo (Misalnya)
    saldo_masuk = 5000  # Pemasukan
    saldo_keluar = 3000  # Pengeluaran
    saldo_keseluruhan = saldo_masuk - saldo_keluar

    # Tampilan saldo dalam bentuk card
    saldo_masuk_label = tk.Label(saldo_frame, text=f"Total Pemasukan: Rp {saldo_masuk}", font=("Arial", 14), bg="#FFFFFF")
    saldo_masuk_label.pack(side="left", padx=20)

    saldo_keluar_label = tk.Label(saldo_frame, text=f"Total Pengeluaran: Rp {saldo_keluar}", font=("Arial", 14), bg="#FFFFFF")
    saldo_keluar_label.pack(side="left", padx=20)

    saldo_keseluruhan_label = tk.Label(saldo_frame, text=f"Sisa Saldo: Rp {saldo_keseluruhan}", font=("Arial", 14), bg="#FFFFFF")
    saldo_keseluruhan_label.pack(side="left", padx=20)

    # Tabel Data Terbaru (Card Style)
    update_label = tk.Label(content_frame, text="Data Transaksi Terbaru", font=("Arial", 16, "bold"), bg="#ECF0F1")
    update_label.pack(pady=20)

    # Frame untuk tabel
    table_frame = tk.Frame(content_frame, bg="#FFFFFF", relief="solid", borderwidth=1, padx=10, pady=10)
    table_frame.pack(fill="both", pady=20)

    # Judul Kolom Tabel dengan desain lebih menarik
    col_headers = ["Jenis Transaksi", "Nominal", "Tanggal", "Deskripsi"]
    header_style = {"font": ("Arial", 12, "bold"), "bg": "#3498DB", "fg": "white", "padx": 10, "pady": 5}
    for col, header in enumerate(col_headers):
        col_label = tk.Label(table_frame, text=header, **header_style)
        col_label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")

    # Data Dummy untuk Tabel (contoh)
    transactions = [
        ("Pemasukan", 5000, "2024-12-19", "Gaji"),
        ("Pengeluaran", 1000, "2024-12-18", "Belanja"),
        ("Pemasukan", 2000, "2024-12-17", "Proyek"),
    ]

    # Menampilkan data transaksi dengan desain yang lebih menarik
    for i, transaction in enumerate(transactions):
        for j, value in enumerate(transaction):
            data_label = tk.Label(table_frame, text=value, font=("Arial", 12), padx=10, pady=5)
            data_label.grid(row=i+1, column=j, padx=10, pady=5)

    # Menambahkan efek hover pada tabel
    def on_enter_table(e):
        e.widget['background'] = "#ECF0F1"  # Warna saat hover
        e.widget['foreground'] = "black"

    def on_leave_table(e):
        e.widget['background'] = "white"  # Warna normal
        e.widget['foreground'] = "black"

    # Mengaplikasikan efek hover pada seluruh data label
    for row in table_frame.winfo_children():
        if isinstance(row, tk.Label):
            row.bind("<Enter>", on_enter_table)
            row.bind("<Leave>", on_leave_table)

    content_label = tk.Label(content_frame, text="Selamat datang di Aplikasi Pengelolaan Keuangan!", font=("Arial", 14))
    content_label.pack(pady=50)

    # Frame untuk Menampilkan Saldo
    saldo_frame = tk.Frame(content_frame, bg="white", padx=20, pady=10)
    saldo_frame.pack(fill="x", pady=10)

    saldo_label = tk.Label(saldo_frame, text="Saldo Keseluruhan", font=("Arial", 16, "bold"))
    saldo_label.pack(side="top", pady=5)

    # Misalnya saldo masuk dan keluar
    saldo_masuk = 5000  # Pemasukan
    saldo_keluar = 3000  # Pengeluaran
    saldo_keseluruhan = saldo_masuk - saldo_keluar

    saldo_masuk_label = tk.Label(saldo_frame, text=f"Total Pemasukan: Rp {saldo_masuk}", font=("Arial", 12))
    saldo_masuk_label.pack(side="left", padx=20)

    saldo_keluar_label = tk.Label(saldo_frame, text=f"Total Pengeluaran: Rp {saldo_keluar}", font=("Arial", 12))
    saldo_keluar_label.pack(side="left", padx=20)

    saldo_keseluruhan_label = tk.Label(saldo_frame, text=f"Sisa Saldo: Rp {saldo_keseluruhan}", font=("Arial", 12))
    saldo_keseluruhan_label.pack(side="left", padx=20)

    # Tabel Data Terbaru
    update_label = tk.Label(content_frame, text="Data Transaksi Terbaru", font=("Arial", 14, "bold"))
    update_label.pack(pady=20)

    # Frame untuk tabel
    table_frame = tk.Frame(content_frame, bg="white", padx=10, pady=10)
    table_frame.pack(fill="x", pady=10)

    # Judul Kolom Tabel
    col_headers = ["Jenis Transaksi", "Nominal", "Tanggal", "Deskripsi"]
    for col, header in enumerate(col_headers):
        col_label = tk.Label(table_frame, text=header, font=("Arial", 12, "bold"))
        col_label.grid(row=0, column=col, padx=10, pady=5)

    # Data Dummy untuk Tabel (untuk contoh)
    transactions = [
        ("Pemasukan", 5000, "2024-12-19", "Gaji"),
        ("Pengeluaran", 1000, "2024-12-18", "Belanja"),
        ("Pemasukan", 2000, "2024-12-17", "Proyek"),
    ]

    # Menampilkan data transaksi di tabel
    for i, transaction in enumerate(transactions):
        for j, value in enumerate(transaction):
            data_label = tk.Label(table_frame, text=value, font=("Arial", 12))
            data_label.grid(row=i+1, column=j, padx=10, pady=5)


    # Halaman Home (dengan saldo)
    content_label = tk.Label(content_frame, text="Selamat datang di Aplikasi Pengelolaan Keuangan!", font=("Arial", 14))
    content_label.pack(pady=50)

    # Menampilkan saldo
    display_saldo()

def display_transactions():
    content_label = tk.Label(content_frame, text="Halaman Transaksi", font=("Arial", 14))
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
    tanggal_label = tk.Label(form_frame, text="Tanggal Transaksi", font=("Arial", 12))
    tanggal_label.grid(row=2, column=0, padx=10, pady=10)

    tanggal_entry = tk.Entry(form_frame, font=("Arial", 12))
    tanggal_entry.grid(row=2, column=1, padx=10, pady=10)

    # Deskripsi Transaksi
    deskripsi_label = tk.Label(form_frame, text="Deskripsi", font=("Arial", 12))
    deskripsi_label.grid(row=3, column=0, padx=10, pady=10)

    deskripsi_entry = tk.Entry(form_frame, font=("Arial", 12))
    deskripsi_entry.grid(row=3, column=1, padx=10, pady=10)

    # List to hold transactions (you may use a database in a real scenario)
    transactions = []

    # Function to save transaction
    def save_transaction():
        jenis_transaksi = transaksi_type_var.get()
        nominal = nominal_entry.get()
        tanggal = tanggal_entry.get()
        deskripsi = deskripsi_entry.get()

        # Save the transaction (add to the transactions list)
        transactions.append((jenis_transaksi, nominal, tanggal, deskripsi))

        # Print for debugging
        print(f"{jenis_transaksi} - Nominal: {nominal} - Tanggal: {tanggal} - Deskripsi: {deskripsi}")

        # Clear the form
        nominal_entry.delete(0, tk.END)
        tanggal_entry.delete(0, tk.END)
        deskripsi_entry.delete(0, tk.END)

        # Refresh the transaction table
        display_transaction_table()

    simpan_button = tk.Button(form_frame, text="Simpan Transaksi", font=("Arial", 12), bg="#1ABC9C", fg="white", command=save_transaction)
    simpan_button.grid(row=4, column=0, columnspan=3, pady=20)

    # Function to display the transaction table
    def display_transaction_table():
        # Remove existing transaction table if any
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Create table header
        col_headers = ["Jenis Transaksi", "Nominal", "Tanggal", "Deskripsi"]
        for col, header in enumerate(col_headers):
            col_label = tk.Label(table_frame, text=header, font=("Arial", 12, "bold"))
            col_label.grid(row=0, column=col, padx=10, pady=5)

        # Display transactions
        for i, transaction in enumerate(transactions):
            for j, value in enumerate(transaction):
                data_label = tk.Label(table_frame, text=value, font=("Arial", 12))
                data_label.grid(row=i+1, column=j, padx=10, pady=5)

    # Tabel Data Transaksi
    update_label = tk.Label(content_frame, text="Data Transaksi Terbaru", font=("Arial", 14, "bold"))
    update_label.pack(pady=20)

    # Frame untuk tabel transaksi
    table_frame = tk.Frame(content_frame, bg="white", padx=10, pady=10)
    table_frame.pack(fill="x", pady=10)

    # Initial call to display an empty table
    display_transaction_table()

    content_label = tk.Label(content_frame, text="Halaman Transaksi", font=("Arial", 14))
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
    tanggal_label = tk.Label(form_frame, text="Tanggal Transaksi", font=("Arial", 12))
    tanggal_label.grid(row=2, column=0, padx=10, pady=10)

    tanggal_entry = tk.Entry(form_frame, font=("Arial", 12))
    tanggal_entry.grid(row=2, column=1, padx=10, pady=10)

    # Deskripsi Transaksi
    deskripsi_label = tk.Label(form_frame, text="Deskripsi", font=("Arial", 12))
    deskripsi_label.grid(row=3, column=0, padx=10, pady=10)

    deskripsi_entry = tk.Entry(form_frame, font=("Arial", 12))
    deskripsi_entry.grid(row=3, column=1, padx=10, pady=10)

    # Simpan Transaksi Button
    def save_transaction():
        jenis_transaksi = transaksi_type_var.get()
        nominal = nominal_entry.get()
        tanggal = tanggal_entry.get()
        deskripsi = deskripsi_entry.get()

        # Proses penyimpanan transaksi (misalnya simpan ke database atau list)
        print(f"{jenis_transaksi} - Nominal: {nominal} - Tanggal: {tanggal} - Deskripsi: {deskripsi}")

        # Clear Form
        nominal_entry.delete(0, tk.END)
        tanggal_entry.delete(0, tk.END)
        deskripsi_entry.delete(0, tk.END)

    simpan_button = tk.Button(form_frame, text="Simpan Transaksi", font=("Arial", 12), bg="#1ABC9C", fg="white", command=save_transaction)
    simpan_button.grid(row=4, column=0, columnspan=3, pady=20)


    content_label = tk.Label(content_frame, text="Halaman Transaksi", font=("Arial", 14))
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
    tanggal_label = tk.Label(form_frame, text="Tanggal Transaksi", font=("Arial", 12))
    tanggal_label.grid(row=2, column=0, padx=10, pady=10)

    tanggal_entry = tk.Entry(form_frame, font=("Arial", 12))
    tanggal_entry.grid(row=2, column=1, padx=10, pady=10)


    # Deskripsi Transaksi
    deskripsi_label = tk.Label(form_frame, text="Deskripsi", font=("Arial", 12))
    deskripsi_label.grid(row=4, column=0, padx=10, pady=10)

    deskripsi_entry = tk.Entry(form_frame, font=("Arial", 12))
    deskripsi_entry.grid(row=4, column=1, padx=10, pady=10)

    # Simpan Transaksi Button
    def save_transaction():
        jenis_transaksi = transaksi_type_var.get()
        nominal = nominal_entry.get()
        tanggal = tanggal_entry.get()
        deskripsi = deskripsi_entry.get()

        # Proses penyimpanan transaksi (misalnya simpan ke database atau list)
        print(f"{jenis_transaksi} - Nominal: {nominal} - Tanggal: {tanggal}  - Deskripsi: {deskripsi}")

        # Clear Form
        nominal_entry.delete(0, tk.END)
        tanggal_entry.delete(0, tk.END)
        deskripsi_entry.delete(0, tk.END)

    simpan_button = tk.Button(form_frame, text="Simpan Transaksi", font=("Arial", 12), bg="#1ABC9C", fg="white", command=save_transaction)
    simpan_button.grid(row=5, column=0, columnspan=3, pady=20)


    content_label = tk.Label(content_frame, text="Halaman Transaksi", font=("Arial", 14))
    content_label.pack(pady=50)

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

# Profil di Sidebar
profile_frame = tk.Frame(sidebar, bg="#2C3E50", pady=20)  # Latar lebih gelap
profile_frame.pack(fill="x")

profile_label = tk.Label(
    profile_frame,
    text="👤 Zulfika",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#2C3E50"
)
profile_label.pack()

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

logout_image = Image.open("assets/img/logout.ico")
logout_image = logout_image.resize((20,20))
logout_icon = ImageTk.PhotoImage(logout_image)
create_sidebar_button("Logout", logout_icon, lambda: change_content("Logout"))

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

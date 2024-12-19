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
    # Hapus semua widget yang ada di main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()
        

    # Buat label default terlebih dahulu
    content_label = tk.Label(main_frame, font=("Arial", 14))

    # Menampilkan konten sesuai pilihan
    if page_name == "Home":
        content_label.config(text="Selamat datang di Aplikasi Pengelolaan Keuangan!")
    elif page_name == "Transaksi":
        content_label.config(text="Halaman Transaksi")
    elif page_name == "Laporan":
        content_label.config(text="Laporan Keuangan")
    elif page_name == "Pengaturan":
        content_label.config(text="Halaman Pengaturan")
    elif page_name == "Logout":
        content_label.config(text="Anda telah Logout.")
    else:
        content_label.config(text=f"Anda Memilih {page_name}")  # Default jika tidak cocok
    
    # Tampilkan label
    content_label.pack(pady=50)

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
sidebar.pack(side="left", fill="y",)

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
main_frame = tk.Frame(root, bg="white", height=550)  # Area utama untuk konten
main_frame.pack(side="right", fill="both", expand=True)

# Menjalankan aplikasi
root.mainloop()

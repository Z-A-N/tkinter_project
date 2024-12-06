import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime

# Fungsi untuk menambah data keuangan
def tambah_transaksi():
    jenis = var_jenis.get()
    jumlah = entry_jumlah.get()
    keterangan = entry_keterangan.get()
    
    if not jumlah.isdigit():
        messagebox.showerror("Error", "Jumlah harus berupa angka.")
        return

    jumlah = int(jumlah)
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simpan data ke file CSV
    with open('data_keuangan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, jenis, jumlah, keterangan])

    # Bersihkan input setelah menyimpan
    entry_jumlah.delete(0, tk.END)
    entry_keterangan.delete(0, tk.END)
    tampilkan_data()

# Fungsi untuk menampilkan data dari file CSV
def tampilkan_data():
    for row in tree.get_children():
        tree.delete(row)
    try:
        with open('data_keuangan.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        open('data_keuangan.csv', 'w').close()

# Fungsi untuk membuat tombol kustom
def buat_tombol(frame, text, command):
    button = tk.Button(
        frame,
        text=text,
        command=command,
        bg="#4CAF50",  # Warna hijau
        fg="white",
        font=("Helvetica", 10, "bold"),
        relief="flat",
        borderwidth=0,
        highlightthickness=0
    )
    button.grid(row=3, column=1, padx=5, pady=10, sticky="ew")
    button.bind("<Enter>", lambda e: button.config(bg="#45a049"))
    button.bind("<Leave>", lambda e: button.config(bg="#4CAF50"))
    return button

# GUI Setup
root = tk.Tk()
root.title("Aplikasi Pengelola Keuangan")
root.geometry("1920x1080")
root.configure(bg="#f2f2f2")

# Canvas untuk latar belakang gradasi
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)

# Membuat gradasi warna
for i in range(1080):
    r = 0x66 + i // 4
    g = 0x9F
    b = 0xFF - i // 4
    
    # Pastikan nilai RGB tidak melebihi batas 0xFF
    r = min(r, 0xFF)
    b = max(b, 0x00)

    # Format warna menjadi valid dengan panjang 6 karakter
    warna = f'#{r:02X}{g:02X}{b:02X}'
    canvas.create_line(0, i, 1920, i, fill=warna)

# Frame di atas Canvas yang dipusatkan
frame = tk.Frame(canvas, bg="#f2f2f2", width=800, height=600)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Menempatkan frame di tengah

# Menyesuaikan frame agar responsif
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Input dan Label
tk.Label(frame, text="Jenis", bg="#f2f2f2", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Label(frame, text="Jumlah", bg="#f2f2f2", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Label(frame, text="Keterangan", bg="#f2f2f2", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")

var_jenis = tk.StringVar(value="Pemasukan")
ttk.OptionMenu(frame, var_jenis, "Pemasukan", "Pemasukan", "Pengeluaran").grid(row=0, column=1, padx=10, pady=10, sticky="ew")

entry_jumlah = ttk.Entry(frame, font=("Helvetica", 12))
entry_jumlah.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

entry_keterangan = ttk.Entry(frame, font=("Helvetica", 12))
entry_keterangan.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Menambahkan tombol kustom
buat_tombol(frame, "Tambah Transaksi", tambah_transaksi)

# Tabel untuk Menampilkan Data
style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"), background="#4CAF50", foreground="black")  # Ubah warna huruf menjadi hitam
style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="#f0f5f5", fieldbackground="#e6f7ff")
style.map("Treeview", background=[("selected", "#82c4c3")])

tree = ttk.Treeview(frame, columns=("Tanggal", "Jenis", "Jumlah", "Keterangan"), show='headings')
tree.heading("Tanggal", text="Tanggal")
tree.heading("Jenis", text="Jenis")
tree.heading("Jumlah", text="Jumlah")
tree.heading("Keterangan", text="Keterangan")
tree.column("Tanggal", anchor="center")
tree.column("Jenis", anchor="center")
tree.column("Jumlah", anchor="center")
tree.column("Keterangan", anchor="center")
tree.grid(row=4, column=0, columnspan=2, pady=20, sticky="nsew")

tampilkan_data()

root.mainloop()

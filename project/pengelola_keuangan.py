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

# GUI Setup
root = tk.Tk()
root.title("Aplikasi Pengelola Keuangan")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

# Input dan Label
tk.Label(frame, text="Jenis").grid(row=0, column=0)
tk.Label(frame, text="Jumlah").grid(row=1, column=0)
tk.Label(frame, text="Keterangan").grid(row=2, column=0)

var_jenis = tk.StringVar(value="Pemasukan")
tk.OptionMenu(frame, var_jenis, "Pemasukan", "Pengeluaran").grid(row=0, column=1)

entry_jumlah = tk.Entry(frame)
entry_jumlah.grid(row=1, column=1)

entry_keterangan = tk.Entry(frame)
entry_keterangan.grid(row=2, column=1)

tk.Button(frame, text="Tambah Transaksi", command=tambah_transaksi).grid(row=3, column=1, pady=5)

# Tabel untuk Menampilkan Data
tree = tk.ttk.Treeview(root, columns=("Tanggal", "Jenis", "Jumlah", "Keterangan"), show='headings')
tree.heading("Tanggal", text="Tanggal")
tree.heading("Jenis", text="Jenis")
tree.heading("Jumlah", text="Jumlah")
tree.heading("Keterangan", text="Keterangan")
tree.pack(pady=10)

tampilkan_data()

root.mainloop()
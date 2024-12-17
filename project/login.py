# Sistem Login dengan tkinter
import tkinter as tk
# Membuat jendela Utama
window = tk.Tk() # Membuat objek window dari kelas Tk (Variabel window mereferensikan objek tk.Tk)

# METODE - METODE DARI OBJEK WINDOW ( Instansiasi dari kelas Tk di Tkinter) #

# Mengatur judul jendela
window.title("Login Form")

# Menentukan Icon jendela (file.icon)
<<
=======
 window.iconbitmap("/assets/logo.ico")
>>>>>>> 42314c0182edd5eb08a9e8d29367298136efb856

# Membuat jendela full screen
window.state("zoomed")

# Membuat Frame (objek : frame)
frame = tk.Frame(window, bg="lightgrey", width=200, height=150)
frame.pack(pady=20, padx=20)

# Menjalankan aplikasi Tkinter
window.mainloop()
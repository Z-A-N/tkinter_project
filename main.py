import tkinter as tk
import login  # Import file login.py
import register  # Import file register.py

def show_main_window():
    root = tk.Tk()
    root.title("Aplikasi Pengelolaan Keuangan")
    root.geometry("800x600")

    # Tombol untuk Login
    login_button = tk.Button(root, text="Login", command=lambda: login.show_login(root))
    login_button.pack(pady=20)

    # Tombol untuk Registrasi
    register_button = tk.Button(root, text="Registrasi", command=lambda: register.show_register(root))
    register_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    show_main_window()

import tkinter as tk
from tkinter import messagebox

# Function to handle the login action
def login():
    email = email_entry.get()
    password = password_entry.get()
    
    if email == "" or password == "":
        messagebox.showwarning("Input Error", "Please enter both email and password.")
    else:
        messagebox.showinfo("Login", "Logged in successfully!")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("600x400")  # Size of the window

# Set the background color
root.config(bg="#a8e6cf")

# Create the login container frame
login_frame = tk.Frame(root, bg="#f0f8ff", width=500, height=350, padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Add the welcome text
welcome_label = tk.Label(login_frame, text="Welcome Back", font=("Arial", 24), bg="#f0f8ff")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Google and Facebook buttons
google_button = tk.Button(login_frame, text="Google", font=("Arial", 12), bg="#00d4ff", fg="white", width=20)
google_button.grid(row=1, column=0, pady=10)

facebook_button = tk.Button(login_frame, text="Facebook", font=("Arial", 12), bg="#007bff", fg="white", width=20)
facebook_button.grid(row=1, column=1, pady=10)

# OR text
or_label = tk.Label(login_frame, text="OR", font=("Arial", 12), bg="#f0f8ff")
or_label.grid(row=2, column=0, columnspan=2, pady=10)

# Email entry
email_label = tk.Label(login_frame, text="Email", font=("Arial", 12), bg="#f0f8ff")
email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(login_frame, font=("Arial", 12), width=30)
email_entry.grid(row=3, column=1, padx=10)

# Password entry
password_label = tk.Label(login_frame, text="Password", font=("Arial", 12), bg="#f0f8ff")
password_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
password_entry = tk.Entry(login_frame, font=("Arial", 12), width=30, show="*")
password_entry.grid(row=4, column=1, padx=10)

# Login button
login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), bg="#007bff", fg="white", command=login)
login_button.grid(row=5, column=0, columnspan=2, pady=20)

# Sign-up link
signup_label = tk.Label(login_frame, text="Don't have an account? Sign up", font=("Arial", 10), bg="#f0f8ff", fg="#007bff")
signup_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

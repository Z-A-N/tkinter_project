import tkinter as tk
from tkinter import messagebox

# Function to handle the registration action
def register():
    full_name = full_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if full_name == "" or email == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill out all fields.")
    else:
        messagebox.showinfo("Registration", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Join Us")
root.geometry("1920x1080")  # Full HD resolution for the window

# Allow resizing in both directions
root.resizable(True, True)

# Apply a gradient background using Canvas
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)

# Gradient code for background (using shades of blue)
canvas.create_rectangle(0, 0, 1920, 1080, fill="#00c6ff", outline="")
canvas.create_rectangle(0, 0, 1920, 1080, fill="#0072ff", outline="", stipple="gray25")

# Create the card frame in the center
card_frame = tk.Frame(root, bg="#ffffff", width=1200, height=700, padx=20, pady=20)
card_frame.place(relx=0.5, rely=0.5, anchor="center")

# Right side frame for form
right_frame = tk.Frame(card_frame, bg="#f5f5f5", width=600, height=700)
right_frame.grid(row=0, column=1, padx=20)

# Title on the right
title_label = tk.Label(right_frame, text="Welcome Back", font=("Arial", 24), bg="#f5f5f5")
title_label.grid(row=0, column=0, pady=20)

# Full Name Entry
full_name_label = tk.Label(right_frame, text="Full Name", font=("Arial", 12), bg="#f5f5f5")
full_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
full_name_entry = tk.Entry(right_frame, font=("Arial", 12), width=30)
full_name_entry.grid(row=2, column=0, padx=10, pady=5)

# Email Entry
email_label = tk.Label(right_frame, text="Email", font=("Arial", 12), bg="#f5f5f5")
email_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(right_frame, font=("Arial", 12), width=30)
email_entry.grid(row=4, column=0, padx=10, pady=5)

# Password Entry
password_label = tk.Label(right_frame, text="Password", font=("Arial", 12), bg="#f5f5f5")
password_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(right_frame, font=("Arial", 12), width=30, show="*")
password_entry.grid(row=6, column=0, padx=10, pady=5)

# Social Media buttons
social_buttons_frame = tk.Frame(right_frame, bg="#f5f5f5")
social_buttons_frame.grid(row=7, column=0, pady=20)

google_button = tk.Button(social_buttons_frame, text="Google", font=("Arial", 12), fg="#0072ff", width=10)
google_button.grid(row=0, column=0, padx=10)

facebook_button = tk.Button(social_buttons_frame, text="Facebook", font=("Arial", 12), fg="#0072ff", width=10)
facebook_button.grid(row=0, column=1, padx=10)

# OR text
or_label = tk.Label(right_frame, text="OR", font=("Arial", 14), bg="#f5f5f5")
or_label.grid(row=8, column=0, pady=10)

# Register button
register_button = tk.Button(right_frame, text="Register", font=("Arial", 14), bg="#0072ff", fg="white", command=register)

# Hover effect for button
def on_enter(event):
    register_button['background'] = '#005bb5'

def on_leave(event):
    register_button['background'] = '#0072ff'

register_button.bind("<Enter>", on_enter)
register_button.bind("<Leave>", on_leave)

register_button.grid(row=9, column=0, pady=20)

# Login link
login_link = tk.Label(right_frame, text="Have an account? Login", font=("Arial", 10), bg="#f5f5f5", fg="#0072ff")
login_link.grid(row=10, column=0, pady=10)

# Run the Tkinter event loop
root.mainloop()

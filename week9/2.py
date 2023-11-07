import tkinter as tk
import mysql.connector as mysql
import re
from tkinter import messagebox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


conn = mysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="test"
)
cursor = conn.cursor(buffered=True)


cursor.execute("CREATE TABLE IF NOT EXISTS users (email VARCHAR(255) PRIMARY KEY, password VARCHAR(255))")
conn.commit()

def validate_login(email, password):
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    
    cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()

    if row is None:
        messagebox.showerror("Invalid Email", "Email not found. Please try again.")
    elif row[0] == password:
        messagebox.showinfo("Login Successful", "You are logged in successfully.")
    else:
        messagebox.showerror("Invalid Password", "Incorrect password. Please try again.")

def validate_registration(email, password, full_name, other_info):

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    cursor.execute("SELECT email FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()

    if row:
        messagebox.showerror("Email Exists", "Email is already registered. Please log in.")
    elif not re.match(r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$", password):
        messagebox.showerror("Invalid Password", "Password does not meet the specified criteria.")
    else:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
        messagebox.showinfo("Registration Successful", "Account created successfully. You can now log in.")

def login_window():
    window = tk.Tk()
    window.title("Login")

    
    bg_color = "SteelBlue1"  # Grey
    fg_color = "black"

    window.configure(bg=bg_color)

    email_label = tk.Label(window, text="Email:", bg=bg_color, fg=fg_color, font=("Abadi", 12))
    password_label = tk.Label(window, text="Password:", bg=bg_color, fg=fg_color, font=("Abadi", 12))
    
    email_entry = tk.Entry(window, font=("Abadi", 12))
    password_entry = tk.Entry(window, show="*", font=("Abadi", 12))


    login_button = tk.Button(window, text="Login", command=lambda: validate_login(email_entry.get(), password_entry.get()), bg=bg_color, fg=fg_color, font=("Abadi", 12))
    register_button = tk.Button(window, text="Register", command=registration_window, bg=bg_color, fg=fg_color, font=("Abadi", 12))
    
    
    email_label.grid(row=0, column=0, padx=10, pady=5)
    email_entry.grid(row=0, column=1, padx=10, pady=5)
    
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry.grid(row=1, column=1, padx=10, pady=5)
    
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    register_button.grid(row=2, column=1, columnspan=2, padx=150, pady=10)

    

    center_window(window, 400, 125) 

    window.mainloop()

def registration_window():
    registration_window = tk.Tk()
    registration_window.title("Registration")


    bg_color = "SteelBlue1" 
    fg_color = "black"

    registration_window.configure(bg=bg_color)

    email_label = tk.Label(registration_window, text="Email:", bg=bg_color, fg=fg_color, font=("Abadi", 12))
    email_label.pack()

    email_entry = tk.Entry(registration_window, font=("Abadi", 12))
    email_entry.pack()

    password_label = tk.Label(registration_window, text="Password:", bg=bg_color, fg=fg_color, font=("Abadi", 12))
    password_label.pack()

    password_entry = tk.Entry(registration_window, show="*", font=("Abadi", 12))
    password_entry.pack()

    full_name_label = tk.Label(registration_window, text="Full Name:", bg=bg_color, fg=fg_color, font=("Abadi", 12))
    full_name_label.pack()

    full_name_entry = tk.Entry(registration_window, font=("Abadi", 12))
    full_name_entry.pack()

    register_button = tk.Button(registration_window, text="Register", command=lambda: validate_registration(email_entry.get(), password_entry.get(), full_name_entry.get(), bg=bg_color, fg=fg_color, font=("Abadi", 12)))
    register_button.pack()

    center_window(registration_window, 400, 200)

    registration_window.mainloop()

login_window()
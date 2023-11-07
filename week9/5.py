import tkinter as tk


root = tk.Tk()
root.title("Login Form")

email_label = tk.Label(root, text="E-mail:")

password_label = tk.Label(root, text="Password:")

email_entry = tk.Entry(root)

password_entry = tk.Entry(root, show="*") 

login_button = tk.Button(root, text="Login")

create_account_button = tk.Button(root, text="Create new account")

email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
create_account_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

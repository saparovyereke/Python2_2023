import tkinter as tk


root = tk.Tk()
root.title("Login Form")

# Создание метки "E-mail"
email_label = tk.Label(root, text="E-mail:")

# Создание метки "Password"
password_label = tk.Label(root, text="Password:")

# Создание поля для ввода E-mail
email_entry = tk.Entry(root)

# Создание поля для ввода пароля
password_entry = tk.Entry(root, show="*")  # Пароль будет отображаться как символы "*"

# Создание кнопки "Login"
login_button = tk.Button(root, text="Login")

# Создание кнопки "Create new account"
create_account_button = tk.Button(root, text="Create new account")

# Размещение элементов на форме с использованием геометрического менеджера grid
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
create_account_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Запуск главного цикла
root.mainloop()
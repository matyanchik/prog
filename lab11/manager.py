import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер паролей")

        self.passwords = {}

        # Оформление интерфейса
        self.label = tk.Label(root, text="Введите сайт и пароль:")
        self.label.pack(pady=10)

        self.site_label = tk.Label(root, text="Сайт:")
        self.site_label.pack(pady=5)
        self.site_entry = tk.Entry(root, width=50)
        self.site_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Пароль:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, width=50)
        self.password_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Добавить пароль", command=self.add_password)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=5)

        # Кнопка для показа пароля
        self.show_button = tk.Button(root, text="Показать пароль", command=self.show_password)
        self.show_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Удалить пароль", command=self.delete_password)
        self.delete_button.pack(pady=5)

        # Привязываем двойной клик к методу show_password
        self.listbox.bind("<Double-Button-1>", self.show_password)

    def add_password(self):
        website = self.site_entry.get()
        password = self.password_entry.get()

        if website and password:
            self.passwords[website] = password
            self.update_listbox()
            self.site_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Добавить пароль", "Пожалуйста, заполните оба поля.")

    def delete_password(self):
        selected_website = self.listbox.get(tk.ACTIVE)
        if selected_website:
            del self.passwords[selected_website]
            self.update_listbox()
        else:
            messagebox.showwarning("Удалить пароль", "Сначала выберите пароль для удаления.")

    def show_password(self, event=None):
        selected_website = self.listbox.get(tk.ACTIVE)
        if selected_website:
            password = self.passwords[selected_website]
            messagebox.showinfo("Пароль", f"Пароль для {selected_website}: {password}")
        else:
            messagebox.showwarning("Показать пароль", "Сначала выберите веб-сайт.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for website in self.passwords.keys():
            self.listbox.insert(tk.END, website)

if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()
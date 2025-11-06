import tkinter as tk
from tkinter import messagebox
import pyperclip

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
        return

    is_ok = messagebox.askokcancel(
        title="Confirm Save",
        message=f"Save this entry?\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}"
    )

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("🔐 Password Manager")
window.config(padx=40, pady=40, bg="#f7f7f7")

# Title
title_label = tk.Label(text="🔐 Password Manager", font=("Arial", 20, "bold"), bg="#f7f7f7", fg="#333")
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Labels
tk.Label(text="Website:", font=("Arial", 12), bg="#f7f7f7").grid(row=1, column=0, sticky="e", pady=5)
tk.Label(text="Email/Username:", font=("Arial", 12), bg="#f7f7f7").grid(row=2, column=0, sticky="e", pady=5)
tk.Label(text="Password:", font=("Arial", 12), bg="#f7f7f7").grid(row=3, column=0, sticky="e", pady=5)

# Entries
website_entry = tk.Entry(width=35, font=("Arial", 12))
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = tk.Entry(width=35, font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "your@email.com")

password_entry = tk.Entry(width=21, font=("Arial", 12))
password_entry.grid(row=3, column=1, pady=5)

# Buttons
generate_button = tk.Button(text="Generate", width=10, font=("Arial", 10), command=lambda: pyperclip.copy("12345678"))
generate_button.grid(row=3, column=2, pady=5)

add_button = tk.Button(text="Add", width=36, font=("Arial", 12), bg="#4CAF50", fg="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=20)

window.mainloop()
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        password_length = int(entry_password_length.get())
    except ValueError:
        messagebox.showwarning("Warning", "Password length must be a number")
        return
    
    if password_length < 8:
        messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    entry_generated_password.delete(0, tk.END)
    entry_generated_password.insert(tk.END, generated_password)

def accept_password():
    password = entry_generated_password.get()
    if not password:
        messagebox.showwarning("Warning", "Please generate a password.")
        return

    messagebox.showinfo("Accepted", f"Your Password: {password}")

def reset_fields():
    entry_password_length.delete(0, tk.END)
    entry_generated_password.delete(0, tk.END)

def main():
    global entry_password_length, entry_generated_password
    root = tk.Tk()
    root.title("Nikhil's Password Generator")
    root.geometry("400x300")
    root.configure(bg="#f5f5f5")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    heading_label = tk.Label(root, text="Nikhil's Password Generator", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
    heading_label.grid(row=0, column=0, columnspan=3, pady=20)

    label_password_length = tk.Label(root, text="Enter Password Length:", bg="#f5f5f5")
    label_password_length.grid(row=1, column=0, sticky=tk.E)
    entry_password_length = tk.Entry(root, width=10)
    entry_password_length.grid(row=1, column=1, columnspan=2, sticky=tk.W)

    label_generated_password = tk.Label(root, text="Generated Password:", bg="#f5f5f5")
    label_generated_password.grid(row=2, column=0, sticky=tk.E)
    entry_generated_password = tk.Entry(root, width=30)
    entry_generated_password.grid(row=2, column=1, columnspan=2, sticky=tk.W)

    button_generate_password = tk.Button(root, text="Generate Password", command=generate_password, bg="#4caf50", fg="white")
    button_generate_password.grid(row=3, column=0, padx=5, pady=10)

    button_accept_password = tk.Button(root, text="Accept", command=accept_password, bg="#2196f3", fg="white")
    button_accept_password.grid(row=3, column=1, padx=5, pady=10)

    button_reset_fields = tk.Button(root, text="Reset", command=reset_fields, bg="#f44336", fg="white")
    button_reset_fields.grid(row=3, column=2, padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

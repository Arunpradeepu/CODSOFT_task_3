import string
import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

def generate(n):
    pw = []
    total = string.ascii_letters + string.digits + string.punctuation
    for _ in range(n):
        pw.append(random.choice(total))
    return ''.join(pw)

def call():
    try:
        n = int(length_entry.get())
        if n <= 0:
            messagebox.showerror("Error", "Enter a positive and non-zero number")
        else:
            password = generate(n)
            result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

frame = tk.Frame(root)
frame.pack(pady=20)

length_label = tk.Label(frame, text="Enter the length of the password:", font=("san-serif", 12))
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(frame, width=10, font=("san-serif", 12))
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(frame, text="Generate Password", width=20, font=("san-serif", 12), command=call)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("san-serif", 12))
result_label.pack(pady=20)

if __name__ == "__main__":
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def process_text():
    text = message_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Shift Value", "Please enter a valid integer for shift.")
        return

    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode)
    result_label.config(text=f"Result:\n{result}")

# Set up the main window
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x400")
root.config(bg="#1e1e1e")

# Title label
title_label = tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 16, "bold"), fg="#00e676", bg="#1e1e1e")
title_label.pack(pady=10)

# Message entry
tk.Label(root, text="Your Message:", font=("Arial", 10, "bold"), fg="#bb86fc", bg="#1e1e1e").pack()
message_entry = tk.Text(root, height=4, width=40, bg="#333", fg="#f5f5f5")
message_entry.pack(pady=5)

# Shift entry
tk.Label(root, text="Shift Value:", font=("Arial", 10, "bold"), fg="#bb86fc", bg="#1e1e1e").pack()
shift_entry = tk.Entry(root, bg="#333", fg="#f5f5f5", width=5)
shift_entry.pack(pady=5)

# Mode selection
mode_var = tk.StringVar(value="encrypt")
tk.Label(root, text="Choose Mode:", font=("Arial", 10, "bold"), fg="#bb86fc", bg="#1e1e1e").pack()
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt", bg="#1e1e1e", fg="#f5f5f5", selectcolor="#333").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt", bg="#1e1e1e", fg="#f5f5f5", selectcolor="#333").pack()

# Submit button
submit_button = tk.Button(root, text="Run Cipher", command=process_text, bg="#00e676", fg="#121212", font=("Arial", 10, "bold"))
submit_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="#00e676", bg="#1e1e1e")
result_label.pack(pady=10)

root.mainloop()

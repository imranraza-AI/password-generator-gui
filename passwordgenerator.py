import tkinter as tk
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = []
    password = []

    if use_upper:
        characters.extend(string.ascii_uppercase)
        password.append(random.choice(string.ascii_uppercase))

    if use_lower:
        characters.extend(string.ascii_lowercase)
        password.append(random.choice(string.ascii_lowercase))

    if use_digits:
        characters.extend(string.digits)
        password.append(random.choice(string.digits))

    if use_symbols:
        characters.extend(string.punctuation)
        password.append(random.choice(string.punctuation))

    if not characters:
        return "Select at least one option"

    remaining = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining))

    random.shuffle(password)
    return "".join(password)


def on_generate():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number")
        return

    if length < 4:
        result_label.config(text="Length must be at least 4")
        return

    password = generate_password(
        length,
        upper_var.get(),
        lower_var.get(),
        digit_var.get(),
        symbol_var.get()
    )

    result_label.config(text=password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var).pack()
tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var).pack()
tk.Checkbutton(root, text="Numbers", variable=digit_var).pack()
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", command=on_generate).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

root.mainloop()

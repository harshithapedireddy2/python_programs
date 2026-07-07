import tkinter as tk

def show_name():
    name = entry.get()                 # Read entered name
    label.config(text="Entered Name: " + name)   # Display in label
    entry.delete(0, tk.END)           # Clear entry field
    entry.insert(0, "Enter your name") # Placeholder text again

root = tk.Tk()

root.title("Name Entry")
root.geometry("400x300")

entry = tk.Entry(root, width=30)
entry.insert(0, "Enter your name")    # Placeholder-style text
entry.pack(pady=20)

button = tk.Button(root, text="Submit", command=show_name)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop()
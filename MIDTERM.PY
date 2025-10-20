import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x300")  # width x height

# Create a label
label = tk.Label(root, text="Hellnooo, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Create an entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a function for the button
def on_click():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

# Create a button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()

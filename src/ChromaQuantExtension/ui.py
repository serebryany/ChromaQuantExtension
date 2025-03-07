import tkinter as tk
from tkinter import filedialog

def upload_file(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        entry_widget.config(state='normal')
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)
        entry_widget.config(state='readonly')

# Create the main application window
root = tk.Tk()
root.title("Upload Product Composition Sheets")
root.geometry("400x200")

# Label and upload button for manually calculated file
tk.Label(root, text="Manually Calculated Product Composition:").pack(pady=5)
manual_entry = tk.Entry(root, width=50, state='readonly')
manual_entry.pack()
tk.Button(root, text="Browse", command=lambda: upload_file(manual_entry)).pack()

# Label and upload button for software calculated file
tk.Label(root, text="ChromaQuant Calculated Product Composition:").pack(pady=5)
software_entry = tk.Entry(root, width=50, state='readonly')
software_entry.pack()
tk.Button(root, text="Browse", command=lambda: upload_file(software_entry)).pack()

# Run the UI
root.mainloop()

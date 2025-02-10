import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_location():
    folder_selected = filedialog.askdirectory()
    location_entry.delete(0, tk.END)
    location_entry.insert(0, folder_selected)

def create_folders():
    location = location_entry.get().strip()
    folder_names = names_entry.get().strip()
    
    if not location:
        messagebox.showerror("Error", "Please select a location.")
        return
    if not folder_names:
        messagebox.showerror("Error", "Please enter folder names.")
        return
    
    folder_list = [name.strip() for name in folder_names.split(",") if name.strip()]
    
    for folder in folder_list:
        folder_path = os.path.join(location, folder)
        try:
            os.makedirs(folder_path, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create {folder}: {e}")
            return
    
    messagebox.showinfo("Success", "Folders created successfully!")

# GUI Setup
root = tk.Tk()
root.title("Create Multiple Folders")
root.geometry("500x250")

tk.Label(root, text="Select Location:").pack(pady=5)
location_entry = tk.Entry(root, width=50)
location_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_location).pack(pady=5)

tk.Label(root, text="Enter Folder Names (comma separated):").pack(pady=5)
names_entry = tk.Entry(root, width=50)
names_entry.pack(pady=5)

tk.Button(root, text="Create Folders", command=create_folders).pack(pady=20)

root.mainloop()

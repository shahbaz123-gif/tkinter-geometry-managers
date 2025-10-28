import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        birth_date = datetime(year, month, day)
        today = datetime.now()
        
        age = today.year - birth_date.year
        
        # Check if birthday has occurred this year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        
        result_label.config(text=f"Your age is: {age} years")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date!")

# Create main window
root = tk.Tk()
root.title("Simple Age Calculator")
root.geometry("300x200")

# Widgets
tk.Label(root, text="Enter Your Birth Date", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Day:").grid(row=0, column=0, padx=5)
day_entry = tk.Entry(frame, width=5)
day_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Month:").grid(row=0, column=2, padx=5)
month_entry = tk.Entry(frame, width=5)
month_entry.grid(row=0, column=3, padx=5)

tk.Label(frame, text="Year:").grid(row=0, column=4, padx=5)
year_entry = tk.Entry(frame, width=8)
year_entry.grid(row=0, column=5, padx=5)

tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
result_label.pack(pady=10)

root.mainloop()
# Creating Time Clock
import tkinter as tk
import time


# function update the time

def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # p=> am/pm   # time format
    clock_label.config(text=current_time)

    clock_label.after(1000, update_time)


# creating window

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)

# configuration of clock

clock_label = tk.Label(root, font=("Arial", 48), bg="black", fg="white")
clock_label.pack(expand=True)

update_time()
root.mainloop()

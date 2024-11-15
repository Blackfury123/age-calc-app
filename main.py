import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        birth_day = int(birth_day_entry.get())
        birth_month = int(birth_month_entry.get())
        birth_year = int(birth_year_entry.get())
        
        today = datetime.today()
        birth_date = datetime(birth_year, birth_month, birth_day)
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_label.config(text=f"Age: {age}")
    except ValueError:
        age_label.config(text="Please enter valid day, month, and year.")

window = tk.Tk()
window.title('Age Calculator')

tk.Label(window, text='Enter Birth Day (DD):').pack()
birth_day_entry = tk.Entry(window)
birth_day_entry.pack()

tk.Label(window, text='Enter Birth Month (MM):').pack()
birth_month_entry = tk.Entry(window)
birth_month_entry.pack()

tk.Label(window, text='Enter Birth Year (YYYY):').pack()
birth_year_entry = tk.Entry(window)
birth_year_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()

calculate_button = tk.Button(window, text='Calculate', command=calculate_age)
calculate_button.pack()

window.mainloop()

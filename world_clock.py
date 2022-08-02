from tkinter import *
from datetime import datetime
import pytz

# Prepare the GUI
root = Tk()
root.title("World Clock")
root.geometry("600x400")
root.config(bg="black")

# Lists to better assort values
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
locations = ["Berlin, Germany", "Chennai, India", "London, United Kingdom", "New York City, USA", "Tokyo, Japan", "Los Angeles, USA"]
time_zones = ['Europe/Berlin', 'Asia/Kolkata', 'Europe/London', 'America/New_York', 'Asia/Tokyo','America/Los_Angeles']

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def buttons(location_num):
    clear_frame()
    root.geometry("400x200")  # change window size for appropriate fit
    t = locations[location_num]  # set location
    buttons.tz = pytz.timezone(time_zones[location_num])  # set timezone

    # Prepare the labels
    text = Label(root, text=t, font=("Arial", 15), relief='groove', padx=10, pady=7.5, 
                    borderwidth=3, bg="black", fg="white")
    text.place(relx=0.5, y=20, anchor=CENTER)

    buttons.time_label = Label(root, font=("Arial", 40), bg="black", fg="white")
    buttons.time_label.pack(expand=True)

    buttons.date_label = Label(root, font=("Arial", 11), bg="black", fg="white")
    buttons.date_label.place(relx=0.5, y=175, anchor=CENTER)

    update()

def update():
    time = datetime.now(buttons.tz).strftime("%H:%M:%S")
    day = days[datetime.today().weekday()]
    date = datetime.now(buttons.tz).strftime(f"{day}, %d.%m.%Y") 

    buttons.time_label.config(text=time)
    buttons.date_label.config(text=date)
    root.after(1000, update)  # update every second


# Import the photos necessary for the (custom) buttons
berlin_photo = PhotoImage(file='button_files\\berlin.png')
chennai_photo = PhotoImage(file='button_files\\chennai.png')
london_photo = PhotoImage(file='button_files\\london.png')
new_york_photo = PhotoImage(file='button_files\\new_york.png')
tokyo_photo = PhotoImage(file='button_files\\tokyo.png')
la_photo = PhotoImage(file='button_files\\la.png')

# Make the title
title = Label(root, text="World Clock", font=("Papyrus", 25, 'bold'), relief='groove', 
                padx=10, pady=7.5, borderwidth=3, bg="black", fg="white")
title.place(relx=0.5, rely=0.125, anchor=CENTER)

# Make the buttons
berlin = Button(root, image= berlin_photo, command=lambda: buttons(0))
berlin.place(relx=0.225, rely=0.35, anchor=CENTER)

chennai = Button(root, image= chennai_photo, command=lambda: buttons(1))
chennai.place(relx=0.775, rely=0.35, anchor=CENTER)

london = Button(root, image= london_photo, command=lambda: buttons(2))
london.place(relx=0.225, rely=0.6, anchor=CENTER)

new_york = Button(root, image= new_york_photo, command=lambda: buttons(3))
new_york.place(relx=0.775, rely=0.6, anchor=CENTER)

tokyo = Button(root, image= tokyo_photo, command=lambda: buttons(4))
tokyo.place(relx=0.225, rely=0.85, anchor=CENTER)

la = Button(root, image= la_photo, command=lambda: buttons(5))
la.place(relx=0.775, rely=0.85, anchor=CENTER)

root.mainloop()

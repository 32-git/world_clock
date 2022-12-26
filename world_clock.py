import tkinter as tk
from customtkinter import *
from PIL import Image
from datetime import datetime
import pytz

# ------------ Preparation ------------
# Create the window
root = CTk()
root.iconbitmap("img\\icon.ico")  # custom defined icon
root.title("World Clock")
root.geometry("625x400")
# root.configure(bg=("grey90", "#19191a"))
set_default_color_theme("theme.json")
set_appearance_mode("dark")

# Lists to better assort values
locations = ["Berlin, Germany", "Chennai, India", "London, UK", "New York, USA", "Tokyo, Japan", "Los Angeles, USA"]
timezones = ['Europe/Berlin', 'Asia/Kolkata', 'Europe/London', 'America/New_York', 'Asia/Tokyo', 'America/Los_Angeles']

# Import the photos necessary for the buttons / switch
images = [
    CTkImage(dark_image=Image.open('img\\germany.png'), size=(22.5,15)), 
    CTkImage(dark_image=Image.open('img\\india.png'), size=(22.5,15)), 
    CTkImage(dark_image=Image.open('img\\uk.png'), size=(22.5,15)), 
    CTkImage(dark_image=Image.open('img\\usa.png'), size=(22.5,15)), 
    CTkImage(dark_image=Image.open('img\\japan.png'), size=(22.5,15)), 
    CTkImage(dark_image=Image.open('img\\usa.png'), size=(22.5,15))
]
img = CTkImage(dark_image=Image.open('img\\theme.png'), size=(27.5,27.5))
switch_var = StringVar(value="on")
# -----------------------------------------------------

def menu():
    # Make the title
    title = CTkLabel(root, text="World Clock", font=("Audiowide", 35), padx=10, pady=7.5, corner_radius=0,
                            text_color=('#008080','#017878'))
    title.place(relx=0.5, rely=0.125, anchor='center')

    # Switch for light/dark mode
    icon = CTkLabel(root, text=None)
    icon.place(relx=0.84, rely=0.082)
    img_button = CTkButton(root, image=img, fg_color="transparent", bg_color="transparent", 
                            hover=None, text=None, border_width=0).place(relx=0.83, rely=0.075)
    theme_switch = CTkSwitch(root, height=25, width=45, command=set_mode, text=None, variable=switch_var, 
                                onvalue="on", offvalue="off")
    theme_switch.place(relx= 0.84, rely= 0.095)
    
    # Make the buttons
    for i in range(6):
        button = CTkButton(root, image=images[i], text=locations[i], 
                                command=lambda i=i: display_time(i))
        buttons.append(button)
    
    # Place all the buttons
    buttons[0].place(relx=0.23, rely=0.35, anchor='center') # Berlin, Germany
    buttons[1].place(relx=0.77, rely=0.35, anchor='center') # Chennai, India
    buttons[2].place(relx=0.23, rely=0.6, anchor='center') # London, UK
    buttons[3].place(relx=0.77, rely=0.6, anchor='center') # New York, USA
    buttons[4].place(relx=0.23, rely=0.85, anchor='center') # Tokyo, Japan
    buttons[5].place(relx=0.77, rely=0.85, anchor='center') # Los Angeles, USA

def set_mode():
    # switch between light/dark mode
    if switch_var.get() == 'on':
        set_appearance_mode("dark")
    else:
        set_appearance_mode("light")

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def display_time(num):
    clear_frame()
    root.geometry("400x200")  # change window size for appropriate fit
    location = locations[num]  # set location
    display_time.tz = pytz.timezone(timezones[num])  # set timezone

    # Prepare the labels
    text = CTkLabel(root, text=location, font=("Arial", 16), padx=10, pady=7.5)
    text.place(relx=0.5, y=20, anchor='center')

    display_time.time_label = CTkLabel(root, font=("Arial", 42))
    display_time.time_label.place(relx=0.5, rely=0.5, anchor='center')
    display_time.date_label = CTkLabel(root, font=("Arial", 12))
    display_time.date_label.place(relx=0.5, y=175, anchor='center')

    update()

def update():
    time = datetime.now(display_time.tz).strftime("%H:%M:%S")
    date = datetime.now(display_time.tz).strftime(f"%A, %d.%m.%Y") 

    display_time.time_label.configure(text=time)
    display_time.date_label.configure(text=date)
    root.after(1000, update)  # update every second

# ---------- Run it ----------
buttons = []
menu()

root.mainloop()
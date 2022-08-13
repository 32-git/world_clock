import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import pytz

# Prepare the GUI
root = ctk.CTk()
root.iconbitmap("img\\icon.ico")  # custom defined icon
root.title("World Clock")
root.geometry("600x400")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("theme.json")

# Lists to better assort values
locations = ["Berlin, Germany", "Chennai, India", "London, United Kingdom", "New York City, USA", "Tokyo, Japan", "Los Angeles, USA"]
timezones = ['Europe/Berlin', 'Asia/Kolkata', 'Europe/London', 'America/New_York', 'Asia/Tokyo','America/Los_Angeles']

switch_var = ctk.StringVar(value="on")
def set_mode():
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def buttons(location_num):
    clear_frame()
    root.geometry("400x200")  # change window size for appropriate fit
    t = locations[location_num]  # set location
    buttons.tz = pytz.timezone(timezones[location_num])  # set timezone

    # Prepare the labels
    text = ctk.CTkLabel(root, text=t, text_font=("Arial", 16), padx=10, pady=7.5, 
                    borderwidth=3)
    text.place(relx=0.5, y=20, anchor='center')

    buttons.time_label = ctk.CTkLabel(root, text_font=("Arial", 42))
    buttons.time_label.place(relx=0.5, rely=0.5, anchor='center')
    buttons.date_label = ctk.CTkLabel(root, text_font=("Arial", 12))
    buttons.date_label.place(relx=0.5, y=175, anchor='center')

    update()

def update():
    time = datetime.now(buttons.tz).strftime("%H:%M:%S")
    date = datetime.now(buttons.tz).strftime(f"%A, %d.%m.%Y") 

    buttons.time_label.configure(text=time)
    buttons.date_label.configure(text=date)
    root.after(1000, update)  # update every second


# Make the title
title = ctk.CTkLabel(root, text="World Clock", text_font=("Audiowide", 25), padx=10, pady=7.5, 
                        borderwidth=1.5, text_color='cyan4')
title.place(relx=0.5, rely=0.125, anchor='center')

# Switch for light/dark mode
img=tk.PhotoImage(file='img\\theme.png')
icon = ctk.CTkLabel(root, image=img)
icon.place(relx=0.84, rely=0.0875)
theme_switch = ctk.CTkSwitch(root, height=25, width=45, command=set_mode, fg_color='grey57',
                                text=None, variable=switch_var, onvalue="on", offvalue="off")
theme_switch.place(relx= 0.84, rely= 0.095)


# Import the photos necessary for the (custom) buttons
germany = tk.PhotoImage(file='img\\germany.png')
india = tk.PhotoImage(file='img\\india.png')
uk = tk.PhotoImage(file='img\\uk.png')
usa = tk.PhotoImage(file='img\\usa.png')
japan = tk.PhotoImage(file='img\\japan.png')

# Make the buttons
berlin = ctk.CTkButton(root, image=germany, text=locations[0], command=lambda: buttons(0), 
                        text_color='SkyBlue4')
berlin.place(relx=0.23, rely=0.35, anchor='center')

chennai = ctk.CTkButton(root, image=india, text=locations[1], command=lambda: buttons(1), 
                        text_color='SkyBlue4')
chennai.place(relx=0.77, rely=0.35, anchor='center')

london = ctk.CTkButton(root, image=uk, text="London, UK", command=lambda: buttons(2), 
                        text_color='SkyBlue4')
london.place(relx=0.23, rely=0.6, anchor='center')

new_york = ctk.CTkButton(root, image=usa, text="New York, USA", command=lambda: buttons(3), 
                        text_color='SkyBlue4')
new_york.place(relx=0.77, rely=0.6, anchor='center')

tokyo = ctk.CTkButton(root, image=japan, text=locations[4], command=lambda: buttons(4), 
                        text_color='SkyBlue4')
tokyo.place(relx=0.23, rely=0.85, anchor='center')

la = ctk.CTkButton(root, image=usa, text=locations[5], command=lambda: buttons(5), 
                        text_color='SkyBlue4')
la.place(relx=0.77, rely=0.85, anchor='center')

root.mainloop()
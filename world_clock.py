import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import pytz

# Prepare the GUI
root = ctk.CTk()
root.title("World Clock")
root.geometry("600x400")
root.config(bg="white")

# Lists to better assort values
locations = ["Berlin, Germany", "Chennai, India", "London, United Kingdom", "New York City, USA", "Tokyo, Japan", "Los Angeles, USA"]
timezones = ['Europe/Berlin', 'Asia/Kolkata', 'Europe/London', 'America/New_York', 'Asia/Tokyo','America/Los_Angeles']

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def buttons(location_num):
    clear_frame()
    root.geometry("400x200")  # change window size for appropriate fit
    t = locations[location_num]  # set location
    buttons.tz = pytz.timezone(timezones[location_num])  # set timezone

    # Prepare the labels
    text = ctk.CTkLabel(root, text=t, text_font=("Arial", 15), padx=10, pady=7.5, 
                    borderwidth=3, bg="white", fg="black")
    text.place(relx=0.5, y=20, anchor='center')

    buttons.time_label = tk.Label(root, font=("Arial", 40), bg="white", fg="black")
    buttons.time_label.place(relx=0.5, rely=0.5, anchor='center')

    buttons.date_label = tk.Label(root, font=("Arial", 11), bg="white", fg="black")
    buttons.date_label.place(relx=0.5, y=175, anchor='center')

    update()

def update():
    time = datetime.now(buttons.tz).strftime("%H:%M:%S")
    date = datetime.now(buttons.tz).strftime(f"%A, %d.%m.%Y") 

    buttons.time_label.config(text=time)
    buttons.date_label.config(text=date)
    root.after(1000, update)  # update every second


# Import the photos necessary for the (custom) buttons
germany = tk.PhotoImage(file='button_files\\germany.png')
india = tk.PhotoImage(file='button_files\\india.png')
uk = tk.PhotoImage(file='button_files\\uk.png')
usa = tk.PhotoImage(file='button_files\\usa.png')
japan = tk.PhotoImage(file='button_files\\japan.png')

# Make the title
title = ctk.CTkLabel(root, text="World Clock", text_font=("Audiowide", 25), padx=10, pady=7.5, 
                        borderwidth=1.5, text_color='cyan4')
title.place(relx=0.5, rely=0.125, anchor='center')


# Make the buttons
berlin = ctk.CTkButton(root, corner_radius=10, image=germany, text="Berlin, Germany", text_font=("Audiowide", 15), 
                        command=lambda: buttons(0), border_width=2, fg_color='LightCyan2', border_color= 'CadetBlue4', 
                        text_color='SkyBlue4',  hover_color='LightSkyBlue2')
berlin.place(relx=0.23, rely=0.35, anchor='center')

chennai = ctk.CTkButton(root, corner_radius=10, image=india, text="Chennai, India", text_font=("Audiowide", 15), 
                        command=lambda: buttons(1), border_width=2, fg_color='LightCyan2', border_color= 'CadetBlue4', 
                        text_color='SkyBlue4',  hover_color='LightSkyBlue1')
chennai.place(relx=0.77, rely=0.35, anchor='center')

london = ctk.CTkButton(root, corner_radius=10, image=uk, text="London, UK", text_font=("Audiowide", 15), 
                        command=lambda: buttons(2), border_width=2, fg_color='LightCyan2', border_color= 'CadetBlue4', 
                        text_color='SkyBlue4',  hover_color='LightSkyBlue1')
london.place(relx=0.23, rely=0.6, anchor='center')

new_york = ctk.CTkButton(root, corner_radius=10, image=usa, text="New York, USA", text_font=("Audiowide", 15), 
                        command=lambda: buttons(3), border_width=2, fg_color='LightCyan2', border_color= 'CadetBlue4', 
                        text_color='SkyBlue4',  hover_color='LightSkyBlue1')
new_york.place(relx=0.77, rely=0.6, anchor='center')

tokyo = ctk.CTkButton(root, corner_radius=10, image=japan, text="Tokyo, Japan", text_font=("Audiowide", 15), 
                        command=lambda: buttons(4), border_width=2, fg_color='LightCyan2', border_color= 'CadetBlue4', 
                        text_color='SkyBlue4',  hover_color='LightSkyBlue1')
tokyo.place(relx=0.23, rely=0.85, anchor='center')

la = ctk.CTkButton(root, corner_radius=10, image=usa, text="Los Angeles, USA", text_font=("Audiowide", 15), 
                        command=lambda: buttons(5), border_width=2, fg_color='LightCyan2', border_color= 'CadetBlue4', 
                        text_color='SkyBlue4',  hover_color='LightSkyBlue1')
la.place(relx=0.77, rely=0.85, anchor='center')

root.mainloop()

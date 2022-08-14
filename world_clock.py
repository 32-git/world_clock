import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import pytz

# ------------ Preparation ------------
# Create the window
root = ctk.CTk()
root.iconbitmap("img\\icon.ico")  # custom defined icon
root.title("World Clock")
root.geometry("600x400")
root.configure(bg=("#ebf0f5", "#19191a"))
ctk.set_default_color_theme("theme.json")
ctk.set_appearance_mode("dark")

# Lists to better assort values
locations = ["Berlin, Germany", "Chennai, India", "London, UK", "New York, USA", "Tokyo, Japan", "Los Angeles, USA"]
timezones = ['Europe/Berlin', 'Asia/Kolkata', 'Europe/London', 'America/New_York', 'Asia/Tokyo','America/Los_Angeles']

# Import the photos necessary for the buttons / switch
images = [tk.PhotoImage(file='img\\germany.png'), tk.PhotoImage(file='img\\india.png'), 
            tk.PhotoImage(file='img\\uk.png'), tk.PhotoImage(file='img\\usa.png'), 
            tk.PhotoImage(file='img\\japan.png')]

img = tk.PhotoImage(file='img\\theme.png')
switch_var = ctk.StringVar(value="on")
# -----------------------------------------------------

def world_clock():
    def menu():
        # Make the title
        title = ctk.CTkLabel(root, text="World Clock", text_font=("Audiowide", 25), padx=10, pady=7.5, 
                                borderwidth=1.5, text_color=('#008080','#017878'))
        title.place(relx=0.5, rely=0.125, anchor='center')

        # Switch for light/dark mode
        icon = ctk.CTkLabel(root, image=img)
        icon.place(relx=0.84, rely=0.082)
        theme_switch = ctk.CTkSwitch(root, height=25, width=45, command=set_mode, text=None, 
                                        variable=switch_var, onvalue="on", offvalue="off")
        theme_switch.place(relx= 0.84, rely= 0.095)#
        
        # Make the buttons
        for i in range(6):
            if i == 5:
                button = ctk.CTkButton(root, image=images[3], text=locations[i], command=lambda: display_time(i), 
                            text_color=('#277575', '#369191'))
            else:
                button = ctk.CTkButton(root, image=images[i], text=locations[i], command=lambda: display_time(i), 
                            text_color=('#277575', '#369191'))
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
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def clear_frame():
        for widget in root.winfo_children():
            widget.destroy()

    def display_time(num):
        clear_frame()
        root.geometry("400x200")  # change window size for appropriate fit
        location = locations[num]  # set location
        display_time.tz = pytz.timezone(timezones[num])  # set timezone

        # Prepare the labels
        text = ctk.CTkLabel(root, text=location, text_font=("Arial", 16), padx=10, pady=7.5, 
                        borderwidth=3)
        text.place(relx=0.5, y=20, anchor='center')

        display_time.time_label = ctk.CTkLabel(root, text_font=("Arial", 42))
        display_time.time_label.place(relx=0.5, rely=0.5, anchor='center')
        display_time.date_label = ctk.CTkLabel(root, text_font=("Arial", 12))
        display_time.date_label.place(relx=0.5, y=175, anchor='center')

        update()

    def update():
        time = datetime.now(display_time.tz).strftime("%H:%M:%S")
        date = datetime.now(display_time.tz).strftime(f"%A, %d.%m.%Y") 

        display_time.time_label.configure(text=time)
        display_time.date_label.configure(text=date)
        root.after(1000, update)  # update every second
    
    menu()

# ---------- Run it ----------
buttons = []
world_clock()

root.mainloop()
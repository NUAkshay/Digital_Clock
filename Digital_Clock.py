from tkinter import Label, Tk

import time

clock = Tk()

clock.title("Digital Clock")

clock.geometry("420x150")

clock.resizable(1, 1)

text_font= ("Times", "78", "bold italic")
background = "#f2e750"
foreground= "#363529"
border = 25

label = Label(clock, font = text_font, bg = background, fg = foreground, bd = border)

label.grid(row = 0, column = 1)

def digital_clock(): 
   live_time = time.strftime("%H:%M:%S")
   label.config(text = live_time)
   label.after(100, digital_clock)

digital_clock()

clock.mainloop()

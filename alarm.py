from tkinter import *
from win10toast import ToastNotifier
import datetime

root = Tk()
root.title("Snap Streaks")
root.iconbitmap(r'C:\Users\chadh\OneDrive\Documents\!Programming!\!Python!\Alarm/icon.ico')

e = Entry(root, width=150, borderwidth=0)
e.grid(row=1, column=0, columnspan=3, padx=50, pady=30)
e.insert(0, "Enter the hour here: ")

e2 = Entry(root, width=150, borderwidth=0)
e2.grid(row=2, column=0, columnspan=3, padx=50, pady=0)
e2.insert(1, "Enter the minute here: ")

e3 = Entry(root, width=150, borderwidth=0)
e3.grid(row=3, column=0, columnspan=3, padx=50, pady=30)
e3.insert(2, "Enter the a.m. or p.m. here: ")


def time():
    hour = e.get()
    minute = e2.get()
    ampm = e3.get()


    while True:
        
        if ampm == "am":
            if int(hour) == int(datetime.datetime.now().hour) and int(minute) == int(datetime.datetime.now().minute):
                toast = ToastNotifier()
                toast.show_toast("Snap Streaks","Time for your daily Snapchat streaks",duration=60,icon_path='icon.ico')
                break
        elif ampm == "pm":
            if int(hour) == int(datetime.datetime.now().hour) - 12 and int(minute) == int(datetime.datetime.now().minute):
                toast = ToastNotifier()
                toast.show_toast("Snap Streaks","Time for your daily Snapchat streaks",duration=60,icon_path='icon.ico')
                break

title = Label(root, text="Snap Streaks", font='Helvetica 25 bold')
title.grid(row=0, column=1)

button1 = Button(root, text="Confirm Alarm", command=time)
button1.grid(row=4, column=1)



#root.configure(bg="black")
root.geometry("1000x500")
root.mainloop()

from tkinter import Tk, Label
from datetime import datetime
window= Tk()
window.title("It's a Digital Clock")
window.geometry("600*300")
window.configure(bg="steelblue")

label= Label(window, font=("Arial Black",78,"bold"), bg="steelblue",fg="lightgreen")
label.pack(pady=100)

def clock():
    time= datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)

clock()
window.mainloop()
from cProfile import label
from tkinter import Tk, Label

window=Tk()
window.title("It's a Digital Clock")
window.geometry("600*300")
window.configure(bg="steelblue")

label= Label(window, font=("Arial Black",78,"bold"), bg="steelblue",fg="transparent")
label.pack(pady=100)
window.mainloop()
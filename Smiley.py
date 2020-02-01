import tkinter as tk
win=tk.Tk()
win.title("SMILEY")
canvas = tk.Canvas(win,bg="white",width=300,height=300)
canvas.pack()
canvas.create_oval((0,0,300,300),fill="yellow")

canvas.create_rectangle((80,90,120,130),fill="black")
canvas.create_rectangle((190,90,230,130),fill="black")
canvas.create_rectangle((100,200,200,220),fill="red")
win.mainloop()
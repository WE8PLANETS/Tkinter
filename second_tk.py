#thenewboston -name of youtube channel used to understand
from tkinter import *  #import tkinter library

root = Tk()    

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)   
bottomFrame.pack(side=BOTTOM)

#adding buttons  fg is used to define color
button1 = Button(topFrame, text="Button 1", fg="blue")
button2 = Button(topFrame, text="Button 2", fg="red")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="black")

button1.pack(side=LEFT)  #if you want to show them use pack
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop() #mainloop is used to put this in loop infinite loop
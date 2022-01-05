from tkinter import *

root = Tk()
root.title("Hello all")

myCanvas = Canvas(root,bg="grey",width=300,height=200)

def turn_red():
    myCanvas.delete("all")
    myCanvas.create_rectangle(10,10,20,20,fill="red")

def turn_blue():
    myCanvas.delete("all")
    myCanvas.create_rectangle(60,60,70,70,fill="blue")
    
myButton1 = Button(root, text="turn red",padx=10,pady=10,command=turn_red)
myButton2 = Button(root, text="turn blue",padx=10,pady=10,command=turn_blue)

myCanvas.pack()
myButton1.pack()
myButton2.pack()

myCanvas.create_rectangle(100,100,110,110,fill="blue")
mainloop()


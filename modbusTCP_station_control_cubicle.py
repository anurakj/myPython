from tkinter import *
from pyModbusTCP.client import ModbusClient
import threading
import time 

root = Tk()

root.title("Station control cubicle")

myCanvas = Canvas(root,bg="grey",width=300,height=200)

def connect_and_poll():
    c = ModbusClient()
    c.host("127.0.0.1")
    c.port(502)
    c.open()
    x = 150    # origin of x
    y = 50    # origin of y
    line_width = 2
    while (1) :
        bits = c.read_discrete_inputs(0,5) #read input register address 0 for 5 number
        myCanvas.create_rectangle(10,10,20,20,fill="green2")
        time.sleep(1)
        print("breaker status: "+ str(bits[0]))
        myCanvas.delete("all")
        myCanvas.create_line(x,y,x,y+50,width=line_width)
        myCanvas.create_line(x,y+70,x,y+120,width=line_width)
        myCanvas.create_line(x,y+50,x+10,y+50,width=line_width)
        if bits[0] == True:
            myCanvas.create_line(x,y+70,x+5,y+40,width=line_width)    # breaker closed
        else:
            myCanvas.create_line(x,y+70,x+30,y+50,width=line_width)    # breaker opened
            
        time.sleep(1)
        
def start_thread():
    threading.Thread(target=connect_and_poll).start()

connectButton = Button(root,text="connect",command=start_thread)

myCanvas.pack()

connectButton.pack()
   
root.mainloop()


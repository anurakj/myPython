from tkinter import *
from pyModbusTCP.client import ModbusClient
import threading
import time 

root = Tk()

root.title("Condition Monitoring System (CMS)")

myCanvas = Canvas(root,bg="grey",width=300,height=200)

def connect_and_poll():
    c = ModbusClient()
    c.host("127.0.0.1")
    c.port(502)
    c.open()
    while (1) :
        reg = c.read_holding_registers(0, 3) #read holding register address 0 for 3 number
        myCanvas.create_rectangle(10,10,20,20,fill="green2")
        time.sleep(1)
        print("current L1: "+ str(reg[0]) + "   L2: " + str(reg[1]) + "   L3: " + str(reg[2]) + "   Amp")
        myCanvas.delete("all")
        myCanvas.create_text(80,10,text="current(A)")
        myCanvas.create_text(40,50,text="L1")
        myCanvas.create_text(40,100,text="L2")
        myCanvas.create_text(40,150,text="L3")        
        myCanvas.create_rectangle(50,50,50+reg[0],60,fill="red")
        myCanvas.create_rectangle(50,100,50+reg[1],110,fill="yellow")
        myCanvas.create_rectangle(50,150,50+reg[2],160,fill="blue")        
        time.sleep(1)
        
def start_thread():
    threading.Thread(target=connect_and_poll).start()

connectButton = Button(root,text="connect",command=start_thread)

myCanvas.pack()

connectButton.pack()
   
root.mainloop()


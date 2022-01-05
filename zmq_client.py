import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
while True:
    sock.send_string("hello")
    mesg = sock.recv_string()
    print (mesg)
    time.sleep(3)

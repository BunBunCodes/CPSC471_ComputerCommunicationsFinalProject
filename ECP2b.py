# udppingserver_no_loss.py 
# first Mod
from socket import * 
import time
import random

# Create a UDP socket 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket 
serverSocket.bind(('', 12000)) 
while True: 
    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024) 
    
    delay = random.randint(10, 20) / 1000  # Convert ms to s
    time.sleep(delay)  # Sleep only accepts seconds
    
    # The server responds 
    serverSocket.sendto(message, address)
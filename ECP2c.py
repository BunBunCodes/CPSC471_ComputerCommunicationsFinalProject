# udppingserver_no_loss.py 
# second Mod
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
    
    specialVal = random.randint(1, 100)
    if (specialVal <= 10):  # 10%
        continue            # this skips the server response
    
    delay = random.randint(10, 20) / 1000  # Convert ms to s
    time.sleep(delay)  # Sleep only accepts seconds
    
    # The server responds 
    serverSocket.sendto(message, address)
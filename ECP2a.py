# from socket import * didnt work here
import socket
# needed for time
import time
# needed for date time in response message
from datetime import datetime


# Server details
serverAddress = ('localhost', 12000)  # Server IP and port
totalPings = 50                       # Total number of pings to send, change this num to 50 for ECP2c
bufferSize = 1024                     # Size of buffer for receiving messages

# Initialize statistics
rttVals = []
packetLossCt = 0

# My name used in pings
myName = "Edith" 

# Create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)  # Setting timeout to 1s

for pingNum in range(1, totalPings + 1):
    # format it
    # %a = abb. weekday name; %b = abb. month name 
    timeStamp = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    message = f"{myName} {pingNum} {timeStamp}"
    
    try:
        # Record the send time
        timeStart = time.time()
        
        # Send the message to the server
        clientSocket.sendto(message.encode(), serverAddress)
        
        # Wait for response from server
        # Recall to run udppingserver_no_loss.py first!
        # Or you'll get an error
        response, _ = clientSocket.recvfrom(bufferSize)
        
        # Record the end time and calculate RTT
        endTime = time.time()
        rtt = (endTime - timeStart) * 1000  # Converting RTT to milliseconds
        rttVals.append(rtt)
        
        # Print server's response and RTT
        print(f"{message}: server reply: {response.decode()}, RTT = {rtt:.2f} ms")
        
    except socket.timeout:
        # Handle case where the request timed out
        print(f"{myName} {pingNum}: timed out, message was lost")
        packetLossCt += 1

# MATH YAY
if rttVals:
    minVal = min(rttVals)
    maxVal = max(rttVals)
    avgVal = sum(rttVals) / len(rttVals)
else:
    minVal = maxVal = avgVal = 0.0

# equation taken from labs
packetLossRt = (packetLossCt / totalPings) * 100

# Check online for proper formatting of integers with decimals and percentages
# Ping Summary
print(f"Min RTT: {minVal:.2f} ms")
print(f"Max RTT: {maxVal:.2f} ms")
print(f"Avg RTT: {avgVal:.2f} ms")
print(f"Packet lost: {packetLossRt:.2f}%")

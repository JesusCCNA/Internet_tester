import socket
import serial
import time

# Check Internet connection
remote_server = "google.com"

def is_connected(hostname):
    try:
        # See if the hostname can be resolved
        host = socket.gethostbyname(hostname)

        # Connect to the host
        s = socket.create_connection((host,80),2)
        s.close()
        print("There is Internet connection")
        return True
    except:
        print("There is NO Internet connection")
    return False

# Communicate the Internet connection state to the arduino through serial COM
# port number should be the one that your arduino is using in your PC

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
def write(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(120)

while True:
    if is_connected(remote_server):
        value = write("1")
        print(value) # printing the value
    else:
        time.sleep(120)

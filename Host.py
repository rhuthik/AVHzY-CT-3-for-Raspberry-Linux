import telnetlib
import socket
import time

# Define the host and port for the Telnet session
TELNET_HOST = "127.0.0.1"
TELNET_PORT = 1000

# Define the Raspberry Pi's IP address and the port to connect to
RASPI_IP = "10.2.24.230"  # Replace with your Raspberry Pi's actual IP address
RASPI_PORT = 5000  # Ensure this port matches the one used in the Raspberry Pi's server script

# Create a Telnet session
tn = telnetlib.Telnet(TELNET_HOST, TELNET_PORT)

def connect_to_raspi():
    try:
        # Try to create a socket connection to the Raspberry Pi
        raspi_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raspi_sock.connect((RASPI_IP, RASPI_PORT))
        print("Connected to the Raspberry Pi server.")
        return raspi_sock
    except socket.error as e:
        print("Connection to Raspberry Pi failed: ", e)
        return None

raspi_sock = connect_to_raspi()

print("Waiting for data...")

# Read and forward data continuously
try:
    while True:
        data = tn.read_some()  # Read some data from the Telnet session
        if data:
            print("Forwarding:", data.decode('ascii'))
            if raspi_sock:
                try:
                    # Forward the received data to the Raspberry Pi
                    raspi_sock.sendall(data)
                except socket.error:
                    print("Lost connection to Raspberry Pi. Attempting to reconnect...")
                    raspi_sock = connect_to_raspi()
            else:
                # Attempt to reconnect if not connected
                raspi_sock = connect_to_raspi()
        else:
            # No data received, you might choose to wait before trying again
            time.sleep(1)
finally:
    # Close the Telnet session and the socket to the Raspberry Pi, if it's open
    tn.close()
    if raspi_sock:
        raspi_sock.close()

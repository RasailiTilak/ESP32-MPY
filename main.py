import machine
import time

# Configure UART1 with RX on GPIO 27 and TX on GPIO 16
uart1 = machine.UART(1, baudrate=9600, rx=27, tx=16)
print("UART configured with RX on GPIO 27 and TX on GPIO 16.")

# Function to send data
def send_data(data):
    uart1.write(data)
    print(f"Data sent: {data}")

# Example data to send
data_to_send = "Hello, RS-232!"

# Infinite loop to send data every second
while True:
    send_data(data_to_send + "\n")  # Adding newline character for better readability on the receiver side
    time.sleep(1)  # Wait for 1 second

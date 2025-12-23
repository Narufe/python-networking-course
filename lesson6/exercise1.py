from telnetlib import Telnet
import time

host = "device.domain.com"
username = "admin"

# Create telnet connection
tn = Telnet(host)

# Wait for the device to respond
time.sleep(1.5)
data = tn.read_very_eager()
print(data)

# def read(telnet_conn, sleep=1.5):

  
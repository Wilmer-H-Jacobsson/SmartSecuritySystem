import time
import ujson
import machine
import config
from machine import Pin
import ntptime

# Setup for sending a request to IFTTT
def http_post(values, url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(config.event_name, config.webhooks_key)):
    import socket                           # Used by HTML get request
    import time                              # Used for delay
    value1, value2 = values.split(' ', 1)   # values = current date and time
    url += '?value1={}'.format(value1)      # value1 = the date --- Passing on the date in the request to be stored in sheets-file
    url += '&value2={}'.format(value2)      # value2 = the time --- Passing on the time in the request to be stored in sheets-file
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialise the socket
    s.connect(addr)                         # Try connecting to host address
    # Send HTTP request to the host with specific path
    s.send(bytes('POST /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receve response
    s.close()                               # Close connection


 # pir Setup
pir = Pin(13 ,mode=Pin.IN) #can be changed to another D-pin if one should wish. Just change 13 to something else.


#if needed, overwrite default time server
ntptime.host = "1.europe.pool.ntp.org"

# A loop to keep checking to see if the motion sensor is triggered.
# If triggered it sends the request to IFTTT and prints in REPL that motion was detected
print("Starting Detection")
while True:
    if pir()==config.motionDetected:
        ntptime.settime()           #syncs the to (almost) local time
        t = time.localtime()
        http_post(values="{:04d}-{:02d}-{:02d} {:02d}.{:02d}.{:02d}".format(t[0], t[1], t[2], t[3] + 2, t[4], t[5])) # calls for the HTTP request function (I have added 2 hours to match my local time)
        print("Motion Detected! Time: {:04d}-{:02d}-{:02d} {:02d}.{:02d}.{:02d}".format(t[0], t[1], t[2], t[3] + 2, t[4], t[5])) # optional print out to the REPL

#if the motion sensor isn't triggered it will just pass
    if pir()==config.noMotionDetected:
        pass
# A short delay to stop the program from sending multiple requests after a single motion is detected
    time.sleep(config.hold_time_sec)

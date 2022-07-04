import network
import config

# Setting up a wifi connection
# code credit to: https://hackmd.io/@lnu-iot/r1aui0B59#Generic-ESP32
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(config.WIFI_SSID, config.WIFI_PASS)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

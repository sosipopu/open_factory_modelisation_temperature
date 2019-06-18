import machine
from network import WLAN
from ws2812 import WS2812
import time
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'congres':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'sufca!2019!dsiun'), timeout=500)
        while not wlan.isconnected():
            chain = WS2812(ledNumber=5)
            data = [
                (0, 0, 255),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                ]
            chain.show(data)
            time.sleep(0.1)
            chain = WS2812(ledNumber=5)
            data = [
                (0, 0, 0),    # Vert
                (0, 0, 255),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                ]
            chain.show(data)
            time.sleep(0.1)
            chain = WS2812(ledNumber=5)
            data = [
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 255),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                ]
            chain.show(data)
            time.sleep(0.1)
            chain = WS2812(ledNumber=5)
            data = [
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 255),    # Vert
                (0, 0, 0),    # Vert
                ]
            chain.show(data)
            time.sleep(0.1)
            chain = WS2812(ledNumber=5)
            data = [
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 0),    # Vert
                (0, 0, 255),    # Vert
                ]
            chain.show(data)
            time.sleep(0.1)
        print('WLAN connection succeeded!')
        break
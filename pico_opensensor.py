from machine import Pin
from time import sleep

led = Pin(pin=17)
sensor = Pin(pin=4)

while True:
    led.on() if not sensor.is_active else led.off()
    sleep(0.5)

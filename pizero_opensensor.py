from gpiozero import LED, DigitalInputDevice
from time import sleep

led = LED(pin=17)
sensor = DigitalInputDevice(pin=4)

while True:
    led.on() if not sensor.is_active else led.off()
    sleep(0.5)

from random import randint

import machine


class _TempHum:

    def __init__(self, pin: machine.Pin):
        pass

    def measure(self):
        pass


    def temperature(self):
        return randint(190, 310)/10


    def humidity(self):
        return randint(340, 640)/10


class DHT11(_TempHum):
    pass


class DHT22(_TempHum):
    pass
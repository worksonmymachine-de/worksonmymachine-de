import asyncio
import machine
import network
from time import sleep
import dht
from paho.mqtt import publish

# Used for WiFi access
ssid = 'myWifi'
password = 'myWifiPassword'

# Sensor and MQTT topics configuration
sensor_id = 'Pantry_TempHumSensor'
mqtt_server = '192.168.188.45'
topic_hum = f'data/raw/{sensor_id}/hum'
topic_temp = f'data/raw/{sensor_id}/temp'
measure_delay_sec = 30
sensor_pin = 17


class IoTSensorTempHum:

    def __init__(self):
        self.temp = None
        self.hum = None
        asyncio.run(self.run())

    async def run(self):
        await asyncio.gather(self.connect_to_wifi(), self.read_sensor())
        await self.publish()
        sleep(measure_delay_sec)

    @staticmethod
    async def connect_to_wifi():
        # connecting to WiFi
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(ssid, password)
        while not station.isconnected():
            sleep(0.3)

    async def read_sensor(self):
        # measuring temp and hum
        sensor = dht.DHT22(machine.Pin(sensor_pin))
        sensor.measure()
        self.temp = sensor.temperature()
        self.hum = sensor.humidity()

    async def publish(self):
        # sending values to MQTT server
        results = ((topic_hum, round(self.temp, 1) if self.hum is not None else 'Error'),
                   (topic_temp, round(self.temp, 1) if self.temp is not None else 'Error'))
        publish.multiple(results, hostname=mqtt_server, client_id=sensor_id)


if __name__ == '__main__':
    IoTSensorTempHum()

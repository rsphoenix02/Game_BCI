import queue
import serial

data_queue = queue.Queue()


def read_serial():

    arduino = serial.Serial('COM4', 115200, timeout=1)

    while True:
        data = arduino.readline()
        reading = int.from_bytes(data, 'little')
        data_queue.put(reading)

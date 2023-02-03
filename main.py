import pygatt
from datetime import datetime

from binascii import hexlify
import time
# The BGAPI backend will attempt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.



import virtualserialports
virtualserialports.run(2, loopback=True, debug=False)
adapter = pygatt.BGAPIBackend()


# stm '00:80:E1:21:C6:79'
"""
try:
    adapter.start()
    device = adapter.scan()
    for i in range (len(device)):
        print (device[i])
    #value = device.char_read("a1e8f5b1-696b-4e4c-87c6-69dfe0b0093b")
finally:
    adapter.stop()
"""
def oszt(x):
    global xre
    xre=x


oszt(0)
def handle_data(handle, value):
    """
    handle -- integer, characteristic read handle the data was received on
    value -- bytearray, the data returned in the notification
    """
   # print("XXXX Received data: %s" ,str(value))
   # print("jott")
    dt = datetime.now()

    x=xre
    oszt(x+1)
    ts = datetime.timestamp(dt)
    data=(value.decode()[0:6])
 #   data=data/100000
    if x>250:
        print(data)
        oszt(0)
    #print("x Timestamp is:"+ str(dt)+str(value.decode()[0:6]))
    return

def handle_data1(handle, value):
    """
    handle -- integer, characteristic read handle the data was received on
    value -- bytearray, the data returned in the notification
    """
    print("YYYY  Received data: %s" ,str(value))
   # print("jott")
    dt = datetime.now()

    ts = datetime.timestamp(dt)
   # print("y Timestamp is:", dt)
    return

def handle_data2(handle, value):
    """
    handle -- integer, characteristic read handle the data was received on
    value -- bytearray, the data returned in the notification
    """
    print("ZZZZ Received data: %s" ,str(value))
   # print("jott")
    dt = datetime.now()

    ts = datetime.timestamp(dt)
    print("Timestamp is:", dt)
    return
try:
    adapter.start()

    device = adapter.connect('00:80:E1:21:C6:79',interval_min=6,interval_max=600)
    value=-1
    #mtu = device.exchange_mtu(64)
    #print("MTU exchanged: {}".format(mtu))
    #value = device.char_read     ("00000003-0000-1000-8000-00805f9b34fb")
    #value = device.char_read_long("00000003-0000-1000-8000-00805f9b34fb")
    print ("Connected")
    print(value)

    value = device.char_read_long("00000010-0000-1000-8000-00805f9b34fb")
    print("Connected VETTT ADAT:")
    print(value)
    device.subscribe("00000003-0000-1000-8000-00805f9b34fb", callback=handle_data,indication=False, wait_for_response=False)
   # device.subscribe("00000001-0000-1000-8000-00805f9b34fb", callback=handle_data1, indication=False,
    #                 wait_for_response=True)
   # device.subscribe("00000002-0000-1000-8000-00805f9b34fb", callback=handle_data2, indication=False,
    #                 wait_for_response=True)
    a_string = "ab"
    value = device.char_write("00000010-0000-1000-8000-00805f9b34fb", bytearray([0x53, 0xFF]), True)
    encoded_string = a_string.encode()
    byte_array = bytearray(encoded_string)
    dt = datetime.now()

    ts = datetime.timestamp(dt)
    print("Timestamp is:", dt)
    ts1=ts
    for i in range(1 ,2):
    #while True:
        #value = device.char_read("0000fe41-8e22-4541-9d4c-21edae82ed19")
        #value = device.char_write("00000002-8e22-4541-9d4c-21edae82ed19", byte_array, False)
   #     value = device.char_read_long("00000003-0000-1000-8000-00805f9b34fb")

        dt = datetime.now()
       # print(value)
        #print("Timestamp is:", dt)
        # print("Connected")
    dt = datetime.now()

    ts = datetime.timestamp(dt)
    print(ts-ts1)

finally:
    #adapter.stop()
    print("fgh")

while True:
    time.sleep(0.0001)






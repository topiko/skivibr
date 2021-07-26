import serial
import time
import pandas as pd
import numpy as np
import sys

dname = sys.argv[1]
runt = float(sys.argv[2])

baud = 230400
ser = serial.Serial('/dev/ttyUSB0', baudrate=baud)
ser.flushInput()

with open(f"{dname}.csv","w") as f:
    f.writelines('t,ax,ay,az\n')

t0 = time.time()

print("START MEASURE:")

while True:
    ser_bytes = ser.readline()
    try:
        accel_vec = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
    except:
        continue


    if not accel_vec.startswith("t="):
        continue

    accel_vec = accel_vec[2:]

    with open(f"{dname}.csv","a") as f:
        f.writelines(f'{accel_vec}\n')

    t1 = time.time()
    if t1 - t0 > runt:
        break



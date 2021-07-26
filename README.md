Get arduino ide and install Adfruit accel library (check the name from inports of mpu6050.ino)

Fix correct usb device and baudrates etc in the readser.py.

Run readser: 
python readser.py nameofrun T
where T is the data collection time. Note there (is a bug?) is some weird behavior and the initial 2 sec of the collection seem to be discarded. Apparently the arduino resets?? when it gets serial initialization from computer side..

After data collection you have file nameofrun.csv in your script folder. You can plot it using python plotacc.py nameofrun (T1 T2), where the optional T1 and T2 are the start and end for the fitting window of damped harmonic oscillator eq.. It will spit out the damping coeff. and frequency. 





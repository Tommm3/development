import machine
import time

pwm12 = machine.PWM(machine.Pin(13))
pwm12.freq(500)
pwm12.duty(0)

while 1:
    for i in range(0,1024):
        pwm12.duty(i)
        time.sleep(0.001)

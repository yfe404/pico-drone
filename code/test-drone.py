import time 
from machine import Pin, ADC, PWM
from utils import get_duty_cycle, map_value


MIN_THROTTLE = 1050
MAX_THROTTLE = 1950

input_pin = Pin(0, Pin.IN)

pwm0 = PWM(Pin(2))      # create PWM object from a pin
pwm1 = PWM(Pin(3))      
pwm2 = PWM(Pin(4))      
pwm3 = PWM(Pin(5))      

print("CONFIG CHECK...")
assert MAX_THROTTLE > MIN_THROTTLE
print("DONE!")

while True:
    #time.sleep(.01)
    throttle = get_duty_cycle(input_pin)
    if throttle > MAX_THROTTLE:
        throttle = MAX_THROTTLE
    if throttle < MIN_THROTTLE:
        throttle = MIN_THROTTLE
        
    pwm0.duty_u16(map_value(throttle))
    print(throttle)

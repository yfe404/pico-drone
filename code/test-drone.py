import time 
from machine import Pin, ADC, PWM
from utils import get_duty_cycle


input_pin = Pin(0, Pin.IN)

pwm0 = PWM(Pin(2))      # create PWM object from a pin
pwm1 = PWM(Pin(3))      
pwm2 = PWM(Pin(4))      
pwm3 = PWM(Pin(5))      

while True:
    time.sleep(.1)

    throttle = get_duty_cycle(input_pin)
    pwm0.duty_u16(filtered_value)

    

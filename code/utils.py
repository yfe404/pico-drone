from machine import Pin, PWM
import time

def get_duty_cycle(input_pin):
    """
    Compute the duty cycle (Pulse Width Modulation - range 1000-2000ms) from the input pin.
    """
    while True:
        # Wait for a rise
        while input_pin.value() == 0:
            pass
        start = time.ticks_us()
        # stop when the signal is low
        while input_pin.value() == 1:
            pass
        end = time.ticks_us()
        duty = end - start
        print (str(duty))
    

if __name__ == "__main__":
    input_pin = Pin(0, Pin.IN)
    get_duty_cycle(input_pin)
    

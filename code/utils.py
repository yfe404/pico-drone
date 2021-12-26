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
        return duty
    

def map_value(value, from_min=1000, from_max=2000, to_min=0, to_max=65000):
    """
    Rescale value from interval [from_min, from_max] to interval 
    [to_min, to_max] using min-max normalization.

    See https://en.wikipedia.org/wiki/Feature_scaling
    """
    if value > from_max or value < from_min:
        raise Exception("Error: value must be between from_min and from_max")

    assert from_min < from_max
    assert to_min < to_max

    a = (value - from_min) * (to_max - to_min)
    b = from_max - from_min
    c = a // b
    new_value = to_min + c
    
    return new_value
        
if __name__ == "__main__":
    input_pin = Pin(0, Pin.IN)
    get_duty_cycle(input_pin)

    

# Created by: Batuhan Durhan
# Created at: October 11 2020 

def on_forever():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    basic.pause(1000)
basic.forever(on_forever)

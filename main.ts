//  Created by: Batuhan Durhan
//  Created at: October 11 2020 
basic.forever(function on_forever() {
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
    basic.pause(1000)
})


#Copyright (c) 2020 MTHS All rights reserved

#Created by: Ernest
#Created on: Nov 2023
#This program moves stepper motors depending on the distance

# variables
distanceToTarget: number = 0

# setup
basic.clear_screen()
basic.show_icon(IconNames.HAPPY)

while True:
    if input.button_is_pressed(Button.A) == True:
        distanceToTarget = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
        # move forwards
        if distanceToTarget > 10:
            basic.show_string(str(distanceToTarget))
            robotbit.stp_car_move(10, 48)
        # move backwards and turn
        if distanceToTarget <= 10:
            basic.show_string(str(distanceToTarget))
            robotbit.stp_car_move(-10, 48)
            robotbit.stp_car_turn(90, 48, 125)

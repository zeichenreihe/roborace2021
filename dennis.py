#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

to_angle_speed = 50
degree_to_turns = 0
max_heading = 0
current_heading = 0
turn_motor = Motor(Port.D)
motor = Motor(Port.A)
def head(motor, heading, speed):
    if heading > max_heading or heading < -1 * heading:
        heading = max_heading
    turn_motor.run_angle(speed, heading)
    global current_heading
    current_heading = heading

def drive(motor, speed):
    motor.run(speed)
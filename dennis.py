#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from sensors import Sensors
from motor_control import MotorControl
from logger import Logger

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

def scan_for_minimum_variant_1(ev3:EV3Brick, TIMER:StopWatch, sensors:Sensors, controller:MotorControl, LOGGER:Logger):
    correctness_offset = 10#cm
    direction = True # True ≙ to the right side
    max_α = 85
    steps = 34 # we do 34 steps in total, 17 for each side

    data = []
    for i in range(steps):
        data.append(0)

    def find_minimum_half(half_steps, step_size, values, direction = False, done = False):
        negative = -1 if direction else 1
        number = half_steps + 0 if direction else -1
        for i in range(half_steps):

            print(str(i) + " " + str(sensors.distance()))
            controller.angle_relative(step_size * negative)
            values[i * negative + number] = sensors.distance()
            
            if values[(i - 0) * negative + number] > (values[(i - 1) * negative + number] + correctness_offset) and \
                values[(i - 2) * negative + number] > (values[(i - 1) * negative + number] + correctness_offset):
                controller.angle_relative(step_size * negative * (-1))
                controller.shoot()
                done = True
                break
        
        controller.angle_absolute(0)
        if not done:
            find_minimum_half(half_steps, step_size, values, not direction, not done)

    find_minimum_half(int(steps / 2), 2 * max_α / steps, data, direction)
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from motor_control import MotorControl
from logger import LOGGER, TIMER
from sensors import Sensors
from utils import Utils
import properties

ev3 = EV3Brick()
#Utils.beep(ev3)
controller = MotorControl()
sensors = Sensors()

print(sensors.reflection_converter(58))
print(sensors.reflection_converter(34))
print(sensors.reflection_converter(12))

Utils.mrda_print_only(ev3, TIMER, sensors, controller)


print(sensors.reflection_converter(58))
print(sensors.reflection_converter(34))
print(sensors.reflection_converter(12))

#sensors.set_reflection([
#    (0, 12),
#    (50, 30),
#    (100, 68)
#])

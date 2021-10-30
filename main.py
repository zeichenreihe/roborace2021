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
import properties

ev3 = EV3Brick()
ev3.speaker.beep()
controller = MotorControl()
sensors = Sensors()


sensors.measure_reflection_drive_area(ev3, TIMER, controller)


#sensors.set_reflection([
#    (0, 12),
#    (50, 30),
#    (100, 68)
#])

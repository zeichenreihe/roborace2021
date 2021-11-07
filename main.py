#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                 Motor, TouchSensor, UltrasonicSensor)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

import properties
from logger import LOGGER, TIMER
from motor_control import MotorControl
from sensors import Sensors
from utils import Utils

ev3 = EV3Brick()
controller = MotorControl()
sensors = Sensors()

#Utils.mrda(ev3, TIMER, sensors, controller)
#Utils.mrda_print_only(ev3, TIMER, sensors, controller)
#Utils.mr(ev3, TIMER, sensors, controller)

Utils.main(ev3, TIMER, sensors, controller, LOGGER, False)
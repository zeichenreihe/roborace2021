from pybricks.ev3devices import ColorSensor, TouchSensor
from pybricks.parameters import Color

import properties

class Sensors():
    color_sensor = ColorSensor(properties.Ports.color_sensor)
    touch_sensor = TouchSensor(properties.Ports.touch_sensor)

    reflection_converter = lambda self, x: x * properties.ReflectionMeasurement.m + properties.ReflectionMeasurement.c

    def is_blue(self):
        return self.color_sensor.color() == Color.BLUE

    def color(self):
        return self.color_sensor.color()

    def is_pressed(self):
        return self.touch_sensor.pressed()
    
    def set_reflection(self, m, c):
        self.reflection_converter =  lambda x: x * m + c
        properties.ReflectionMeasurement.m = m
        properties.ReflectionMeasurement.c = c
    
    def reflection(self):
        return self.color_sensor.reflection()
    
    def reflection_converted(self):
        "returns the position of the sensor from 0 (black) to 100 (white)"
        return self.reflection_converter(self.reflection())

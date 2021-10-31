from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.parameters import Color
import properties

class Sensors():
    color_sensor = ColorSensor(Port.S1)

    reflection_converter = lambda self, x: (x - properties.ReflectionMeasurement.c) / properties.ReflectionMeasurement.m

    def is_blue(self):
        return self.color_sensor.color() == Color.BLUE

    def color(self):
        return self.color_sensor.color()
    
    def set_reflection(self, m, c):
        self.reflection_converter =  lambda x: (x - c) / m
        properties.ReflectionMeasurement.m = m
        properties.ReflectionMeasurement.c = c
    
    def reflection(self):
        return self.color_sensor.reflection()
    
    def reflection_converted(self):
        "returns the position of the sensor from 0 (black) to 100 (white)"
        return self.reflection_converter(self.reflection())

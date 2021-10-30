from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.parameters import Color

class Sensors():
    color_sensor = ColorSensor(Port.S1)

    def is_blue(self):
        return self.color_sensor.color() == Color.BLUE
    def color(self):
        return self.color_sensor.color()
    def set_reflection(list):
        """
        sets the reflection
        Arguments:
            [(at, value), ...]
                at: the position (0 = black border, 100 = white border) where the value is measured
                value: the reflection at that location on the paper (measured by the sensor)
        """
    def reflection(self):
        return self.color_sensor.reflection()
    def reflection_converted(self):
        "returns the position of the sensor from 0 (black) to 100 (white)"
        return self.color_sensor.reflection()

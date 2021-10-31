from pybricks.parameters import Port
DRIVE_AREA_WIDTH = 38#cm
SENSOR_WIDTH = 2#cm

class ReflectionMeasurement:
    m = 8.70625 # f(x) = m * x + c
    c = 0.5025
    v = 10

class Ports:
    big_motor = Port.A
    direction_motor = Port.D

class Brick:
    is_silent = False
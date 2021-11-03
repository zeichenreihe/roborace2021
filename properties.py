from pybricks.parameters import Port

class DriveArea:
    width = 38#cm

class ReflectionMeasurement:
    # f(x) = m * x + c = 2.083333333333333  * x + -18.05555555555556
    m = 2.083333333333333
    c = -18.05555555555556
    v = 10

class Ports:
    big_motor = Port.A
    direction_motor = Port.D
    shoot_motor = Port.B

    color_sensor = Port.S1
    touch_sensor = Port.S4
    distance_sensor = Port.S3

class Brick:
    sensor_width = 2#cm
    is_silent = False
    tps = 20

class DriveSetting:
    center = 30 # the center in percent from black to white

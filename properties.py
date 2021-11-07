from pybricks.parameters import Port

class DriveArea:
    width = 38#cm

class ReflectionMeasurement:
    # f(x) = m * x + c = 1.87793427230047 * x + -14.6322378716745
    m = 1.87793427230047
    c = -14.6322378716745
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
    center = 50 # the center in percent from black to white
    Kp = 2
    Ki = 0
    Kd = 0

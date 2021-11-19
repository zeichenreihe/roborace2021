from pybricks.parameters import Port

class DriveArea:
    width = 38#cm

class ReflectionMeasurement:
    # f(x) = m * x + c = 1.96078431372549 * x + -16.01307189542484
    m = 1.96078431372549
    c = -16.01307189542484
    v = 10

class Ports:
    big_motor = Port.A
    direction_motor = Port.D
    shoot_motor = Port.B

    color_sensor = Port.S1
    touch_sensor = Port.S4
    distance_sensor = Port.S3

class Brick:
    shoot = True
    sensor_width = 2#cm
    is_silent = False
    tps = 20

class MotorControl:
    turn_motor_speed = 60

    shoot_motor_speed = 80
    
    α_per_s = 942 / 40
    main_motor_full_speed = 10

class DriveSetting:
    v = 300
    center = 50 # the center in percent from black to white
    Kp = 2.5
    Ki = 0
    Kd = -0.5

    from_gradient_to_white = 30 # difference to think its the white area

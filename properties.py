from pybricks.parameters import Port

class DriveArea:
    parabola_in_semicircle = True
    parabola_angle = 47#° 0° ≙ in 90° from dirve area, 90° ≙ in drive direction
    width = 38#cm

class ReflectionMeasurement:
    # f(x) = m * x + c = 2.424242424242424 * x + -23.73737373737374
    m = 2.424242424242424
    c = -23.73737373737374
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
    skip_shoot = False
    shoot_correction = True
    shoot_correction_function = lambda x: 0
    #shoot_correction_function = lambda x: - (15 / 31)  * x + 15
    #shoot_correction_function = lambda x: - (36 / 32 * x)
    #shoot_correction_function = lambda x: abs(x - 16) / 2

    sensor_width = 2#cm
    is_silent = False
    tps = 20

class MotorControl:
    turn_motor_speed = 300

    shoot_motor_speed = 300
    
    α_per_s = 942 / 40
    main_motor_full_speed = 10

class DriveSetting:
    v = 450
    center = 70 # the center in percent from black to white
    Kp = 1.5#2.5
    Ki = 0
    Kd = -0.5

    from_gradient_to_white = 30 # difference to think its the white area

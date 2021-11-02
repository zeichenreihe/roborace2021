from pybricks.ev3devices import Motor
from pybricks.parameters import Direction, Port, Stop

import properties


class MotorControl():
    current_speed = 0
    
    main_motor = Motor(properties.Ports.big_motor, Direction.COUNTERCLOCKWISE)
    α_per_s = 942 / 40
    main_motor_full_speed = 10
    
    # min max = +-84 degree
    turn_motor = Motor(properties.Ports.direction_motor, Direction.CLOCKWISE, [24, 48])
    turn_motor_speed = 20
    turn_blocking = True

    shoot_motor = Motor(properties.Ports.shoot_motor, Direction.CLOCKWISE, [24, 40])
    shoot_motor_speed = 50

    def change_v_relative(self, Δv):
        self.current_speed = self.main_motor.speed()
        self.current_speed += Δv
        self.main_motor.run(self.current_speed)
    
    def change_v_absolute(self, v):
        self.current_speed = v
        self.main_motor.run(v)
    
    def change_Δs_relative(self, Δs, v, blocking):
        "Δs in m/s, v in deg/s"
        α_rotation = Δs * self.α_per_s
        self.main_motor.run_angle(v, α_rotation, Stop.HOLD, blocking)
    
    def stop(self):
        self.current_speed = 0
        self.main_motor.stop()
    
    def angle_absolute(self, angle_absolute_to, blocking = True, hold = Stop.HOLD): # 9ms
        self.turn_motor.run_target(self.turn_motor_speed, angle_absolute_to, hold, blocking)
    
    def angle_relative(self, angle_to_rotate, blocking = True, hold = Stop.HOLD):
        self.turn_motor.run_angle(self.turn_motor_speed, angle_to_rotate, hold, blocking)
    
    def angle_track(self, angle_to_track):
        self.turn_motor.track_target(angle_to_track)

    def shoot(self):
        self.shoot_motor.run_angle(self.shoot_motor_speed, 180, Stop.HOLD, True)
        self.shoot_motor.run_angle(self.shoot_motor_speed, 180, Stop.HOLD, False)

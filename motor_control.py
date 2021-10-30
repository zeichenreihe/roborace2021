from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
import properties

class MotorControl():
    

    current_speed = 0
    
    main_motor = Motor(properties.Ports.big_motor)
    α_per_s = 942 / 40
    main_motor_full_speed = 10
    
    # min max = +-84 degree
    turn_motor = Motor(properties.Ports.direction_motor, Direction.CLOCKWISE, [24, 48])
    turn_motor_speed = 20
    turn_blocking = True

    def change_v_relative(self, Δv):
        v_curr = self.main_motor.speed()
        self.main_motor.run(Δv + v_curr)
    def change_v_absolute(self, v):
        self.main_motor.run(v)
    def change_Δs_relative(self, Δs, v, blocking):
        "Δs in m/s, v in deg/s"
        α_rotation = Δs * self.α_per_s
        self.main_motor.run_angle(v, α_rotation, Stop.HOLD, blocking)
    def stop(self):
        self.current_speed = 0
    def angle_absolute(self, angle_absolute_to): # 9ms
        self.turn_motor.run_target(self.turn_motor_speed, angle_absolute_to, Stop.HOLD, self.turn_blocking)
    def angle_relative(self, angle_to_rotate):
        self.turn_motor.run_angle(self.turn_motor_speed, angle_to_rotate, Stop.HOLD, self.turn_blocking)
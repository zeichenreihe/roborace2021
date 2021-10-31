from sensors import Sensors

from pybricks.hubs import EV3Brick
from pybricks.tools import StopWatch
from pybricks.tools import wait

from motor_control import MotorControl
import properties

class Utils:
    def get_f_x_refleciton():
        return "f(x) = " + str(properties.ReflectionMeasurement.m) + "  * x + " + str(properties.ReflectionMeasurement.c)
    
    def mr(ev3:EV3Brick, watch:StopWatch, sensors:Sensors):
        "measure reflection - blocks execution, prints the values of the reflection from the color sensor"
        while True:
            ev3.screen.clear()
            value = sensors.color_sensor.reflection()
            time = watch.time()
            print(str(time) + "\t\t" + str(value))
            ev3.screen.print(str(time))
            ev3.screen.print(str(value))
            wait(100)     
    
    def mrda(ev3:EV3Brick, watch:StopWatch, sensors:Sensors, controller:MotorControl):
        "measure reflection drive area - automatically (setup in 90° to drive direction) drives accross the area"
        print("old function was: " + Utils.get_f_x_refleciton())
        ev3.screen.clear()

        n = 4
        
        values = []
        distance_between_measurement_points = (properties.DRIVE_AREA_WIDTH - properties.SENSOR_WIDTH) / (n - 1)
        for i in range(n):
            Utils.beep(ev3)
            value = sensors.reflection()
            time = watch.time()
            
            print(str(i * 100/ (n - 1)) + " " + str(value) + "\t" + str(time))
            ev3.screen.print(str(i) + " " + str(value))

            values.append((
                i * 100/ (n - 1),
                value
            ))
            if i in range(n - 1):
                controller.change_Δs_relative(distance_between_measurement_points, properties.ReflectionMeasurement.v, True)
        del value, time, distance_between_measurement_points, n

        point_average = lambda a, b: ( (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 )

        values[0] = point_average(values[0], values[1])
        values[1] = point_average(values[2], values[3])
        del point_average

        get_m = lambda a, b: (b[1] - a[1]) / (b[0] - a[0])
        m = get_m(values[0], values[1])
        del get_m

        c = values[0][1] - values[0][1] * m
        del values

        sensors.set_reflection(m, c)
        print("new function is: " + Utils.get_f_x_refleciton())
    
    def mrda_print_only(ev3:EV3Brick, watch:StopWatch, sensors:Sensors, controller:MotorControl):
        n = 20
        distance_between_measurement_points = (properties.DRIVE_AREA_WIDTH - properties.SENSOR_WIDTH) / (n - 1)
        for i in range(n):
            Utils.beep(ev3)
            value = sensors.reflection()
            
            print("(" + str(i * 100 / (n - 1)) + "," + str(value) + "),")

            if i in range(n - 1):
                controller.change_Δs_relative(distance_between_measurement_points, properties.ReflectionMeasurement.v, True)
    
    def beep(ev3:EV3Brick):
        if not properties.Brick.is_silent:
            ev3.speaker.beep()
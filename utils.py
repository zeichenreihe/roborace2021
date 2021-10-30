from sensors import Sensors

from pybricks.hubs import EV3Brick
from pybricks.tools import StopWatch
from pybricks.tools import wait

from motor_control import MotorControl
import properties

class Utils:
    def measure_reflection(sensors:Sensors, ev3:EV3Brick, watch:StopWatch):
        "blocks execution, prints the values of the reflection from the color sensor"
        while True:
            ev3.screen.clear()
            value = sensors.color_sensor.reflection()
            time = watch.time()
            print(str(time) + "\t\t" + str(value))
            ev3.screen.print(str(time))
            ev3.screen.print(str(value))
            wait(100)     
    def measure_reflection_drive_area(sensors:Sensors, ev3:EV3Brick, watch:StopWatch, controller:MotorControl):
        ev3.screen.clear()
        values = []
        for i in range(3):
            ev3.speaker.beep()
            value = sensors.color_sensor.reflection()
            time = watch.time()
            print(str(i) + " " + str(value) + "\t@ t = " + str(time))
            ev3.screen.print(properties.ReflectionMeasurement.desciptions[i][0] + " " + str(value))
            values.append((i*50,value))
            if i in range(2):
                controller.change_Δs_relative((properties.DRIVE_AREA_WIDTH - properties.SENSOR_WIDTH) / 2, properties.ReflectionMeasurement.v, True)
        print(str(values))
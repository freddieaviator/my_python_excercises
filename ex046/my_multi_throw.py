import math
import numpy as np

angle = np.array([35,40,45])
velocity = np.array([35,40,45])
throw_height = float(input("Input throw height in meter: "))

angle_radian = np.radians(angle)
throw_velocity = velocity/3.6
horizontal_velocity = throw_velocity * np.cos(angle_radian)
vertical_velocity = throw_velocity * np.sin(angle_radian)
ball_airtime = (vertical_velocity + np.sqrt(vertical_velocity**2 + 2*9.81*throw_height))/9.81
throw_distance = horizontal_velocity * ball_airtime

print(f"""The throw angle in radians is: {angle_radian}
The throw velocity in m/s is: {throw_velocity}
The throw velocity in the horizontal direction in m/s is: {horizontal_velocity}
The throw velocity in the vertical direction in m/s is: {vertical_velocity}
The ball airtime is: {ball_airtime}
The throw distance is: {throw_distance}""")


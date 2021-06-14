import math

angle = float(input("Input angle in degrees: "))
velocity = float(input("Input velocity in km/h: "))
throw_height = float(input("Input throw height in meter: "))

angle_radian = math.radians(angle)
throw_velocity = velocity/3.6
horizontal_velocity = throw_velocity * math.cos(angle_radian)
vertical_velocity = throw_velocity * math.sin(angle_radian)
ball_airtime = (vertical_velocity + math.sqrt(vertical_velocity**2 + 2*9.81*throw_height))/9.81
throw_distance = horizontal_velocity * ball_airtime

print(f"The throw angle in radians is: {angle_radian:.2f}")
print(f"The throw velocity in m/s is: {throw_velocity:.2f}")
print(f"The throw velocity in the horizontal direction in m/s is: {horizontal_velocity:.2f}")
print(f"The throw velocity in the vertical direction in m/s is: {vertical_velocity:.2f}")
print(f"The ball airtime is: {ball_airtime:.2f}")
print(f"The throw distance is: {throw_distance:.2f}")

#f) a little bit less than 45 degrees for the longest throw.
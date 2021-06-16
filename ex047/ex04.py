import math

def kmh_to_ms(velocity):
    return velocity/3.6

def velocity_decomposition(velocity,angle):
    angle_radian = math.radians(angle)
    throw_velocity = kmh_to_ms(velocity)
    horizontal_velocity = throw_velocity * math.cos(angle_radian)
    vertical_velocity = throw_velocity * math.sin(angle_radian)
    return horizontal_velocity,vertical_velocity


def throw_possition(velocity,angle,time,init_height = 1.8)->float:
    """ Calculates throw-distance and use time instead of airtime if time<airtime

    Args: Velocity, Angle, Time and optional height    
    Returns: Float with the throw-distance using arg time if < airtime
    otherwise using airtime.
    """
    horizontal_velocity,vertical_velocity = velocity_decomposition(velocity,angle)
    ball_airtime = airtime(vertical_velocity,init_height)

    if(time < ball_airtime):
        return horizontal_velocity * time
    else:
        return horizontal_velocity * ball_airtime

def airtime(velocity_y,init_height,g = 9.81):
    return (velocity_y + math.sqrt(velocity_y**2 + 2*g*init_height))/g


def throw_distance(velocity,angle,init_height = 1.8)->float:
    """ Calculates throw-distance

    Args: Vertical velocity, Height and optional g-force    
    Returns: Float with the throw-distance
    """
    horizontal_velocity,vertical_velocity = velocity_decomposition(velocity,angle)
    ball_airtime = airtime(vertical_velocity,init_height)
    return horizontal_velocity * ball_airtime

print(throw_distance(45,45))
print(throw_possition(45,45,1))


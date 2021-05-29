def angle_to_time(angle):
    if angle == 90:
        return 1.1
    elif angle == 45:
        return 0.7


def cm_to_time(cm):
    # ensure speed is 50%
    if cm == 1:
        return 0.3
    elif cm == 2:
        return 0.7

# precalculated by measuring
def angle_to_time(angle):
    if angle == 90:
        return 0.40
    elif angle == 45:
        return 0.20


def cm_to_time(cm):
    # ensure speed is 50%
    a_cm = 0.8
    if cm == 1:
        return 0.8
    elif cm == 2:
        return 0.16
    elif cm == 4:
        return 0.32

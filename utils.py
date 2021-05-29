# precalculated by measuring
def angle_to_time(angle):
    if angle == 90:
        return 0.40
    elif angle == 45:
        return 0.20


def cm_to_time(cm):
    # ensure speed is 50%
    a_cm = 0.8
    return a_cm * cm

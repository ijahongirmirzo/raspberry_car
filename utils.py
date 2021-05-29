# precalculated by measuring
def angle_to_time(angle):
    if angle == 90:
        return 0.64
    elif angle == 45:
        return 0.32


def cm_to_time(cm):
    # ensure speed is 50%
    if cm == 1:
        return 0.15
    elif cm == 2:
        return 0.3

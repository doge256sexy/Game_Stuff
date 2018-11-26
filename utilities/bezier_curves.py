__author__ = 'Gregorio Manabat III'

def de_casteljaus(control_points, t):
    new_bez = []
    for i in range(len(control_points)-1):
        new_bez.append((control_points[i][0] * (1 - t) + control_points[i + 1][0] * t, control_points[i][1] * (1 - t) + control_points[i + 1][1] * t))
    if len(new_bez) == 1:
        return new_bez[0]
    else:
        return de_casteljaus(new_bez, t)
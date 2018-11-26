__author__ = 'Gregorio Manabat III'

def line(x1, y1, x2, y2, grid, colored, update_func):
    steps = max(abs(x2 - x1), abs(y2 - y1))
    for i in range(steps):
        x = int(interpolate(x1, x2, i/steps))
        y = int(interpolate(y1, y2, i/steps))
        grid[x][y] = colored
        update_func(x, y)


def interpolate(x1, x2, t):
    return x1 * t + x2 * (1 - t)
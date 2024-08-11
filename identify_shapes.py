import numpy as np

def identify_circle(XY):
    center = np.mean(XY, axis=0)
    radius = np.mean(np.sqrt((XY[:, 0] - center[0])**2 + (XY[:, 1] - center[1])**2))
    return center, radius

def identify_line(XY):
    p1, p2 = XY[0], XY[-1]
    return p1, p2

import numpy as np
from scipy.interpolate import interp1d

def complete_curve(XY):
    x = XY[:, 0]
    y = XY[:, 1]
    interp_func = interp1d(x, y, kind='linear', fill_value="extrapolate")
    new_x = np.linspace(x.min(), x.max(), num=100)
    new_y = interp_func(new_x)
    return np.column_stack((new_x, new_y))

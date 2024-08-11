import numpy as np

def detect_symmetry(XY):
    center = np.mean(XY, axis=0)
    distances = np.linalg.norm(XY - center, axis=1)
    return np.allclose(distances, distances[::-1])

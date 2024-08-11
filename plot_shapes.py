import numpy as np
import matplotlib.pyplot as plt

def plot(paths_XYs, output_file=None):
    plt.figure(figsize=(10, 10))
    for path_XYs in paths_XYs:
        for XY in path_XYs:
            plt.plot(XY[:, 0], XY[:, 1], marker='o')
    plt.title('Beautified Doodles')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.gca().set_aspect('equal', adjustable='box')
    if output_file:
        plt.savefig(output_file)
        print(f"Plot saved to {output_file}")
    else:
        plt.show()
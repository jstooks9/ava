import numpy as np

def sample_points(ymin, ymax):
    """
    sampled points are always on the user-supplied problem boundaries
    ymax is the height of the original image

    sample y1
    sample y2

    return y1, y2
    """

    y1 = np.random.randint(ymin, high=ymax)
    y2 = np.random.randint(ymin, high=ymax)

    return y1, y2
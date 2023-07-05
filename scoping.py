"""
Scoping out the program

To read an image:
import matplotlib.image as mpimg
filename = 'test-image.png''
img = mpimg.imread(filename)

img.shape = (height, width, 4)
img[:,:,0] = R value
img[:,:,1] = G value
img[:,:,2] = B value
img[:,:,3] = brightness value

all values are floating points between 0.0 and 1.0 
    representing the intensity of the relevant
    quantity

true height, true width:
    physical dimension of the drawing (e.g., 8.5"x11")

plot image with:
plt.imshow(img)
plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Analysis:
    def __init__(self, filename, colors, weights):
        self.filename = filename
        self.colors = colors
        self.weights = weights

def sample_points(x1, x2, height):
    """
    pick two points on the problem boundaries

    shouldn't do it this way.
    should sample angle and starting point instead
    then calculate the end point
    """
    point1 = (x1, np.random.random()*height)
    point2 = (x2, np.random.random()*height)

    return point1, point2

def process_image(filename):
    img = mpimg.imread(filename)
    return img

def get_scale(img):
    dims = img.shape
    height = dims[0]
    width = dims[1]

    return height, width

def score_vector(img, vector_image):
    vector_image = vector_image.astype(bool)
    blue = (0.259, 0.522, 0.957)
    blue_collapse = np.sum(blue)
    green = (0, 1, 0)
    gray = (0.953, 0.953, 0.953)
    white = (1, 1, 1)

    r = np.where(vector_image, img[:,:,0], 0)
    g = np.where(vector_image, img[:,:,1], 0)
    b = np.where(vector_image, img[:,:,2], 0)

    # new_img = np.zeros(img.shape)
    # new_img[:,:,0] = r
    # new_img[:,:,1] = g
    # new_img[:,:,2] = b

    r_score = r.flatten()
    g_score = g.flatten()
    b_score = b.flatten()

    r_score = np.around(r_score, decimals=3)
    g_score = np.around(g_score, decimals=3)
    b_score = np.around(b_score, decimals=3)

    score = 0
    for i in range(len(r_score)):
        rgb = (r_score[i], g_score[i], b_score[i])
        if rgb == blue:
            score += 1
        elif rgb == green:
            score += 3.5

    plt.figure()
    # plt.imshow(new_img, origin='upper')
    plt.imshow(r, origin='upper')
    plt.figure()
    plt.imshow(g, origin='upper')
    plt.figure()
    plt.imshow(b, origin='upper')

    print("shielding score =", score)

    return score

def draw_vector(point1, point2, height, width, true_height, true_width,
                    tolerance=1e-1):
    """points are (x, y) tuples

        need to return the coordinates of the 
        set of pixels that the vector passes
        through

        f(x) = (y2-y1)/(x2-x1)*x + y1

        The function has units of inches (or)
    """

    # each pixel has boundaries (x_i, y_i) and (x_i+1, y_i+1)

    pixel_width = true_width / width
    pixel_height = true_height / height

    x1 = point1[0] * pixel_width
    y1 = point1[1] * pixel_height
    x2 = point2[0] * pixel_width
    y2 = point2[1] * pixel_height

    slope = (y2 - y1) / (x2 - x1)
    y_intercept = y1

    f = lambda x: slope * x + y_intercept

    # for now, take the bottom left corner to be (0,0)

    # initialize vector
    vector_image = np.zeros((height, width), dtype=bool)

    for i in range(height):
        for j in range(width):
            # calculate the boundaries of the pixel
            x_min = j * pixel_width
            x_max = (j + 1) * pixel_width
            y_min = i * pixel_height
            y_max = (i + 1) * pixel_height

            # test if the function passes through here
            # if f(x_min) > y_min and f(x_max) < y_max:
            if f(x_min) + tolerance > y_min and f(x_max) < y_max + tolerance:
                vector_image[i, j] = True
                # print(x_min, y_min, f(x_min), x_max, y_max, f(x_max))

    vector_image = vector_image.astype(float)

    return vector_image

def main():
    # 1347 x 1062
    bound1 = 133
    bound2 = 1200
    filename = 'test-image.png'
    true_height = 120
    true_width = 1347/1062*120
    # blue = (0, 0, 1)
    # green = (0, 1, 0)
    # colors = (blue, green)
    # weights = (1, 3.5)
    # my_analysis = Analysis(filename, colors, weights)
    point1 = (15, 200)
    point2 = (600, 700)
    point1 = (0, 0)
    point2 = (1347, 1062)
    # point1 = (0, 1062)
    # point2 = (1347, 0)
    # point1 = (bound1, 200)
    # point2 = (bound2, 700)
    img = process_image(filename)
    height, width = get_scale(img)
    my_vector = draw_vector(point1, point2, height, width, true_height, true_width)
    plt.figure()
    plt.imshow(my_vector, origin='upper')
    plt.colorbar()
    # plt.grid()
    # plt.show()

    score = score_vector(img, my_vector)

    plt.show()
    return None

if __name__ == '__main__':
    main()
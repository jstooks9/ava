from PIL import Image, ImageDraw

import numpy as np
import matplotlib.pyplot as plt

from draw_line_and_sum_colors import *
from sample_points import *
from score_line import *


def main():
    # provide input information
    n = int(100) # number of vectors to sample
    scorecard = {(0, 255, 0, 255): 3.5, # green steel
                    (0, 0, 255, 255): 1, # blue concrete
                }
    filename = 'test-image-2.png'
    high_outname = 'most_shielding.png'
    low_outname = 'least_shielding.png'
    im = Image.open(filename)
    width, height = im.size
    # x1 = 80
    # x2 = 1250
    # ymax = 957
    # ymin = 61
    x1 = 0
    x2 = width
    ymin = 0
    ymax = height

    low_score = 1e9
    low_y1 = 0
    low_y2 = 0
    high_score = 0
    high_y1 = 0
    high_y2 = 0
    for i in range(n):
        y1, y2 = sample_points(ymin, ymax)
        color_sum = draw_line_and_sum_colors(filename, (x1, y1), (x2,y2))
        score = score_line(color_sum, scorecard)
        if score < low_score:
            low_score = score
            low_y1 = y1
            low_y2 = y2
        if score > high_score:
            high_score = score
            high_y1 = y1
            high_y2 = y2
        print("Sample %g complete." % i)
    print('low score', low_y1, low_y2, low_score)
    print('high score', high_y1, high_y2, high_score)
    draw_line_and_sum_colors(filename, (x1, low_y1), (x2, low_y2), 
                                outname=low_outname, print=True)
    draw_line_and_sum_colors(filename, (x1, high_y1), (x2, high_y2), 
                                outname=high_outname, print=True)

if __name__ == '__main__':
    main()
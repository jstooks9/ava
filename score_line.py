def score_line(color_sum, scorecard):

    score = 0
    for color, count in color_sum.items():
        for material, weight in scorecard.items():
            if color == material:
                print(count, weight, count*weight)
                score += count * weight
    return score

def main():
    pass

if __name__ == '__main__':
    main()
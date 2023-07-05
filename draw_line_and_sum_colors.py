from PIL import Image, ImageDraw

def draw_line_and_sum_colors(image_path, start_point, end_point,
                                outname='output_image.png', print=False):
    # Load the image
    image = Image.open(image_path)
    width, height = image.size

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Draw the line on the image
    draw.line((start_point, end_point), fill=(255, 0, 0), width=2)

    # Sum the number of pixels for each color
    color_sum = {}
    for y in range(min(start_point[1], end_point[1]), max(start_point[1], end_point[1])):
        for x in range(min(start_point[0], end_point[0]), max(start_point[0], end_point[0])):
            pixel = image.getpixel((x, y))
            if pixel not in color_sum:
                color_sum[pixel] = 0
            color_sum[pixel] += 1

    # Print the color sums
    # for color, count in color_sum.items():
    #     print(f"Color {color}: {count} pixels")

    # Save the modified image
    if print:
        image.save(outname)

    return color_sum

def main():
    # Example usage
    image_path = "test-image.png"
    start_point = (0, 0)
    end_point = (1000, 1000)

    draw_line_and_sum_colors(image_path, start_point, end_point)

    return None

if __name__ == '__main__':
    main()
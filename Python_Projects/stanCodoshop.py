"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red)**2+(blue-pixel.blue)**2+(green-pixel.green)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r_sum = 0
    g_sum = 0
    b_sum = 0
    count = 0
    for i in range(len(pixels)):
        r_sum += pixels[i].red
        g_sum += pixels[i].green
        b_sum += pixels[i].blue
        count += 1
    r_avg = r_sum / count
    g_avg = g_sum / count
    b_avg = b_sum / count
    rgb = [r_avg, g_avg, b_avg]  # Create a list that contains average red, green and blue values
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    average_rgb = get_average(pixels)
    best = 0  # Find the smallest distance from average red, green, and blue values
    pixels_box = pixels[0]  # Save the pixel with smallest distance
    for i in range(len(pixels)):
        compared = get_pixel_dist(pixels[i], average_rgb[0], average_rgb[1], average_rgb[2])
        if i == 0:  # Set initial value
            best = compared
        if best > compared:  # If compared is less than best, save the compared value and pixel
            best = compared
            pixels_box = pixels[i]
    return pixels_box


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    pixel_lst = []  # Create a list to save pixels at the same position in different photos
    for x in range(result.width):
        for y in range(result.height):
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixel_lst.append(pixel)
            best = get_best_pixel(pixel_lst)  # Get the best pixel in pixel_lst
            result_p = result.get_pixel(x, y)
            result_p.red = best.red
            result_p.green = best.green
            result_p.blue = best.blue
            pixel_lst = []  # Clear the list to save pixels at another positions
    # Write code to populate image and create the 'ghost' effect
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

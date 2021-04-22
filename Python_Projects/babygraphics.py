"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE) / len(YEARS)  # Count the interval
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * interval
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)  # Draw upper horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)  # Draw lower horizontal line
    for i in range(len(YEARS)):  # Draw vertical lines of each year
        line_x = get_x_coordinate(LINE_WIDTH, i)
        canvas.create_line(line_x, 0, line_x, CANVAS_HEIGHT)
        canvas.create_text(line_x + TEXT_DX, CANVAS_HEIGHT, text=YEARS[i], anchor=tkinter.SW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # Divide the distance between upper and lower line into (1000-1) proportions, which helps define y
    # 1000-1→ if rank == 1, y == GRAPH_MARGIN_SIZE
    interval = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / (1000 - 1)
    for i in range(len(lookup_names)):
        for j in range(len(YEARS)):
            x1 = get_x_coordinate(LINE_WIDTH, j)
            # Remember to turn the datatype of YEARS[j](int) into str
            if str(YEARS[j]) in name_data[lookup_names[i]]:  # if YEARS[j] exists in name_data[entered name]
                rank = name_data[lookup_names[i]][str(YEARS[j])]
                y1 = GRAPH_MARGIN_SIZE + (int(rank) - 1) * interval
            else:  # if YEARS[j] doesn't exist in name_data[entered name]
                rank = '*'
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            canvas.create_text(x1 + TEXT_DX, y1, text=(lookup_names[i], rank), anchor=tkinter.SW, fill=COLORS[i])
            if j != len(YEARS)-1:  # if j is the last, does not need to execute the code below
                x2 = get_x_coordinate(LINE_WIDTH, j+1)
                if str(YEARS[j+1]) in name_data[lookup_names[i]]:
                    y2 = GRAPH_MARGIN_SIZE + (int(name_data[lookup_names[i]][str(YEARS[j+1])]) - 1) * interval
                else:
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[i])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

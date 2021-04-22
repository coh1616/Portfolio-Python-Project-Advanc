"""
File: draw_line.py
Name:Yunchuan Kao
-------------------------
The program displays the points at odd number of clicks and becomes a line at even number of clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Create global variables for different stacks to use
window = GWindow()
count = 0
former = GOval(10, 10)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point)


def point(m):
    global count, former
    dot = GOval(10, 10)
    count += 1
    former_x = former.x
    former_y = former.y
    x = m.x - dot.width / 2
    y = m.y - dot.height / 2
    # If count is odd, show a point
    if count % 2 == 1:
        window.add(dot, x, y)
    # If count is even, remove the last point and show a line
    else:
        line = GLine(former_x, former_y, x, y)
        window.remove(former)
        window.add(line)
    # To record the last point's position and save the last point as former
    former_x = x
    former_y = y
    former = dot


if __name__ == "__main__":
    main()

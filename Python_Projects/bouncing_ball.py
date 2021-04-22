"""
File: bouncing_ball.py
Name: Yunchuan Kao
-------------------------
The program displays the animation of bouncing ball with gravity.
And the bouncing height after every collision will reduce.
The animation will not be triggered anymore after 3 complete bouncing turns.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Create global variables
# Set a variable to determine when the ball can move
move = True
# Set a variable to compute how many times user has clicked
click_number = 0
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global move, click_number, ball
    # Show the ball at the beginning
    ball.filled = True
    window.add(ball)
    onmouseclicked(start)
    # If user has clicked, it'll remove the initial ball
    if click_number > 0:
        window.remove(ball)


def start(m):
    global move, click_number
    # Set original y speed as 0
    vy = 0
    ball.filled = True
    window.add(ball)
    # When the ball is moving, it won't be influenced by clicks
    if move:
        # If user has clicked over 3 times, the ball will remain at the original position and won't move
        click_number += 1
        if click_number < 4:
            # Turn off the move and the ball won't be affected during the bouncing period
            move = False
            while ball.x < window.width-ball.width:
                ball.move(VX, vy)
                if ball.y+vy >= window.height-ball.height:
                    vy *= -REDUCE
                else:
                    vy += GRAVITY
                pause(DELAY*3)
            window.add(ball, START_X, START_Y)
            # Turn on the move and the ball starts a new bouncing process
            move = True


if __name__ == "__main__":
    main()

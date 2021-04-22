"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width - self.paddle.width) / 2,
                        (self.window.height - self.paddle.height - paddle_offset))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

        self.move = False  # Set move so the ball won't be influenced by clicks

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)
        self.paddle_offset = PADDLE_OFFSET  # Set paddle_offset as an attribute so it can be used in methods
        self.row = brick_rows  # Count the number of rows
        self.col = brick_cols  # Count the number of columns

        # Draw bricks
        y = brick_offset
        for i in range(brick_rows):
            x = 0  # Put position x in for loop to reset the x value at every row
            for j in range(brick_cols):
                self.rect = GRect(brick_width, brick_height)
                self.rect.filled = True
                color = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow', 'green', 'green', 'blue', 'blue']
                self.rect.fill_color = color[i]
                self.window.add(self.rect, x, y)
                x += (brick_width + brick_spacing)
            y += (brick_height + brick_spacing)

    def check_collisions(self):
        """
        Check whether the ball collides anything.
        If the ball collides an object, return the object. If it doesn't, return None.
        """
        maybe_obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        maybe_obj_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if maybe_obj_1 is not None:
            return maybe_obj_1
        else:
            if maybe_obj_2 is not None:
                return maybe_obj_2
            else:
                if maybe_obj_3 is not None:
                    return maybe_obj_3
                else:
                    if maybe_obj_4 is not None:
                        return maybe_obj_4
                    else:
                        return None

    def start(self, event):
        """
        After user clicked, the move turns from False to True meaning the game starts.
        """
        self.move = True

    def paddle_move(self, event):
        """
        Connect the paddle to the mouse, if the mouse moves, the paddle goes with it
        :param event: mouse moved event
        """
        x = event.x - self.paddle.width / 2
        y = self.window.height - self.paddle.height - self.paddle_offset
        if x >= self.window.width - self.paddle.width:
            self.window.add(self.paddle, self.window.width - self.paddle.width, y)
        elif x <= 0:
            self.window.add(self.paddle, 0, y)
        else:
            self.window.add(self.paddle, x, y)

    # Getters
    def get_dx(self):
        """
        Get the ball's horizontal speed
        """
        return self.__dx

    def get_dy(self):
        """
        Get the ball's vertical speed
        """
        return self.__dy


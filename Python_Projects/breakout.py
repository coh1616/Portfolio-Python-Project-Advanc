"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    dy = graphics.get_dy()
    dx = graphics.get_dx()
    box = graphics.row * graphics.col  # Count how many bricks
    while True:
        pause(FRAME_RATE)
        if graphics.move and lives > 0:  # If move is true and there are remaining lives
            graphics.ball.move(dx, dy)
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                dx *= -1
            if graphics.ball.y <= 0:
                dy *= -1
            if graphics.ball.y >= graphics.window.height - graphics.ball.height:  # If user doesn't pick up the ball
                lives -= 1
                graphics.window.remove(graphics.ball)  # Remove the falling ball
                graphics.move = False  # Turn off the move
            obj = graphics.check_collisions()  # Whether the ball collides the objects
            if obj == graphics.paddle:  # If the ball collides the paddle, the ball bounces back
                dy = -dy
            # If the ball collides bricks, the ball bounces back and the bricks are removed
            elif obj != graphics.paddle and obj is not None:
                dy = -dy
                graphics.window.remove(obj)
                box -= 1  # If the bricked are removed, the game ends
        elif lives < 0:  # User loses
            break
        elif box == 0:  # User wins
            break
        else:  # If user haven't started the game
            graphics.window.add(graphics.ball, (graphics.window.width-graphics.ball.width) / 2,
                                (graphics.window.height-graphics.ball.height) / 2)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_RED

exp= design.Experiment(
    name="Screen edges",
    background_colour= C_BLACK
)

control.initialize(exp)

screen_width, screen_height = exp.screen.size
square_length = screen_width * 0.05
line_width = 1

left_pos = (-screen_width/2 + square_length / 2, 0)
right_pos = (screen_width / 2 - square_length / 2, 0)
top_pos = (0, screen_height / 2 - square_length / 2)
bottom_pos = (0, -screen_height / 2 + square_length / 2)

positions = [left_pos, right_pos, top_pos, bottom_pos]

canvas = stimuli.BlankScreen()

for pos in positions : 
    square = stimuli.Rectangle(
        size=(square_length, square_length),
        position = pos,
        colour=C_RED,
        line_width=line_width
    )
    square.plot(canvas)

canvas.present()

exp.keyboard.wait()

control.end()
from expyriment import design, control, stimuli

exp=design.Experiment(name = "launching")
control.initialize(exp)


def draw(left_square, right_square):
    left_square.present(clear=True, update = False)
    right_square.present(clear=False, update = True)

square_lenght = 50
square_size = (square_lenght, square_lenght)
step_size = 10

left_square = stimuli.Rectangle(
    size = square_size,
    colour = (225, 0, 0),
    position = (-400, 0)
)

right_square = stimuli.Rectangle(
    size = square_size,
    colour = (0,255,0),
    position = (0,0)
)
control.start(subject_id = 1)

draw(left_square, right_square)
exp.clock.wait (1000)

distance_traveled = 0

while left_square.distance(right_square)>square_lenght:
    left_square.move((step_size,0))
    distance_traveled += step_size
    draw (left_square, right_square)

moved_by_right_square = 0

while moved_by_right_square < distance_traveled:
    right_square.move((step_size, 0))
    moved_by_right_square += step_size
    draw(left_square,right_square)

draw(left_square,right_square)
exp.clock.wait(1000)

control.end()
from expyriment import design, control, stimuli, misc
control.set_develop_mode()

exp = design.Experiment(name = "Kanizsa-rectangle", background_colour=misc.constants.C_GREY)

control.initialize(exp)

bg_screen = stimuli.BlankScreen()

def draw_kanizsa_rectangle(bg_screen, aspect_ratio=2.0, rect_scale=0.25, circle_scale=0.05):
    screen_w, screen_h = exp.screen.size
    rect_width = int(screen_w * rect_scale)
    rect_height = int(rect_width / aspect_ratio)
    half_rect_w = rect_width / 2.0
    half_rect_h = rect_height / 2.0

    rect = stimuli.Rectangle(
    size=(rect_width, rect_height), 
    colour= misc.constants.C_GREY, 
    position=(0, 0)
    )

    circle_size = int(screen_w * circle_scale) 
    tl= (-half_rect_w, half_rect_h)
    tr= (half_rect_w, half_rect_h)
    bl= (-half_rect_w, -half_rect_h)
    br=(half_rect_w, -half_rect_h)


    circle1 = stimuli.Circle(radius=(circle_size), colour="black", position=tl)
    circle2 = stimuli.Circle(radius=(circle_size), colour="black",position=tr)
    circle3 = stimuli.Circle(radius=(circle_size), colour="white", position=bl)
    circle4 = stimuli.Circle(radius=(circle_size), colour="white", position=br)

    circle1.plot(bg_screen)
    circle2.plot(bg_screen)
    circle3.plot(bg_screen)
    circle4.plot(bg_screen)
    rect.plot(bg_screen)

draw_kanizsa_rectangle(bg_screen, aspect_ratio=2.0, rect_scale=0.25, circle_scale=0.05)

control.start(subject_id=1)
bg_screen.present()
exp.keyboard.wait()
control.end()
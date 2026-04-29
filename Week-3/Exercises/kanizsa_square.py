from expyriment import design, control, stimuli, misc
control.set_develop_mode()

exp = design.Experiment(name = "Kanizsa-square", background_colour=misc.constants.C_GREY)

control.initialize(exp)


screen_w, screen_h = exp.screen.size
square_size = int(screen_w * 0.25)
center= (0,0)
half_square = square_size / 2.0
square = stimuli.Rectangle(size=(square_size, square_size), colour= misc.constants.C_GREY, position=center)


circle_size = int(screen_w * 0.05) 
tl= (-half_square, half_square)
tr= (half_square, half_square)
bl= (-half_square, -half_square)
br=(half_square, -half_square)


circle1 = stimuli.Circle(radius=(circle_size), colour="black", position=tl)
circle2 = stimuli.Circle(radius=(circle_size), colour="black",position=tr)
circle3 = stimuli.Circle(radius=(circle_size), colour="white", position=bl)
circle4 = stimuli.Circle(radius=(circle_size), colour="white", position=br)


bg_screen = stimuli.BlankScreen()
circle1.plot(bg_screen)
circle2.plot(bg_screen)
circle3.plot(bg_screen)
circle4.plot(bg_screen)
square.plot(bg_screen)

control.start(subject_id=1)
bg_screen.present()
exp.keyboard.wait()
control.end()
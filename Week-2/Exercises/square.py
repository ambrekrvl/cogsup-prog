from expyriment import design, control, stimuli

exp=design.Experiment(name="square")
control.initialize(exp)

fixation = stimuli.FixCross() 

square = stimuli.Rectangle(size =(50, 50), colour=(0, 0, 255))

control.start(subject_id=1)

fixation.present(clear=True, update=True)

exp.clock.wait(1000)

square.present(clear=True, update = True)

exp.keyboard.wait()

control.end()
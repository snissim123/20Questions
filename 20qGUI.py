from graphics import *
from button import Button


def nextQuestion(win, myO):

	instructions = Text(Point(1.2, 4.5), "Is this thing a {}".format(myO))
	instructions.setTextColor("SlateGray")
	instructions.setFace("times roman")
	instructions.setSize(24)
	instructions.draw(win)

	yesButton = Button(win, Point(3.2, 3), .8, .5, "yes")
	yesButton.activate()

	noButton = Button(win, Point(4.8, 3), .8, .5, "no")
	noButton.activate()

	nextQ = False
	yes = False

	while not nextQ:
		pt = win.getMouse()

		if yesButton.clicked(pt):
			instructions.undraw()
			yesButton.remove()
			noButton.remove()
			nextQ = True
			yes = True

		elif noButton.clicked(pt):
			instructions.undraw()
			yesButton.remove()
			noButton.remove()
			nextQ = True

	return yes


def q20():
	# Setting up graphics window and making it visually appealing.
	win = GraphWin("20 Questions", 800, 600)
	win.setCoords(0.0, 0.0, 8.0, 6.0)
	win.setBackground("LightGray")

	title = Text(Point(4.0, 5.5), "20 Questions")
	title.setTextColor("SteelBlue")
	title.setFace("times roman")
	title.setSize(32)
	title.draw(win)

	# Prompting the user to interact with the program in a visually pleasing way.
	instructions = Text(Point(3.5, 4.5), "Welcome to 20 Questions! Please think of an item to begin the game.")
	instructions.setTextColor("SlateGray")
	instructions.setFace("times roman")
	instructions.setSize(24)
	instructions.draw(win)


	startButton = Button(win, Point(4, 3), 2, .6, "start")
	startButton.activate()

	begin = False

	while not begin:
		pt = win.getMouse()
		if startButton.clicked(pt):
			instructions.undraw()
			startButton.remove()
			begin = True


	# Prompting the user to interact with the program in a visually pleasing way.
	instructions = Text(Point(2.2, 4.5), "Great! Let's get started. Is this thing a(n):")
	instructions.setTextColor("SlateGray")
	instructions.setFace("times roman")
	instructions.setSize(24)
	instructions.draw(win)

	animalButton = Button(win, Point(2, 3), .8, .5, "animal")
	animalButton.activate()

	mineralButton = Button(win, Point(3.3, 3), .8, .5, "mineral")
	mineralButton.activate()

	vegetableButton = Button(win, Point(4.6, 3), .8, .5, "vegetable")
	vegetableButton.activate()

	otherButton = Button(win, Point(5.9, 3), .8, .5, "other")
	otherButton.activate()

	nextQ = False

	while not nextQ:
		pt = win.getMouse()

		if animalButton.clicked(pt):
			instructions.undraw()
			animalButton.remove()
			mineralButton.remove()
			vegetableButton.remove()
			otherButton.remove()
			nextQ = True

		elif mineralButton.clicked(pt):
			instructions.undraw()
			animalButton.remove()
			mineralButton.remove()
			vegetableButton.remove()
			otherButton.remove()
			nextQ = True

		elif vegetableButton.clicked(pt):
			instructions.undraw()
			animalButton.remove()
			mineralButton.remove()
			vegetableButton.remove()
			otherButton.remove()
			nextQ = True

		elif otherButton.clicked(pt):
			instructions.undraw()
			animalButton.remove()
			mineralButton.remove()
			vegetableButton.remove()
			otherButton.remove()
			nextQ = True


	qCount = 1

	while qCount < 20:
		ans = nextQuestion(win, " ___ ")
		qCount += 1

	win.close()


q20()




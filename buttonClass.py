from graphics import *


class Button:
	"""This class creates functioning buttons."""

	def __init__(self, win, center, width, height, label):
		"""Initializing the parameters and creating the button box."""
		self.xMin = center.getX() - width / 2
		self.xMax = center.getX() + width / 2
		self.yMin = center.getY() - height / 2
		self.yMax = center.getY() + height / 2
		pt1 = Point(self.xMin, self.yMin)
		pt2 = Point(self.xMax, self.yMax)
		self.outline = Rectangle(pt1, pt2)
		self.outline.setFill('lightgray')
		self.outline.draw(win)
		self.label = Text(center, label)
		self.label.draw(win)
		# All buttons start off deactivated.
		self.deactivate()
		self.setLabel(label)


	def activate(self):
		"""This will activate the button object to which it is called."""
		self.label.setFill('black')
		self.outline.setWidth(2)
		self.active = True

	def deactivate(self):
		"""This will deactivate the button object to which it is called."""
		self.label.setFill('darkgrey')
		self.outline.setWidth(1)
		self.active = False

	def clicked(self, pt):
		"""This checks whether the point clicked is located somewhere within the button shape."""
		wasClicked = False
		if self.xMin <= pt.getX() and self.xMax >= pt.getX():
		    if self.yMin <= pt.getY() and self.yMax >= pt.getY():
		        if self.active == True:
		            wasClicked = True
		return wasClicked

	def remove(self):
		self.outline.undraw()
		self.label.undraw()
		self.active = False

	def setLabel(self, l):
		"""An easy way to change the label of a button. This enables you to rename a button rather than having to undraw and redraw a button."""
		self.label.setText(l)
		

	def getLabel(self):
		"""This will return the text of the button label."""
		return self.label.getText()


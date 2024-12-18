import graphics as gf
from random import randint

win = gf.GraphWin("Minha Janela", 400, 350)
circle = gf.Circle(gf.Point(100, 150), 10)
colors = ["red", "blue", "green", "orange", "yellow", "black"]
circle.setFill("red")
circle.draw(win)

while True:
    mouse = win.getMouse()
    new_circle = gf.Circle(mouse, 10)
    color = randint(0, len(colors)-1)
    new_circle = gf.setFill(colors[color])
    new_circle.draw(win)
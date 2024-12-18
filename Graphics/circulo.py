import graphics as gf

def main():
    win = gf.GraphWin( "Minha Janela", 400, 350)
    c = gf.Circle(gf.Point(200, 150), 10)
    c.draw(win)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
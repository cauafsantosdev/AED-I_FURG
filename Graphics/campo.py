import graphics as gf

def main():
    win = gf.GraphWin("Beira-Rio", 1000, 667)
    campo = gf.Rectangle(gf.Point(50, 50), gf.Point(950, 617))
    campo.draw(win)
    circulo = gf.Circle(gf.Point(500, 333), 80)
    circulo.draw(win)
    meiocampo = gf.Line(gf.Point(500, 50), gf.Point(500, 617))
    meiocampo.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
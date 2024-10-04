#Lab Week 5                       2/14/24
#Lab Section 2
#By Paige LaFave
#Goal: Prompt user for a side length, (x,y) coordinates, number of shapes, and space between shapes.
#       to then create the shape "hexadecagon" in a window however many times you inputed. 

def hexadecagonTurtle(s, x, y, nr, sr):
    import turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("#FFE5B4")
    t.color("darkmagenta")
    t.fillcolor("lightcyan")
    for _ in range(nr):
        x = x + sr
        t.teleport(x,y)
        t.begin_fill()
        for _ in range(16): 
            t.forward(s)
            t.left(22.5)
        t.end_fill()    
    wn.exitonclick() #close window

def main(): 
    s = float(input("Please enter the length of your side: "))
    x = float(input("Please enter your x coordinate: "))
    y = float(input("Please enter your y coordinate: "))
    nr = int(input("Please enter the numer of hexadecagons you would like: "))
    sr = float(input("Please enter the amount of space you would like between shapes: "))
    hexadecagonTurtle(s, x, y, nr, sr)
    return s, x, y, nr, sr

if __name__ == "__main__":
    main()

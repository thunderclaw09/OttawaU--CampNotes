from turtle import *
from random import random
from time import sleep


def get_pixel_color(x, y):
    y = -y
    canvas = getcanvas()
    ids = canvas.find_overlapping(x, y, x, y)

    if ids:
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color:
            return color

    return "white"


class Maze (Turtle):
    def __init__(self):
        super(Maze, self).__init__()
        self.hideturtle()
        self.speed(0)

    def go(self):
        # goto corner
        self.up()
        self.goto(-150, -150)
        self.down()

        # draw perimeter
        for i in range(2):
            self.forward(300)
            self.left(90)
            self.forward(300-cell_width)
            self.up()
            self.forward(cell_width)
            self.down()
            self.left(90)

        # draw columns
        self.right(90)
        for x in range(cell_width-150, 150, cell_width):
            self.up()
            self.goto(x, 150)
            self.down()
            for y in range(cell_width, 301, cell_width):
                if random() > col_density:
                    self.up()
                self.forward(cell_width)
                self.down()

        # draw rows
        self.left(90)
        for y in range(cell_width - 150, 150, cell_width):
            self.up()
            self.goto(-150, y)
            self.down()
            for x in range(cell_width, 301, cell_width):
                if random() > row_density:
                    self.up()
                self.forward(cell_width)
                self.down()


class Solver (Turtle):
    def __init__(self):
        super(Solver, self).__init__()
        self.color((0, 1, 0))
        self.shape('turtle')
        self.shapesize(cell_width/50)

        # I added this
        self.angle = 0
        self.isObstacleRight = False
        self.isObstacleLeft = False
        self.isObstacleUp = False
        self.isObstacleDown = False

        self.sides = [self.isObstacleRight, self.isObstacleLeft, self.isObstacleUp, self.isObstacleDown]
        self.wayOut = None

    def start(self):
        self.up()
        self.goto(-150-cell_width/2, -150+cell_width/2)
        self.down()

    def is_winning(self):
        return get_pixel_color(150 + cell_width/2, 150 - cell_width/2) != 'white'

    

    def go(self):
        # YOUR CODE HERE
        

        if self.angle >= 360:
            self.angle = self.angle - 360
            print("Angle reset.")
        
        # Checks for obstacles
        if (get_pixel_color(self.xcor() + cell_width/2, self.ycor()) == 'black'):
            self.isObstacleRight = True
        else: 
            self.isObstacleRight = False

        if (get_pixel_color(self.xcor(), self.ycor() - cell_width/2) == 'black'):
            self.isObstacleDown = True
        else:
            self.isObstacleDown = False

        if (get_pixel_color(self.xcor() - cell_width/2, self.ycor()) == 'black'):
            self.isObstacleLeft = True
        else:
            self.isObstacleLeft = False

        if (get_pixel_color(self.xcor(), self.ycor() + cell_width/2) == 'black'):
            self.isObstacleUp = True
        else:
            self.isObstacleUp = False

        self.sides = [self.isObstacleRight, self.isObstacleLeft, self.isObstacleUp, self.isObstacleDown]
        for i in range(len(self.sides)):
            if self.sides[i] == False:
                self.wayOut = i # Remember, you don't want to go the way back you came
                print("way out:", i)
                self.sides
                break

        if self.wayOut == 0: # right # maybe find the index of it?
            self.forward(cell_width)
            sleep(1)
        elif self.wayOut == 1: # left
            self.backward(cell_width)
            sleep(1)
        elif self.wayOut == 2: # up
            self.left(90)
            self.forward(cell_width)
            self.right(90)
            sleep(1)
        elif self.wayOut == 3: # down
            self.right(90)
            self.forward(cell_width)
            self.left(90)
            sleep(1)
        else:
            print("weird direction", self.wayOut)

        


        
        
        


        # if self.angle == 0:
        #     if (not self.isObstacleRight):
        #         self.forward(cell_width)
        #         sleep(1)
        #     else:
        #         self.right(90)
        #         self.angle += 90
        #         sleep(1)

        # elif self.angle == 90: # facing down
        #     if (not self.isObstacleDown):
        #         self.forward(cell_width)
        #         sleep(1)
        #     else:
        #         self.right(90)
        #         self.angle += 90
        #         sleep(1)

        # elif self.angle == 180:
        #     if (not self.isObstacleLeft):
        #         self.forward(cell_width)
        #         sleep(1)
        #     else:
        #         self.right(90)
        #         self.angle += 90
        #         sleep(1)

        # elif self.angle == 270:
        #     if (not self.isObstacleUp):
        #         self.forward(cell_width)
        #         sleep(1)
        #     else:
        #         self.right(90)
        #         self.angle += 90
        #         sleep(1)
        # else:
        #     print("weird angle")
        
        # # self.goto(150 + cell_width/2, 150 - cell_width/2)


cell_width = 100
col_density = .3
row_density = .3


while True:
    screen = Screen()
    screen.clear()

    maze = Maze()
    maze.go()

    solver = Solver()
    solver.start()

    while not solver.is_winning():
        solver.go()

    sleep(1)

######################333
# MAN WHY IS THIS SO BROKEN
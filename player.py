from graphics import *


class Player:
    def __init__(self):
        self._radius = 20
        self._facing = "North"
        self.xPos = 250
        self.yPos = 250

    @property
    def position(self):
        return

    @property
    def radius(self):
        return self._radius

    @property
    def facing(self):
        return self._facing

    @property
    def getPlayerToDraw(self):
        centre = Point(self.xPos, self.yPos)
        facer = self.getFacer(centre)
        circle = Circle(centre, self.radius)

        return [circle, facer]

    def getFacer(self, centre: Point):
        end = centre.clone()
        match self.facing:
            case "North":
                end.y = end.y - self.radius
            case "South":
                end.y = end.y + self.radius
            case "East":
                end.x = end.x - self.radius
            case "West":
                end.x = end.x + self.radius
        line = Line(end, centre )
        line.setFill("Red")
        return line

    def react(self, key):
        match key:
            case "Up" | "Down":
                self.move(key)
            case "Left" | "Right":
                self.turn(key)
            case _:
                print("pressed: ",key)

    def move(self, key):
        match key:
            case "Up":
                match self.facing:
                    case "North":
                        self.yPos -= 2*self.radius
                    case "South":
                        self.yPos += 2*self.radius
                    case "East":
                        self.xPos -= 2*self.radius
                    case "West":
                        self.xPos += 2*self.radius
            case "Down":
                match self.facing:
                    case "North":
                        self.yPos += 2*self.radius
                    case "South":
                        self.yPos -= 2*self.radius
                    case "East":
                        self.xPos += 2*self.radius
                    case "West":
                        self.xPos -= 2*self.radius

    def turn(self, key):
        match key:
            case "Left":
                match self._facing:
                    case "North":
                        self._facing = "East"
                    case "South":
                        self._facing = "West"
                    case "East":
                        self._facing = "South"
                    case "West":
                        self._facing = "North"
            case "Right":
                match self._facing:
                    case "North":
                        self._facing = "West"
                    case "South":
                        self._facing = "East"
                    case "East":
                        self._facing = "North"
                    case "West":
                        self._facing = "South"

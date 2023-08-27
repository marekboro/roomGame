class Player:
    def __init__(self):
        self._radius = 5
        self._facing = "North"
        self.xPos = 250
        self.yPos = 250
        
    @property
    def position(self):
        return 
    @property
    def radius(self):
        return self.radius
    
    @property
    def facing(self):
        return self._facing
    
    def react(self,key):
        match key:
            case "Up" | "Down":
                self.move(key)
            case _:
                self.turn(key)
                
    def move(self,key):
        match key:
            case "Up":
                match self.facing:
                    case "North":
                        self.yPos += self.radius
                    case "South":
                        self.yPos -= self.radius
                    case "East":
                        self.xPos -= self.radius
                    case "West":
                        self.xPos += self.radius
            case "Down":
                match self.facing:
                    case "North":
                        self.yPos -= self.radius
                    case "South":
                        self.yPos += self.radius
                    case "East":
                        self.xPos += self.radius
                    case "West":
                        self.xPos -= self.radius
    
    def turn(self,key):
        match key:
            case "Left":
                match self.facing:
                    case "North":
                        self.facing = "West"
                    case "South":
                        self.facing = "East"
                    case "East":
                        self.facing = "North"
                    case "West":
                        self.facing = "South"
            case "Right":
                # match self.facing:
                #     case "North":
                #         self.facing = "West"
                #     case "South":
                #         self.facing = "East"
                #     case "East":
                #         self.facing = "North"
                #     case "West":
                #         self.facing = "South"
                ...



  
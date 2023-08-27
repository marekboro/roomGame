from graphics import *
from room import *
from player import *

room:Room
roomWindow: GraphWin

def main():
    createRoom()
    drawARoom()
    drawAPlayer()
    
        
def createRoom():
    global room
    room = Room()


def drawAPlayer():
    
   
    
    # room = roomWindow
    playerLocation = getStartingLocation(room)
    drawPlayer(playerLocation)
    
    ...

def getStartingLocation(room):
    return getCentreOfRoom(room)
    
def drawPlayer():
    ...
        
def getCentreOfRoom(room):
    ...  
  
def drawARoom():
    global room
    global roomWindow
    roomWindow = GraphWin(room.getName, *room.dimensions)
    roomWindow.setBackground(room.background) 
    key = ""
    while key != "q":
       key = handleUserKeys()
        
    roomWindow.close()
    
def handleUserKeys():
    global roomWindow
    key = roomWindow.getKey()
    print(key)
    match key:
        case "Up":
            print("going UP")
        case "Left":
            print("going LEFT")
        case "Right":
            print("going RIGHT")
        case "Down":
            print("going DOWN")
    
    return key
    
      
    
    # for element in gameScreen:
    #     element.draw(roomWindow)


if __name__=="__main__":
    main()
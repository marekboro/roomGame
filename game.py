from graphics import *
from room import *
from player import *

room: Room
roomWindow: GraphWin
player: Player


def main():
    createRoom()
    createPlayer()
    drawARoom()
    drawPlayer()


def createRoom():
    global room
    room = Room()


def createPlayer():
    global player
    player = Player()


# def drawPlayer():
#     global roomWindow
#     global player
#     playerToDraw = player.getPlayerToDraw()
#     for element in playerToDraw:
#         element.draw(roomWindow)


def getStartingLocation(room):
    return getCentreOfRoom(room)


def getCentreOfRoom(room):
    ...


def drawARoom():
    global room
    global roomWindow
    global player
    updatedPlayerDrawElements:list =[]
    roomWindow = GraphWin(room.getName, *room.dimensions)
    roomWindow.setBackground(room.background)
   
    key = ""
    while key != "q":
        for element in updatedPlayerDrawElements:
            element.undraw()
        updatedPlayerDrawElements=[*player.getPlayerToDraw]
        for element in updatedPlayerDrawElements:
            element.draw(roomWindow)
        key = handleUserKeys(player)
        
    roomWindow.close()


def handleUserKeys(player: Player):
    global roomWindow
    key = roomWindow.getKey()
    player.react(key)
    
    match key:
        case "Up":
            print("going forward")
        case "Left":
            print("turning left")
        case "Right":
            print("turning right")
        case "Down":
            print("going back")

    return key

if __name__ == "__main__":
    main()

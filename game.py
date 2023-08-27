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
    roomWindow = GraphWin(room.getName, *room.dimensions)
    roomWindow.setBackground(room.background)
    # playerToDraw = player.getPlayerToDraw
    # for element in playerToDraw:
    #     element.draw(roomWindow)
    key = ""
    while key != "q":
        playerToDraw = player.getPlayerToDraw
        for element in playerToDraw:
            element.draw(roomWindow)
        key = handleUserKeys(player)

    roomWindow.close()


def handleUserKeys(player: Player):
    global roomWindow
    key = roomWindow.getKey()
    player.react(key)
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


if __name__ == "__main__":
    main()

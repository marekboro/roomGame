class Room:
    def __init__(self):
        self._height = 500
        self._width = 500
        self._name = "Room"
        self._background = "White"
        
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
    @property
    def dimensions(self):
        return self._width, self._height
    
    @property
    def getName(self):
        return self._name
    
    @property
    def background(self):
        return self._background
    
    
class Taxicab:
    
    
    def __init__(self, x, y):
        
        self._x_coord = x
        self._y_coord = y
        self._odometer = 0
    
    def get_x_coord(self):
        
        return self._x_coord
    
    def get_y_coord(self):
        
        return self._y_coord
    
    def get_odometer(self):
        
        return self._odometer
    
    def move_x(self, distance):
        
        self._x_coord += distance
        self._odometer += abs(distance)
    
    def move_y(self, distance):
        
        self._y_coord += distance
        self._odometer += abs(distance)


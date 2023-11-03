class Taxicab:
    

    def __init__(self, x, y):
        
        self.__x = x
        self.__y = y
        self.__odometer = 0
    
    def get_x_coord(self):
        
        return self.__x
    
    def get_y_coord(self):
        
        return self.__y
    
    def get_odometer(self):
        
        return self.__odometer
    
    def move_x(self, dx):
        
        self.__x += dx
        self.__odometer += abs(dx)
    
    def move_y(self, dy):
      
        self.__y += dy
        self.__odometer += abs(dy)


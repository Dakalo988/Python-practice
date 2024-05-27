# _ one underscore public
# __Private

class Speed:
    def __init__(self): 
        self.speed = 10
        self.__new_speed =100
        
    def get_new_speed(self)
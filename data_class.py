class Data():
    x_cord = 0
    y_cord = 0
    time = 0

    def __init__(self,x_cord, y_cord, time):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.time = time
    
    def get_x(self):
        return self.x_cord

    def get_y(self):
        return self.y_cord

    def get_time(self):
        return self.time

class Biker:
    def __init__(self, x, y, img_file):
        self.x = y
        self.y = y
        self.img_file = img_file
    
    def move_right(self):
        self.x += 5
    def move_left(self):
        self.x -= 5
    def move_down(self):
        self.y -= 5
    def move_up(self):
        self.y += 5
        
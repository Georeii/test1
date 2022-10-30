class Point():

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def add_y(self,addy):
        self.y += addy
    def add_x(self,addx):
        self.x += addx

    def print_x_y(self):
        print(self.x,self.y)


poit = Point("сторока")
poit.print_x_y()
poit.add_y(12)
poit.print_x_y()
poit.add_x(14)
poit.print_x_y()
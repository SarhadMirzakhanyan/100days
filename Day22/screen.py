import turtle

CANVAS_HEIGTH = 600
CANVAS_WIDTH = 1000

class Screen():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        #tk_canvas = self.screen.getcanvas()
        self.screen.setup(width=1000,height=600)
        self.screen.screensize(980,580)

        self.screen.tracer(0)
        self.screen.listen()
        self.screen.delay(3)
    
    def get_screen(self):
        return self.screen


if __name__ == "__main__":
    screen = Screen()
    my_screen  = screen.get_screen()
    my_screen.bgcolor("orange")
    my_screen.exitonclick()


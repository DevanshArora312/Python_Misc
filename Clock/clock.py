import turtle as tr
import time as tm
try:
    tr.Screen()
    tr.tracer(0)
    class spoke():
        def __init__(self,x,y,ang):
            self.x=x
            self.y=y
            self.ang=ang
        def draw(self):
            tr.pu()
            tr.goto(self.x,self.y)
            tr.setheading(self.ang)
            tr.fd(85)
            tr.pd()
            
            tr.fd(25)

    class hand():
        def __init__(self,l,ut):
            self.l=l
            self.ut=ut
        def draw(self):
            tr.ht()
            tr.pu()
            tr.goto(0,15)
            tr.pd()
            if self.ut==1:
                z=5
                n=6
                tr.pensize(5)
                tr.pencolor("yellow")
            elif self.ut==2:
                z=4
                n=6
                tr.pensize(5)
                tr.pencolor("orange")
            elif self.ut==3:
                z=3
                n=30
                tr.pensize(5)
                tr.pencolor("red")
            a=tm.localtime()[z]*n
            tr.setheading(90-a)
            tr.fd(self.l)
            tr.pensize(1)
            tr.pencolor("black")
    def draw_main():
        tr.pu()
        tr.goto(0,-100)
        tr.pd()
        for i in range(770):
            tr.pencolor("cyan")
            tr.pensize(10)
            tr.fd(1)
            tr.left(0.5)
            tr.pensize(1)
            tr.pencolor("black")
            
        for i in range(0,361,30):
            sp=spoke(0,15,i)
            tr.pencolor("lime")
            tr.pensize(5)
            sp.draw()
            tr.pensize(1)
            tr.pencolor("black")

        tr.fillcolor("Black")
        tr.begin_fill()    
        for i in range(360):
            tr.pu()
            tr.goto(0,15)
            tr.pd()
            tr.fd(1.5)
            tr.right(1)
        tr.end_fill()
    hand1=hand(70,1)
    hand2=hand(65,2)
    hand3=hand(50,3)
    while True:
        tr.ht()

        tr.reset()
        draw_main()
        hand1.draw()
        hand2.draw()
        hand3.draw()
        tr.update()

except tr.Terminator:
    exit

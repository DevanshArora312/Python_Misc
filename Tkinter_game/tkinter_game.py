from tkinter import *
import pygame
import sys

t=Tk()
t.geometry("150x150")
t.resizable(0,0)

def ifquits():
    pygame.quit()
    t.destroy()
    sys.exit()
    #exit()
class grass():
    def __init__(self,x,y,h):
        self.x=x
        self.y=y
        self.h=h
    def make(self):
        for i in range(self.h):
            pygame.draw.polygon(win,("Dark Green"),[(self.x,self.y),(self.x+15,self.y-15),(self.x+30,self.y)])
            self.x+=30
class sky():
    def __init__(self,x,y,h):
        self.x=x
        self.y=y
        self.h=h
    def make(self):
        pygame.draw.rect(win,("Sky Blue"),(self.x,self.y,500,self.h))
class cloud():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def make(self):
        pygame.draw.rect(win,("White"),(self.x,self.y,30,20))
        pygame.draw.rect(win,("White"),(self.x+20,self.y+10,30,20))
        pygame.draw.rect(win,("White"),(self.x+40,self.y,30,20))
#t.geometry("250x250")
def pipe(x1,y1,x2):
    pygame.draw.rect(win,(0,255,0),(x1,y1,30,50))
    y2=y1+25//2
    pygame.draw.rect(win,(0,255,0),(x1,y2,500,30))
    pygame.draw.rect(win,(0,255,0),(x2,y1,30,50))

def ground(x,y):
    pygame.draw.rect(win,(138,54,15),(x,y,500,40))

def ladder(x,y,h,n):
    pygame.draw.rect(win,(152,102,31),(x,y,5,h))
    pygame.draw.rect(win,(152,102,31),(x+20,y,5,h))
    #n=5
    x1=x
    y1=y+10
    for i in range(n):
        pygame.draw.rect(win,(152,102,31),(x1,y1,20,5))
        y1+=15

def goal():
    pygame.draw.circle(win,("Purple"),(470,440),20)


win=pygame.display.set_mode((500,500),pygame.NOFRAME)
win.fill((0,0,0))
class shit():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        win.fill((0,0,0))
        sky(0,0,500).make()
        grass(0,460,20).make()
        cloud(10,10).make()
        cloud(170,30).make()
        cloud(370,10).make()
        cloud(10,190).make()
        cloud(250,220).make()
        cloud(330,310).make()
        pipe(0,100,470)
        pipe(0,350,470)
        ground(0,460)
        ground(0,250)
        ladder(70,100,215,13)
        ladder(350,240,170,11)
        ladder(90,340,140,9)
        pygame.draw.rect(win,(255,0,0),(self.x,self.y,10,10))
        if self.x>470:
            self.x=470
        if self.y<20:
            self.y=20
        if self.y>450:
            self.y=450
        if self.x<20:
            self.x=20
        if self.x>=470 and self.y>=440:
            print("You win!")
            t.destroy()
            pygame.quit()
            sys.exit()
        #if self.x

        goal()
        pygame.display.update()
        
    def down(self):
        self.y+=10
        B= self.x>370 or self.x<350
        C= self.x>90 or self.x<70
        if not B:
            if self.y>352 and self.y<375:
                self.y=352
        if not C:
            if self.y>240 and self.y<270:
                self.y=240
        if self.y>450:
            self.y=450
        if self.x not in range(90,110) and self.y>352 and self.x not in range(350,370) and self.y in range(250,370):
            self.y=352
        if self.x not in range(70,90) and self.y>240 and self.x not in range(350,370) and self.y in range(110,260):
            self.y=240
        if C and self.y > 102 and self.y<120:
            self.y=102
        shit.draw(self)
        
    def up(self):
        self.y-=10
        A= self.x>110 or self.x<90
        B= self.x>370 or self.x<350
        C= self.x>90 or self.x<70
        if not A:
            if self.y<352 and self.y>340 :
                self.y=352
        if not B:
            if self.y<240:
                self.y=240
        if B and C and self.y in range(100,249):
            self.y=240
        if not C:
            if self.y<100:
                self.y=100
        if C and self.y in range(0,100):
            self.y=100
        if self.y in range(350,450) and A :
            self.y=450
        if B  and A and self.y in range(260,349):
            self.y=352
        shit.draw(self)
        
    def lt(self):
        self.x-=10
        if self.y in range(360,449) and self.x>110 :
            self.x-=10
                
        if self.y in range(360,449) and self.x<90 :
            self.x+=10
        if self.y in range(260,349) and self.x>370 :
            self.x-=10
        if self.y in range(260,349) and self.x<350 :
            self.x+=10
        if self.y in range(110,240) and self.x>90 :
            self.x-=10
        if self.y in range(110,240) and self.x<70 :
            self.x+=10
        shit.draw(self)
    def rt(self):
        self.x+=10
        if self.y in range(360,449) and self.x>110 :
            self.x-=10
        if self.y in range(360,449) and self.x<90 :
            self.x+=10
        if self.y in range(260,349) and self.x>370 :
            self.x-=10
        if self.y in range(260,349) and self.x<350 :
            self.x+=10
        if self.y in range(110,240) and self.x>90 :
            self.x-=10
        if self.y in range(110,240) and self.x<70 :
            self.x+=10
        
        #print(self.y)
        shit.draw(self)

box=shit(150,240)##50,102
box.draw()

Button(t,text="Down",command=box.down,bg="black",fg="lime").pack()
Button(t,text="Right",command=box.rt,bg="black",fg="lime").pack()
Button(t,text="Left",command=box.lt,bg="black",fg="lime").pack()
Button(t,text="Up",command=box.up,bg="black",fg="lime").pack()
Button(t,text="Quit",command=ifquits,bg="black",fg="lime").pack()

t.mainloop()

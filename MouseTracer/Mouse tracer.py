import turtle as t
import pyautogui as p
import time
import ctypes

#t.screensize(1920,1080)
t.setup(width=1.0,height=1.0)
t.tracer(0)
c=0

def go():
    p.click(1290,13)

    z=[t.xcor(),t.ycor()]
    p.click(z[0]+671,z[1]+368)
    t.update()
    
t.title("Vellapanti")

def DetectClick(button):
    #Waits watchtime seconds. Returns True on click, False otherwise
    if button in (1, '1', 'l', 'L', 'left', 'Left', 'LEFT'):
        bnum = 0x01
    while 1:
        if ctypes.windll.user32.GetKeyState(bnum) not in [0, 1]:#Net se chepa h ye pura function
            # ^ this returns either 0 or 1 when button is not being held down
            return True
        else:
            return False

go()
q=None

while True:
    t.update()
    
    if not DetectClick("left"):
        q=p.position()
        q=list(q)
        q[0]-=671
        q[1]-=368
        try:
            for i in range(2):
                q[i]-=x_old[i]
        except:
            #q[1]+=820
            pass
        
    if DetectClick("left"):
        z=[t.xcor(),t.ycor()]
        x=p.position()
        x=list(x)
        x[0]-=671
        x[1]-=368

            
        if c==0:
            p.click(671,368)
            #p.dragTo(z[0]+635,z[1]+410,1,button="left")
            z=[t.xcor(),t.ycor()]
            k=[z[0]+x[0],z[1]-x[1]]
            t.pu()
            t.goto(k)
            t.pd()
            c+=1
        else:
            if q is not None:
                d=[z[0]+q[0],z[1]-q[1]]
                t.pu()
                t.goto(d)
                t.pd()
                q=None
            n=[x[0]-x_old[0],x[1]-x_old[1]]
            k=[z[0]+n[0],(z[1]-n[1])]
            t.goto(k)
        x_old=x.copy()
        t.update()

'''
while True:
    
    if c==0:
        
        k=[z[0]+x[0],z[1]+x[1]]
        t.goto(k)
        c+=1
    else:
        
        n=[x[0]-x_old[0],x[1]-x_old[1]]
        k=[z[0]+n[0],(z[1]-n[1])]
        t.goto(k)
    x_old=x.copy()
    t.update()
'''

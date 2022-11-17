import random
import tkinter as t
import time
l=[['','',''],['','',''],['','','']]
s=[[True,True,True],[True,True,True],[True,True,True]]

tk=t.Tk()

###########################################################
"""
Trust me , you don't want to read this. Go ahead if you love getting strokes.
"""

def think():
    Bool_Val=False
    for i in range(3):
        for j in range(3):
            if i==j==1:
                pass
            Bool_Val+=s[i][j]
    """
                Computer trying to win
    """
    for i in range(3):
        if l[i][0]==l[i][1]=="X":
            if s[i][2]:
                l[i][2]="X"
                s[i][2]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=2,row=i)
                return 0
        elif l[0][i]==l[1][i]=="X":
            if s[2][i]:
                l[2][i]="X"
                s[2][i]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=i,row=2)
                return 0
        elif l[i][0]==l[i][2]=="X":
            if s[i][1]:
                l[i][1]="X"
                s[i][1]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=i)
                return 0
        elif l[0][i]==l[2][i]=="X":
            if s[1][i]:
                l[1][i]="X"
                s[1][i]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=i,row=1)
                return 0
        elif l[i][1]==l[i][2]=="X":
            if s[i][0]:
                l[i][0]="X"
                s[i][0]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=0,row=i)
                return 0
        elif l[1][i]==l[2][i]=="X":
            if s[0][i]:
                l[0][i]="X"
                s[0][i]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=i,row=0)
                return 0
    ########
    if l[0][0]==l[1][1]=="X":
        if s[2][2]:
            l[2][2]="X"
            s[2][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=2,row=2)
            return 0
    elif l[1][1]==l[2][2]=="X":
        if s[0][0]:
            l[0][0]="X"
            s[0][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=0,row=0)
            return 0
    elif l[0][0]==l[2][2]=="X":
        if s[1][1]:
            l[1][1]="X"
            s[1][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=1)
            return 0
    elif l[0][2]==l[2][0]=="X":
        if s[1][1]:
            l[1][1]="X"
            s[1][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=1)
            return 0
    elif l[0][2]==l[1][1]=="X":
        if s[2][0]:
            l[2][0]="X"
            s[2][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=0,row=2)
            return 0
    elif l[1][1]==l[2][0]=="X":
        if s[0][2]:
            l[0][2]="X"
            s[0][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=2,row=0)
            return 0
    ####################################################################################
    """
                Computer Blocking you
    """
    for i in range(3):
        if l[i][0]==l[i][1]=="O":
            if s[i][2]:
                l[i][2]="X"
                s[i][2]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=2,row=i)
                return 0
        if l[0][i]==l[1][i]=="O":
            
            if s[2][i]:
                l[2][i]="X"
                s[2][i]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=i,row=2)
                return 0
        if l[i][0]==l[i][2]=="O":
            
            if s[i][1]:
                l[i][1]="X"
                s[i][1]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=i)
                return 0
        if l[0][i]==l[2][i]=="O":
            if s[1][i]:
                l[1][i]="X"
                s[1][i]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=i,row=1)
                return 0
        if l[i][1]==l[i][2]=="O":
            if s[i][0]:
                l[i][0]="X"
                s[i][0]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=0,row=i)
                return 0
        if l[1][i]==l[2][i]=="O":
            if s[0][i]:
                l[0][i]="X"
                s[0][i]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=i,row=0)
                return 0
    ########
    if l[0][0]==l[1][1]=="O":
        if s[2][2]:
            l[2][2]="X"
            s[2][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=2,row=2)
            return 0
    if l[1][1]==l[2][2]=="O":
        if s[0][0]:
            l[0][0]="X"
            s[0][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=0,row=0)
            return 0
    if l[0][0]==l[2][2]=="O":
        if s[1][1]:
            l[1][1]="X"
            s[1][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=1)
            return 0
    if l[0][2]==l[2][0]=="O":
        if s[1][1]:
            l[1][1]="X"
            s[1][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=1)
            return 0
    if l[0][2]==l[1][1]=="O":
        if s[2][0]:
            l[2][0]="X"
            s[2][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=0,row=2)
            return 0
    if l[1][1]==l[2][0]=="O":
        if s[0][2]:
            l[0][2]="X"
            s[0][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=2,row=0)
            return 0
    ################################################################################
    """
                    Trick Breaker
    """
    if (l[0][0]==l[2][2]=="O" or l[0][2]==l[2][0]=="O") and l[1][1]=="X":
        if s[0][1]:
            l[0][1]="X"
            s[0][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=0)
            return 0
        if s[1][0]:
            l[1][0]="X"
            s[1][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=1,column=0)
            return 0
        if s[2][1]:
            l[2][1]="X"
            s[2][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=2,column=1)
            return 0
        if s[1][2]:
            l[1][2]="X"
            s[1][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=1,column=2)
            return 0
        else:
            pass
        
    if l[1][1]=="O" and Bool_Val:
        if s[0][2]:
            l[0][2]="X"
            s[0][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=0,column=2)
            return 0

    if l[2][0]==l[1][1]=="O" and l[0][2]=="X" :
        if s[0][0]:
            l[0][0]="X"
            s[0][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=0,column=0)
            return 0
    if l[0][1]==l[1][2]=="O" :
        if s[0][2]:
            l[0][2]="X"
            s[0][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=0,column=2)
            return 0
    if l[0][1]==l[1][0]=="O" :
        if s[0][0]:
            l[0][0]="X"
            s[0][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=0,column=0)
            return 0
    if l[2][1]==l[1][0]=="O" :
        if s[2][0]:
            l[2][0]="X"
            s[2][0]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=2,column=0)
            return 0
    if l[2][1]==l[1][2]=="O" :
        if s[2][2]:
            l[2][2]="X"
            s[2][2]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(row=2,column=2)
            return 0

    ################################################################################
    """
                Random move
    """
    if s[1][1]==True:
        if s[1][1]:
            l[1][1]="X"
            s[1][1]=False
            t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=1,row=1)
            return 0
    else:
        while True:
            p,q=random.randint(0,2),random.randint(0,2)
            if s[p][q]:
                l[p][q]="X"
                s[p][q]=False
                t.Label(tk,text="X",padx=varpadx+4,pady=varpady+4).grid(column=q,row=p)
                return 0
       
############################################################




def win_check():
   if l[0][0]==l[0][1]==l[0][2]=="O":
       #print("You win!")
       return False
   elif l[1][0]==l[1][1]==l[1][2]=="O":
       #print("You win!")
       return False
   elif l[2][0]==l[2][1]==l[2][2]=="O":
       #print("You win!")
       return False
   elif l[0][0]==l[1][0]==l[2][0]=="O":
       #print("You win!")
       return False
   elif l[0][1]==l[1][1]==l[2][1]=="O":
       #print("You win!")
       return False
   elif l[0][2]==l[1][2]==l[2][2]=="O":
       #print("You win!")
       return False
   elif l[0][0]==l[1][1]==l[2][2]=="O":
       #print("You win!")
       return False
   elif l[0][2]==l[1][1]==l[2][0]=="O":
       #print("You win!")
       return False
   else:
       return True

def lose_check():
    if l[0][0]==l[0][1]==l[0][2]=="X":
       #print("You Lose!")
       return False
    elif l[1][0]==l[1][1]==l[1][2]=="X":
       #print("You Lose!")
       return False
    elif l[2][0]==l[2][1]==l[2][2]=="X":
       #print("You Lose!")
       return False
    elif l[0][0]==l[1][0]==l[2][0]=="X":
       #print("You Lose!")
       return False
    elif l[0][1]==l[1][1]==l[2][1]=="X":
       #print("You Lose!")
       return False
    elif l[0][2]==l[1][2]==l[2][2]=="X":
       #print("You Lose!")
       return False
    elif l[0][0]==l[1][1]==l[2][2]=="X":
       #print("You Lose!")
       return False
    elif l[0][2]==l[1][1]==l[2][0]=="X":
       #print("You Lose!")
       return False
    else:
        return True
def fin_check():
    run=False
    for i in s:
        for j in i:
            if j==True:
                run=True
                return run
    return run

def end_check():
    win_val=win_check()
    lose_val=lose_check()
    fin_val=fin_check()
    if win_val==False:
        for i in range(3):
            for j in range(3):
                if s[i][j]==True:
                    t.Label(tk,text="",padx=varpadx+4,pady=varpady+4).grid(column=j,row=i)
        time.sleep(1.5)
        #tk.destroy()
        tk_temp=t.Tk()
        t.Label(tk_temp,text="You Win!!",bg="black",fg="white",font=("Arial",30)).pack()
        tk_temp.mainloop()

    if lose_val==False:
        #print(s)
        for i in range(3):
            for j in range(3):
                if s[i][j]==True:
                    t.Label(tk,text="",padx=varpadx+4,pady=varpady+4).grid(column=j,row=i)
        time.sleep(1.5)
        #tk.destroy()
        tk_temp=t.Tk()
        t.Label(tk_temp,text="You Lose!!",bg="black",fg="white",font=("Arial",30)).pack()
        tk_temp.mainloop()
        
    if lose_val==win_val==True and fin_val==False:
        time.sleep(1.5)
        #tk.destroy()
        tk_temp=t.Tk()
        t.Label(tk_temp,text="It's a Draw!!",bg="black",fg="white",font=("Arial",30)).pack()
        tk_temp.mainloop()

def main():
    global varpadx
    global varpady
    varpadx=20
    varpady=10
    class but():
        def __init__(self,x,y):
            self.x=x
            self.y=y
        
        def make(self):
            win_val=""
            
            def sel():
                global win_val
                global self_coords
                info=btn.grid_info()
                self_coords=[info["row"],info["column"]]
                t.Label(tk,text="O",padx=varpadx+2,pady=varpady+2).grid(column=info["column"],row=info["row"])
                btn.destroy()
                s[info["row"]][info["column"]]=False
                l[info["row"]][info["column"]]="O"
                #print(s,"\n\n",l)
                end_check()
                think()
                end_check()
            btn=t.Button(tk,text="",command=sel,padx=varpadx,pady=varpady)
            btn.grid(column=self.x,row=self.y)
            #print(btn)
            
    b1=but(0,0)
    b2=but(0,1)
    b3=but(0,2)
    b4=but(1,0)
    b5=but(1,1)
    b6=but(1,2)
    b7=but(2,0)
    b8=but(2,1)
    b9=but(2,2)
    b_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

    for i in range(1,10):
        a=i%3-1
        b=i//3
        if i in [3,6,9]:
            b-=1
            a=2
        b_list[i-1].make()


try:
    main()

except :
    exit



t.mainloop()

from tkinter import *
t=Tk()
t.geometry("150x200")
t.resizable(0,0)

t.configure(bg="light blue")

def dels():
    tx.delete("end-2c")
def clear():
    tx.delete(1.0,"end")

def w_get(x):
    val=tx.get(1.0,"end-1c")
    if ">" in val:
        clear()
    if "+" in val or "-" in val or "*" in val or "/" in val:
        if x in ["+","-","*","/"]:
            tx.delete("end-2c")
    tx.insert(END,str(x))


def Ent():
    val=tx.get(1.0,"end-1c")
    try:
        val=val.lstrip("0")
        x=eval(val)
        tx.delete(1.0,"end")
        tx.insert(END,">>>{0}\n".format(val))
        tx.insert(END,x)
    except:
        tx.delete(1.0,"end")
        tx.insert(END,"Error")

#Entry(t,textvariable=a).place(x=0,y=0,height=40)
tx=Text(t,height=3,width=50,relief="groove",bg="light grey")
tx.place(x=0,y=0)
button_height=55
Button(t,text="1",bg="black",fg="lime",command=lambda:w_get(1),padx=10).place(x=0,y=button_height)
Button(t,text="2",bg="black",fg="lime",command=lambda:w_get(2),padx=10).place(x=35,y=button_height)
Button(t,text="3",bg="black",fg="lime",command=lambda:w_get(3),padx=10).place(x=65,y=button_height)
Button(t,text="4",bg="black",fg="lime",command=lambda:w_get(4),padx=10).place(x=0,y=button_height+30)
Button(t,text="5",bg="black",fg="lime",command=lambda:w_get(5),padx=10).place(x=35,y=button_height+30)
Button(t,text="6",bg="black",fg="lime",command=lambda:w_get(6),padx=10).place(x=65,y=button_height+30)
Button(t,text="7",bg="black",fg="lime",command=lambda:w_get(7),padx=10).place(x=0,y=button_height+60)
Button(t,text="8",bg="black",fg="lime",command=lambda:w_get(8),padx=10).place(x=35,y=button_height+60)
Button(t,text="9",bg="black",fg="lime",command=lambda:w_get(9),padx=10).place(x=65,y=button_height+60)
Button(t,text="Clear",bg="black",fg="lime",command=lambda:clear()).place(x=0,y=button_height+120)
Button(t,text="0",bg="black",fg="lime",command=lambda:w_get(0),padx=10).place(x=0,y=button_height+90)
Button(t,text="<-",bg="black",fg="lime",command=lambda:dels(),padx=6).place(x=80,y=button_height+120)
Button(t,text="Enter",bg="black",fg="lime",command=lambda:Ent()).place(x=40,y=button_height+120)
Button(t,text="+",bg="black",fg="lime",command=lambda:w_get("+"),padx=10).place(x=35,y=button_height+90)
Button(t,text="-",bg="black",fg="lime",command=lambda:w_get("-"),padx=10).place(x=65,y=button_height+90)
Button(t,text="*",bg="black",fg="lime",command=lambda:w_get("*"),padx=10).place(x=95,y=button_height)
Button(t,text="/",bg="black",fg="lime",command=lambda:w_get("/"),padx=10).place(x=95,y=button_height+30)
Button(t,text=".",bg="black",fg="lime",command=lambda:w_get("."),padx=10).place(x=95,y=button_height+60)


t.mainloop()

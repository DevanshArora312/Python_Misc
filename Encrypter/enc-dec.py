import tkinter as t
import random as r

key=[['a','b','c','d','e','f','.','+'],['g','h','i','j','k','l',',','_'],['m','n','o','p','q','r','/','>'],['s','t','u','v','w','x',':','<'],['y','z','1','2','3','4','-','?'],['5','6','7','8','9','0',')','`'],[' ','!','@','#','$','%','(','&'],['^','*','{','}','[',']','=',';']]
key2="abcdefghijklmnopqrstuvwxyz1234567890 `!@#$%^&*(){}[]:;?/+=><,.-_"
for i in key:
    print(i)
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

def DToB(n):
    count=0
    s=''
    no = str(bin(n).replace("0b", ""))
    for i in range(4-len(no)):
        count+=1
    for i in range(count):
        s+='0'
    s+=no
    return s

def btod(binary):
      
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return str(decimal)

def enc_bin(enc):
    fin=""
    fin1=""
    enc=str(enc)
    text1=""
    for i in enc:
        if i.isalpha():
            pass
        else:
            text1+=i
    enc=list(text1)
    for i in enc:
        x=int(i)
        new=DToB(x)
        fin+=new
    for i in fin:
        fin1+=i
        if r.randint(0,1):
            fin1+=key2[r.randint(0,25)]

    return fin1

def dec_bin(no):
    no1=""
    for i in no:
        if i.isalpha():
            pass
        else:
            no1+=i
    l=list(no1)
    new_l=[]
    for i in range(0,len(l),4):
        x=l[i]+l[i+1]+l[i+2]+l[i+3]
        new_l.append(x)
    for i in range(len(new_l)):
        x=new_l[i]
        x=list(x)
        hm=[]
        count=0
        for j in range(len(x)):
           if x[j]=="1":
               hm.append("1")
               count+=1
           elif count==0 and x[j]=="0":
               pass
           else:
               hm.append("0")
        x=""
        for q in hm:
            x+=q
        new_l[i]=x

    sl=[]
    for i in new_l:
        z=btod(int(i))
        sl.append(str(z))

    fin_str=""
    for i in sl:
        fin_str+=i

    #print(fin_str)

    return decrypt(fin_str)

    
               
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

def enc_alp(enc):
    enc=(str(enc)).lower()
    text1=""
    for i in enc:
        if i.isalpha():
            pass
        else:
            text1+=i
    new=""
    for i in text1:
        new+=key2[int(i)-1]
        q=r.randint(0,1)
        if q:
            new+=str(r.randint(0,9))

    return new

def dec_alp(dec):
    new=""
    dec=(str(dec)).lower()
    for i in dec:
        if i.isdigit():
            pass
        else:
            for j in range(len(key2)):
                if i==key2[j]:
                    new+=str(int(j)+1)

    #print(new)
    return decrypt(new)


def new_gen():
    z=key.copy()
    for i in range(len(z)):
        r.shuffle(z[i])

    r.shuffle(z)

    return z


'''
def tkE():
    t1=t.Toplevel()
    t1.geometry('200x200')
    t.Label(t1,text="Enter Text to Encrypt:").place(x=20,y=20)
    x=t.StringVar()
    t.Entry(t1,textvariable=x).place(x=70,y=20)
    def get():
        #global variable_x
        variable_x=x.get()
        con=enc_adv(encrypt(variable_x))
        t.Label(t1,text="The encrypted text is: {0}".format(con)).place(x=20,y=100)
    t.Button(t1,text="Submit",command=get,bg="lime",fg="brown").place(x=20,y=50)
    

def tkD():
    t1=t.Toplevel()
    t1.geometry('200x200')
    t.Label(t1,text="Enter Text to Decrypt:").place(x=20,y=20)
    y=t.StringVar()
    t.Entry(t1,textvariable=y).place(x=70,y=20)
    def get():
        #global variable_y
        variable_y=y.get()
        con=dec_adv(variable_y)
        t.Label(t1,text="The Decrypted text is: {0}".format(con)).place(x=20,y=100)
    t.Button(t1,text="Submit",command=get,bg="lime",fg="brown").place(x=20,y=50)
    
s=t.Tk()
s.geometry("300x100")
t.Label(s,text="Welcome To Encrypter/Decrypter",bg="cyan",fg="Purple").place(x=50,y=0)
t.Button(s,text="Encrypt text",command=tkE,bg="lime",fg="brown").place(x=20,y=30)
t.Button(s,text="Decrypt text",command=tkD,bg="lime",fg="brown").place(x=20,y=60)


t.mainloop()
'''
while True:
    print("""
--------------- Menu Of Functions ---------------
1)Encrypt Data to Normal Form
2)Encrypt Data to Binary Form
3)Encrypt Data to Alpha-Numeric Form
4)Decrypt Data from Normal Form
5)Decrypt Data from Binary Form
6)Decrypt Data from Alpha-Numeric Form
7)Create a New Key
8)Exit
""")
    x=input("Enter Your Choice:")
    if x.isdigit():
        x=int(x)
        if x==1:
            a=input("Enter Data:")
            print("The Encrypted Data is:",encrypt(a))
        elif x==2:
            a=input("Enter Data:")
            print("The Encrypted Data is:",enc_bin(encrypt(a)))
        elif x==3:
            a=input("Enter Data:")
            print("The Encrypted Data is:",enc_alp(encrypt(a)))
        elif x==4:
            a=input("Enter Data:")
            print("The Decrypted Data is:",decrypt(a))
        elif x==5:
            a=input("Enter Data:")
            print("The Decrypted Data is:",dec_bin(a))
        elif x==6:
            a=input("Enter Data:")
            print("The Decrypted Data is:",dec_alp(a))
        elif x==7:
            z=new_gen()
            print("The Old Key is :")
            for i in key:
                print(i)
            print("The New Key is:")
            for i in z:
                print(i)
            q=input("Do you wish to replace the key for rest of the program?(y/n)::")
            while True:
                if q.lower()=="y":
                    key = z
                    break
                elif q.lower()=="n":
                    break
                else:
                    print("Please Enter a Valid Option!")
            
        elif x==8:
            exit()
        else:
            print("Please Enter a Valid Option!")
    else:
        print("Please Enter a Valid Option!")

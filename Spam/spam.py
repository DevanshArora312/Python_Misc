import pyautogui as p
import time as t
t.sleep(7)
f=open("script.txt","r")
for i in f:
    p.typewrite(i)
    p.press("enter")
    
    

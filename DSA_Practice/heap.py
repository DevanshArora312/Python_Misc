class heap():
    
    def __init__(self,values=[]):
        self.values=values
        self._list=[0]
        for i in self.values:
            self._list.append(i)

    def swap(self,index1,index2):
        self._list[index1],self._list[index2]=self._list[index2],self._list[index1]

    def _floatdown(self,index):
        left_child_index=index*2
        right_child_index=index*2 + 1
        run=False
        if len(self._list) > right_child_index and self._list[index] < self._list[right_child_index]:
            new_index=right_child_index
            run= True
        if len(self._list) > left_child_index and self._list[index] < self._list[left_child_index]:
            new_index=left_child_index
            run=True
        if run:
            self.swap(index,new_index)
            self._floatdown(new_index)
        
    def _floatup(self,index):
        parent=index//2
        if parent==0:
            return
        if self._list[index]>self._list[parent]:
            self.swap(index,parent)
            new_index=parent
            self._floatup(new_index)
            
    def push(self,value):
        self._list.append(value)
        self._floatup(len(self._list)-1)
    def peek(self):
        print("The top value of heap is:",self._list[1])

    def _pop(self):
        if len(self._list) > 2:
            self.swap(1,len(self._list)-1)
            x=self._list.pop()
            print("Popped value==>",x)
            self._floatdown(1)
        elif len(self._list) == 2:
            x=self._list.pop()
            print("Popped value==>",x)
        else:
            print("None")

    def temp_show(self):
        print(self._list)


heap1=heap([])
while True:
    print(""" What Do You want to do:
1. Peek
2. Push
3. Pop
4. Show
    """
          )
    try:
        x= int(input("Enter Your Choice"))
    except:
        pass
    if x==1:
        heap1.peek()
    elif x==2:
        v=int(input("Enter in the value:"))
        heap1.push(v)
    elif x==3:
        heap1._pop()
    elif x==4:
        heap1.temp_show()
    

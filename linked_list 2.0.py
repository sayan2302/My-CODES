class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linked_list:
    def __init__(self,head=None):
        self.head=head
    def insert_at_beginning(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.insert_at_beginning(data)
            return
        i=self.head
        while i.next:
            i=i.next
        i.next=new_node
    def print(self):
        if self.head==None:
            print("Empty LL")
            return
        i=self.head
        string=''
        while i:
            string+=str(i.data)+' -> '
            i=i.next
        print(string[:-4])
    def clear(self):
        self.head=None
    def insert_values(self,*l):
        for i in l:
            self.insert_at_end(i)
    def length(self):
        c=0
        i=self.head
        while i:
            c+=1
            i=i.next
        return(c)
    def insert_at_index(self,data,pos):
        if pos<0 or pos>self.length():
            raise Exception('Wrong Index')
        c=0
        i=self.head
        if pos==0 or i==None:
            self.insert_at_beginning(data)
            return
        while i:
            if c==pos-1:
                next_element=i.next
                i.next=Node(data,next_element)
                return
            i=i.next
            c+=1
    def replace_at_index(self,data,pos):
        if self.head==None:
            raise Exception('Empty LL')
        if pos<0 or pos>self.length()-1 :
            raise Exception('Wrong Index')
        c=0
        i=self.head
        if pos==0:
            i.data=data
            return
        for _ in range(pos):
            i=i.next
        i.data=data
    def remove_at_index(self,pos):
        if self.head==None:
            raise Exception('Empty LL')
        if pos<0 or pos>self.length()-1:
            raise Exception('Wrong Index')
        i=self.head
        if pos==0:
            i=i.next
        for _ in range(pos-1):
            i=i.next
        i.next=i.next.next
    def reverse(self):
        prev=None
        curr=self.head
        after=curr.next
        while after!=None:
            curr.next=prev
            prev=curr
            curr=after
            after=curr.next
        curr.next=prev
        self.head=curr

def loop_maker(ll): #pass the linked list object in argument (not the head)
    first_ele=ll.head
    second_ele=first_ele.next
    for i in range(ll.length()-1):
        ll.head=ll.head.next
    ll.head.next=second_ele
    ll.head=first_ele
def check_loop(ll): #pass the linked list object in argument (not the head)
    if ll.head==None or ll.head.next==None:
        return False
    slow,fast=ll.head,ll.head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:return True
    return False
def loop_remover(ll): #pass the linked list object in argument (not the head)
    if ll.head==None or ll.head.next==None:return
    slow,fast,p1=ll.head,ll.head,ll.head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            p2=slow
            break
    if fast.next==None and fast.next.next==None:return
    while True:
        if p1.next==p2.next:
            p2.next=None
            break
        p1=p1.next
        p2=p2.next

#LOOP RELATED DRIVER STATEMENTS
# l1=linked_list()
# l1.insert_values(1,2,3,4,5)
# loop_maker(l1)
# l2=linked_list()
# l2.insert_values(3,5,9,1)
# print('loop =',check_loop(l1))
# loop_remover(l1)
# print('loop =',check_loop(l1))
# l1.print()

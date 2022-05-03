#q2a
class MyMailQue:
    def __init__(self) :
        self.mails = []
        self.size = 0

    def enqueue(self, data):
        self.mails.append(data)
        self.size += 1 

    def dequeue(self):
        if self.size > 1:
            popped = self.mails[0]
            self.mails = self.mails[1:]
            self.size -= 1
            return popped
        elif self.size == 1:
            popped = self.mails[0]
            self.mails = []
            self.size -= 1
            return popped
        else:
            return None

    def display(self):
        for i in self.mails:
            print(i)
#q2b
class MailBox:
    def __init__(self):
        self.mailbox = {
            'example': MyMailQue(),
        }
    
    def createMailBox(self, addr) :
        try:
            self.mailbox[addr] = MyMailQue()
        except Exception:
            print('Error')
        
    
    def send(self, sender, receiver, mailbody) :
        if self.mailbox.get(receiver):
            tuple_mail = (sender, mailbody)
            self.mailbox.get(receiver).enqueue(tuple_mail)
        else:
            print('Can\'t sent')

    def receive(self, addr) :
        if self.mailbox.get(addr):
            Queue = self.mailbox.get(addr)
            return Queue.dequeue()
        else:
            print('Cant receive')


Mailserver = MailBox()
Mailserver.createMailBox("mymail")
Mailserver.createMailBox("classmateMail")

Mailserver.send("mymail", "classmateMail", "Hello ! How are you ?" )
Mailserver.send("mymail", "classmateMail", "Please prepare assignment for Data structure ")
Mailserver.send("classmateMail", "mymail", "I got your assignment and will prepare it ! ")
Mailserver.send("mymail", "classmateMail", "Thanks you and see you later ! ")

mail = Mailserver.receive("mymail")
print("My receive mail :" + str(mail) )

mail = Mailserver.receive("classmateMail")
print("My classmate receive mail :" + str(mail) )


#test case 1
Test1Server = MailBox()
Test1Server.createMailBox('test1')
Test1Server.createMailBox('test2')

Test1Server.send('test1', 'test2', "Email 1 for testing")

mail = Test1Server.receive('test2')
print("test2 receive mail :" + str(mail) )

#test case 2
Test2Server = MailBox()
Test2Server.createMailBox('test3')
mail = Test2Server.receive('test3')
print("test3 receive mail :" + str(mail) )

#test case 3
Test3Server = MailBox()
mail = Test3Server.receive('test4')
print("test4 receive mail :" + str(mail) )

#q3
class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

class Path:
    def __init__(self):
        self.store = []
        pass

    def searchPath(self, root):
        self.store.append(root)
        if root.data == 'end':
            for item in self.store:
                if item.data == "end":
                    print(f"{item.data}")
                else:
                    print(f"{item.data}->", end="")
            return
        else:
            if root.left_node:
                self.searchPath(root.left_node)
            elif root.right_node:
                self.searchPath(root.right_node)

    def searchAllPath(self, root):
        if root is None:
            return
    
        self.store.append(root)
        if root.left_node or root.right_node:
            self.searchAllPath(root.left_node)
            self.searchAllPath(root.right_node)
        else:
            weight = 0
            for i in self.store:
                if i.data == "end":
                    print(f'{i.data}', end='')
                    print(f'\t{weight}')
                else:
                    print(f"{i.data}->", end='')
                    if i.data != 'start':
                        weight += i.data
    
        self.store.pop()
    
    def searchPathByWeight(self, root, end):
        if root is None:
            return

        self.store.append(root)
        if root.left_node is None and root.right_node is None:
            weight = 0
            for i in self.store:
                if i.data == "end":
                    print(f'{i.data}', end='')
                    print(f'\t{weight}')
                else:
                    print(f"{i.data}->", end='')
                    if i.data != 'start':
                        weight += i.data
        
        if root.left_node and root.right_node:
            if root.left_node.data < root.right_node.data:
                self.searchPathByWeight(root.left_node,end)
            else:
                self.searchPathByWeight(root.right_node,end)

        self.store.pop()

#test 1
Start_node = Node('start')

a=8
b=88
c=84
d=48
e=80
f=840
g=880

Start_node = Node('start')
b_node = Node(b)
d_node = Node(d)
e_node = Node(e)
End_node = Node('end')

Start_node.left_node = b_node
b_node.left_node = d_node
b_node.right_node = e_node
d_node.right_node = End_node
e_node.left_node = End_node


mypath = Path()
mypath.searchPath(Start_node)

print('mypath.searchAllPath: ')
mypath.store = []
mypath.searchAllPath(Start_node)

print('mypath.searchPathByWeight')
mypath.store = []
mypath.searchPathByWeight(Start_node, End_node)


start = Node('start')
a_node = Node(a)
b_node = Node(b)
b2 = Node(b)
c_node = Node(c)
c2 = Node(c)
d_node = Node(d)
d2 = Node(d)
e_node = Node(e)
e2 = Node(e)
f_node = Node(f)
f2 = Node(f)
g_node = Node(g)
end = Node('end')

start.left_node = b_node
start.right_node = c_node

b_node.left_node = d_node
b_node.right_node = e2

c_node.left_node = f2
c_node.right_node = g_node

d_node.left_node = f_node
d_node.right_node = e_node

e2.right_node = d2

f2.right_node = c2

g_node.left_node = b2
g_node.right_node = a_node

f_node.right_node = end
e_node.right_node = end
d2.right_node = end
c2.left_node = end
b2.left_node = end
a_node.left_node = end

mypath2 = Path()
print('mypath2')
mypath2.searchAllPath(start)

mypath2.store = []
print('mypath2')
mypath2.searchPathByWeight(start, end)

nodeStart = Node('start')

node6915 = Node(6915)
node300 = Node(300)
node59 = Node(59)
node31 = Node(31)
node21 = Node(21)
node12 = Node(12)
node45 = Node(45)
node786 = Node(786)
node86 = Node(86)
node68 = Node(68)
node88 = Node(88)
node48 = Node(48)
node689 = Node(689)
node777 = Node(777)
node1 = Node(1)
node996 = Node(996)
node8964 = Node(8964)
node101 = Node(101)
node911 = Node(911)
node899 = Node(899)
node517 = Node(517)
node7 = Node(7)
node167 = Node(167)
node169 = Node(169)
node612 = Node(612)
node831 = Node(831)
node721 = Node(721)
node609 = Node(609)
node107 = Node(107)
node1911 = Node(1911)
node1001 = Node(1001)

nodeEnd = Node('end')

nodeStart.left_node = node6915
nodeStart.right_node = node300

node6915.left_node = node59
node6915.right_node = node31

node59.left_node = node45
node59.right_node = node786

node45.left_node = node689
node45.right_node = node777

node689.left_node = node101
node689.right_node = node911

node31.left_node = node86

node86.left_node = node1

node1.left_node = node899
node1.right_node = node517

node899.left_node = node612
node899.right_node = node831

node612.left_node = node107

node107.left_node = node1911
node107.right_node = node1001

node517.left_node = node721
node517.right_node = node609

node300.left_node = node21
node300.right_node = node12

node21.left_node = node68
node21.right_node = node88

node68.right_node = node996

node996.right_node = node7

node12.right_node = node48

node48.left_node = node8964

node8964.left_node = node167
node8964.right_node = node169

node101.left_node = nodeEnd
node911.left_node = nodeEnd
node1911.left_node = nodeEnd
node1001.left_node = nodeEnd
node831.left_node = nodeEnd
node721.left_node = nodeEnd
node609.left_node = nodeEnd
node7.left_node = nodeEnd
node167.left_node = nodeEnd
node169.left_node = nodeEnd
node88.left_node = nodeEnd
node777.left_node = nodeEnd
node786.left_node = nodeEnd

mypath3 = Path()
print('mypath3')
mypath3.searchAllPath(nodeStart)

mypath3.store = []
print('mypath3')
mypath3.searchPathByWeight(nodeStart, nodeEnd)

#test 2
node_start = Node('start')
node_end = Node('end')

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_8 = Node(8)
node_9 = Node(9)
node_10 = Node(10)
node_11 = Node(11)
node_12 = Node(12)
node_13 = Node(13)
node_14 = Node(14)
node_15 = Node(15)
node_16 = Node(16)
node_17 = Node(17)
node_18 = Node(18)
node_19 = Node(19)
node_20 = Node(20)
node_21 = Node(21)
node_22 = Node(22)
node_23 = Node(23)
node_24 = Node(24)
node_25 = Node(25)
node_26 = Node(26)
node_27 = Node(27)
node_28 = Node(28)
node_29 = Node(29)
node_30 = Node(30)
node_31 = Node(31)

node_start.left_node = node_1
node_start.right_node = node_2

node_1.left_node = node_3
node_1.right_node = node_4

node_3.left_node = node_7
node_3.right_node = node_8

node_7.left_node = node_15
node_7.right_node = node_16

node_8.left_node = node_17
node_8.right_node = node_18

node_4.left_node = node_9
node_4.right_node = node_10

node_9.left_node = node_19
node_9.right_node = node_20

node_10.right_node = node_21

node_2.left_node = node_5
node_2.right_node = node_6

node_5.left_node = node_11
node_5.right_node = node_12

node_11.left_node = node_22

node_12.right_node = node_23

node_6.left_node = node_13
node_6.right_node = node_14

node_13.left_node = node_24

node_14.left_node = node_25
node_14.right_node = node_26

node_26.left_node = node_27
node_26.right_node = node_28

node_27.left_node = node_29
node_27.right_node = node_30

node_28.right_node = node_31

node_15.right_node = node_end
node_16.right_node = node_end
node_17.right_node = node_end
node_18.right_node = node_end
node_19.right_node = node_end
node_20.right_node = node_end
node_21.right_node = node_end
node_22.left_node = node_end
node_23.left_node = node_end
node_24.left_node = node_end
node_25.left_node = node_end
node_29.left_node = node_end
node_30.left_node = node_end
node_31.left_node = node_end

mypath4 = Path()
print('mypath4')
mypath4.searchAllPath(node_start)

mypath4.store = []
print('mypath4')
mypath4.searchPathByWeight(node_start, node_end)

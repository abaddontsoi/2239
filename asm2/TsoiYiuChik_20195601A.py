class MyMailQue:
    def __init__(self) :
        # implement a queue with an array
        self.queue = []
        self.size = 0
    
    def enqueue(self, data):
        # insert data at the end of queue 
        self.queue.append(data)
        self.size += 1 
    
    def dequeue(self):
        # take out data at the beginning of the queue
        # remove it and return the data taken out
        if self.size > 0:
            popped = self.queue[0]
            self.queue.pop(0)
            self.size -= 1
            return popped
        else:
            return None
    
    def display(self):
        # show all the data in the queue
        for i in self.queue:
            print(i)

class MailBox:
    def __init__(self):
        # define a dictionary which 
        # contain mail queue (MyMailQue).
        self.mailbox = {}
    
    def createMailBox(self, addr) :
        # create a new mail queue attached to dictionary defined 
        # with addr as key
        try:
            if self.mailbox.get(addr):
                print('Email exists, can\'t create mailbox')
            else:
                self.mailbox.update({
                    addr: MyMailQue()
                })
        except Exception:
            print('Can\'t create mailbox')
    
    def send(self, sender, receiver, mailbody) :
        # find mail queue of the receiver in dictionary, 
        # enqueue a data as tuple which include sender 
        # and mailbody to the queue
        try:
            mail = (sender, mailbody)
            self.mailbox[receiver].enqueue(mail)
        except Exception:
            print('Can\'t send the mail')

    def receive(self, addr) :
        # find mail queue in dictionary by addr
        # return the first item in queue with (sender, mailbody) 
        # remove it in the queue.
        try:
            myQueue = self.mailbox[addr]
            return myQueue.dequeue()
        except Exception:
            print('Can\'t receive email')

Mailserver = MailBox()
Mailserver.createMailBox('a')
Mailserver.createMailBox('b')

Mailserver.send('a', 'b', 'Hello ! How are you ?')
Mailserver.send('a', 'b', 'Please prepare assignment for Data structure')
Mailserver.send('b', 'a', 'I got your assignment and will prepare it ! ')
Mailserver.send('a', 'b', 'Thanks you and see you later ! ')

mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('b')
print('My classmate receive mail :' + str(mail) )


# mailbox test case 1
mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

# mailbox test case 2
Mailserver.send('a', 'a', 'Send email to myself')
mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )


# mailbox test case 3
Mailserver.send('a', 'c', 'Send email to user not exists')
mail = Mailserver.receive('c')
print('C receives mail :' + str(mail) )

class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        return f'{self.data}'

class Path:
    def __init__(self):
        self.pathArray = []
        self.allPaths = []
        pass

    def __repr__(self):
        return f'{self.pathArray}'

    def searchPath(self, root: Node):
        path_list = [root]
        if root.left_node:
            path_list += self.searchPath(root.left_node)
        elif root.right_node:
            path_list += self.searchPath(root.right_node)
        return path_list

    def searchAllPath(self, root: Node, initWeight = 0):
        self.pathArray.append(root)
        if root.data != 'Start' and root.data != 'End':
            initWeight += root.data
        
        if root.left_node is None and root.right_node is None:
            for node in self.pathArray:
                if node.data =="End":
                    print(f"{node}", end='')
                    print(f"\t{initWeight}")
                else:
                    print(f"{node}->", end='')

            temp = [i for i in self.pathArray]
            self.allPaths.append(temp)
            self.pathArray.pop()
        else:
            if root.left_node:
                self.searchAllPath(root.left_node, initWeight)
            if root.right_node:
                self.searchAllPath(root.right_node, initWeight)

            self.pathArray.pop()


    def searchPathByWeight(self, root: Node, last: Node):
        self.pathArray.append(root)

        if root is last: # if root.left_node is None and root.right_node is None
            for node in self.pathArray:
                if node.data =="End":
                    print(f"{node}")
                else:
                    print(f"{node}->", end='')
        else:
            if root.left_node and root.right_node:
                if root.left_node.data <= root.right_node.data:
                    self.searchPathByWeight(root.left_node, last)
                if root.right_node.data < root.left_node.data:
                    self.searchPathByWeight(root.right_node, last)
            elif root.left_node:
                self.searchPathByWeight(root.left_node, last)
            elif root.right_node:
                self.searchPathByWeight(root.right_node, last)
            self.pathArray.pop()

# student id: 20195601A
# a = 95
# b = 56
# c = 60
# d = 1
# e = 96
# f = 50
# g = 61

start = Node('Start')
b = Node(56)
d = Node(1)
e = Node(96)
end = Node('End')

start.left_node = b
b.left_node = d
b.right_node = e
d.right_node = end
e.left_node = end

pathA = Path()
for i in pathA.searchPath(start):
    if i.data == 'End':
        print(i)
    else:
        print(f"{i}->", end=' ')

start = Node('Start')
a = Node(95)
b = Node(56)
b2 = Node(56)
c = Node(60)
c2 = Node(60)
d = Node(1)
d2 = Node(1)
e = Node(96)
e2 = Node(96)
f = Node(50)
f2 = Node(50)
g = Node(61)
end = Node('End')

start.left_node = b
start.right_node = c

b.left_node = d
b.right_node = e2

c.left_node = f2
c.right_node = g

d.left_node = f
d.right_node = e

e2.right_node = d2

f2.right_node = c2

g.left_node = b2
g.right_node = a

f.right_node = end
e.right_node = end
d2.right_node = end
c2.left_node = end
b2.left_node = end
a.left_node = end

mypath = Path()
mypath.searchAllPath(start)
mypath.searchPathByWeight(start, end)


# test case 1 of question 3:
Start = Node("Start")
End = Node('End')

# generate nodes
nodeList = []
for i in range(1,32):
    nodeList.append(Node(i))

# connecting nodes
Start.left_node = nodeList[0]
Start.right_node = nodeList[1]

nodeList[0].left_node = nodeList[29]
nodeList[0].right_node = nodeList[28]

nodeList[1].left_node = nodeList[14]
nodeList[1].right_node = nodeList[13]

nodeList[29].left_node = nodeList[23]
nodeList[29].right_node = nodeList[22]

nodeList[28].left_node = nodeList[27]
nodeList[28].right_node = nodeList[26]

nodeList[23].left_node = nodeList[21]
nodeList[23].right_node = nodeList[20]

nodeList[22].left_node = nodeList[19]
nodeList[22].right_node = nodeList[18]

nodeList[27].left_node = nodeList[17]
nodeList[27].right_node = nodeList[16]

nodeList[26].left_node = nodeList[25]
nodeList[26].right_node = nodeList[24]

nodeList[14].left_node = nodeList[12]
nodeList[14].right_node = nodeList[11]

nodeList[12].left_node = nodeList[15]
nodeList[12].right_node = nodeList[5]

nodeList[11].left_node = nodeList[6]
nodeList[11].right_node = nodeList[4]

nodeList[13].left_node = nodeList[10]
nodeList[13].right_node = nodeList[7]

nodeList[10].left_node = nodeList[3]
nodeList[10].right_node = nodeList[2]

nodeList[7].left_node = nodeList[8]
nodeList[7].right_node = nodeList[9]

nodeList[21].right_node = End
nodeList[20].right_node = End
nodeList[19].right_node = End
nodeList[18].right_node = End
nodeList[17].right_node = End
nodeList[16].right_node = End
nodeList[25].right_node = End
nodeList[24].right_node = End

nodeList[15].left_node = End
nodeList[5].left_node = End
nodeList[6].left_node = End
nodeList[4].left_node = End
nodeList[3].left_node = End
nodeList[2].left_node = End
nodeList[8].left_node = End

nodeList[9].left_node = nodeList[30]
nodeList[30].left_node = End

print('\nTest case 1: ')
testCase1 = Path()
print(f"Testing of searchAllPath(Start):")
testCase1.searchAllPath(Start)
print(f"Testing of searchPathByWeight(Start,End):")
testCase1.searchPathByWeight(Start,End)


# test case 2 of question 3:
Start = Node("Start")
End = Node('End')

# generate nodes
nodeList2 = []
for i in range(1,33):
    nodeList2.append(Node(i))

# connecting nodes
Start.left_node = nodeList2[0]
Start.right_node = nodeList2[1]

nodeList2[0].left_node = nodeList2[2]

nodeList2[2].left_node = nodeList2[6]
nodeList2[2].right_node = nodeList2[7]

nodeList2[6].left_node = nodeList2[14]
nodeList2[6].right_node = nodeList2[15]

nodeList2[7].left_node = nodeList2[16]
nodeList2[7].right_node = nodeList2[17]

nodeList2[17].left_node = nodeList2[3]

nodeList2[3].left_node = nodeList2[8]
nodeList2[3].right_node = nodeList2[9]

nodeList2[8].left_node = nodeList2[18]
nodeList2[8].right_node = nodeList2[19]

nodeList2[9].left_node = nodeList2[20]
nodeList2[9].right_node = nodeList2[21]

nodeList2[1].left_node = nodeList2[4]
nodeList2[1].right_node = nodeList2[5]

nodeList2[4].left_node = nodeList2[10]
nodeList2[4].right_node = nodeList2[11]

nodeList2[10].left_node = nodeList2[22]
nodeList2[10].right_node = nodeList2[23]

nodeList2[11].left_node = nodeList2[24]
nodeList2[11].right_node = nodeList2[25]

nodeList2[5].left_node = nodeList2[12]
nodeList2[5].right_node = nodeList2[13]

nodeList2[12].left_node = nodeList2[26]
nodeList2[12].right_node = nodeList2[27]

nodeList2[13].left_node = nodeList2[28]
nodeList2[13].right_node = nodeList2[29]

nodeList2[23].left_node = nodeList2[30]
nodeList2[23].right_node = nodeList2[30]

nodeList2[24].left_node = nodeList2[31]

nodeList2[14].left_node = End
nodeList2[15].left_node = End
nodeList2[16].left_node = End
nodeList2[18].left_node = End
nodeList2[19].left_node = End
nodeList2[20].left_node = End
nodeList2[21].left_node = End
nodeList2[22].right_node = End
nodeList2[30].right_node = End
nodeList2[31].right_node = End
nodeList2[25].right_node = End
nodeList2[26].right_node = End
nodeList2[27].right_node = End
nodeList2[28].right_node = End
nodeList2[29].right_node = End

print('\nTest case 2: ')
testCase2 = Path()
print(f"Testing of searchAllPath(Start):")
testCase2.searchAllPath(Start)
print(f"Testing of searchPathByWeight(Start,End):")
testCase2.searchPathByWeight(Start,End)

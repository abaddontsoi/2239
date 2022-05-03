class MyMailQue:
    def __init__(self) :
        self.q = []
        self.size = 0
    
    def enqueue(self, data):
        self.q.append(data)
        self.size += 1 
    
    def dequeue(self):
        if self.size > 1:
            popped = self.q[0]
            self.q = self.q[1:]
            self.size -= 1
            return popped
        elif self.size == 1:
            popped = self.q[0]
            self.q = []
            self.size -= 1
            return popped
        else:
            return None

    
    def display(self):
        for i in self.q:
            print(i)

class MailBox:
    def __init__(self):
        self.box = {}
    
    def createMailBox(self, addr) :
        self.box.update({
          addr: MyMailQue()
        })
    
    def send(self, sender, receiver, mailbody) :
        mail = (sender, mailbody)
        self.box[receiver].enqueue(mail)

    def receive(self, addr) :
        myQ = self.box[addr]
        return myQ.dequeue()

Mailserver = MailBox()
Mailserver.createMailBox('123')
Mailserver.createMailBox('321')

Mailserver.send('123', '321', 'Hello ! How are you ?')
Mailserver.send('123', '321', 'Please prepare assignment for Data structure')
Mailserver.send('321', '123', 'I got your assignment and will prepare it ! ')
Mailserver.send('123', '321', 'Thanks you and see you later ! ')

mail = Mailserver.receive('123')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('321')
print('My classmate receive mail :' + str(mail) )


# mailbox test case 1
Mailserver.send('123', '321', 'I like python!')
mail = Mailserver.receive('321')
print('My classmate receive mail :' + str(mail) )

mail = Mailserver.receive('321')
print('My classmate receive mail :' + str(mail) )

# mailbox test case 2
Mailserver.send('321', '321', 'To myself for testing')
mail = Mailserver.receive('321')
print('My classmate receive mail :' + str(mail) )

# mailbox test case 3
Mailserver.send('321', '123', 'I like python too!')
mail = Mailserver.receive('123')
print('My receive mail :' + str(mail) )

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.data}'

class Path:
    def __init__(self):
        self.paths = []

    def searchPath(self, start: Node):
        self.paths.append(start)
        if start and start.data == 'End':
            print(self.paths)
        else:
            if start.left:
                self.searchPath(start.left)
            elif start.right:
                self.searchPath(start.right)

    def searchAllPath(self, root: Node):
        if root is None:
            return
    
        self.paths.append(root)
        if root.left is None and root.right is None:
            w = 0
            for i in self.paths:
                if i.data == "End":
                    print(f'{i}', end='')
                    print(f'\t{w}')
                else:
                    print(f"{i}->", end='')
                    if i.data != 'Start':
                        w += i.data
    
        self.searchAllPath(root.left)
        self.searchAllPath(root.right)    
        self.paths.pop()


    def searchPathByWeight(self, root: Node, last: Node):
        if root is None:
            return

        self.paths += [root]
        if root.left is None and root.right is None:
            # weight = 0
            for i in self.paths:
                print(f"{i}->", end='')
        
        if root.left:
            self.searchPathByWeight(root.left, last)
        elif root.right:
            self.searchPathByWeight(root.right, last)

        self.paths.pop()

a = 42
b = 28
c = 88
d = 80
e = 48
f = 280
g = 8000

node_a = Node(a)
node_b = Node(b)
node_c = Node(c)
node_d = Node(d)
node_e = Node(e)
node_f = Node(f)
node_g = Node(g)

node_start = Node('Start')
node_end = Node('End')

node_start.left = node_b
node_b.left = node_d
node_b.right = node_e

node_d.right = node_end
node_e.left = node_end

path = Path()
path.searchPath(node_start)

path.paths = []
print('path.searchAllPath(node_start):')
path.searchAllPath(node_start)

path.paths = []
print('path.searchPathByWeight(node_start, node_end):')
path.searchPathByWeight(node_start, node_end)


Start = Node('Start')
End = Node('End')

Odds = [Node(i) for i in range(1, 70, 2)]
Even = [Node(i) for i in range(2, 71, 2)]

Start.left = Even[0]
Start.right = Even[1]

Even[0].left = Even[2]
Even[0].right = Even[3]

Even[2].left = Even[6]
Even[2].right = Even[7]

Even[6].left = Even[14]
Even[6].right = Even[15]

Even[14].left = Even[26]

Even[0].left = Even[27]

Even[7].left = Even[16]
Even[7].right = Even[17]

Even[16].left = Even[28]
Even[16].right = Even[29]

Even[3].left = Even[8]
Even[3].right = Even[9]

Even[8].left = Even[18]

Even[18].left = Even[30]

Even[9].left = Even[19]
Even[9].right = Even[20]

Even[19].right = Even[31]

Even[1].left = Even[4]
Even[1].right = Even[5]

Even[4].left = Even[10]
Even[4].right = Even[11]

Even[11].left = Even[21]
Even[11].right = Even[22]

Even[21].left = Even[32]

Even[5].left = Even[12]
Even[5].right = Even[13]

Even[12].right = Even[23]

Even[23].right = Even[33]

Even[13].left = Even[24]
Even[13].right = Even[25]

Even[25].right = Even[34]

Even[26].right = End
Even[27].right = End
Even[28].right = End
Even[29].right = End
Even[30].right = End
Even[31].right = End
Even[32].right = End
Even[33].right = End
Even[34].right = End
Even[17].right = End
Even[20].right = End
Even[10].right = End
Even[22].right = End
Even[24].right = End

Path1 = Path()
print('\nsearchAllPath()')
Path1.searchAllPath(Start)
print('\nsearchPathByWeight()')
Path1.searchPathByWeight(Start, End)

Start.left = Odds[0]
Start.right = Odds[1]

Odds[0].left = Odds[2]
Odds[0].right = Odds[3]

Odds[2].left = Odds[6]
Odds[2].right = Odds[7]

Odds[6].left = Odds[14]
Odds[6].right = Odds[15]

Odds[14].left = Odds[26]

Odds[0].left = Odds[27]

Odds[7].left = Odds[16]
Odds[7].right = Odds[17]

Odds[16].left = Odds[28]
Odds[16].right = Odds[29]

Odds[3].left = Odds[8]
Odds[3].right = Odds[9]

Odds[8].left = Odds[18]

Odds[18].left = Odds[30]

Odds[9].left = Odds[19]
Odds[9].right = Odds[20]

Odds[19].right = Odds[31]

Odds[1].left = Odds[4]
Odds[1].right = Odds[5]

Odds[4].left = Odds[10]
Odds[4].right = Odds[11]

Odds[11].left = Odds[21]
Odds[11].right = Odds[22]

Odds[21].left = Odds[32]

Odds[5].left = Odds[12]
Odds[5].right = Odds[13]

Odds[12].right = Odds[23]

Odds[23].right = Odds[33]

Odds[13].left = Odds[24]
Odds[13].right = Odds[25]

Odds[25].right = Odds[34]

Odds[26].right = End
Odds[27].right = End
Odds[28].right = End
Odds[29].right = End
Odds[30].right = End
Odds[31].right = End
Odds[32].right = End
Odds[33].right = End
Odds[34].right = End
Odds[17].right = End
Odds[20].right = End
Odds[10].right = End
Odds[22].right = End
Odds[24].right = End

Path2 = Path()
print('\nsearchAllPath()')
Path2.searchAllPath(Start)
print('\nsearchPathByWeight()')
Path2.searchPathByWeight(Start, End)
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) :
        return f"{self.data}"

class Path:
    def __init__(self):
        self.store = []
        pass

    def searchPath(self, root: Node):
        self.store.append(root)
        if root.data == 'end':
            # self.pathArray.append(root)
            for item in self.store:
                if item.data == "end":
                    print(f"{item.data}")
                else:
                    print(f"{item.data}->", end="")
            return
        else:
            if root.left:
                # self.pathArray.append(root.left_node)
                self.searchPath(root.left)
            elif root.right:
                # self.pathArray.append(root.right_node)
                self.searchPath(root.right)

    def searchAllPath(self, root: Node):
        if root is None:
            return
    
        self.store.append(root)
    
        if root.left is None and root.right is None:
            weight = 0
            for i in self.store:
                if i.data == "end":
                    print(f'{i}', end='')
                    print(f'\t{weight}')
                else:
                    print(f"{i}->", end='')
                    if i.data != 'start':
                        weight += i.data
    
        self.searchAllPath(root.left)
        self.searchAllPath(root.right)
    
        self.store.pop()
    
    def searchPathByWeight(self, root: Node, end: Node):
        if root is None:
            return

        self.store.append(root)
        if root.left is None and root.right is None:
            weight = 0
            for i in self.store:
                if i.data == "end":
                    print(f'{i}', end='')
                    print(f'\t{weight}')
                else:
                    print(f"{i}->", end='')
                    if i.data != 'start':
                        weight += i.data
        
        if root.left:
            self.searchPathByWeight(root.left, end)
        elif root.right:
            self.searchPathByWeight(root.right, end)
        
        self.store.pop()


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

Start_node.left = b_node
b_node.left = d_node
b_node.right = e_node
d_node.right = End_node
e_node.left = End_node


mypath = Path()
mypath.searchPath(Start_node)

# clean the buffer
print('\nmypath.searchAllPath: ')
mypath.store = []
mypath.searchAllPath(Start_node)

# clean the buffer
print('\nmypath.searchPathByWeight')
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

start.left = b_node
start.right = c_node

b_node.left = d_node
b_node.right = e2

c_node.left = f2
c_node.right = g_node

d_node.left = f_node
d_node.right = e_node

e2.right = d2

f2.right = c2

g_node.left = b2
g_node.right = a_node

f_node.right = end
e_node.right = end
d2.right = end
c2.left = end
b2.left = end
a_node.left = end

mypath2 = Path()
print('\nmypath2.searchAllPath(start): ')
mypath2.searchAllPath(start)

mypath2.store = []
print('\nmypath2.searchPathByWeight(start, end)')
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

nodeStart.left = node6915
nodeStart.right = node300

node6915.left = node59
node6915.right = node31

node59.left = node45
node59.right = node786

node45.left = node689
node45.right = node777

node689.left = node101
node689.right = node911

node31.left = node86

node86.left = node1

node1.left = node899
node1.right = node517

node899.left = node612
node899.right = node831

node612.left = node107

node107.left = node1911
node107.right = node1001

node517.left = node721
node517.right = node609

node300.left = node21
node300.right = node12

node21.left = node68
node21.right = node88

node68.right = node996

node996.right = node7

node12.right = node48

node48.left = node8964

node8964.left = node167
node8964.right = node169

node101.left = nodeEnd
node911.left = nodeEnd
node1911.left = nodeEnd
node1001.left = nodeEnd
node831.left = nodeEnd
node721.left = nodeEnd
node609.left = nodeEnd
node7.left = nodeEnd
node167.left = nodeEnd
node169.left = nodeEnd
node88.left = nodeEnd
node777.left = nodeEnd
node786.left = nodeEnd

mypath2 = Path()
print('\nmypath2.searchAllPath(start): ')
mypath2.searchAllPath(nodeStart)

mypath2.store = []
print('\nmypath2.searchPathByWeight(start, end)')
mypath2.searchPathByWeight(nodeStart, nodeEnd)


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

node_start.left = node_1
node_start.right = node_2

node_1.left = node_3
node_1.right = node_4

node_3.left = node_7
node_3.right = node_8

node_7.left = node_15
node_7.right = node_16

node_8.left = node_17
node_8.right = node_18

node_4.left = node_9
node_4.right = node_10

node_9.left = node_19
node_9.right = node_20

node_10.right = node_21

node_2.left = node_5
node_2.right = node_6

node_5.left = node_11
node_5.right = node_12

node_11.left = node_22

node_12.right = node_23

node_6.left = node_13
node_6.right = node_14

node_13.left = node_24

node_14.left = node_25
node_14.right = node_26

node_26.left = node_27
node_26.right = node_28

node_27.left = node_29
node_27.right = node_30

node_28.right = node_31

node_15.right = node_end
node_16.right = node_end
node_17.right = node_end
node_18.right = node_end
node_19.right = node_end
node_20.right = node_end
node_21.right = node_end
node_22.left = node_end
node_23.left = node_end
node_24.left = node_end
node_25.left = node_end
node_29.left = node_end
node_30.left = node_end
node_31.left = node_end

mypath3 = Path()
print('\nmypath3.searchAllPath(node_start)')
mypath3.searchAllPath(node_start)

mypath3.store = []
print('\nmypath3.searchPathByWeight(node_start, node_end)')
mypath3.searchPathByWeight(node_start, node_end)

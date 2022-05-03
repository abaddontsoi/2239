class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        return f'{self.data}'

    def post_order(self, root):
        if root:
            root.post_order(root.left_node)
            root.post_order(root.right_node)
            print(root.data, end=' ')

    def pre_order(self, root):
        if root:
            print(root.data, end=' ')
            root.pre_order(root.left_node)
            root.pre_order(root.right_node)

    def in_order(self, root):
        if root:
            root.in_order(root.left_node)
            print(root.data, end=' ')
            root.in_order(root.right_node)

    def searchPath(self, root, list: list):
        left_list = list
        right_list = list
        if root:
            if root.data == 'End':
                left_list.append(root)
                right_list.append(root)
            else:
                # print(root.data, end=' ')
                left_list.append(root)
                root.searchPath(root.left_node, left_list)
                right_list.append(root)
                root.searchPath(root.right_node, right_list)
                print(left_list)
                print(right_list)

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.PreorderTraversal(root.left_node)
            res += self.PreorderTraversal(root.right_node)
        return res

class Path:
    def __init__(self):
        self.pathArray = []
        self.allPaths = []
        pass

    def __repr__(self):
        return f'{self.pathArray}'

    def searchPath(self, root: Node):
        self.pathArray.append(root)
        if root.data == 'End':
            # self.pathArray.append(root)
            return
        else:
            if root.left_node:
                # self.pathArray.append(root.left_node)
                self.searchPath(root.left_node)
            elif root.right_node:
                # self.pathArray.append(root.right_node)
                self.searchPath(root.right_node)

    def searchAllPath(self, root: Node, initWeight = 0):
        self.pathArray.append(root)
        if root.data != 'Start' and root.data != 'End':
            initWeight += root.data
        
        if root.left_node is None and root.right_node is None:
            print(f"{self.pathArray}   {initWeight}")
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
        if root.data != 'Start' and root.data != 'End':
            # initWeight += root.data
            pass
        if root is last: # if root.left_node is None and root.right_node is None
            print(f"{self.pathArray}")
            # self.pathArray.pop()
        else:
            if root.left_node and root.right_node:
                if root.left_node.data < root.right_node.data:
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

# pathlist = []
mypath = Path()
mypath.searchAllPath(start)
mypath.searchPathByWeight(start, end)


init = Node('Start')
b = Node(56)
d = Node(1)
e = Node(96)
fin = Node('End')

init.left_node = b

b.left_node = d
b.right_node = e

d.right_node = fin

e.left_node = fin

mypath2 = Path()
mypath2.searchPath(init)

for i in mypath2.pathArray:
    print(f"{i}",end='')
    if i.data != 'End':
        print('->', end=' ')
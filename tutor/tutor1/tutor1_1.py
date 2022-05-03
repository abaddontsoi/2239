h = 6
print("The height of the tree is :")
print(h)

if h > 10:
    print("It is a tall tree")
elif h <= 3:
    print("It is a short tree")
else:
    print("It is a medium tree")

i = 0 
while i<h:
    j = 0
    while j<i+1:
        print("*", end = '')
        j += 1
    print()
    i += 1

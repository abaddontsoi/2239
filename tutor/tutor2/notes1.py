
count = 0

for i in range(0, 5):
    for j in range(5,i,-1):
        count+=1
        print('j is:', end=' ')
        print(j)
    print(f'iteration {i} done')


print(count)
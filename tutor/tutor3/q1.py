from itertools import count


def computeSum(item, n):
    i = None
    j = None
    sum = None
    i = 0

    count = 0
    while i < n:
        sum = item[0]
        j = 1
        while j <= i:
            print(count)
            sum += item[j]
            j += 1
            count += 1
        print("Sum for array ", i, " is ", sum)
        i += 1
e = [5, 4, 3, 11, 9]
s = computeSum(e, len(e))
print(s)
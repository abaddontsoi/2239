o1 = (
    (6, 10, 10, 12, 14), (30, 45, 54), (81, 80, 39, 32), (1, 2, 3, 4)
)

o2 = (
    (4, 10, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)
)

# o1_ava = []
# o2_ava = []

# o1_temp = 0
# o2_temp = 0

# for item in o1:
#     for i in item:
#         o1_temp += i
#     o1_ava.append([o1_temp/len(item)])
#     o1_temp = 0

# for item in o2:
#     for i in item:
#         o2_temp += i
#     o2_ava.append([o2_temp/len(item)])
#     o2_temp = 0

def q3(tuples):
    t_ava=[]
    # t_temp = 0
    # for item in tuples:
    #     for i in item:
    #         t_temp += i
    #     t_ava.append([t_temp/len(item)])
    #     t_temp = 0
    for item in tuples:
        t_ava.append([sum(item)/len(item)])
        
    return t_ava

print(q3(o1)) # should be [[10.4], [43.0], [58.0], [2.5]]
print(q3(o2)) # should be [[3.0], [23.666666666666668], [-6.0], [-1.6666666666666667]]

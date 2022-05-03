# a) bubble sort

def asort(our_list):
    swapped = True
    num_of_iterations = 0

    while(swapped):
        swapped = False
        for j in range(len(our_list)- num_of_iterations - 1):
            if our_list[j] > our_list[j+1]:
                # Swap  
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                swapped = True
        num_of_iterations += 1
        print(our_list)
 
our_list = [19, 13, 6, 2, 18, 8]
# asort(our_list)
# print(our_list)
# b) [2, 6, 8, 13, 18, 19]


def asort2(the_list):
    for i in range(len(the_list)):
        
        min_index = i

        for j in range(i+1, len(the_list)):

            if the_list[j]<the_list[min_index]:
                min_index = j

        the_list[i], the_list[min_index] = the_list[min_index], the_list[i]

q2_list = [4, 7, 5, 9, 6, 3, 2, 8, 1]
asort2(q2_list)
print(q2_list)
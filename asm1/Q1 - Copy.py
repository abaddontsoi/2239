# Q1a)
class Employee():
    # create a constructor
    # with 2 parameters
    def __init__(self, name: str, salary: int):
        self.name = name # initiate the instance variable name
        self.salary = salary # initiate the instance variable salary

    # print an Employee item
    def __str__(self):
        string = self.name + ', ' + str(self.salary)
        return string
    
    # Q2a)  A method insertionSort to accept Employee list 
    # and sort the list by using their salary
    def insertionSort(others: list): 
        for i in range(1, len(others)):
            key = others[i]

            j = i - 1
            # print(key)

            while j >= 0 and key.salary < others[j].salary:
                others[j + 1] = others[j]
                j -= 1
            others[j + 1] = key

# Q1b)
# create a list EmpList, with elements mentioned in the question
EmpList = [
    # Q1c)
    # put all the element mentioned in question to EmpList
    Employee('Ada', 15000),
    Employee('Brian', 18000),
    Employee('Carson', 12000),
    Employee('Dave', 14000),
]


#Q2c)
# Print the information of each Employee before and after sorting
print('Before Insertion Sort: ')
for item in EmpList:
    print(item)
# Before Insertion Sort:
# Ada,15000
# Brian,18000
# Carson,12000
# Dave,14000


print('\nAfter Insertion Sort: ')
# Q2b) Call insertionSort method 
#   to sort the list by using employee’s salary
Employee.insertionSort(EmpList)
for item in EmpList:
    print(item)
# After Insertion Sort:
# Carson,12000
# Dave,14000
# Ada,15000
# Brian,18000

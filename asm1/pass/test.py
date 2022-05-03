class Employee():
    
    def insertionSort(items): #method insertionSort to accept Employee list and sort the list by using their salary 
            for i in range(1, len(items)):
                key = items[i]

                j = i - 1

                while j >= 0 and key.salary < items[j].salary:
                    items[j + 1] = items[j]
                    j -= 1
                items[j + 1] = key

    def __init__(self, name, salary):#Two instance variables
            self.name = name #name, data type: String
            self.salary = salary #salary, data type: integer

    def __str__(self): #One constructor with two parameters
            Emp = self.name + ',' + str(self.salary)
            #initialize the member variable name
            #initialize the member variable salary
            return Emp

EmpList = [] #Create a list EmpList

EmpList = [
    Employee('Ada',15000),
    Employee('Brian',18000),
    Employee('Carson',12000),
    Employee('Dave',14000),
]
#Put the employee information in the list

#) Print the information of each Employee before and after sorting
print('Before Insertiom Sort')
for item in EmpList:
    print(item)
print('\nAfter Insertion Sort')
Employee.insertionSort(EmpList)
for item in EmpList:
    print(item)

#test case 1
case1 = [
    Employee('ada',19500),
    Employee('Dave',32401),
    Employee('Brain',20008)
]
print('\nAfter Insertion Sort case 1')
Employee.insertionSort(case1)
for item in case1:
    print(item)

#test case 2
case2 = [
    Employee('Ken',1),
    Employee('Carson',10),
    Employee('Kennis',200)
]
print('\nAfter Insertion Sort case 2')
Employee.insertionSort(case2)
for item in case2:
    print(item)

#test case 3
case3 = [
    Employee('Bunny Rabbit',50),
    Employee('Pionner',0),
    Employee('Onkyo',0),
    Employee('Denon',350),
    Employee('Bowers&Wilkins',100000)
]

print('\nAfter Insertion Sort case 3')
Employee.insertionSort(case3)
for item in case3:
    print(item)
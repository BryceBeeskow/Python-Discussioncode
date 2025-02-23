# Bryce Beeskow
# Final Exam Coding
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow

#Employee class
class Employee:

    count_employees = 0

    def __init__(self, name, id, title):

        self.name = name

        self.id = id

        self.title = title

        Employee.count_employees += 1

    def __str__(self):
        return f'Name:{self.name} ID:{self.id} Title:{self.title}'        

    def isIDHigher(self,coworker):
        if self.id > coworker.id:
            return f'{self.name}\'s ID ({self.id}) is greater than {coworker.name}\'s ID ({coworker.id})'
        else:
            return f'{coworker.name}\'s ID ({coworker.id}) is greater than {self.name}\'s ID ({self.id})'
        #return self.id > coworker.id

#TennisPro subclass
class TennisPro(Employee):

    def __init__(self, gameswon, hourlypay, ranking):
        self.gameswon = gameswon
        self.hourlypay = hourlypay
        self.ranking = ranking
    
    def  isUSPTALevelHigher(self, other):
        if self.ranking > other.ranking:
            return f'Ranking: {self.ranking}'
        else: return f'Ranking: {other.ranking}'
        
    def __str__(self):
        return f'Games Won:{self.gameswon} hourlypay:{self.hourlypay} Ranking:{self.ranking}'        
    
employee1 = Employee("Ashley",1345, 'HR')
employee2 = Employee("Jeff", 1234, 'IT Tech')

print(employee1,'\n',employee2)      

print(employee1.isIDHigher(employee2)) 


print(f'Number of Employees: {Employee.count_employees}')

e1 = TennisPro(3, 26, 2)
e2 = TennisPro(4, 32, 3)

print(e1)
print(e2)
print(e1.isUSPTALevelHigher(e2))
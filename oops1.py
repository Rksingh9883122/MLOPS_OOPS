class employee:
    
    def __init__(self):
        print(id(self))
        self.id = 8104
        self.salary = '75000_dollars'
        self.designation = "Sr_ML_Engineer"
        
        
# creating an object the employee class
    def travel(self, destination):
        print(f'Travelling to {destination}')

Raj = employee()
Raj.Qualification = 'M.Tech In Applied AI'
print(Raj.Qualification)
print(id(Raj))

Rajiv = employee()
print(id(Rajiv))

Raj.travel('New York')
    
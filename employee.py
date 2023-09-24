"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class MonthlyEmployee:
    def __init__(self, name, monthly_salary, bonus, commission_per_contract, num_contracts):
        super().__init__
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus = bonus
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts

    def get_pay(self):
        return self.monthly_salary + self.bonus + (self.commission_per_contract*self.num_contracts)
    
class ContractEmployee:
    def __init__(self, name, hourly_rate, hours_worked, commission_per_contract, num_contracts):
        super().__init__
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts

    def get_pay(self):
        base_pay = self.hourly_rate * self.hours_worked
        commission = self.commission_per_contract * self.num_contracts
        return base_pay + commission

billie = MonthlyEmployee('Billie', 4000, 0, 0, 0)
charlie = ContractEmployee('Charlie', 25, 100, 0, 0)
renee = MonthlyEmployee('Renee', 3000, 0 , 200, 4)
jan = ContractEmployee('Jan', 25, 150, 220, 3)
robbie = MonthlyEmployee('Robbie', 2000, 1500, 0, 0)
robbie.commission_per_contract = 1500
ariel = ContractEmployee('Ariel', 30, 120, 600, 1)

employees = [billie, charlie, renee, jan, robbie, ariel]

for Employee in employees:
    pay = Employee.get_pay()
    print(f"{Employee.name} earns {pay}.")
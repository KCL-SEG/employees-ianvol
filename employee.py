"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, explanation):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class MonthlyEmployee:
    def __init__(self, name, monthly_salary, bonus, commission_per_contract, num_contracts, explanation):
        super().__init__
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus = bonus
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts
        self.explanation = explanation

    def get_pay(self):
        return self.monthly_salary + self.bonus + (self.commission_per_contract*self.num_contracts)
    
class ContractEmployee:
    def __init__(self, name, hourly_rate, hours_worked, commission_per_contract, num_contracts, explanation):
        super().__init__
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts
        self.explanation = explanation

    def get_pay(self):
        base_pay = self.hourly_rate * self.hours_worked
        commission = self.commission_per_contract * self.num_contracts
        return base_pay + commission

billie = MonthlyEmployee('Billie', 4000, 0, 0, 0, 'Billie works on a monthly salary of 4000. Their total pay is 4000.')
charlie = ContractEmployee('Charlie', 25, 100, 0, 0, 'Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.')
renee = MonthlyEmployee('Renee', 3000, 0 , 200, 4, 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.')
jan = ContractEmployee('Jan', 25, 150, 220, 3, 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.')
robbie = MonthlyEmployee('Robbie', 2000, 1500, 0, 0, 'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.')
ariel = ContractEmployee('Ariel', 30, 120, 600, 1, 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.')

employees = [billie, charlie, renee, jan, robbie, ariel]

for Employee in employees:
    pay = Employee.get_pay()
    print(f"{Employee.name} earns {pay}.")
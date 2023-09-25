"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class SalaryWithoutCommissionEmployee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class HourlyWithoutCommissionEmployee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."

class SalaryWithBonusCommissionEmployee:
    def __init__(self, name, monthly_salary, bonus):
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def get_pay(self):
        return self.monthly_salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."

class HourlyWithBonusCommissionEmployee:
    def __init__(self, name, hourly_rate, hours_worked, bonus):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus = bonus

    def get_pay(self):
        base_pay = self.hourly_rate * self.hours_worked
        bonus = self.bonus
        total_pay = base_pay + bonus
        return total_pay

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."

class SalaryWithContractCommissionEmployee:
    def __init__(self, name, monthly_salary, commission_per_contract, num_contracts):
        self.name = name
        self.monthly_salary = monthly_salary
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts

    def get_pay(self):
        return self.monthly_salary + (self.commission_per_contract * self.num_contracts)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

class HourlyWithContractCommissionEmployee:
    def __init__(self, name, hourly_rate, hours_worked, commission_per_contract, num_contracts):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.commission_per_contract = commission_per_contract
        self.num_contracts = num_contracts

    def get_pay(self):
        base_pay = self.hourly_rate * self.hours_worked
        commission = self.commission_per_contract * self.num_contracts
        total_pay = base_pay + commission
        return total_pay

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


billie = SalaryWithoutCommissionEmployee('Billie', 4000)
charlie = HourlyWithoutCommissionEmployee('Charlie', 25, 100)
renee = SalaryWithContractCommissionEmployee('Renee', 3000, 200, 4)
jan = HourlyWithContractCommissionEmployee('Jan', 25, 150, 220, 3)
robbie = SalaryWithBonusCommissionEmployee('Robbie', 2000, 1500)
ariel = HourlyWithBonusCommissionEmployee('Ariel', 30, 120, 600)

employees = [billie, charlie, renee, jan, robbie, ariel]

for Employee in employees:
    pay = Employee.get_pay()
    print(f"{Employee.name} earns {pay}.")
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

def get_pay(Employee):
    pay = 0
    match Employee:
        case "billie":
            pay = 4000
            print("Billie works on a monthly salary of 4000.  Their total pay is 4000.")
        case "charlie":
            pay = 100 * 25
            print("Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.")
        case "renee":
            pay = 3000 + 4(200)
            print("Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.")
        case "jan":
            pay = (150*25) + (3*220)
            print("Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.")
        case "robbie":
            pay = 2000 + 1500
            print("Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.")
        case "ariel":
            pay = (120*30) + 600
            print("Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.")



class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Nabin', 'Dhami', 500000)
emp_2 = Employee('Santosh', 'Tiwari', 600000)
print(emp_1.fullname(), emp_1.pay)
print(emp_2.fullname(), emp_2.pay)

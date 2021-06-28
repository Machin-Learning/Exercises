class Employee:
    def __init__(self,full_name,**a):
        self.full_name = full_name
        self.a = a
        self._first_name = self.full_name.split(' ')[0]
        self.last_name = self.full_name.split(' ')[1]


Nancy = Employee('Nancy Draw')
Maya = Employee('Maya Jones',salary = 72000)
William = Employee('William Smith',salary=60000,dept='Accounting')

print(Nancy._first_name)
print(Maya.last_name)
print(William.dept)
class Ones_threes_nines():
    def __init__(self,num):
        self.num = num
        self.ones = self.count_ones()
        self.threes = self.count_threes()
        self.nines = self.count_nines()

    def count_ones(self):
        return self.num

    def count_threes(self):
        return int(self.num/3)

    def count_nines(self):
         return int(self.num/9)


test1 = Ones_threes_nines(5)
print(test1.ones)
print(test1.threes)
print(test1.nines)
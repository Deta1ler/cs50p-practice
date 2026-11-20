class PiggyBank:
    def __init__(self, balance=0.0):
        if balance < 0:
            raise ValueError("Отрицательный баланс")
        self.balance = balance #self.balance это поле, свойство .balance которое принадлежит конкретному
                               #обьекту self


    def deposit(self, amount):    #обязательное наличие self
        if amount <= 0:
          raise ValueError("Нельзя положить 0 или отрицательную сумму") 
        self.balance = self.balance + amount



bank_a = PiggyBank(100) #PiggyBank(100) - constructor call (вызов конструктора)
                        #фактически это инит обьекта, а потом присвоение его переменной 
                        #bank_a(экземпляр)
                        #bank_a.__init__(100) равносильно PiggyBank.__init__(bank_a, 100)

bank_a.deposit(50)
print(bank_a.balance)

from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self,amount):
        return float(amount)

class CardPayment(Payment):
    def pay(self,amount):
        return float(amount)        

upi = UPIPayment()
print(upi.pay(1000))

card = CardPayment()
print(card.pay(2000))
from savingsaccount import SavingsAccount

class Bank(object):
    def __init__(self):
        self.accounts= {}

    def __str__(self):
        return '\n'.join(map(str,self.accounts.values()))

    def makeKey(self,name,pin):
        return name + '/' + str(pin)
    
    def add(self,account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account
    
    def remove(self,name,pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key,None)

    def get(self,name,pin):
        key = self.makeKey(name,pin)
        return self.accounts.get(key,None)
    
    def computeInterest(self):
        total = 0.0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total
    
def createBank(num):
    bank = Bank()
    lstNames = ['Mark', 'Karl', 'Jarold', 'Angel', 'Jhoana']
    pins = 1000

    for names in range(num):
        bank.add(SavingsAccount(lstNames[names], pins, 5000.00))
        pins +=1
    
    return bank
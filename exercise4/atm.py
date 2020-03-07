from breezypythongui import EasyFrame
from bank import Bank, createBank
import tkinter

class ATM(EasyFrame):
    def __init__(self,bank):
        EasyFrame.__init__(self,title = "ATM", width=500, height=150)
        self.bank = bank
        self.account = None
        #simple labels 
        self.nameLabel = EasyFrame.addLabel(self, "Name",1,1)
        self.pinLabel = EasyFrame.addLabel(self, "PIN",3,1)
        self.amountLabel = EasyFrame.addLabel(self,"Amount",5,1)
        self.statusLabel = EasyFrame.addLabel(self,"Status",7,1)


        #creating I/O text fields
        self.nameField = EasyFrame.addTextField(self,"", 1, 2)
        self.pinField = EasyFrame.addTextField(self, "", 3,2 )
        self.amountField = EasyFrame.addFloatField(self,"",5,2)
        self.statusField = EasyFrame.addTextField(self,"", 7,2)

        #creating buttons for user to click
        self.balanceButton = EasyFrame.addButton(self,"Balance", 1,3)
        self.depositButton = EasyFrame.addButton(self, "Deposit", 3,3)
        self.widthdrawButton = EasyFrame.addButton(self, "Withdraw", 5,3)
        self.loginButton = EasyFrame.addButton(self,"Login", 7,3)
 
        #connecting buttons to the appropriate functions
        self.loginButton['command'] = self.login
        self.balanceButton['command'] = self.getBalance
        self.depositButton['command'] = self.sendDeposit
        self.widthdrawButton['command'] = self.getWithdraw
        self.trials = 0 #counting the number of trials of logins

        #states of the buttons when first opened
        self.balanceButton['state'] = 'disabled'
        self.depositButton['state'] = 'disabled'
        self.widthdrawButton['state'] = 'disabled'

        

        
    def login(self):
        
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name,pin)
        if self.account: 
            self.trials = 0
            self.statusField.setText("Hello, " + name + "!")
            self.balanceButton['state'] = 'normal'
            self.depositButton['state'] = 'normal'
            self.widthdrawButton['state'] = 'normal'
            self.loginButton['state'] = 'normal'
            self.loginButton['text'] = 'Logout'
            self.loginButton['command'] = self.logout 
        else:
            self.statusField.setText("Name and pin not found!")
            self.trials +=1
            print(self.trials)
            if self.trials >= 3:
                self.balanceButton['state'] = 'disabled'
                self.depositButton['state'] = 'disabled'
                self.widthdrawButton['state'] = 'disabled'
                self.loginButton['state'] = 'disabled'
                self.warning = EasyFrame.messageBox(self, title = "WARNING", message = "POLICE REINFORCEMENTS ON THEIR WAY TO YOUR LOCATION")
                
    
    def logout(self):
        self.account = None
        self.nameField.setText('')
        self.pinField.setText('')
        self.amountField.setNumber(0)
        self.statusField.setText('Welcome to the Bank!')
        self.balanceButton['state'] = 'disabled'
        self.depositButton['state'] = 'disabled'
        self.widthdrawButton['state'] = 'disabled'
        self.loginButton['text'] = 'Login'
        self.loginButton['command'] = self.login

    def getBalance(self):
        balance = self.account.getBalance()
        self.statusField.setText("Balance: $"+ str(balance))
    
    def getWithdraw(self):
        amount = self.amountField.getNumber()
        message = self.account.widthdraw(amount)
        if message:
            self.statusField.setText(message)
        else:
            self.statusField.setText("Withdrawal successful!")
    
    def sendDeposit(self):
        amount = self.amountField.getNumber()
        self.account.deposit(amount)
        self.statusField.setText("Amount of " + str(amount) + " deposited")



def main(fileName = None):

    if not fileName: 
        bank = createBank(5)
    else:
            bank(fileName)
    print(bank)
    atm = ATM(bank)
    atm.mainloop()

if __name__ == '__main__':
    main()
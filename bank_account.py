class BankAccount():

    def __init__(self, owner, balance):
         self.owner = owner
         self.balance = balance
    
    def deposit(self):

        valid_flag = False
        while not valid_flag:
            money = input('how money you wants to deposit ?')
            money = int(money)
            if (money > 0):
                bill_of_twenty = int(input('how money of bill 20$ wants to deposit ?'))
                bill_of_fifty = int(input('how money of bill 50$ wants to deposit ?'))
                bill_of_hundred = int(input('how money of bill 100$ wants to deposit ?'))
                sum_user_deposited = ((bill_of_twenty * 20) + (bill_of_fifty * 50) + (bill_of_hundred * 100))
                print('the sum of money you want to deposit is {}$' .format(sum_user_deposited))
                self.balance = self.balance + sum_user_deposited
                another_deposit = input(' you want to deposit more bills ? yes/no')
                if another_deposit == 'yes':
                    valid_flag = False                  
                else:
                    return ' Your balance for today is {}$ \n bye bye have a nice day!' .format(self.balance)
            else:
                return 'cant accept the deposit is invaled !!'
                 

    def withdraw(self):

        withdraws_money = int(input('how money you want to withdraw ?'))
        if(withdraws_money < self.balance):
            if(withdraws_money < 20 ):
                return 'an not withdraw the this amount'
            if(withdraws_money >= 20 and withdraws_money <= 100 ):
                if( withdraws_money % 20 == 0 or withdraws_money == 70 or withdraws_money == 90):
                    new_balance = self.balance - withdraws_money
                    return('your balance is {}$' .format(new_balance)) 
                else:
                    return 'can not withdraw the this amount'
            if(withdraws_money > 100):
                if(withdraws_money % 10 == 0):
                    new_balance = self.balance - withdraws_money
                    return('your balance is {}$' .format(new_balance))              
                else:
                    return 'can not withdraw the this amount'
        return 'can not withdraw the this amount, there is not a sufficient balance'

class Owner(BankAccount):

    def __init__(self, credit_card_number, password, owner, balance):
         super().__init__(owner, balance)
         self.credit_card_number = credit_card_number
         self.password = password

    def check_owner_info(self):

        chance = 0
        while chance < 2:
            credit_card_number = input('please enter the credit card number')
            password = input('please enter the password')        
            if(credit_card_number == self.credit_card_number and password == self.password):
                chose = input('you wants to deposit or to withdraw ?')
                if (chose == 'deposit'):
                    return(self.deposit())
                if (chose == 'withdraw'):
                    return(self.withdraw())
                else:
                    return 'your choice not available!'
            else:
                chance = chance + 1
                print ('one ore more from the details wrong, try again !' ) 
        return ' the card has been eaten by the machine !! '
        

if __name__ == '__main__':
    my_account = Owner('1234','123','abeer', 350)
    print(my_account.check_owner_info())

class OnlineWallet:
    balance = 0
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def get_name(self):
        return self.name
        
    def get_balance(self):
        return self.balance       
  
    def set_balance(self, balance):
        print('Введите новый баланс клиента:')
        self.balance = balance

    def display_info(self):
        print(f'Клиент "{self.name}". Баланс: {self.balance} руб.')
        
Ivan = OnlineWallet('Иван Петров')
Ivan.display_info()
Ivan.balance = 50
Ivan.display_info()

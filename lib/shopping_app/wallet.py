class Wallet:
    
    from ownable import set_owner
    
    owner = None
    def __init__(self, owner): #recibe el objeto User/Seller como "owner" 
        self.set_owner(owner) #wallet.owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount

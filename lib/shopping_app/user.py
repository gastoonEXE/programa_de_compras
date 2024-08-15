from wallet import Wallet

class User:
    from item_manager import show_items, items_list, pick_items, show_items

    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)   #se crea un objeto Wallet al cual se le pasa el objeto User/Seller
        # Cuando se crea una instancia de Usuario o una instancia de una clase 
        #que hereda el Usuario, tiene una billetera con él mismo como propietario.   
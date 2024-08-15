from customer import Customer
from item import Item
from seller import Seller

seller = Seller("tienda DIC") # seller (vendedor) se declara como objeto Seller

for i in range(10):
    Item("CPU", 40830, seller)
    Item("memoria", 13880, seller)
    Item("placa madre", 28980, seller)
    Item("unidad de fuente de alimentación", 8980, seller)
    Item("caja de la computadora", 8727, seller)
    Item("HDD de 3,5 pulgadas", 10980, seller)
    Item("SSD de 2,5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("enfriador de CPU", 13400, seller)
    Item("tablero grafico", 23800, seller)

print("🤖 por favor dime tu nombre")
customer = Customer(input())

print("🏧 Por favor ingresa el monto a cargar a tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ empezar a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor ingrese el número de producto")
    number = int(input())

    print("⛏ Por favor ingrese la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
        
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 cantidad total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres terminar de comprar?(yes/no)")
    end_shopping = input() == "yes"

print("💸 ¿Confirmar tu compra?(yes/no)")
if input() == "yes":
    customer.cart.check_out()

    
print("\n\n\n୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name} propiedad de")
customer.show_items() #tengo que mostrar lo comprado
print(f"😱👛 {customer.name} saldo de billetera de: {customer.wallet.balance}")

print(f"📦 {seller.name} estado del stock")
seller.show_items() # se tiene que mostrar lo que le sobro del stock
print(f"😻👛 {seller.name} saldo de billetera de: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items() # se muestra lo del carrito (tiene que estar vacio)
print(f"🌚 cantidad total: {customer.cart.total_amount()}")

print("🎉 fin")

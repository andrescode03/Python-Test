# PRUEBA FINAL PYTHON

# Create a dictionary for save the products 
inventory = {}

# I create 7 funtions for make diferents options to later call one to one

# This funtion is for push a product at the inventory (dictionary)
def push_product(name, price, quantity): 
    if name in inventory:
        print("este producto ya se encuentra agregado dentro del inventario")
    # If the name what the user put in the option, is not in the inventory, we can save in the inventory
    else:
        inventory[name ] = (price, quantity)
        print(f"Producto '{name}' añadido correctamente.")

# This funtion is for search the products what are in the inventory 
def search_product(name):
    if name  in inventory:
        price, quantity = inventory[name]
        print(f"{name} - Precio: {price} y la Cantidad: {quantity}")
    else:
        print("Producto no encontrado en el inventario.")

# This funtions i for update or renew de price of some product what are in the inventory 
def update_price(name , new_price):
    if name  in inventory:
        _, quantity = inventory[name]
        inventory[name ] = (new_price, quantity)
        print(f"Precio de '{name}' actualizado a {new_price}.")
    else:
        print("Producto no encontrado en el inventario.")
# This funtion is for remove or delete some product what are in the inventory
def delete_product(name):
    if name  in inventory:
        del inventory[name ]
        print(f"Producto '{name}' eliminado del inventario.")
    else:
        print("Producto no encontrado en el inventario.")

# This funtion is for calculate the total coast of the inventory, i use a other funtion (lambda), to make this operation
# Lambda is just for saw the values in the inevntory and make the operation
def total_inventory():
    calcular_valor = lambda: sum(price * quantity for price, quantity in inventory.values())
    total = calcular_valor()
    print(f"Valor total del inventario: {total}")

# This funtion is for valid product at the inventory, with the Name, Price and quantity
def save_products():
    name = input("Ingrese el nombre del producto: ")
    #In this option i create a try-except for validate if the number what user put in price and quatity is a positive number 
    try:
        price = float(input("Ingrese el precio del producto: "))
        quantity = int(input("Ingrese la cantidad disponible: "))
        if price < 0 or quantity < 0:
            print("El precio y la cantidad deben ser positivos.")
        else:
            push_product(name, price, quantity)
    except ValueError:
        print("Debes ingresar números válidos para el precio y la cantidad.")


# I create a funtion for a menu options, this funtion is a bucle while, for iterar till the user choose or put the correct option
def menu():
    while True:
        print("\n--- THE STORE ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Ver inventario completo")
        print("6. Calcular valor total del inventario")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        # Then i create diferent contionals for the options, here the user choose the option and the program return a funtion
        if opcion == "1":
            save_products()
        if opcion == "2":
            name = input("Ingrese el nombre del producto a consultar: ")
            search_product(name)
        elif opcion == "3":
        # In this option i create a try-except for validate if the number what user put is a positive number 
            name = input("Ingrese el nombre del producto: ")
            try:
                new_price = float(input("Ingrese el nuevo precio: "))
                if new_price < 0:
                    print("El precio debe ser positivo.")
                else:
                    update_price(name, new_price)
            except ValueError:
                print("Debes ingresar un número válido para el precio.")
        elif opcion == "4":
            name = input("Ingrese el nombre del producto a eliminar: ")
            delete_product(name)
        elif opcion == "5":
            # This option run for the key an values of the inventory and print the inventory from the store
            if inventory:
                print("\nInventario actual:")
                for name, (price, quantity) in inventory.items():
                    print(f"{name} - Precio: {price} - Cantidad: {quantity}")
            else:
                print("El inventario está vacío.")
        elif opcion == "6":
            total_inventory()
        elif opcion == "7":
            print("Llegaste al final de la tienda")
            break

menu()

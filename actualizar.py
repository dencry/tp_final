import sqlite3, mostrar
from colorama import Fore, init

init(autoreset=True)

def actualizar_un_producto():
    """
    Permite eliminar un producto de la lista
    """

    #conectar a la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:
        print(Fore.CYAN + "\n=== 'ACTUALIZAR' un producto ===")

        # Mostrar todos los productos y comprobar 
        if not mostrar.mostrar_lista_de_productos():
            print(Fore.YELLOW + "\n[INFO] No hay productos registrados en la base de datos.")
            return

        #Id del producto a actualizar
        id_producto = input("\nIngrese el ID del producto a 'ACTUALIZAR': ")

        if not id_producto.isdigit():
            print(Fore.RED + "\n[ERROR] El ID ingresado no es valido.")
            return
        
        id_producto = int(id_producto)

        # Verificar si el producto esta en la base de datos
        cursor.execute("SELECT nombre, categoria FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.YELLOW + "\nNo se encontro el producto en la base de datos.")
            return
        
        mostrar.menu_actualizar()

        opcion = input("\nElige una opción: ")

        if opcion == "1":

            nuevo_precio = input("\nIngrese el nuevo precio a 'ACTUALIZAR': ")

            if not nuevo_precio.isdigit():
                print(Fore.RED + "\n[ERROR] El PRECIO ingresado no es valido.")
                return

            nuevo_precio = int(nuevo_precio)
            
            #Confirmar antes la actualizaciion
            confirmar = input(Fore.YELLOW + f"\n¿Esta seguro que quiere 'ACTUALIZAR' el producto {producto[0]} {producto[1]}? (S/N): ").strip().lower()

            if "" != confirmar != "s":
                print(Fore.GREEN + "\nLa actualización ah sido cancelada.")
                return

            # Actualizar el precio del producto
            cursor.execute('UPDATE productos SET precio = ? WHERE id = ?', (nuevo_precio, id_producto))
            conexion.commit()

            print(Fore.GREEN + f"\n[EXITO] El producto '{producto[0]}' '{producto[1]}' fue actualizado correctamente.")

        elif opcion == "2":

            nuevo_stock = input("\nIngrese el nuevo stock a 'ACTUALIZAR': ")

            if not nuevo_stock.isdigit():
                print(Fore.RED + "\n[ERROR] El stock ingresado no es valido.")
                return

            nuevo_stock = int(nuevo_stock)
            
            #Confirmar antes la actualizaciion
            confirmar = input(Fore.YELLOW + f"\n¿Esta seguro que quiere 'ACTUALIZAR' el producto {producto[0]} {producto[1]}? (S/N): ").strip().lower()

            if "" != confirmar != "s":
                print(Fore.GREEN + "\nLa actualización ah sido cancelada.")
                return

            # Actualizar el stock del producto
            cursor.execute('UPDATE productos SET stock = ? WHERE id = ?', (nuevo_stock, id_producto))

            #Confirmar la transacción
            conexion.commit()

            print(Fore.GREEN + f"\n[EXITO] El producto '{producto[0]}' '{producto[1]}' fue actualizado correctamente.")

        else:
            print(Fore.RED + "\n[ERROR] Opcion no valida.")

    except sqlite3.Error as e:
        print(Fore.RED + f"\n[ERROR] Se produjo un error al actualizar el precio del producto: {e}")

    finally:
        conexion.close()
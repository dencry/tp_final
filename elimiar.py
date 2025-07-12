import sqlite3, mostrar
from colorama import Fore, init

init(autoreset=True)

def eliminar_un_producto():
    """
    Permite eliminar un producto de la lista
    """

    #conectar a la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:
        print(Fore.CYAN + "\n=== 'Eliminar' un producto ===")

        # Mostrar todos los productos
        if not mostrar.mostrar_lista_de_productos():
            print(Fore.YELLOW + "\n[INFO] No hay productos registrados en la base de datos.")
            return

        #Id del producto a eliminar
        id_producto = input("\nIngrese el ID del producto a 'ELIMINAR': ")

        if not id_producto.isdigit():
            print(Fore.RED + "\n[ERROR] El ID ingresado no es valido.")
            return
        
        id_producto = int(id_producto)

        # Verificar si el producto en la base de datos
        cursor.execute("SELECT nombre, categoria FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        # Mostrar un mensaje si no se encontro
        if not producto:
            print(Fore.YELLOW + "\nNo se encontro el producto en la base de datos.")
            return
        
        #Confirmar antes de eliminar
        confirmar = input(Fore.YELLOW + f"¿Esta seguro que quiere eliminar el producto {producto[0]} {producto[1]}? (S/N): ").strip().lower()

        if "" != confirmar != "s":
            print(Fore.GREEN + "\nLa eliminacion del producto ah sido cancelada.")
            return

        #Eliminar el producto
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

        #Confirmar la transacción
        conexion.commit()

        print(Fore.GREEN + f"\n[EXITO] El producto '{producto[0]}' '{producto[1]}' fue eliminado correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error al eliminar el producto: {e}")

    finally:
        conexion.close()
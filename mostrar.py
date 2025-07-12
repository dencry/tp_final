import sqlite3
from colorama import Fore, init

init(autoreset=True)

def menu_pricipal():
    print(Fore.WHITE + f"""\n{"":=^32}
******** Menu Principal ********
{"":=^32}
1. Regristrar un nuevo producto
2. Mostrar productos registrados
3. Actualizar un producto
4. Eliminar un producto
5. Buscar un producto por ID
6. Informacion de Stock
{"":=^32}
7. Salir""")
    
def menu_actualizar():
    print(Fore.WHITE + """{"":=^32}
\n¿Que desea actualizar?
{"":=^32}
1. Actualizar precio
2. Actualizar Stock
""")

def mostrar_lista_de_productos():
    """
    Muestra todos los productos de la base de datos.
    """
    
    # Sincronizar con la Base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:

        cursor.execute("SELECT id, nombre, precio, stock, categoria, descripcion FROM productos")
        productos = cursor.fetchall()

        if productos:
            print(Fore.CYAN + "\n=== 'LISTA' de productos ===\n")

        for producto in productos:
            print(Fore.WHITE + f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]} u., Categoria: {producto[4]}, Descripcion: {producto[5]}.")

        # Cerrar coneccion
        conexion.close()

        return productos

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error: {e}")

    finally:
        conexion.close()

def mostrar_producto_por_id():
    """
    Mostrar producto por su ID
    """

    # Sincronizar con la Base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
        
    try:
        # Id del producto a mostrar
        id_producto = input("\nIngrese el ID del producto: ")

        if not id_producto.isdigit():
            print(Fore.RED + "\n[ERROR] El ID ingresado no es valido.")
            return
        
        id_producto = int(id_producto)

        # Verificar si el producto en la base de datos
        cursor.execute("SELECT nombre, categoria FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.YELLOW + "\nNo se encontro el producto en la base de datos.")
            return
        
        print(Fore.WHITE + f"\nNombre: {producto[0]} Categoria: {producto[1]}.")

        # Cerrar coneccion
        conexion.close()

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error: {e}")

    finally:
        conexion.close()

def reporte_de_productos():
    pass
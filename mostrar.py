import sqlite3, crear
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
6. Reporte de stock
{"":=^32}
7. Salir""")
    
def menu_actualizar():
    print(Fore.WHITE + f"""{"":=^32}
¿Que desea actualizar?
{"":=^32}
1. Actualizar precio
2. Actualizar Stock""")
    
def registrar():
    # Muestro un menu para registrar un producto
    print(Fore.CYAN +  "\n=== 'REGISTAR' un nuevo producto ===\n")

    #Solicitar datos con validaciones vasicas
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    descripcion = input("Ingrese una breve descripción del producto: ")
    stock = input("Ingrese la cantidad disponible del producto: ").strip()
    precio = input("Ingrese el precio del producto: ").strip()
    categoria = input("Ingrese la categoria del producto: ").strip().lower()

    crear.cargar_producto(nombre, stock, precio, descripcion, categoria)

def mostrar_lista_de_productos():
    """ Muestra todos los productos de la base de datos. """
    
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

        return productos

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error: {e}")

    finally:
        conexion.close()

def mostrar_producto_por_id():
    """ Mostrar producto por su ID """

    # Sincronizar con la Base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
        
    try:
        # Id del producto a mostrar
        id_producto = input("\nIngrese el ID del producto: ").strip()

        if not id_producto.isdigit():
            print(Fore.RED + "\n[ERROR] El ID ingresado no es valido.")
            return
        
        id_producto = int(id_producto)

        # Verificar si el producto en la base de datos
        cursor.execute("SELECT nombre, precio, stock, categoria, descripcion FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.YELLOW + "\nNo se encontro el producto en la base de datos.")
            return
        
        print(Fore.CYAN + f"\n=== Informacion de productos con el ID {id_producto} ===")

        print(Fore.WHITE + f"\nNombre: {producto[0]}, Precio: ${producto[1]}, Stock: {producto[2]}u., Categoria: {producto[3]}, Descripcion: {producto[4]}.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error: {e}")

    finally:
        conexion.close()

def reporte_de_productos():
    """ Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario """

    # Sincronizar con la Base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:
        limite = input("\nIngrese el límite de stock: ").strip()

        if not limite.isdigit():
            print(Fore.RED + "\n[ERROR] El límite debe ser un número entero positivo.")
            return

        limite = int(limite)

        cursor.execute("SELECT id, nombre, precio, stock, categoria, descripcion FROM productos WHERE stock <= ? ", (limite,))
        productos = cursor.fetchall()

        if not productos:
            print(Fore.YELLOW + f"\nNo hay productos con stock menor o igual a {limite} u.")
            return

        print(Fore.CYAN + f"\n=== Productos con stock menor o igual a {limite}u. ===\n")

        for producto in productos:
            print(Fore.WHITE + f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]}u., Categoria: {producto[4]}, Descripcion: {producto[5]}.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error: {e}")

        # Registro
        crear.registro(f"[ERROR] Se produjo un error: {e}")

    finally:
        conexion.close()
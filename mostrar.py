import sqlite3
from colorama import Fore, init

init(autoreset=True)

# Stock minimo
stock_minimo = 50

def menu_pricipal():
    print(Fore.WHITE + f"""\n{"":=^32}
******** Menu Principal ********
{"":=^32}
1. Regristrar un nuevo producto
2. Mostrar productos registrados
3. Actualizar un producto
4. Eliminar un producto
{"":=^32}
5. Salir""")
    
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
            print(Fore.WHITE + f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]} u., Categoria: {producto[4]}, Descripcion: {producto[5]}.",end="")
            # Comprobar stock si es bajo
            if producto[3] > stock_minimo:
                print(Fore.YELLOW +"[INFO] stock bajo.")
            else:
                print()

        # Cerrar coneccion
        conexion.close()

        return productos

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Se produjo un error: {e}")

    finally:
        conexion.close()
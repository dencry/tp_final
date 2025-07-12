import sqlite3
from colorama import Fore, init

init(autoreset=True)

def crear_db():
    #Conexion a la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    #Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >= 0),
            precio REAL NOT NULL CHECK(precio > 0),
            categoria TEXT NOT NULL
        )
    ''')

    #Confirmar los cambios y cerrar la coneccion
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "\n[INFO] La base de datos fue creada con exito!")

def cargar_producto():
    """
    Solicitar los datos del producto y registrarlo en la base de datos, validando la entrada.
    """

    #conectar a la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:
        print(Fore.CYAN +  "\n=== 'REGISTAR' un nuevo producto ===\n")

        #Solicitar datos con validaciones vasicas
        nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
        descripcion = input("Ingrese la descripcion del producto: ")
        stock = input("Ingrese la cantidad del producto: ").strip()
        precio = input("Ingrese el precio del producto: ").strip()
        categoria = input("Ingrese la categoria del producto: ").strip().lower()

        #Validacion
        if not nombre or not descripcion or not categoria:
            print(Fore.RED + "\n[ERROR] EL nombre, descripcion y categotia no pueden estar vacíos.")
            return

        if not stock.isdigit() or not precio.isdigit():
            print(Fore.RED + "\n[ERROR] La Cantidad/Precio debe ser numerico.")
            return
        
        #Insertar en la base de datos
        cursor.execute('''INSERT INTO productos (nombre, descripcion, stock, precio, categoria) VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, stock, precio, categoria))
        
        #Confirmar la transacción
        conexion.commit()

        print(Fore.GREEN + f"\n[EXITO] El producto '{nombre.upper()}' fue agregado correctamente.")

    except sqlite3.Error as e:

        print(Fore.RED + f"\n[ERROR] Error en la base de datos: {e}.")

    finally:
        conexion.close()
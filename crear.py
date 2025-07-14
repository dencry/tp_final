import sqlite3, mostrar, datetime
from colorama import Fore, init

init(autoreset=True)

def registro(mensaje):
    # Registro en archivo de texto
        archivo = open("nombres.txt", "a", encoding="utf-8")
        archivo.write(f"[{datetime.datetime.now()}] {mensaje}\n")
        archivo.close()

def crear_db():
    # Conexion a la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    # Crear tabla si no existe
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

def cargar_producto(nombre, stock, precio, descripcion= "None", categoria = "None"):
    """ Solicitar los datos del producto y registrarlo en la base de datos, validando la entrada. """

    #conectar a la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()

    try:
        #Validacion
        if not nombre:
            print(Fore.RED + "\n[ERROR] EL nombre no pueden estar vacíos.")
            return

        if not stock.isdigit():
            print(Fore.RED + "\n[ERROR] La Cantidad debe ser numerico.")
            return
        
        if not precio.isdigit():
            print(Fore.RED + "\n[ERROR] El precio debe ser numerico.")
            return
        
        if precio < 0 or stock <= 0:
            print(Fore.RED +"\n[ERROR] El producto/cantidad no deven se menos o igual a 0.")
            return
        
        stock, precio = int(stock), float(precio)
        
        #Insertar en la base de datos
        cursor.execute('''INSERT INTO productos (nombre, descripcion, stock, precio, categoria) VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, stock, precio, categoria))
        
        #Confirmar la transacción
        conexion.commit()

        print(Fore.GREEN + f"\n[EXITO] El producto '{nombre.upper()}' fue agregado correctamente.")

        # Registro
        registro(f"Se carco un nuevo producto: '{nombre.upper()}'.")

    except sqlite3.Error as e:
        print(Fore.RED + f"\n[ERROR] Error en la base de datos: {e}.")

        # Registro
        registro(f"\n[ERROR] Error en la base de datos: {e}.")

    finally:
        conexion.close()
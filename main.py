# Importacion de CRUD y Colorama

import crear, mostrar, actualizar, elimiar
from colorama import Fore, init

init(autoreset=True)
        
def main():
    
    crear.crear_db()

    while True:
        mostrar.menu_pricipal()

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            # Regristrar un nuevo producto
            crear.cargar_producto()
        
        elif opcion == "2":
            # Mostrar productos registrados
            if not mostrar.mostrar_lista_de_productos():
                print(Fore.YELLOW + "\n[INFO] No hay productos registrados en la base de datos.")
        
        elif opcion == "3":
            # Actualizar un producto
            actualizar.actualizar_un_producto()

        elif opcion == "4":
            # Eliminar un producto
            elimiar.eliminar_un_producto()

        elif opcion == "5":
            # Salis del programa
            print(Fore.GREEN + "\nGracias por ultilizar el sistema. ¡Hasta luego!\n")
            break

        else:
            print(Fore.RED + "\n[ERROR] Opcion no valida.")

        #Mensaje para continuar
        input(Fore.YELLOW + "\nPrecione 'ENTER' para continuar...")

main()
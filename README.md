# Entrega de TFI (Trabajo Final Integrador) de Talento Tech. 12/7/2025

# Nombre y Apellido: Damian Fabian Madroñal
# DNI: 34600962
# Email: dmx02277@gmail.com

<!-- Mensaje del profesor: -->

<!-- Hola Damián,

A la primera ejecución, el programa falla con un error crítico y no permite agregar productos. 

En estas líneas de la función cargar_producto() del módulo crear.py:

        if precio < 0 or stock <= 0:
            print(Fore.RED +"\n[ERROR] El producto/cantidad no deven se menos o igual a 0.")
            return
        
        stock, precio = int(stock), float(precio)
Hay una validación incorrecta porque estás comparando precio y stock, que todavía son un tipo de dato string, con números; utilizando operadores de comparación (if precio < 0 or stock <= 0). 

Eso no es posible, sin antes convertir el string del input a dato numérico, razón por la cual devuelve error crítico en la línea 56. Siempre debemos realizar las conversiones de string a número antes de evaluar condiciones donde haya números implicados. Vos estás haciendo la conversión en la línea 60, es decir, después de la evaluación de condiciones de la línea 56. Por esto el programa no puede agregar el producto, dado que al no pasar la validación no graba en la base de datos ningún valor. Corrigiendo el agregado de la conversión antes de evaluar las condiciones podría operarse con esa funcionalidad de agregar productos.

De todas formas, analizando el código además de la organización en módulos separados del programa, en cada uno de los módulos, usaste funciones para encapsular y modularizar las distintas operaciones ofrecidas en el menú.

La implementación de colorama, sin duda, le aportará mayor legibilidad y una rápida identificación de los mensajes devueltos por la consola.

Aplicas manejo de errores con try-except al hacer las validaciones y conversiones, al procesar los input para actualizar, eliminar, al realizar la consulta sql para mostrar. Genera un reporte al iniciar el programa creando un txt.

Recordemos la importancia de implementar manejo de transacciones para poder aplicar "rollback" ante problemas de lecto-escritura en la base de datos. 

El código, en su conjunto, está bien organizado y cumple con la consigna.
Felicitaciones por el trabajo realizado, Damián.
Saludos,
Matías. -->
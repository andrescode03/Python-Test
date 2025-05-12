# Python-Test

# Este trabajo esta elaborado con Python3

### La prueba de final de Python, se basaba en contruir un menú de opciones par auna tienda, en la cual el usuario pudiera escoger entre las diferentes opciones que se le prensentan, y de esta manera poder gestionar su inventario de manera efectiva.

Para desarrollar este programa, lo principal fue crear un estructura que guardara los datos que le requerimos al usuario.
Los diccionarios en Python, son una forma organizada de almacenar estos datos y poder luego buscarlos por su llave y su valor.

### Para este caso damos el siguiente ejemplo de un diccionario, para referenciarnos mejor.
Inventario = {
  "arroz" : 3.500
}

Para este caso, vemos que dentro de un diccionario se almacenan datos, en el ejemplo anterio tenemos que la llave es el "arroz" y el valor es "3.500".

Para el proyecto del inventario en una tienda, creamos diferentes funciones dentro de Python, esto nos permite crear dentro de cad auna un flujo de trabajo, para ahorrarnos trabajo y refetir lineas de codigo cuando tengamos que llevarle esa funcion al usuario.


- `Funcionalidad 1`: Creamos una función para indicar en el diccionario que vamos a recibir 2 datos:
- 1. Una llave que va a ser el nombre del producto
  2. Una tupla con dos valores (el precio y la cantidad)
  
- `Funcionalidad 2`: En la segunda función le damos la opción al usuario de poder buscar un producto por su nombre.
  
- `Funcionalidad 3`: En esta función podemos llamar el producto que el usuario nos indique, y si este producto se encuentra dentro del inventario (diccionario), podemos actualizar el precio que el producto tenga actualmente.
- `Funcionalidad 4`: En la cuarta funcionalidad el usuario tiene la opcion de eliminar alguno de los productos.
  1. Debe buscarlo por su nombre
  2. Luego si este nombre coincide con algun producto que tengamos dentro el inventario, con la opcion (del), dentro de Python, nos permite eliminarla dentro del inventario (diccionario)
- `Funcionalidad 5`: En la función 3, nos permite calcular el total del inventario, teniendo muy presente que debemos hacer una operacion entre precio y cantidad de producto, para obtener de esta manera una cifra concreta de que tenemos en el inventario.
  1. Para esta función, tulizamos a su vez, una función (lambda), la cual se invoca en una sola oportunidad, y nos permite hacer por ejemplo una operación con los valores que tenemos dentro del inventario.
     ### calcular_valor = lambda: sum(price * quantity for price, quantity in inventory.values())
     Lo que hace como tal esta función, es hacer una suma y dentro de ella va a estar recorriendo en los valores del inventario, el precio y la cantidad para calcular el inventario.
- `Funcionalidad 6`: Esta función nos permite agregar productos al inventario con precio y cantidad, estos valores como se especifican en el código, deben ser númericos para que puedan tomarse dentro del programa, tambien deben ser positivos para que se reocnozca algún cambio dentro del mismo.

- `Funcionalidad 7`: La función 7, crea un menú de opciones para el usuario, de esta manera, el usuario podra empezar a elegir entre las opción que desee.
  En este punto resaltamos:
  1. La opciones del menú son las funciones que describimos anteriormente.
  2. Cada vez que el usuario elige una opción, loq ue hace el código en el back es que que ejecuta la función que esta anclada a esa opción.
 
  #Presentamos un ejemplo práctico

## Opciones de manú
  --- THE STORE ---
1. Añadir producto
2. Consultar producto
3. Actualizar precio
4. Eliminar producto
5. Ver inventario completo
6. Calcular valor total del inventario
7. Salir


# QLEON PROJECT

Qleon es un lenguaje de programación creado con motivos académicos.
Para esta primera parte del proyecto realizamos un lexer, a continuación se muestra una pequeña guía de usuario para poder usarlo.

### Tipos de datos

En Qleon utilizamos datos dinamicos, los cuales serán inferidos.

#### Ejemplo:

```
- 5  Entero.
- 6.2 Float
- "Hola" String.
```

### Declaración de variables

En Qleon la declaracion de variables es bastante sencilla, al utilizar datos dinámicos, solo se le debe indicar al lenguaje que variable se usará.


#### Ejemplo:

```

var = value ###Estructura de declaración

radio = 5

pi = 3.141592

saludo = "Hola mundo!"


```


### Comentarios

Los comentarios nos permiten incluir en nuestro código explicaciones o notas acerca de cada línea de código presente en nuestro programa.
En QLEON los comentarios se realizan usando 3 almohadillas.

#### Ejemplo

```
### Este es un Ejemplo de comentario.

```


### Imprimir en pantalla


Para imprimir en pantalla en Qleon se utiliza la sentencia show.

#### Ejemplo

```

show("Hola mundo")

```


### Operaciones matemáticas básicas.

En Qleon se admiten operaciones matemáticas básicas como suma, resta, multiplicación y división.


#### Ejemplo

```

suma = 5 +4

resta = 5-2

división = 8/4

multiplicacion = 12*4

operacionesCompuestas = (12*4)/2


```


### Condicionales

Para controlar el flujo en ciertas instrucciones se incluyen los condicionales en QLEON de la siguiente forma:


#### Ejemplo

```
if (x > 3){

    ### Código
}
```


### Operadores logicos y de comparación

Los operadores logicos y de comparación nos permitirán implementar condicionales más específicos en nuestras instrucciones.


### Operadores de comparación

Los operadores de comparación nos permitirán contrastar entre cantidades. 


```
> ### Mayor qué.

< ### Menor qué.

>= ### Mayor o igual qué.

<= ### Menor o igual qué.


```

### Operadores lógicos

Los operadores lógicos nos permiten evaluar expresiones lógicas, estas devuelven falso o verdadero.


```
&& ### Operador lógico AND.

|| ### Operador lógico OR.

```


### Ejemplo uso operadores lógicos y de comparación

```

if (x > 3 && x <5){
   ### Código
}


if (x > 3 || x >= 5){
   ### Código
}

```


### Funciones

En Qleon se admiten el uso de funciones como una forma de mejorar la división y reutilización del código de nuestro programa. Se declaran de la siguiente forma:

```

fun nombreFuncion(parametros){

    ### Codigo

}

```


### Ciclos

En Qleon se admiten los siguientes ciclos:


```

while (condicion){

    ### Codigo

}


for (condiciones){
    ### Codigo
}


```


### Esto es todo hasta ahora...

Qleon es un proyecto en desarrollo, con el tiempo se irán añadidendo características importantes.

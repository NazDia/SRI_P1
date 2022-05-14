# SRI_P1

## 1. Objetivos del Proyecto:

Se desea crear un Sistema de Recuperacion de Informacion capaz de recuperar los documentos deseados dado una consulta(query), devolviendo a partir de esta una lista conteniendo los mas importantes con respecto a los terminos que se buscan.

## 2. Modelo usado:

El modelo usado no es ninguno oficialmente definido; consiste en una mezcla de algunas caracteristicas del modelo booleano con otras del modelo vectorial.

Del modelo booleano se toma una parte de la formulacion de la consulta, la consulta consiste en tres conjuntos de palabras, las palabras claves a buscar, que, como en el modelo booleano, se les asigna como valor asociado 1. Tambien se pueden especificar palabras a excluir en la consulta (la busqueda no se realiza igual que el modelo booleano por lo que se usa de modo distinto este dato de la consulta). Tambien se añade la opcion de buscar palabras menos importantes en la consulta, estas palabras tendran un valor asociado de 0.5.

Del modelo vectorial se toma principalmente la forma de calcular la relevancia de los documentos con respecto a la consulta (la similitud). Se extraen los terminos y se calculan tanto el `tf` como el `idf` los cuales son usados para calcular los `w_{i,j}` de los documentos, en cuanto al vector de la consulta ya viene dado con 1 en las palabras clave y 0.5 en las palabras de menor importancia. El `idf` es calcualdo siempre con respecto a un subtotal de documentos, que serian todos aquellos documentos que no contengan los terminos excluidos.

Se decidio usar el modelo descrito anteriormente porque es necesario extraer los documentos mas relevantes, requiriendo por tanto el uso de un modelo que provea tal caracteristica; el tipo de consulta que se decidio usar hace que sea necesario integrar parte de las caracteristicas de la entrada de consulta del modelo booleano o el probabilistico. No se usaron caracteristicas extra del modelo probabilistico debido a la dificultad de calcular la probabilidad de la ocurrencia de los terminos en los documentos relevantes y que debido al tamaño de la base de datos de prueba, la regulacion de las probabilidades por retroalimentacion con la poca cantidad de pruebas que se puedan realizar va a ser muy poco determinante.

## 3. Detalles de implementacion:

Como una interfaz de usuario para comunicarse con el Sistema de Recuperacion de Informacion implementado se usa la biblioteca de python `streamlit` (vea como ejecutar el programa en la siguiente seccion), la cual no solo permite acceder al sistema solo desde la computadora del usuario, sino que permite el acceso por la red.

Para la extraccion de los terminos en los documentos de la base de datos (los cuales deben estar en la carpeta `./DB/` y no en carpetas dentro de esta) se usa la biblioteca `nltk`, una vez extraidos los terminos por documentos se guardaran datos al respecto en los archivos term_docs y doc_terms, para evitar calculo innecesario repetido del procesamiento realizado por `nltk`. Notar que el procesado de los documentos con `nltk` toma bastante tiempo y que en la primera ejecucion del programa, en la cual se haga dicho procesamiento, la pagina abierta por `streamlit` aparecera sin responder hasta que se termine este proceso.

## 4.Ejecucion:

Asegurese de tener instalados los paquetes descritos en `requirements.txt` y luego, en el directorio del proyecto, ejecute el comando:

`streamlit run main.py`


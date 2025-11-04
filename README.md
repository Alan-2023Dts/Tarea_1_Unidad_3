# Tarea 1 - Unidad 3

Este repositorio contiene la tarea de programación solicitada en la unidad. A continuación se detalla la estructura del proyecto, el enunciado resumido de los ejercicios, contratos de las funciones esperadas, casos de prueba y una lista paso a paso de lo que debes implementar.

## Estructura del proyecto

Archivos presentes y su propósito (implementa o modifica estos archivos cuando se indique):

- `Ecuaciones_Simultaneas.py` — Debe contener la(s) función(es) encargadas de resolver sistemas de dos ecuaciones lineales de la forma ax + by + c = 0 y px + qy + r = 0.
- `Suma_numeros_Extremos.py` — Debe contener la lógica para el ejercicio 2: sumar dígitos en posiciones simétricas respecto al dígito central.
- `Utilidades.py` — Módulo para funciones auxiliares (por ejemplo: convertir número a lista de dígitos, validaciones de entrada, lectura/parseo).
- `Main.py` — Programa principal que orquesta la ejecución de los ejercicios y muestra resultados por pantalla.
- `Menu.py` — Interfaz por consola para elegir qué ejercicio ejecutar (opcional pero recomendado).
- `README.md` — (este archivo) Instrucciones, contratos, pruebas y pasos a seguir.

## Requisitos / Enunciado resumido

Ejercicio 1
- Crear una función que resuelva el sistema:
	ax + by + c = 0
	px + qy + r = 0

	La función debe recibir los parámetros a, b, c, p, q, r y devolver:
	- una variable lógica (bool) indicando si existe solución única,
	- los valores de x e y (floats) cuando exista solución única.

	Si no existe solución única (determinante cero) la función debe indicar con la variable lógica que no hay solución única y NO devolver valores numéricos válidos para x e y (pueden devolverse `None`).

	Resolver con dicho módulo las ecuaciones siguientes (comprobar los tres casos):
	1) 3x + 2y - 7 = 0
		 9x - 5y + 1 = 0
	2) 3x + 2y - 7 = 0
		 9x + 6y - 21 = 0
	3) 3x + 2y - 7 = 0
		 9x + 6y - 20 = 0

Ejercicio 2
- Programa que reciba por teclado un número entero positivo y muestre, de izquierda a derecha, la suma de dígitos en posiciones simétricas respecto al centro.
- Ejemplos:
	- Entrada: 2354869
		Salida: 2+9 = 11, 3+6 = 9, 5+8 = 13, 4
	- Entrada: 6582
		Salida: 6+2 = 8, 5+8 = 13

	Recomendación de diseño: implementar en `Utilidades.py` una función que dada una cadena o entero devuelve la lista de dígitos. Luego en `Suma_numeros_Extremos.py` realizar la lógica de combinar extremos y producir la salida formateada.

## Contratos (mínimos) y comportamiento esperado

1) Función para ecuaciones simultáneas (ejemplo de firma en Python):

- Nombre sugerido: `resolver_sistema(a, b, c, p, q, r)`
- Entradas: a,b,c,p,q,r (numéricos, int o float)
- Salida: (tiene_solucion, x, y)
	- `tiene_solucion`: bool — True si hay solución única, False si el determinante es cero
	- `x`, `y`: float si `tiene_solucion` es True; `None` en caso contrario

Comportamiento:
- Calcular determinante D = a*q - p*b
- Si D != 0: usar cramer para x y y y devolver (True, x, y)
- Si D == 0: devolver (False, None, None)

2) Función(es) auxiliares para dígitos (ejemplo):
- `digitos_de_entero(n: int) -> List[int]` — devuelve lista de dígitos (orden izquierdo->derecho)
- `sumar_simetricos(digitos: List[int]) -> List[Union[int, Tuple[int,int]]]` — devuelve la lista de sumas (o pares y la central si existe)

## Lista paso a paso - Implementación (lo que tienes que hacer)

Sigue estos pasos en orden. Apóyate en los nombres de archivos que ya existen.

1) `Ecuaciones_Simultaneas.py`
	 - Implementa `resolver_sistema(a, b, c, p, q, r)` con el contrato arriba.
	 - Añade validación mínima: asegurarse de que los parámetros son numéricos (int/float). Si hay error de tipo, lanzar `TypeError` con mensaje claro.
	 - Añade una pequeña función de prueba dentro del archivo (o una `if __name__ == '__main__':`) que calcule los tres casos de prueba del enunciado y muestre resultados en consola.

2) `Utilidades.py`
	 - Implementa `digitos_de_entero(n)` que acepta int positivo y devuelve lista de dígitos.
	 - Implementa validaciones: si n < 0 -> ValueError; si n no es entero -> TypeError.

3) `Suma_numeros_Extremos.py`
	 - Importa `digitos_de_entero` desde `Utilidades.py`.
	 - Implementa la función principal que recibe un entero y devuelve/visualiza las sumas simétricas en el formato pedido.
	 - Asegúrate de manejar los casos de longitud par e impar (si impar, el dígito central se muestra tal cual al final).

4) `Main.py` y `Menu.py`
	 - `Menu.py`: crea un pequeño menú para que el usuario elija ejecutar ejercicio 1 o 2.
	 - `Main.py`: importar el menú y/o ejecutar ejemplos automáticos si se desea. Proveer instrucciones claras por consola para ingresar datos.

5) Pruebas manuales que debes realizar (en consola):
	 - Ejecuta `Ecuaciones_Simultaneas.py` o llama a su función desde `Main.py` con los tres pares de ecuaciones. Anota las salidas:
		 - Caso 1: debe mostrar una solución (x,y) numérica.
		 - Caso 2: indicar que hay infinitas soluciones (o al menos que no hay solución única).
		 - Caso 3: indicar que no existe solución.
	 - Ejecuta `Suma_numeros_Extremos.py` con los ejemplos 2354869 y 6582 y comprueba el formato de salida.

## Ejemplos de salida esperada

- Ejercicio 1 (ejemplo):
	- Entrada: (3, 2, -7, 9, -5, 1)
	- Salida: Tiene solución: True, x = ..., y = ... (valores numéricos)

- Ejercicio 2 (ejemplo):
	- Entrada: 2354869
	- Salida en consola: 2+9 = 11, 3+6 = 9, 5+8 = 13, 4

## Casos límite y notas de diseño (edge cases)

- Ecuaciones: manejar determinante cercano a 0 (si usas floats, compara con tolerancia muy pequeña si procede).
- Suma de dígitos: entrada no numérica o negativa debe producir mensajes de error claros.
- Evita salir del programa con excepciones sin control: captura errores en `Main.py` y muestra mensajes legibles.

## Cómo entregar / subir PDF

- Crea un PDF que contenga:
	1) Tu nombre y matrícula (si corresponde).
 2) Capturas de pantalla o texto con las salidas de los tres casos del Ejercicio 1.
 3) Código fuente (puedes pegar fragmentos relevantes) o explicar brevemente la implementación.
 4) Ejecuciones de prueba del Ejercicio 2 con los ejemplos y sus salidas.
 5) Breves conclusiones.

- Nombra el archivo del PDF exactamente: `Act1-NombreAlumno.pdf` reemplazando NombreAlumno por tu nombre.
- Sube el PDF donde indique el profesor/entorno de entrega o sube en la plataforma correspondiente.

## Qué más puedo hacer (sugerencias / extras) — opcional

- Añadir tests unitarios con `unittest` para `resolver_sistema` y las funciones de dígitos.
- Añadir manejo de entradas por línea de comandos con `argparse` en `Main.py`.
- Documentar con docstrings cada función.

---




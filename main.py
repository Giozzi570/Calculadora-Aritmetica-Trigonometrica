"""
🔥 ¡Domina las Matemáticas con Python! 🐍 | Aritmética y Trigonometría en un Solo Código 💻✨
"""

"""Importamos las funciones necesarias desde los módulos correspondientes:

1. Desde el módulo 'funciones.funciones_aritmeticas' (que se encuentra en la carpeta 'funciones'):
   - Suma: Para realizar operaciones de suma.
   - Resta: Para realizar operaciones de resta.
   - Division: Para realizar operaciones de división.
   - Multiplicacion: Para realizar operaciones de multiplicación.

2. Desde el módulo 'funciones.funciones_trigonometricas' (también en la carpeta 'funciones'):
   - Tan: Para calcular la tangente de un ángulo.
   - Sin: Para calcular el seno de un ángulo.
   - Cos: Para calcular el coseno de un ángulo.

Estas funciones permiten realizar operaciones matemáticas básicas y trigonométricas de manera modular y organizada.
"""
from funciones.funciones_aritmeticas import Suma,Resta,Division,Multiplicacion
from funciones.funciones_trigonometricas import Tan,Sin,Cos

"""
Diccionarios que mapean nombres de operaciones (strings) a sus funciones correspondientes:
- 'funciones_aritmeticas': Suma, Resta, Division, Multiplicacion.
- 'funciones_trigonometricas': Tan, Sin, Cos.

Permiten ejecutar dinámicamente operaciones basadas en la entrada del usuario.
"""
funciones_aritmeticas = {
    "suma" : Suma ,
    "resta" : Resta,
    "division" : Division,
    "multiplicacion" : Multiplicacion
}

funciones_trigonometricas = {
    "tan" : Tan,
    "sin" : Sin,
    "cos" : Cos
}

# Solicita al usuario una operación, convierte la entrada a minúsculas y elimina espacios en blanco.
operacion = (input("¿Que operacion desea realizar? ")).lower().strip()

# Verifica si la operación ingresada está en el diccionario de funciones aritméticas.
if operacion in funciones_aritmeticas:
    # Solicita dos números al usuario.
    num1, num2 = float(input("Numero 1: ")), float(input("Numero 2: "))
    # Ejecuta la operación aritmética seleccionada y muestra el resultado.
    print(f"La {operacion} entre {num1} y {num2} da como resultado {funciones_aritmeticas[operacion](num1, num2)}")

# Si no es una operación aritmética, verifica si es una función trigonométrica.
elif operacion in funciones_trigonometricas:
    # Solicita un número al usuario.
    num1 = float(input("Numero 1: "))
    # Ejecuta la función trigonométrica seleccionada y muestra el resultado.
    print(f"La funcion {operacion} de {num1} da como resultado {funciones_trigonometricas[operacion](num1)}")

# Si la operación no existe en ninguno de los diccionarios, muestra un mensaje de error.
else:
    # Informa al usuario que la operación no existe y lista las opciones disponibles.
    print(f"La operacion {operacion} no existe, eliga entre {','.join(funciones_aritmeticas)}{','.join(funciones_trigonometricas)}")
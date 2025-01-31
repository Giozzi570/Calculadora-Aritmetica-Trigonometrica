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

# Le pedimos al usuario una operacion que desee realizar y usamos los metodos lower() y strip() uno para pasar todo a minuscula y el otro para borrar los espacios en blanco
operacion = (input("¿Que operacion desea realizar? ")).lower().strip()

if operacion in funciones_aritmeticas:
    num1,num2 = float(input("Numero 1: ")), float(input("Numero 2: "))
    print(f"La {operacion} entre {num1} y {num2} da como resultado {funciones_aritmeticas[operacion](num1,num2)}")
elif operacion in funciones_trigonometricas:
    num1 = float(input("Numero 1: "))
    print(f"La funcion {operacion} de {num1} da como resultado {funciones_trigonometricas[operacion](num1)}")
else:
    print(f"La operacion {operacion} no existe,eliga entre {','.join(funciones_aritmeticas)}{','.join(funciones_trigonometricas)}")
    
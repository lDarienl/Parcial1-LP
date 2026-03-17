# Punto 4 — Rendimiento: compilado vs interpretado (recursivo)

Se compara el tiempo de ejecución de una **función recursiva** (Fibonacci ingenuo) en:

- **C** (compilado)
- **Python** (interpretado)

## Ajustar parámetros

En ambos programas se pueden ajustar los parametros:

- `N`: tamaño del problema (por defecto 35)
- `REPS`: número de repeticiones (por defecto 5)

## Análisis de Resultados y Conclusiones

Tras ejecutar el benchmark con $N=35$ y 5 repeticiones, se observan los siguientes tiempos promedio:
- **C (Compilado):** ~0.019s
- **Python (Interpretado):** ~1.545s

### Conclusiones:
1. **Diferencia de Rendimiento:** C es aproximadamente **80 veces más rápido** que Python en esta tarea específica.
2. **Costo de la Recursión:** En Python, cada llamada a la función `fib` implica una sobrecarga significativa en el manejo de la pila (stack), gestión de tipos dinámicos y el conteo de referencias. En C, al estar optimizado con `-O2`, el compilador reduce las llamadas a instrucciones de salto muy eficientes.
3. **Compilado vs Interpretado:** C traduce el código directamente a lenguaje máquina antes de la ejecución. Python debe interpretar el bytecode mediante la PVM (Python Virtual Machine), lo cual añade una capa de latencia en algoritmos con alta intensidad de cómputo como Fibonacci recursivo ($O(2^n)$).
4. **Escalabilidad:** Como notamos al intentar subir a $N=50$, el crecimiento exponencial del algoritmo hace que Python se vuelva inviable rápidamente, mientras que C aún puede manejar valores ligeramente superiores antes de degradarse.
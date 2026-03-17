# Punto 3 — Calculadora `sqrt` con Flex + Bison (Newton-Raphson)

Implementa una calculadora en C que evalúa expresiones con:

- números reales
- `+ - * / ( )`
- función `sqrt(x)` **sin usar** `sqrt()` de `math.h` (se usa Newton-Raphson)

La **entrada** se lee desde un archivo de texto y la **salida** va por consola (una línea por expresión).

\[
x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)
\]

## Archivo de entrada (ejemplo)

En `pruebas.txt`:

```
sqrt(4)
sqrt(144)
sqrt(2)
sqrt(0)
sqrt(0.25)
3 + sqrt(9) * 2
(10 + 5) * (20 / sqrt(25))
-5 + sqrt(100)
sqrt(-4)
10 / 0
5 + @
sqrt(16

```

## Manejo de Errores
La calculadora detecta y reporta:
- División por cero.
- Raíces de números negativos.
- Caracteres no reconocidos (Léxico).
- Errores de estructura/paréntesis (Sintáctico).

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

En `input.txt`:

```
sqrt(144)
sqrt(2)
3 + sqrt(9) * 2
10 / (2 + 3)
```

## Probar rápido


# Punto 2 — AFD para ID (Python)

ER dada:

```
[A-Za-z][A-Za-z0-9]*
```

## Lógica del Autómata
El AFD consta de 3 estados principales:
- **Estado 0 (START):** Estado inicial. Solo transiciona al estado 1 si recibe una letra `[A-Za-z]`. Cualquier otro carácter lleva al estado de error (DEAD).
- **Estado 1 (IN):** Estado de aceptación. Permite letras o números de forma indefinida.
- **Estado 2 (DEAD):** Estado trampa. Una vez se ingresa un carácter inválido (como un símbolo o empezar por número), la cadena es rechazada.

## Tests

```bash
python3 main.py hola
python3 main.py A9
python3 main.py _x
```


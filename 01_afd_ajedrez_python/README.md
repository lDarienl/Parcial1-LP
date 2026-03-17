# Punto 1 — ER + AFD (movimientos ajedrez)

## Lenguaje (definición usada)

Se acepta una cadena con la forma:

```
\[
\text{ATOM}\;(\text{espacios opcionales})\;(\rightarrow\ \text{o}\ X)\;(\text{espacios opcionales})\;\text{ATOM}
\]
```

Para efectos de la implementación del AFD, se simplificó el ATOM como cualquier secuencia de letras seguida de un dígito opcional (1-8), asegurando la compatibilidad con los ejemplos

Donde:

- `->` representa “mover a”
- `X` representa “captura”
- `ATOM` representa una notación descriptiva simplificada como en los ejemplos:
  - `p->k4`
  - `kbp X qn`

### ATOM (notación descriptiva simplificada)

Un `ATOM` válido cumple:

- Debe empezar por una letra.
- Se permiten:
  - **bando** opcional: `k` o `q`
  - **pieza/cualificador** opcional: `b`, `n` o `r`
  - `p` opcional (para peón)
  - o bien una **pieza** directa: `p k q r b n`
  - y opcionalmente un **dígito de 1 a 8** (ej: `k4`)

Esto cubre los ejemplos `p`, `k4`, `kbp`, `qn`, etc.

## Expresión regular (equivalente)

Con \(\s\) como espacio/tab:

```
ATOM = ( ( [kq] [bnr]? p? ) | ( [pkqrbn] ) ) [1-8]?
MOVE = ATOM \s* (->|X) \s* ATOM
```

## Tests

```bash
python3 main.py "p->k4"
python3 main.py "kbp X qn"
python3 main.py "qbp->q4"
python3 main.py "xx->k4"
```


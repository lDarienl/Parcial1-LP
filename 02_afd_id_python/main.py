from __future__ import annotations

import sys
from dataclasses import dataclass


def _is_letter(ch: str) -> bool:
    o = ord(ch)
    return (65 <= o <= 90) or (97 <= o <= 122)


def _is_digit(ch: str) -> bool:
    o = ord(ch)
    return 48 <= o <= 57


@dataclass(frozen=True)
class IdentifierDFA:
    """
    AFD para la ER:
      [A-Za-z][A-Za-z0-9]*
    """

    def accepts(self, s: str) -> bool:
        START = 0
        IN = 1
        DEAD = 2

        state = START

        for ch in s:
            if state == START:
                if _is_letter(ch):
                    state = IN
                else:
                    state = DEAD
            elif state == IN:
                if _is_letter(ch) or _is_digit(ch):
                    state = IN
                else:
                    state = DEAD
            else:
                return False

        return state == IN


def main(argv: list[str]) -> int:
    dfa = IdentifierDFA()

    if len(argv) >= 2:
        s = argv[1]
        print("ACEPTE" if dfa.accepts(s) else "NO ACEPTE")
        return 0

    # Mínimo 5 pruebas: 3 ACEPTE y 2 NO ACEPTE
    tests = [
        ("abc", True),
        ("A1", True),
        ("Z999", True),
        ("1abc", False),
        ("a-b", False),
    ]

    ok = True
    for s, expected in tests:
        got = dfa.accepts(s)
        ok &= got == expected
        print(f"{s!r:8} => {'ACEPTE' if got else 'NO ACEPTE'} (esperado: {expected})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


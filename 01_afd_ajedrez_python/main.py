from __future__ import annotations

import sys
from dataclasses import dataclass


def _is_space(ch: str) -> bool:
    return ch in (" ", "\t")


def _is_letter(ch: str) -> bool:
    o = ord(ch)
    return (65 <= o <= 90) or (97 <= o <= 122)


def _is_digit_1_8(ch: str) -> bool:
    return ch in "12345678"


@dataclass(frozen=True)
class DFA:
    def accepts(self, s: str) -> bool:
        START = 0
        A1 = 1  
        A2 = 2  
        WS_AFTER_A = 3
        ARROW_DASH = 4
        AFTER_OP = 5  
        WS_BEFORE_B = 6
        B1 = 7  
        B2 = 8  
        WS_END = 9
        DEAD = 10

        state = START

        def dead() -> None:
            nonlocal state
            state = DEAD

        for ch in s:
            if state == START:
                if _is_space(ch):
                    dead()
                elif _is_letter(ch):
                    state = A1
                else:
                    dead()

            elif state == A1:
                if _is_letter(ch):
                    state = A1
                elif _is_digit_1_8(ch):
                    state = A2
                elif _is_space(ch):
                    state = WS_AFTER_A
                elif ch == "X":
                    state = AFTER_OP
                elif ch == "-":
                    state = ARROW_DASH
                else:
                    dead()

            elif state == A2:
                if _is_space(ch):
                    state = WS_AFTER_A
                elif ch == "X":
                    state = AFTER_OP
                elif ch == "-":
                    state = ARROW_DASH
                else:
                    dead()

            elif state == WS_AFTER_A:
                if _is_space(ch):
                    state = WS_AFTER_A
                elif ch == "X":
                    state = AFTER_OP
                elif ch == "-":
                    state = ARROW_DASH
                else:
                    dead()

            elif state == ARROW_DASH:
                if ch == ">":
                    state = AFTER_OP
                else:
                    dead()

            elif state == AFTER_OP:
                if _is_space(ch):
                    state = WS_BEFORE_B
                elif _is_letter(ch):
                    state = B1
                else:
                    dead()

            elif state == WS_BEFORE_B:
                if _is_space(ch):
                    state = WS_BEFORE_B
                elif _is_letter(ch):
                    state = B1
                else:
                    dead()

            elif state == B1:
                if _is_letter(ch):
                    state = B1
                elif _is_digit_1_8(ch):
                    state = B2
                elif _is_space(ch):
                    state = WS_END
                else:
                    dead()

            elif state == B2:
                if _is_space(ch):
                    state = WS_END
                else:
                    dead()

            elif state == WS_END:
                if _is_space(ch):
                    state = WS_END
                else:
                    dead()

            else:  # DEAD
                return False

        return state in (B1, B2, WS_END)


def main(argv: list[str]) -> int:
    dfa = DFA()

    if len(argv) >= 2:
        s = " ".join(argv[1:])
        print("ACEPTA" if dfa.accepts(s) else "NO ACEPTA")
        return 0

    tests = [
        ("p->k4", True),
        ("kbp X qn", True),
        ("qbp->q4", True),
        ("p - > k4", False),
        ("->k4", False),
        ("p->", False),
        ("kbpXqn", True),
        ("p->k9", False),
    ]

    ok = True
    for s, expected in tests:
        got = dfa.accepts(s)
        ok &= got == expected
        print(f"{s!r:12} => {'ACEPTA' if got else 'NO ACEPTA'} (esperado: {expected})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


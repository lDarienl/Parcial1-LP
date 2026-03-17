from __future__ import annotations

import os
import sys
from dataclasses import dataclass

from antlr4 import CommonTokenStream, InputStream


def _ensure_generated_on_path() -> None:
    gen_dir = os.path.join(os.path.dirname(__file__), "antlr_gen")
    if gen_dir not in sys.path:
        sys.path.insert(0, gen_dir)


@dataclass(frozen=True)
class FiboEngine:
    @staticmethod
    def fibo_upto(n: int) -> list[int]:
        if n < 0:
            return []
        seq: list[int] = [0]
        if n == 0:
            return seq
        seq.append(1)
        a, b = 0, 1
        while True:
            a, b = b, a + b
            if b > n:
                break
            seq.append(b)
        return seq


def run(text: str) -> str:
    _ensure_generated_on_path()
    from FiboLexer import FiboLexer  # type: ignore
    from FiboParser import FiboParser  # type: ignore
    from FiboVisitor import FiboVisitor  # type: ignore

    class Visitor(FiboVisitor):  # type: ignore
        def visitExpr(self, ctx):  # noqa: N802
            n = int(ctx.INT().getText())
            seq = FiboEngine.fibo_upto(n)
            return ", ".join(str(x) for x in seq)

    lexer = FiboLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = FiboParser(stream)
    tree = parser.prog()
    out = Visitor().visit(tree)
    return str(out)


def main(argv: list[str]) -> int:
    if len(argv) >= 2:
        text = " ".join(argv[1:]).strip()
    else:
        text = input().strip()

    try:
        print(run(text))
        return 0
    except ModuleNotFoundError:
        print(
            "Error: no encuentro los archivos generados en ./antlr_gen.\n"
            "Ejecuta:\n"
            "  antlr4 -Dlanguage=Python3 -visitor -no-listener grammar/Fibo.g4 -o antlr_gen",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


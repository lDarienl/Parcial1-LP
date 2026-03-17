from __future__ import annotations

import time


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main() -> int:
    N = 35
    REPS = 5

    times = []
    out = None
    for _ in range(REPS):
        t0 = time.perf_counter()
        out = fib(N)
        t1 = time.perf_counter()
        times.append(t1 - t0)

    avg = sum(times) / len(times)
    print(f"Python fib({N}) = {out}")
    print(f"REPS={REPS} avg={avg:.6f}s min={min(times):.6f}s max={max(times):.6f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


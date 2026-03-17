#define _POSIX_C_SOURCE 199309L

#include <stdio.h>
#include <stdint.h>
#include <time.h>

static int64_t fib(int n) {
  if (n < 2) return n;
  return fib(n - 1) + fib(n - 2);
}

static double now_s(void) {
  struct timespec ts;
  clock_gettime(CLOCK_MONOTONIC, &ts);
  return (double)ts.tv_sec + (double)ts.tv_nsec * 1e-9;
}

int main(void) {
  const int N = 35;
  const int REPS = 5;

  double min = 1e100, max = 0.0, sum = 0.0;
  int64_t out = 0;

  for (int i = 0; i < REPS; i++) {
    double t0 = now_s();
    out = fib(N);
    double t1 = now_s();
    double dt = t1 - t0;
    if (dt < min) min = dt;
    if (dt > max) max = dt;
    sum += dt;
  }

  printf("C fib(%d) = %lld\n", N, (long long)out);
  printf("REPS=%d avg=%.6fs min=%.6fs max=%.6fs\n", REPS, sum / REPS, min, max);
  return 0;
}


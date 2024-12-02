#include <stdio.h>
#include <stdlib.h>

#define TARGET_COUNT 5
#define START_NUMBER 200000000

int find_smallest_divisors(unsigned long long N, unsigned long long *divisors) {
    int count = 0;
    for (unsigned long long i = 2; i * i <= N && count < TARGET_COUNT; i++) {
        if (N % i == 0) {
            divisors[count++] = i;
            while (N % i == 0) {
                N /= i;
            }
        }
    }
    if (N > 1 && count < TARGET_COUNT) {
    divisors[count++] = N;
    }
    return count;
}
unsigned long long calculate_M(unsigned long long N) {
    unsigned long long divisors[TARGET_COUNT];
    int count = find_smallest_divisors(N, divisors);
    if (count < TARGET_COUNT) {
        return 0;
    }
    unsigned long long M = 1;
    for (int i = 0; i < TARGET_COUNT; i++) {
        M *= divisors[i];
}
return M;
}
int main() {
    unsigned long long N = START_NUMBER + 1;
    unsigned long long M_values[5];
    int found_count = 0;
    while (found_count < 5) {
    unsigned long long M = calculate_M(N);
    if (M > 0 && M < N) {
        M_values[found_count++] = M;
    }
        N++;
    }
    printf("Найденные значения M(N):\n");
    for (int i = 0; i < 5; i++) {
        printf("%llu\n", M_values[i]);
    }
    return 0;
}
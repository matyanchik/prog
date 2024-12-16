#include <stdio.h>
#include <gmp.h>

int count_ones(const mpz_t number) {
    int count = 0;
    mpz_t temp;
    mpz_init(temp);
    mpz_set(temp, number);
    while (mpz_cmp_ui(temp, 0) > 0) {
        count += mpz_tstbit(temp, 0);
        mpz_fdiv_q_2exp(temp, temp, 1);
    }
    mpz_clear(temp);
    return count;
}
int main() {
    mpz_t value;
    mpz_init(value);
    mpz_ui_pow_ui(value, 2, 1022);
    mpz_t temp;
    mpz_init(temp);
    mpz_ui_pow_ui(temp, 2, 511);
    mpz_add(value, value, temp);
    mpz_sub_ui(value, value, 511);
    int ones_count = count_ones(value);
    printf("Количество единиц в двоичной записи: %d\n", ones_count);
    mpz_clear(value);
    mpz_clear(temp);
    return 0;
}
#include <stdio.h>
#include <math.h>

double f(double x) {
    if (x >= -1 && x <= 1) {
        return exp(-2 * sin(x));
    } else if (x > 1 && x <= 2) {
        return x * x - 1/tan(x);
    } else {
        return NAN;
    }
}

int main() {
    FILE *fp = fopen("output_for.txt", "w");

    for (double x = -1.0; x <= 2.0; x += 0.1) {
        fprintf(fp, "%lf %lf\n", x, f(x));
    }

    fclose(fp);
    return 0;
}
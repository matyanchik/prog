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
    double x = -1.0;
    FILE *fp = fopen("output_while.txt", "w");

    while (x <= 2.0) {
        fprintf(fp, "%lf %lf\n", x, f(x));
        x += 0.1;
    }

    fclose(fp);
    return 0;
}
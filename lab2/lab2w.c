#include <stdio.h>
#include <math.h>

float f(float x, float h) {
    const float eps = h / 2;
    if (x >= -1.0f - eps && x <= 1.0f + eps)
        return exp(-2 * sin(x));
    else if (x > 1 - eps && x <= 2 + eps)
        return pow(x, 2) - (1.0 / tan(x));
    return 0.0f;
}
int main() {
    float h, x = 0;
    scanf("%f", &h);
    printf("x\t\tf(x)\n");
    while(x <= 2.0f) {
        printf("%f\t%f\n", x+h, f(x, h));
        x += h;
    }
    return 0;
}

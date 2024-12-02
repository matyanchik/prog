# Лабораторная работа №1

## Вариант 7
## Задание
1. Разбрать код программы из примера.
2. Составить блок-схему алгоритма для своего варианта.
3. Написать программу, решающую задачу по своему варианту.
4. Оформить отчёт в README.md.

## Программа
```c
#include <stdio.h>

int sum_of_digits(int n) {
    int sum = 0;
    n = (n < 0) ? -n : n;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int a, b;

    printf ("Введите число a -> ");
    scanf ("%d", &a);
    printf ("Введите число b -> ");
    scanf ("%d", &b);

    int sum_a = sum_of_digits(a);
    int sum_b = sum_of_digits(b);

    int min_sum = sum_a < sum_b ? sum_a : sum_b;

    if (min_sum == 0) {
        printf("Ошибка: Сумма равна нулю, деление невозможно.\n");
    } else {
        double quotient = min_sum / (double)b;
        printf ("Частное наименьшей суммы и второго параметра (b): %2f\n", quotient);
    }
    return 0;
}
```

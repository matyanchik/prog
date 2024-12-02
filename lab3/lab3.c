#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100;
    }
}
void reverse(int *arr, int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
void processArray(int *arr, int size, int target) {
    int index = -1;
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            index = i;
            break;
        }
    }
    if (index != -1) {
        reverse(arr, 0, index - 1);
        reverse(arr, index + 1, size - 1);
    } else {
        reverse(arr, 0, size - 1);
    }
}
void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int main() {
    srand(time(0));
    int n;
    printf("Введите количество элементов массива: ");
    scanf("%d", &n);
    int *arr = (int *)malloc(n * sizeof(int));
    generateArray(arr, n);
    printf("Сгенерированный массив: ");
    printArray(arr, n);
    int target;
    printf("Введите искомый элемент: ");
    scanf("%d", &target);
    processArray(arr, n, target);
    printf("Результирующий массив: ");
    printArray(arr, n);
    free(arr);
    return 0;
}
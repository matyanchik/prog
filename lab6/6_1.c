#include <stdio.h>

int main() {
    int total_words = 5 * 5 * 5 * 5 * 5;    
    int starting_with_E = 5 * 5 * 5 * 5;
    int ending_with_A = 5 * 5 * 5 * 5;
    int starting_with_E_and_ending_with_A = 5 * 5 * 5;
    int invalid_words = starting_with_E + ending_with_A -
starting_with_E_and_ending_with_A;
    int valid_words = total_words - invalid_words;
    printf("Количество различных кодовых слов: %d\n", valid_words);
    return 0;
}
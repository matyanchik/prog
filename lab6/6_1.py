total_words = 5 ** 5
words_starting_with_E = 5 ** 4
words_ending_with_A = 5 ** 4
words_starting_with_E_and_ending_with_A = 5 ** 3

invalid_words = (words_starting_with_E + words_ending_with_A - 
                 words_starting_with_E_and_ending_with_A)

valid_words = total_words - invalid_words
print(valid_words)
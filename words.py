def print_upper_words(words):
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    for word in words:
        if word[0].lower() == 'e' or if word[0].upper() =='E':
            print(word.upper())

def print_word_letters(words, letters):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
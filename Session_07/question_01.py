def analyze_text(text) :
    words = text.split(' ')
    count_words = 0
    count_palindrome = 0
    dic_words = {}
    most_word = ''
    most_word_num = 0
    most_len = 0
    most_len_word = ''
    short_len = len (words[0])
    short_len_word = words[0]
    for i in words :
        count_words += 1
        if len(i) > most_len :
            most_len = len(i)
            most_len_word = i
        if len(i) < short_len :
            short_len = len(i)
            short_len_word = i
        if i.lower() == i[::-1].lower() :
            count_palindrome += 1
        if i in dic_words :
            dic_words [i] += 1
        else :
            dic_words [i] = 1
    for i, j in dic_words.items() :
        if j > most_word_num :
            most_word_num = j
            most_word = i
    
    count_upper = 0
    count_lower = 0
    count_digit = 0
    dic_letters = {}
    most_letters = ''
    most_letters_num = 0
    for i in text.replace(' ','') :
        if i.islower() :
            count_lower += 1
        if i.isupper() :
            count_upper += 1
        if i.isdigit() :
            count_digit += 1
        if i in dic_letters :
            dic_letters [i] += 1
        else :
            dic_letters [i] = 1
    for n, m in dic_letters.items() :
        if m > most_letters_num and n.isalpha() :
            most_letters_num = m
            most_letters = n
            
    count_letters = count_lower + count_upper
    
    return {'words': count_words,
            'letters': count_letters,
            'digits': count_digit,
            'most_common_letter': most_letters,
            'most_common_word': most_word,
            'longest_word': most_len_word,
            'shortest_word': short_len_word,
            'palindrome_words_count': count_palindrome,
            'uppercase': count_upper,
            'lowercase': count_lower}

text = input('Enter your sentence :\n')
analyze = analyze_text(text)
print('\n',analyze)    
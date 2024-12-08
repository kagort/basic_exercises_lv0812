# Вывести последнюю букву в слове
word = 'Архангельск'

last_symbol = word[-1]
print(last_symbol)


# Вывести количество букв "а" в слове
word = 'Архангельск'

len_word = len(word)
print(len_word)


# Вывести количество гласных букв в слове
word = 'Архангельск'

word_lower = word.lower()
vowels = 'аеёиоуыэюя'
vowels_sum = 0

for letter in word_lower:
    if letter in vowels:
        vowels_sum += 1
print(vowels_sum)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_set= sentence.split()
word_count = len(words_set)
print(word_count)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words_set = sentence.split()
for word in words_set:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_set = sentence.split()
word_count = len(words_set)
sum_letters = len(sentence) # sum(len(word) for word in words_set)  - Так можно писать?
len_word_avg = sum_letters / word_count
print(len_word_avg)
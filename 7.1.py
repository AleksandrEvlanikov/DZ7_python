# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

# import re
#
# text = 'Пара-Ра-рам рам-пам-Папам па-РА-па-да'
# text = text.lower()
# phrases = text.split()
# print(text)
# pattern = 'аеёиоуыэюя'
# phrases = text.split()
# for i in re.finditer(pattern, text):
#     if i:
#         print('Найдено ', i.group())
#     else:
#         print('Не найдено ')

def count_vowels(word):
    vowels = 'аеиуяою'
    return sum(1 for i in word.lower() if i in vowels)

def check_rhythm(poem):
    phrases = poem.split()
    phrases_lengths = [sum(count_vowels(word) for word in j.split('-')) for j in phrases]
    if len(set(phrases_lengths)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
result = check_rhythm(poem)
print(result)



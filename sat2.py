#version 1.1

vowels = set('ауоыиэяюёе')
consonants = set('бвгджзйклмнпрстфхцчшщ')

count_v = 0
count_c = 0

word = input()
word = word.lower()

for letter1 in word:
    if letter1 in vowels:
        count_v +=1 
print('Количество гласных букв равно', count_v, 'раз')

for letter2 in word:
    if letter2 in consonants:
        count_c += 1

print('Количество согласных букв равно', count_c, 'раз')
print('Количество гласных и согласных равна' ount_v + count_v))
print('Длинна текста равна' len(word))

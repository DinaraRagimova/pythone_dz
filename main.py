sentence = input('Введите строку: ')

total = sentence.count('кот') + sentence.count('КОТ') + sentence.count('Кот')
print(total)
text = input("Введите текст: ") #Ввод текста
text = text.lower() #Замена на маленькие буквы

punctuation = [".", ",", "!", "?"] #Список знаков пунктуации

    
for i in punctuation:
    text = text.replace(i, "") #Замена знаков пунктуации на пустую строку

words = text.split() #Выписывание всех словов отдельно


word_frequency = {} #Создание пустого списока для частоты слов
for word in words: #Перебор всех слов
    if word in word_frequency: #Если слово есть в списке - прибавление к значению + 1
        word_frequency[word] += 1
    else: #Если слова нет в списке - оставляем 1
        word_frequency[word] = 1


print("Количество разных слов:",len(set(words))) #Преобразование списка в множество и подсчет всех слов в множестве
print("Частота слов:")
for word, frequency in word_frequency.items(): #Вывод словаря с  ключами (словами) и их значениями (частотой)
    print(f"{word}: {frequency}")

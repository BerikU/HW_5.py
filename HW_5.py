 # Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

# def del_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)
#
# text = input("Введите текст: ")
# my_text = del_words(text)
# print(my_text)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

# code_text = input()
# list_1 = []
# coding = ''
#
# for i in range(len(code_text)):
#     if code_text[i] not in list_1:
#         list_1.append(code_text[i])
#
# for j in range(len(list_1)):
#     count = 0
#     for u in range(len(code_text)):
#         if list_1[j] == code_text[u]:
#             count += 1
#     coding = coding + str(count) + list_1[j]
#
# print(coding)
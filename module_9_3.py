first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x,y in zip(first, second) if len(x) - len(y) != 0)   # Записываем в список
                                                                                         # first_result значения разницы
                                                                                         # длин элиментов списков
                                                                                         # first и second по элементно
                                                                                         # используя цикл for значений
                                                                                         # х, у поэлементно
                                                                                         # (с одинаковыми индексами),
                                                                                         # исключая элементы списков
                                                                                         # с одинаковой длиной

second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))    # Записываем в список second_result
                                                                                # результат сравнения длин элементов
                                                                                # списков используя цикл for
                                                                                # для элементов списков first и second
                                                                                # поэлементно (с одинаковыми индексами)
                                                                                # исходя из длинны списков


print(list(first_result))
print(list(second_result))
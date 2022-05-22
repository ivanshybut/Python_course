#Создать переменную типа String
a = "Orange"

#Создать переменную типа Integer
b = 2

#Создать переменную типа Float
c = 1.5

#Создать переменную типа Bytes
d = bytes(5)

#Создать переменную типа List
e = [1, 2, 3, ["Mike", 18]]

#Создать переменную типа Tuple
f = ((1, 2), "Hello", "World")

#Создать переменную типа Set
g = {"cherry", "banana", "apple"}

#Создать переменную типа Frozen set
h = frozenset(["Tiger", "Cat"])

#Создать переменную типа Dict
i = {"Russia": "Moscow", "USA": "Washington"}

#Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(type(a), a, "\n",
      type(b), b, "\n",
      type(c), c, "\n",
      type(d), d, "\n",
      type(e), e, "\n",
      type(f), f, "\n",
      type(g), g, "\n",
      type(h), h, "\n",
      type(i), i)

#Создать 2 переменные String, создать переменную в которой сканкатезируете эти переменные .
#Вывести в консоль
per_1 = "Hello"
per_2 = "World!!!"
per_3 = per_1 + " " + per_2
print(per_3)

#Вывести в одну строку переменные типа String и Integer используя "," (Запятую)
per_4 = "I like HONDA CRV"
per_5 = 3
print(per_4, per_5)

#Вывести в одну строку переменные типа String и Integer используя "+" (Плюс)
print(per_4 + " " + str(per_5))

import math

#  1. Создать переменную item_1 типа integer.
item_1 = 9

#  2. Создать переменную item_2 типа integer.
item_2 = 3

#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2

#  4. Вывести result_sum в консоль.
print("result_sum = ", result_sum)

#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = item_1 - item_2

#  6. Вывести result_subtr в консоль.
print("result_subtr = ", result_subtr)

#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
resul_multi = item_1 * item_2

#  8. Вывести result_multi в консоль.
print("result_multi = ", resul_multi)

#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2

#  10. Вывести result_exp в консоль.
print("result_exp = ", result_exp)

#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1, item_2)

#  12. Вывести result_m_exp в консоль.
print("result_m_exp = ", result_m_exp)

#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_1 ** 0.5

#  14. Вывести result_s_root в консоль.
print("result_s_root = ", result_s_root)

#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_1)

#  16. Вывести result_m_s_root в консоль.
print("result_m_s_root = ", result_m_s_root)

#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_1, 0.5)

#  18. Вывести result_mp_s_root в консоль.
print("result_mp_s_root = ", result_mp_s_root)

#  19. Присвоить переменной item_1 odd значение
item_1 = 11
if item_1 % 2 != 0:
    print("item_1 = Переменная -odd", item_1)
else:
    print("item_1 = Переменная -even", item_1)

#  20. Присвоить переменной item_2 even значение
item_2 = 4
if item_2 % 2 == 0:
    print("item_2 = Переменная -even", item_2)
else:
    print("item_2 = Переменная -odd", item_2)

#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1 / item_2

#  22. Вывести result_division в консоль.
print("result_division = ", result_division)

#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)

#  24. Вывести result_m_floor в консоль.
print("result_m_floor = ", result_m_floor)

#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)

#  26. Вывести result_m_ceil в консоль.
print("result_m_ceil = ", result_m_ceil)

#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = round(result_division)

#  28. Вывести result_int в консоль.
print("result_int = ", result_int)

#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1 // item_2

#  30. Вывести result_no_division_loss в консоль.
print("result_no_division_loss = ", result_no_division_loss)

#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2

#  32. Вывести result_division_loss в консоль.
print("result_division_loss = ", result_division_loss)

# Дальше будет реализация через арифметические действия с присваиванием.

#  33. Создать переменную item_3 и присвоить ей целое число
item_3 = 8

#  34. Прибавить 10 к item_3 с присвоением.
item_3 += 10

#  35. Вывести item_3 в консоль.
print("item_3 = ", item_3)

#  36. Отнять 5 от item_3 с присвоением.
item_3 -= 5

#  37. Вывести item_3 в консоль.
print("item_3 = ", item_3)

#  38. Умножить item_3 на 3 с присвоением.
item_3 *= 3

#  39. Вывести item_3 в консоль.
print("item_3 = ", item_3)

#  40. Разделить item_3 на 2 с присвоением.
item_3 /= 2

#  41. Вывести item_3 в консоль.
print("item_3 = ", item_3)

#  42. Возвести в степень 2 item_3 с присвоением.
item_3 **= 2

#  43. Вывести item_3 в консоль.
print("item_3 = ", item_3)

#  44. Найти квадратный корень item_3 с присвоением.
item_3 **= 0.5

#  45. Вывести item_3 в консоль.
print("item_3 = ", item_3)

#  46. Присвоить остаток от деления item_3
item_3 %= 2

#  47. Вывести item_3 в консоль.
print("item_3 = ", item_3)

# Boolean

# 48. Создать переменную b_item_t и присвоить True
b_item_t = True

# 49. Создать переменную b_item_f и присвоить False
b_item_f = False

# 50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = (b_item_t + b_item_f)

# 51. Вывести b_item_relult_sum в консоль.
print("b_item_result_sum = ", b_item_result_sum)

# 52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_relult_subtr = (b_item_t - b_item_f)

# 53. Вывести b_item_relult_subtr в консоль.
print("b_item_relult_subtr = ", b_item_relult_subtr)

# 54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_relult_multi = b_item_t * b_item_f

# 55. Вывести b_item_relult_multi в консоль.
print("b_item_relult_multi = ", b_item_relult_multi)

# 56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
# b_item_relult_division = b_item_t / b_item_f

# 57. Вывести b_item_relult_division в консоль. (Получить ошибку)
# print("b_item_relult_division = ", b_item_relult_division)

# 58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)

# 59. Вывести b_item_1_int в консоль.
print("b_item_1_int = ",b_item_1_int)

# 60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int
b_item_2_int = int(b_item_f)

# 61. Вывести b_item_2_int в консоль.
print("b_item_2_int = ", b_item_2_int)


#  1. Создать переменную int_item со значением 10
int_item = 10

#  2. Создать переменную comp_item со значением 18
comp_item = 18

#  3. Создать переменную mult_int в которй умножите int_item на 2
mult_int = int_item * 2

#  4. Создать переменную item_2 со значением True
item_2 = True

#  5. Создать переменную item_3 со значением False
item_3 = False

#  6. Создать переменную item_4 со значением 0
item_4 = 0

#  7. Создать переменную item_5 со значением 1
item_5 = 1

#  8. Создать переменную usd_item со значением ‘usd’
usd_item = "usd"

#  9. Создать переменную usd_usd_rate со значением 1
usd_usd_rate = 1

#  10. Создать переменную eur_item со значением ‘eur’
eur_item = "eur"

#  11. Создать переменную usd_eur_rate со значением 0.86
usd_eur_rate = 0.86

#  12. Создать переменную uah_item со значением ‘uah’
uah_item = "uah"

#  13. Создать переменную usd_uah_rate со значением 26.23
usd_uah_rate = 26.23

#  14. Создать переменную chf_item со значением ‘chf’
chf_item = "chf"

#  15. Создать переменную usd_chf_rate со значением 0.91
usd_chf_rate = 0.91

#  16. Создать переменную rub_item со значением ‘rub’
rub_item = "rub"

#  17. Создать переменную usd_rub_rate со значением 71.88
usd_rub_rate = 71.88

#  18. Создать переменную byn_item со значением ‘byn’
byn_item = "byn"

#  19. Создать переменную usd_byn_rate со значением 2.46
usd_byn_rate = 2.46

#  20. Сделать if в котором будет условие: если mult_int больше comp_item,
#  то вывести в консоль (“Переменная mult_int больше”, comp_item)
if mult_int > comp_item:
    print("Переменная mult_int больше", comp_item)

#  21. Создать переменную div_int в которй разделить int_item на 2
div_int = int_item / 2

#  22. Сделать if в котором будет условие: если div_int меньше comp_item,
#  то вывести в консоль (“Переменная div_int меньше”, comp_item)
if div_int < comp_item:
    print("Переменная div_int меньше", comp_item)

#  23. Создать переменную item_1 в которй прибавить 10 к переменной int_item
item_1 = 10 + int_item

#  24. Сделать if в котором будет условие: если item_1 меньше comp_item,
#  то вывести в консоль (“Переменная item_1 меньше”, comp_item),
#  иначе, вывести в консоль (“Переменная item_1 больше или равна”, comp_item)
if item_1 < comp_item:
    print("Переменная item_1 меньше", comp_item)
else:
    print("Переменная item_1 больше или равна", comp_item)

#  25. Сделать if в котором будет условие: если item_2, то вывести в консоль (“Переменная item_2 = ”, item_2),
#  иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
if item_2:
    print("Переменная item_2 = ", item_2)
else:
    print("Переменная item_2 = ", item_3)

#  26. Сделать if в котором будет условие: если item_3, то вывести в консоль (“Переменная item_3 = ”, item_2),
#  иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
if item_3:
    print("Переменная item_3 = ", item_2)
else:
    print("Переменная item_3 = ", item_3)

#  27. Сделать if в котором будет условие: если item_5, то вывести в консоль (“Переменная item_5 = ”, item_5),
#  иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
if item_5:
    print("Переменная item_5 = ", item_5)
else:
    print("Переменная item_5 = ", item_4)

#  28. Сделать if в котором будет условие: если item_4, то вывести в консоль (“Переменная item_4 = ”, item_5),
#  иначе, вывести в консоль (“Переменная item_4 = ”, item_4)
if item_4:
    print("Переменная item_4 = ", item_5)
else:
    print("Переменная item_4 = ", item_4)

#  29. Создать переменную currency_convertor со значением item_2
currency_convertor = item_2

#  30. Сделать if в котором будет условие: если currency_convertor, то выполнять следующие шаги задания,
#  иначе, вывести в консоль (“Переменная currency_convertor = ”, item_3)
if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == "eur":
        currency_result = target_currency_amount / usd_eur_rate
        print(target_currency_amount, eur_item, "=", currency_result, usd_item)
    elif target_currency == "uah":
        currency_result = target_currency_amount / usd_uah_rate
        print(target_currency_amount, uah_item, "=", currency_result, usd_item)
    elif target_currency == "chf":
        currency_result = target_currency_amount / usd_chf_rate
        print(target_currency_amount, chf_item, "=", currency_result, usd_item)
    elif target_currency == "byn":
        currency_result = target_currency_amount / usd_byn_rate
        print(target_currency_amount, byn_item, "=", currency_result, usd_item)
    elif target_currency == "rub":
        currency_result = target_currency_amount / usd_rub_rate
        print(target_currency_amount, rub_item, "=", currency_result, usd_item)
    else:
        print("Unknow currency")
else:
    print("Переменная currency_convertor = ", item_3)

#  31. Внутри if currency_convertor сделать следующие If условия :
#                     31.1 Создать переменную currency_usd со значением usd_item
#                     31.2 Создать переменную target_currency со значением eur_item
#                     31.3 Создать переменную target_currency_amount значением 50
#                     31.4 Создать переменную currency_result со значением 0
#                     31.4 Сделать if в котором будет условие: если target_currency равен ‘eur’,
#                     то в теле этого if в значении переменной currency_result высчитать сколько долларов получится
#                     при target_currency_amount и usd_eur_rate. Результат вывести в консоль (target_currency_amount,
#                     eur_item, “=”, currency_result, usd_item)
#                     31.5 Сделать elif в котором будет условие: если target_currency равен ‘uah’,
#                     то в теле этого if в значении переменной currency_result высчитать сколько долларов получится
#                     при target_currency_amount и usd_uah_rate. Результат вывести в консоль
#                     (target_currency_amount, uah_item, “=”, currency_result, uah_item)
#                     31.6 Сделать elif с остальными валютами
# …
#                     31.7 Последним оставить else, при выполнений которого в консоль выведется (“Unknow currency”)


# Цилы While
# Создать переменную count со значением 0
# Создать переменную range_count со значением 10
# Создать переменную for_count со значением 0
# Создать переменную run  со значением True

count = 0
range_count = 10
for_count = 0
run = True

# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	5.1 Выводить в консоль “Hello Cycle”

while run:
    print('Hello Cycle')

# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	6.1 Выводить в консоль (“Step =”, count)
# 	6.2 Переменной count прибавлять 1 с присвоением.

while run:
    count += 1
    print('Step =', count)

# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
# 	7.1 Выводить в консоль (“Step =”, count)
# 	7.2 Переменной count прибавлять 1 с присвоением.

while count < range_count:
    print('Step =', count)
    count += 1

# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
# 	8.1 Выводить в консоль (“Step =”, count)
# 	8.2 Переменной count прибавлять 1 с присвоением.
# 	8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)

while count < range_count:
    print('Step =', count)
    count += 1
    if count == 3:
        print('Step =', count, 'If body')

# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	9.1 Выводить в консоль (“Step =”, count)
# 	9.2 Переменной count прибавлять 1 с присвоением.
# 	9.2 Сделать if с условием, если count равен range_count то цикл остановится.
# 	9.3 В теле if вывести в консоль (“STOP”, count)

while run:
    print('Step =', count)
    count += 1
    if count == range_count:
        break
        print('STOP', count)

# Цилы For
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# Тело цикла:
# 10.1 Вывести в консоль (‘Step =’, item)

for item in range(for_count, range_count):
    print('Step =', count)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# Тело цикла:
# 11.1 Вывести в консоль (‘Step =’, item)
# 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
# 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
# 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
# 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).

for item in range(0, 30):
    print('Step =', item)
    if item == 5:
        print('Item =', item)
    if item == 10:
        print('Item =', item)
    if item < 4:
        print('Item <', item)
    if item >= 27:
        print('Item >=', item)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# Тело цикла:
# 12.1 Вывести в консоль (‘Step =’, item)
# 12.2 Сделать if с условием, если item равен  7.
# 	 - В теле if создать переменную inner_count равную 0
# 	 - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
# 	 - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
# 	Тело внутреннего цикла For:
# 		-- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
# 		-- Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
# 	- За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)

for item in range(0, range_count + 1):
    print('Step =', item)
    if item == 7:
        inner_count = 0
        print('-- inner_count =', inner_count)
        for inner_item in range(0, item):
            print('-------- Inner_Step =', inner_count)
            if inner_item == 5:
                inner_count = inner_item
        print('-- inner_count =', inner_count)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
# Тело цикла:
# 13.1 Вывести в консоль (‘Step =’, item)
# 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
# 	- В теле if вывести (‘If_item =’, item)
# 	- В теле if поставить continue
# 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)

for item in range(0, 20):
    print('Step =', item)
    if item > 7 and item < 12:
        print('If_item =', item)
        continue
print('End_interation =', item)






# Python_course

* Создать переменную типа ```String```
```python
a = "Orange"
```
* Создать переменную типа ```Integer``
```python
b = 2
````
* Создать переменную типа ```Float```

```python
c = 1.5
````

* Создать переменную типа ```Bytes```

```python
d = bytes(5)
````

* Создать переменную типа ```List```
```python
e = [1, 2, 3, ["Mike", 18]]
````


* Создать переменную типа ```Tuple```
```python
f = ((1, 2), "Hello", "World")
````


* Создать переменную типа ```Set```
```python
g = {"cherry", "banana", "apple"}
````


* Создать переменную типа ```Frozen set```
```python
h = frozenset(["Tiger", "Cat"])
````


* Создать переменную типа ```Dict```
```python
i = {"Russia": "Moscow", "USA": "Washington"}
````

* Вывести в консоль все выше перечисленные переменные с добавлением типа данных
```python
print(type(a), a, "\n",
      type(b), b, "\n",
      type(c), c, "\n",
      type(d), d, "\n",
      type(e), e, "\n",
      type(f), f, "\n",
      type(g), g, "\n",
      type(h), h, "\n",
      type(i), i)
````


- Создать 2 переменные String, создать переменную в которой сканкатезируете эти переменные .
  - Вывести в консоль
```python
per_1 = "Hello"
per_2 = "World!!!"
per_3 = per_1 + " " + per_2
print(per_3)
````


* Вывести в одну строку переменные типа ```String``` и ```Integer``` используя ```"," ```(Запятую)
```python
per_4 = "I like HONDA CRV"
per_5 = 3
print(per_4, per_5)
````

* Вывести в одну строку переменные типа ```String``` и ```Integer``` используя ```"+"``` (Плюс)
```python
print(per_4 + " " + str(per_5))
````
---

# import math
1. Создать переменную ```item_1``` типа ```integer```.
```python
item_1 = 9
````
2. Создать переменную ```item_2``` типа ```integer```.
```python
item_2 = 3
````
3. Создать переменную ```result_sum``` в которой вы суммируете ```item_1``` и ```item_2```.
```python
result_sum = item_1 + item_2
````
4. Вывести ```result_sum ``` в консоль.
```python
print("result_sum = ", result_sum)
````
5. Создать переменную ```result_subtr``` в которой вы вычитаете большую по значению переменную из меньшей по значению.
```python
result_subtr = item_1 - item_2
````
 6. Вывести ```result_subtr``` в консоль.
```python
print("result_subtr = ", result_subtr)

````
7. Создать переменную ```result_multi``` в которой вы умножаете ```item_1``` на ```item_2```.
```python
resul_multi = item_1 * item_2
````
8. Вывести ```result_multi``` в консоль.
```python
print("result_multi = ", resul_multi)
````
9. Создать переменную ```result_exp``` в которой вы ```item_1``` возводите в степень ```item_2```.
```python
result_exp = item_1 ** item_2
````
 10. Вывести result_exp в консоль.
```python
print("result_exp = ", result_exp)
````
11. Создать переменную ```result_m_exp``` в которой вы ```item_1``` возводите в степень ```item_2``` используя библиотеку - math.
```python
result_m_exp = math.pow(item_1, item_2)
````
12. Вывести ```result_m_exp``` в консоль.
```python
print("result_m_exp = ", result_m_exp)
````
13. Создать переменную ```result_s_root``` в которой вы найдёте квадратный корень любой из переменной ```item```
```python
result_s_root = item_1 ** 0.5
````
14. Вывести ```result_s_root``` в консоль.
```python
print("result_s_root = ", result_s_root)
````
15. Создать переменную ```result_m_s_root``` в которой вы найдёте квадратный корень любой из переменной ```item``` используя библиотеку  + math.
```python
result_m_s_root = math.sqrt(item_1)
````
16. Вывести ```result_m_s_root``` в консоль.
```python
print("result_m_s_root = ", result_m_s_root)
````
17. Создать переменную ```result_mp_s_root``` в которой вы найдёте квадратный корень любой из переменной ```item``` используя библиотеку + math используя метод ```pow```.
```python
result_mp_s_root = math.pow(item_1, 0.5)
````
18. Вывести ```result_mp_s_root ``` в консоль.
```python
print("result_mp_s_root = ", result_mp_s_root)
````
19. Присвоить переменной ```item_1 odd``` значение
```python
item_1 = 11
if item_1 % 2 != 0:
    print("item_1 = Переменная -odd", item_1)
else:
    print("item_1 = Переменная -even", item_1)
````
20. Присвоить переменной ```item_2 even``` значение
```python
item_2 = 4
if item_2 % 2 == 0:
    print("item_2 = Переменная -even", item_2)
else:
    print("item_2 = Переменная -odd", item_2)
````
21. Создать переменную result_division в которой вы разделите ```item_1``` на ```item_2```.
```python
result_division = item_1 / item_2
````
 22. Вывести ```result_division``` в консоль.
```python
print("result_division = ", result_division)
````
23. Создать переменную ```result_m_floor``` и ```result_division``` округлить до ближайшего целого меньшего чем ```result_division```.
```python
result_m_floor = math.floor(result_division)
````
24. Вывести ```result_m_floor``` в консоль.
```python
print("result_m_floor = ", result_m_floor)
````
25. Создать переменную ```result_m_ceil``` и ```result_division``` округлить до ближайшего целого большего чем ```result_division```.
```python
result_m_ceil = math.ceil(result_division)
````
 26. Вывести ```result_m_ceil``` в консоль.
```python
print("result_m_ceil = ", result_m_ceil)
````
27. Создать переменную ```result_int``` и ```result_division ``` округлить до ближайшего целого через явное приведение.
```python
result_int = round(result_division)
````
 28. Вывести ```result_int``` в консоль.
```python
print("result_int = ", result_int)
````
29. Создать переменную ```result_no_division_loss``` в которой вы разделите ```item_1``` на ```item_2``` без остатка.
```python
result_no_division_loss = item_1 // item_2
````
30. Вывести ```result_no_division_loss``` в консоль.
```python
print("result_no_division_loss = ", result_no_division_loss)
````
31. Создать переменную ```result_division_loss ``` в которой вы найдёте остаток от деления ```item_1``` на ```item_2```.
```python
result_division_loss = item_1 % item_2
````
32. Вывести ```result_division_loss ``` в консоль.
```python
print("result_division_loss = ", result_division_loss)
````


# Дальше будет реализация через арифметические действия с присваиванием.
33. Создать переменную ```item_3``` и присвоить ей целое число
```python
item_3 = 8
````
34. Прибавить 10 к ```item_3``` с присвоением.
```python
item_3 += 10
````
35. Вывести ```item_3``` в консоль.
```python
print("item_3 = ", item_3)
````
36. Отнять 5 от ```item_3 ``` с присвоением.
```python
item_3 -= 5
````
37. Вывести ```item_3 ``` в консоль.
```python
print("item_3 = ", item_3)
````
38. Умножить ```item_3 ``` на 3 с присвоением.
```python
item_3 *= 3
````
39. Вывести ```item_3```  в консоль.
```python
print("item_3 = ", item_3)
````
40. Разделить ```item_3 ``` на 2 с присвоением.
```python
item_3 /= 2
````
41. Вывести ```item_3``` в консоль.
```python
print("item_3 = ", item_3)
````
42. Возвести в степень 2 ```item_3 ``` с присвоением.
```python
item_3 **= 2
````
43. Вывести ```item_3``` в консоль.
```python
print("item_3 = ", item_3)
````
44. Найти квадратный корень ```item_3 ``` с присвоением.
```python
item_3 **= 0.5
````
45. Вывести ```item_3``` в консоль.
```python
print("item_3 = ", item_3)
````
46. Присвоить остаток от деления ```item_3```
```python
item_3 %= 2
````
47. Вывести ```item_3``` в консоль.
```python
print("item_3 = ", item_3)
````
# Boolean

* Создать переменную ```b_item_t ``` и присвоить ```True```
```python
b_item_t = True
````

* Создать переменную ```b_item_f ``` и присвоить ```False```
```python
b_item_f = False
````

* Создать переменную ```b_item_relult_sum ``` и присвоить сумму ```b_item_t и b_item_f```
```python
b_item_result_sum = (b_item_t + b_item_f)
````

* Вывести ```b_item_relult_sum```  в консоль.
```python
print("b_item_result_sum = ", b_item_result_sum)
````

* Создать переменную``` b_item_relult_subtr ```и присвоить разницу ```b_item_t и b_item_f```
```python
b_item_relult_subtr = (b_item_t - b_item_f)
````

* Вывести ```b_item_relult_subtr``` в консоль.
```python
print("b_item_relult_subtr = ", b_item_relult_subtr)
````

* Создать переменную ```b_item_relult_multi``` и присвоить умножение ```b_item_t и b_item_f```
```python
b_item_relult_multi = b_item_t * b_item_f
````

* Вывести ```b_item_relult_multi ``` в консоль.
```python
print("b_item_relult_multi = ", b_item_relult_multi)
````

* Создать переменную ```b_item_relult_division ``` и присвоить деление ```b_item_t и b_item_f```
```python
b_item_relult_division = b_item_t / b_item_f
````
*  Вывести ```b_item_relult_division ``` в консоль. (Получить ошибку)
```python
# print("b_item_relult_division = ", b_item_relult_division)
````

* Создать переменную ``` b_item_1_int ``` и присвоить явное приведение``` b_item_t к int```
```python
b_item_1_int = int(b_item_t)
````
* Вывести ```b_item_1_int``` в консоль.
```python
print("b_item_1_int = ",b_item_1_int)
````

* Создать переменную ```b_item_2_int``` и присвоить явное приведение ```b_item_2 ``` к ```int``` 
```python
b_item_2_int = int(b_item_f)
````

* Вывести ```b_item_2_int ``` в консоль.
```python
print("b_item_2_int = ", b_item_2_int)
````


---


- Создать переменную ```int_item``` со значением ```10```
```python
int_item = 10
````

- Создать переменную ```comp_item``` со значением ```18```
```python
comp_item = 18
````

- Создать переменную ```mult_int``` в которй умножите ```int_item``` на ```2```
```python
mult_int = int_item * 2
````

- Создать переменную ```item_2``` со значением ```True```
```python
item_2 = True
````

- Создать переменную ```item_3``` со значением ```False```
```python
item_3 = False
````

- Создать переменную ```item_4``` со значением ```0```
```python
item_4 = 0
````

- Создать переменную ```item_5``` со значением ```1```
```python
item_5 = 1
````

- Создать переменную ```usd_item``` со значением ```‘usd’```
```python
usd_item = "usd"
````

- Создать переменную ```usd_usd_rate``` со значением ```1```
```python
usd_usd_rate = 1
````

- Создать переменную ```eur_item``` со значением ```‘eur’```
```python
eur_item = "eur"
````

- Создать переменную ```usd_eur_rate ``` со значением ```0.86```
```python
usd_eur_rate = 0.86
````

- Создать переменную ```uah_item``` со значением ```‘uah’```
```python
uah_item = "uah"
````

- Создать переменную ```usd_uah_rate``` со значением ```26.23```
```python
usd_uah_rate = 26.23
````

- Создать переменную ```chf_item``` со значением ```‘chf’```
```python
chf_item = "chf"
````

- Создать переменную ```usd_chf_rate``` со значением ```0.91```
```python
usd_chf_rate = 0.91
````

- Создать переменную ```rub_item ``` со значением ```‘rub’```
```python
rub_item = "rub"
````

- Создать переменную ```usd_rub_rate``` со значением ```71.88```
```python
usd_rub_rate = 71.88
````

- Создать переменную ```byn_item``` со значением ```‘byn’```
```python

byn_item = "byn"
````

- Создать переменную ```usd_byn_rate``` со значением ````2.46```
```python
usd_byn_rate = 2.46
````


- Сделать ``` if ```в котором будет условие: если ```mult_int``` больше ```comp_item```,
  - то вывести в консоль (“Переменная ```mult_int``` больше”, ```comp_item```)
```python
if mult_int > comp_item:
    print("Переменная mult_int больше", comp_item)
````

- Создать переменную ```div_int``` в которй разделить ```int_item``` на ```2```
```python
div_int = int_item / 2
````

- Сделать ```if``` в котором будет условие: если ```div_int``` меньше ```comp_item```,
  - то вывести в консоль (“Переменная ```div_int``` меньше”, ```comp_item```)
```python
if div_int < comp_item:
    print("Переменная div_int меньше", comp_item)
````

- Создать переменную ```item_1 ``` в которй прибавить ```10``` к переменной ```int_item```
```python
item_1 = 10 + int_item
````

- Сделать ```if``` в котором будет условие: если ```item_1 ``` меньше ```comp_item```,
  -то вывести в консоль (“Переменная ```item_1 меньше```”, ```comp_item```),
  - иначе, вывести в консоль (“Переменная ```item_1``` больше или равна”,``` comp_item```)
```python
if item_1 < comp_item:
    print("Переменная item_1 меньше", comp_item)
else:
    print("Переменная item_1 больше или равна", comp_item)
````

- Сделать ```if``` в котором будет условие: если ```item_2```, то вывести в консоль (“Переменная ```item_2``` = ”, ```item_2```),
  - иначе, вывести в консоль (“Переменная ```item_2``` = ”, ```item_3```)
```python
if item_2:
    print("Переменная item_2 = ", item_2)
else:
    print("Переменная item_2 = ", item_3)
````

- Сделать ```if``` в котором будет условие: если ```item_3```, то вывести в консоль (“Переменная ```item_3``` = ”, ```item_2```),
  - иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
```python
if item_3:
    print("Переменная item_3 = ", item_2)
else:
    print("Переменная item_3 = ", item_3)
````

- Сделать ```if``` в котором будет условие: если ```item_5``` , то вывести в консоль (“Переменная ```item_5``` = ”, ```item_5```),
  - иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
```python
if item_5:
    print("Переменная item_5 = ", item_5)
else:
    print("Переменная item_5 = ", item_4)
````

- Сделать ```if ``` в котором будет условие: если ```item_4```, то вывести в консоль (“Переменная ```item_4 ``` = ”, ```item_5```),
  - иначе, вывести в консоль (“Переменная ```item_4``` = ”, ```item_4```)
```python
if item_4:
    print("Переменная item_4 = ", item_5)
else:
    print("Переменная item_4 = ", item_4)
````

- Создать переменную ```currency_convertor``` со значением ```item_2```
```python
currency_convertor = item_2
````

- Сделать ```if``` в котором будет условие: если```  currency_convertor```, то выполнять следующие шаги задания,
  - иначе, вывести в консоль (“Переменная ```currency_convertor = ```”, ```item_3```)
```python
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
````




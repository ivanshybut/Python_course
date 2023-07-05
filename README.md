# Python course

* Синтаксис Python
1. Условные выражения (if-else):
```python
x = 5
if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
```
2. Циклы (for и while):
```python
   # Цикл for
fruits = ["яблоко", "банан", "апельсин"]

for fruit in fruits:
    print(fruit)

# Цикл while
count = 0

while count < 5:
    print(count)
    count += 1
```
3. Функции:
``` python
def greet(name):
    print("Привет, " + name + "!")

greet("Алиса")
```
4. Работа со строками:
``` python
# Объединение строк
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# Форматирование строк
name = "Алиса"
age = 25
message = f"Меня зовут {name} и мне {age} лет"
print(message)

# Получение подстроки
word = "Python"
substring = word[0:4]
print(substring)
```
5. Работа со списками:
``` python
fruits = ["яблоко", "банан", "апельсин"]

# Добавление элемента в конец списка
fruits.append("груша")

# Доступ к элементам списка по индексу
print(fruits[2])

# Итерация по элементам списка
for fruit in fruits:
    print(fruit)
```
6. Работа с числами:
```python
# Математические операции
x = 5
y = 3

sum = x + y
difference = x - y
product = x * y
quotient = x / y

print(sum, difference, product, quotient)

# Операторы сравнения
a = 10
b = 5

greater = a > b
less = a < b
equal = a == b
not_equal = a != b

print(greater, less, equal, not_equal)
```
7. Работа с условиями и логическими операторами:
``` python
x = 10
y = 5

# Логическое И (and)
if x > 0 and y > 0:
    print("Оба числа положительные")

# Логическое ИЛИ (or)
if x > 0 or y > 0:
    print("Хотя бы одно число положительное")

# Логическое НЕ (not)
if not x > 0:
    print("Число отрицательное или равно нулю")
```
8. Использование оператора цикла for для итерации по последовательности:
``` python
fruits = ["яблоко", "банан", "апельсин"]

# Итерация с использованием индексов
for i in range(len(fruits)):
    print(fruits[i])

# Итерация с использованием элементов
for fruit in fruits:
    print(fruit)
```
9. Использование оператора цикла while для выполнения блока кода до тех пор, пока условие истинно:
``` python
count = 0

while count < 5:
    print(count)
    count += 1
```
10. Введение в функции и возвращение значений:
``` python
def multiply(x, y):
    result = x * y
    return result

product = multiply(3, 4)
print(product)
```
11. Использование ветвления в возвращаемых значениях функций:
``` python
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

result = absolute_value(-3)
print(result)
```



"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def recur(n):
    if n == 0:
        return 0
    return n + recur(n - 1)


n = int(input('Введите число: '))
sum_count = recur(n)
if sum_count == n * (n + 1) / 2:
    print(f'результат {sum:.2f}, равенство выполняется')
else:
    print(f'результат {sum:.2f}, равенство не выполняется')

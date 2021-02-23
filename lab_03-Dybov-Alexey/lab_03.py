### Лабораторная работа № 3: Рекурсия

# Вопрос 1
def sum(n):
    """Вычисляет сумму всех положительных целых от 1 до n включительно.
    Считай, что n >= 1.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    summa = 0
    if n == 0:
        return 0
    elif n == 1:
        return summa + 1
    else:
        return n + sum(n-1)

# Подвопрос 2.1
def sum_every_other_number(n):
    """Возвращает частичную сумму натуральных чисел до n включительно, в которую числа входят через одно.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1    
    else:
        return n + sum_every_other_number(n - 2)
    
# Подвопрос 2.2
def fibonacci(n):
    """Возвращает n-ое число Фибоначчи.

    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return fibonacci(n - 1) + fibonacci(n - 2)

# Подвопрос 2.3
def even_digits(n):
    """Возвращает долю чётных цифр в числе n.

    >>> even_digits(23479837) # 3 / 8
    0.375
    """
    def f(n,counter,num_evens):
        if n == 0:
            return counter / num_evens
        if n % 2 == 0:
            counter += 1
        num_evens += 1
        return f(n // 10, counter, num_evens) 
    return f(n, 0 ,0)

# Вопрос 3
def hailstone(n):
    """Выводит последовательность чисел-градин. Возвращает кол-во элементов.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        print(n)
        return 1
    elif n % 2 == 0:
        print(n)
     #   ar += 1
        return hailstone(n // 2) + 1
    else:
        print(n)
      #  ar += 1
        return hailstone(3 * n + 1) + 1

# Вопрос 4
def gcd(a, b):
    """Возвращает НОД для a и b. Нужно использовать рекурсию.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a == b:
        return a
    if a < b:
        return gcd(a , b - a)
    else:
        return gcd(a - b, a)

# Вопрос 5
def paths(m, n):
    """Вычисляет количество путей из одного угла в другой на поле M на N.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 and n == 1:
        return 1
    if m == 1:
        return 1
    if n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)

# Вопрос 6
def print_move(origin, destination):
    """Печатает информацию о перемещении диска."""
    print("Перемещение диска со стержня", origin, "на стержень", destination)

def move_stack(n, start, end):
    """Выводит последовательность перемещений n дисков с начального стержня
    на конечный в соответствии с правилами Ханойских башен .

    Аргументы:
        n (int): количество дисков
        start (int): начальный стержень, то есть 1, 2 или 3 
        end (int): конечный стержень, то есть 1, 2 или 3

    В задаче в точности три стержня, начальный и конечный должны различаться. Предполагается,
    что на начальном стержне находится не менее n дисков увеличивающегося размера, а конечный
    либо пуст, либо верхний диск больше любого другого из n дисков на первом стержне.

    >>> move_stack(1, 1, 3)
    Перемещение диска со стержня 1 на стержень 3
    >>> move_stack(2, 1, 3)
    Перемещение диска со стержня 1 на стержень 2
    Перемещение диска со стержня 1 на стержень 3
    Перемещение диска со стержня 2 на стержень 3
    >>> move_stack(3, 1, 3)
    Перемещение диска со стержня 1 на стержень 3
    Перемещение диска со стержня 1 на стержень 2
    Перемещение диска со стержня 3 на стержень 2
    Перемещение диска со стержня 1 на стержень 3
    Перемещение диска со стержня 2 на стержень 1
    Перемещение диска со стержня 2 на стержень 3
    Перемещение диска со стержня 1 на стержень 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Плохие аргументы"
    if n==1:
        print_move(start,end)
    else:
        tmp = 6 - start - end
        move_stack(n-1,start,tmp)
        print_move(start,end)
        move_stack(n-1,tmp,end)
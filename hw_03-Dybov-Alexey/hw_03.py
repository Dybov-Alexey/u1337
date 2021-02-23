### HW_02: Рекурсия

# Вопрос 1.

def g(n):
    """Возвращает значение G(n), вычисленное рекурсивно.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Возвращает значение G(n), вычисленное итеративно.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        return n
    else:
        i = 3
        a,s,d = 3,2,1
        sum = 0
        while i != n:
            sum = a + 2 * s + 3 * d
            d = s
            s = a
            a = sum
            i += 1
    return sum
# Вопрос 2.

def has_seven(k):
    """Проверка наличия цифры 7 в k
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    if k % 10 !=7 and k // 10 == 0:
        return False
    return has_seven(k // 10)
# Вопрос 3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"

def pingpong(n):
    """Возвращает n-ый элемент последовательности «пинг-понг».

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def ping(n,a,c,flag):
        c += flag
        if a == n:
            return c
        if has_seven(a) or a % 7 == 0:
            flag *= -1
        return ping(n,a+1,c,flag)
    return ping(n,1,0,1)

# Вопрос 4.

def ten_pairs(n):
    """Возвращает число пар цифр в положительном целом n, в сумме образующих 10.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def f(a,n,c):
        if n % 10 + a==10:
            c+=1
        if n // 10 == 0:
            return c
        return f(a,n//10,c)
    if n // 10 == 0:
        return 0
    return f(n % 10,n // 10,0) + ten_pairs(n // 10)
# Вопрос 5.

def count_change(amount):
    """Возвращает количество способов размена amount киберденьгами.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def power(i,k):
        if k == 0:
            return 1
        if k == 1:
            return i
        return i * power(i,k-1)

    def count_partitions(n, m):
        """Подсчет разбиений n на не превосходящие m части.
        >>> count_partitions(6, 4)
        9
        >>> count_partitions(10, 10)
        42
        """
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            with_m = count_partitions(n-m, m)
            without_m = count_partitions(n, m-power(2,k-1))
            return with_m + without_m
    i = 2
    k = 0
    while power(i,k) <= amount:
        k += 1
    return count_partitions(amount,power(2,k-1))

# Вопрос 6. 

from operator import sub, mul

"""def make_anonymous_factorial():
    "Возвращает выражение, вычисляющее факториал.

    >>> make_anonymous_factorial()(5)
    120
    ""
    return (lambda f: lambda k: f (f, k)) (lambda f, k: k if k == 1 else else mul(k, f(f, sub(k, 1))))"""
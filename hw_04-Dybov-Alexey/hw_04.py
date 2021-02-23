### HW_04: Абстрактные типы данных

# Вопрос 1.
def interval(a, b):
    """Создает интервал от a до b."""
    return [a,b]

def lower_bound(x):
    """Возвращает нижнюю границу интервала x."""
    return x[0]

def upper_bound(x):
    """Возвращает верхнюю границу интервала x."""
    return x[1]

def str_interval(x):
    """Возвращает строковое представление интервала x.

    >>> str_interval(interval(-1, 2))
    'от -1 до 2'
    """
    return 'от {0} до {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Возвращает интервал всевозможных сумм значений из x и y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    'от 3 до 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Возвращает интервал всевозможных произведений значений из x и y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    'от -8 до 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Вопрос 2.
def div_interval(x, y):
    """Возвращает интервал, содержащий частные любых значений из x на 
    любые значения из y.

    Деление реализовано как умножение x на величину, обратную к y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    'от -0.25 до 0.5'
    """
    assert lower_bound(y)!=0 and upper_bound(y)!=0
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Вопрос 3.
def sub_interval(x, y):
    """Возвращает интервал, содержащий разности любых значений из x с 
    любыми значениями из y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    'от -9 до -2'
    """
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Вопрос 4.
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# Вот эти два интервала дают разные результаты при вычислении сопротивления параллельных резисторов:
# interval(10, 20), interval(10, 20)
# Вопрос 5.
def multiple_references_explanation():
    return """Par2 возвращает интервал точнее, чем par1 из-за множественных ссылок в par1"""

# Вопрос 6.
def quadratic(x, a, b, c):
    """Возвращает интервал, описывающий область значения квадратичной функции с
    коэффициентами a, b и c для интервала области определения x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    'от -3 до 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    'от 0 до 10'
    """
    vertex = -b / 2 / a
    vertey = a * vertex * vertex + b * vertex + c
    up = upper_bound(x)
    low = lower_bound(x)
    point1 = a * up * up + b * up + c
    point2 = a * low * low + b * low + c
    print(vertey,point1,point2,up,low)
    if vertey >= up or vertey <=low:
        return interval(min(point1,point2),max(point1,point2))
    else:
        return interval(min(vertey,point1,point2),max(vertey,point1,point2))

# Вопрос 7.
def polynomial(x, c):
    """Возвращает интервал, описывающий область значения полиномиальной функции с
    коэффициентами c для интервала области определения x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    'от -3 до 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    'от 0 до 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    'от 18.0 до 23.0'
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Метод Ньютона (вдруг пригодится)

def improve(update, close, guess=1, max_updates=100):
    """Итеративно улучшает guess с помощью update, пока close(guess) является ложью или
    количество итераций меньше max_updates."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, guess=1):
    """Возвращает нули функции f, имеющую производную df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

def newton_update(f, df):
    """Возвращает функцию update для функции f, имеющей производную df, используя
    метод Ньютона."""
    def update(x):
        return x - f(x) / df(x)
    return update
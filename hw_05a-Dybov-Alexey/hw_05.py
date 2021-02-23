### HW_05: Абстрактные типы данных, изменчивые функции и генераторы

###########
# Деревья #
###########

def tree(label, branches=[]):
    """Создаёт новое дерево с заданным корневым значением и списком ветвей."""
    for branch in branches:
        assert is_tree(branch), 'ветви должны быть деревьями'
    return [label] + list(branches)

def label(tree):
    """Возвращает корневое значение дерева."""
    return tree[0]

def branches(tree):
    """Возвращает список ветвей дерева."""
    return tree[1:]

def is_tree(tree):
    """Возвращает True, если аргумент — дерево, иначе False."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Возвращает True, если список веток пуст, иначе False."""
    return not branches(tree)

def print_tree(t, indent=0):
    """Выводит представление дерева, в котором каждое значение узла
    сдвигается на два пробела за каждый уровень глубины.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Возвращает копию t. Используется только для тестов.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

# Вопрос 1.
def replace_leaf(t, old, new):
    """Возвращает новое дерево, в котором все листы со значением old заменены на new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # копирование yggdrasil для тестирования
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Проверка, что исходное дерево не изменилось
    True
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

##########
# Мобили #
##########

def mobile(left, right):
    """Создаёт мобиль из правой и левой сторон."""
    assert is_side(left), "Аргумент left должен быть стороной (side)"
    assert is_side(right), "Аргумент right должен быть стороной (side)"
    return ['mobile', left, right]

def is_mobile(m):
    """Проверяет, что m является мобилем."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Возвращает левую сторону мобиля."""
    assert is_mobile(m), "Аргумент m должен быть мобилем (mobile)"
    return m[1]

def right(m):
    """Возвращает правую сторону мобиля."""
    assert is_mobile(m), "Аргумент m должен быть мобилем (mobile)"
    return m[2]

def side(length, mobile_or_weight):
    """Создаёт ветвь (сторону) из длины стержня length и одного из:
       мобиля mobile или груза weight."""
    assert is_mobile(mobile_or_weight) or is_weight(mobile_or_weight)
    return ['side', length, mobile_or_weight]

def is_side(s):
    """Проверяет, что s — сторона side."""
    return type(s) == list and len(s) == 3 and s[0] == 'side'

def length(s):
    """Возвращает длину стержня стороны."""
    assert is_side(s), "Аргумент s должен быть стороной (side)"
    return s[1]

def end(s):
    """Возвращает мобиль или груз."""
    assert is_side(s), "Аргумент s должен быть стороной (side)"
    return s[2]

# Вопрос 2.
def weight(size):
    """Создаёт груз размера size."""
    assert size > 0
    "*** ТВОЙ КОД ЗДЕСЬ ***"

def size(w):
    """Возвращает размер груза."""
    assert is_weight(w), 'Аргумент w должен быть грузом (weight)'
    "*** ТВОЙ КОД ЗДЕСЬ ***"

def is_weight(w):
    """Проверяет, что w — груз."""
    return type(w) == list and len(w) == 2 and w[0] == 'weight'

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)

def total_weight(m):
    """Возвращает полный вес m — груза или мобиля.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "Аргумент m должен быть мобилем или грузом"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

# Вопрос 3.
def balanced(m):
    """Проверяет, что мобиль m сбалансирован.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 4.
def totals_tree(m):
    """Возвращает дерево, описывающее распределение веса в мобиле.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 5.
def make_counter():
    """Возвращает функцию counter.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 6.
def make_fib():
    """Возвращает функцию, возвращающую следующее число Фибоначчи при каждом вызове.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 7.
def make_withdraw(balance, password):
    """Возвращает защищённую паролем функцию withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Недостаточно средств'
    >>> error = w(25, 'hwat')
    >>> error
    'Неверный пароль'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Неверный пароль'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Неверный пароль'
    >>> w(10, 'hax0r')
    "Твой аккаунт заблокирован. Попытки входа: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Твой аккаунт заблокирован. Попытки входа: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 8.
def make_joint(withdraw, old_password, new_password):
    """Возвращает защищенную паролем функцию, которая присоединяется к существующей функции withdraw с новым паролем.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Неверный пароль'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Неверный пароль'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Недостаточно средств'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Неверный пароль'
    >>> j2(5, 'secret')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Твой аккаунт заблокирован. Попытки входа: ['my', 'secret', 'password']"
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"

# Вопрос 9.
def generate_paths(t, x):
    """Возвращает генератор всех возможных путей от корня t до значения x в виде списков.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"
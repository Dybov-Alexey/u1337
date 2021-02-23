### Лабораторная работа № 5: Списки и деревья"""

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    return [label(tree)] + sum([leaves(b) for b in branches(tree)], [])
# Вопрос 1.
def acorn_finder(t):
    """Возвращает True, если t содержит узел со значением 'жёлудь', иначе False.

    >>> scrat = tree('жёлудь')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('ветвь1', [tree('лист'), tree('жёлудь')]), tree('ветвь2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    def leaves(tree):
        if is_leaf(tree):
            return [label(tree)]
        return [label(tree)] + sum([leaves(b) for b in branches(tree)], [])
    lst = leaves(t)
    for b in lst:
        if b == 'жёлудь':
            return True
    return False

# Вопрос 2.
def prune_leaves(t, vals):
    """Возвращает изменённую копию t, в которой все листья со значениями, равными
    элементам списка vals, удаляются.  Возвращает None, если от дерева ничего не осталось.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t) and (label(t) in vals):
        return None
    return tree(label(t), [prune_leaves(x, vals) for x in branches(t) if not is_leaf(x) or ((label(x) not in vals) and is_leaf(x))])

# Вопрос 3.
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def h(f):
        nonlocal n
        n = f(n)
        return n
    return h

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

# Шекспир и словари

# Вопрос 4.
def build_successors_table(tokens):
    """Возвращает словарь: ключи — слова; значения — списки последующих слов.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table.update({prev:[]})
        table[prev] += [word]
        prev = word
    return table

# Вопрос 5.
def construct_sent(word, table):
    """Печатает случайную фразу начиная со слова word, составляя её по table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'

    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result += word +' '
        word = random.choice(table.get(word,0))
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Возвращает слова пьес Шекспира списком."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Раскомментируй две следующие строки
tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# Вопрос 6.
def sprout_leaves(t, vals):
    """Наращивает новые листы, содержащие данные из vals на каждый лист
    исходного дерева t и возвращает результирующее дерево.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t),[tree(x) for x in vals])
    else:
        bs = [sprout_leaves(b,vals) for b in branches(t)]
        return tree(label(t), bs)

# Вопрос 7.
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"
"""Игра в Свинью."""

from dice import six_sided, four_sided, make_test_dice

GOAL_SCORE = 100  # Цель игры — набрать 100 очков.

######################
# Часть 1: Симулятор #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Симулирует бросание игральной кости DICE в точности NUM_ROLLS > 0 раз.
    Возвращает либо сумму результатов, либо 1, если хоть раз выпала 1.

    num_rolls:  Число бросков кости, которые нужно сделать.
    dice:       Функция без аргументов, возвращает результат отдельного броска.
    """
    # Эти assert-инструкции проверяют, что num_rolls является положительным
    # целым.
    assert type(num_rolls) == int, 'Значение num_rolls должно быть целым.'
    assert num_rolls > 0, 'Значение num_rolls должно быть больше нуля.'
    # НАЧАЛО ЗАДАЧИ 1
    sum = 0
    flag = False
    while num_rolls!=0:
        if dice() == 1:
            flag = True
        sum = sum + dice()
        num_rolls = num_rolls - 1
    if flag == False:
        return sum
    else:
        return 1
    # КОНЕЦ ЗАДАЧИ 1


def free_bacon(score):  
    """Возвращает количество очков от броска 0 костей (Халявный бекон).

    score:  Текущие очки противника.
    """
    assert score < 100, 'Игра должна быть завершена.'
    # НАЧАЛО ЗАДАЧИ 2
    return 10 - min(score // 10,score % 10)
    # КОНЕЦ ЗАДАЧИ 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Симуляция хода с NUM_ROLLS бросками кости DICE, значение num_rolls может
    быть равно нулю (Халявный бекон). Возвращает количество очков, полученное
    текущим игроком за ход.

    num_rolls:       Число бросков кости, которые нужно сделать.
    opponent_score:  Количество очков противника.
    dice:            Функция без аргументов, возвращает результат одного броска.
    """
    # Не трогай эти ассерты, они помогают отыскивать ошибки.
    assert type(num_rolls) == int, 'Значение num_rolls должно быть целым.'
    assert num_rolls >= 0, 'Невозможно бросить кость отрицательное количество раз в take_turn.'
    assert num_rolls <= 10, 'Невозможно бросить кость более 10 раз.'
    assert opponent_score < 100, 'Игра должна быть завершена.'
    # НАЧАЛО ЗАДАЧИ 3
    if num_rolls==0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls,dice)
    # КОНЕЦ ЗАДАЧИ 3


def is_swap(player_score, opponent_score):
    """
    Проверяет, что очки игроков должны поменяться местами.
    """
    # НАЧАЛО ЗАДАЧИ 4
    if player_score//100 != 0:
        numeral1 = player_score//100
    elif player_score // 10 == 0:
        numeral1 = player_score % 10
    else:
        numeral1 = player_score//10
    if opponent_score//100 != 0:
        numeral2 = opponent_score//100
    elif opponent_score // 10 == 0:
        numeral2 = opponent_score % 10
    else:
        numeral2 = opponent_score//10
    if numeral1 * player_score % 10 == numeral2 * opponent_score % 10:
        return True
    else:
        return False
    # КОНЕЦ ЗАДАЧИ 4


def other(player):
    """Возвращает индекс противника, допустимые значения PLAYER: 0 и 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def silence(score0, score1):
    """Ничего не сообщает (смотри Часть 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Cимулирует игру в Свинью и возвращает итоговые очки
    для обоих игроков: сначала очки игрока «0», затем очки игрока «1».

    Функция strategy принимает очки обоих игроков (текущего игрока и противника)
    и возвращает количество бросков для текущего игрока в этом ходе.

    strategy0:  Стратегия игрока 0, он ходит первым.
    strategy1:  Стратегия игрока 1, он ходит вторым.
    score0:     Начальное количество очков игрока 0.
    score1:     Начальное количество очков игрока 1.
    dice:       Функция без аргументов, возвращает результат отдельного броска.
    goal:       Игра заканчивается и кто-то побеждает при достижении этого количества очков.
    say:        Функция-комментарий для вызова в конце первого хода.
    feral_hogs: Булева величина, указывающая на включение правила Мохнатых хрюшек.
    """
    player = 0  # Хранит информацию о том, чей ход; игрока 0 или игрока 1.
    # НАЧАЛО ЗАДАЧИ 5
    last_dice1 = -5
    last_dice0 = -5
    while score0 < goal and score1 < goal:
        if player:
            str_result1 = strategy1(score1, score0)
            if abs(last_dice1 - str_result1) == 2 and feral_hogs:
                score1 += 3
 
            score1 += take_turn(str_result1, score0, dice)
            last_dice1 = str_result1
        else:
            str_result0 = strategy0(score0, score1)
            if abs(last_dice0 - str_result0) == 2 and feral_hogs:
                score0 += 3
 
            score0 += take_turn(str_result0, score1, dice)
            last_dice0 = str_result0
 
        if is_swap(score1, score0):
                score1, score0 = score0, score1
 
        player = other(player)
    # КОНЕЦ ЗАДАЧИ 5
    # (кстати, отступ для решения задачи 6 может быть недостаточным)
    # НАЧАЛО ЗАДАЧИ 6

    # КОНЕЦ ЗАДАЧИ 6
    return score0, score1


########################
# Часть 2: Комментарии #
########################


def say_scores(score0, score1):
    """Сообщает текущий счёт каждого игрока."""
    print("Игрок 0 набрал", score0, "очков, а Игрок 1 набрал", score1)
    return say_scores

def announce_lead_changes(previous_leader=None):
    """Возвращает функцию, которая сообщает о смене лидера.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Игрок 0 вырвался вперёд на 5
    >>> f2 = f1(5, 12)
    Игрок 1 вырвался вперёд на 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Игрок 0 вырвался вперёд на 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != previous_leader:
            print('Игрок', leader, 'вырвался вперёд на', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

def both(f, g):
    """Выводит дав сообщения — первое с помощью f, второе с помощью g.

    NOTE: Следующие примеры не могут иметь место в реальной игре, это
    просто доктесты.

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Игрок 0 набрал 10 очков, а Игрок 1 набрал 0
    Игрок 0 вырвался вперёд на 10
    >>> h2 = h1(10, 6)
    Игрок 0 набрал 10 очков, а Игрок 1 набрал 6
    >>> h3 = h2(6, 17)
    Игрок 0 набрал 6 очков, а Игрок 1 набрал 17
    Игрок 1 вырвался вперёд на 11
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, previous_high=0, previous_score=0):
    """Выводит сообщение, когда ход приносит максимальное за игру количество
    очков игроку WHO.

    NOTE: Следующие примеры не могут иметь место в реальной игре, это
    просто доктесты.

    >>> f0 = announce_highest(1) # Сообщает только об успехах Игрока 1
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 очка(ов)! Лучший результат для Игрока 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 очка(ов)! Лучший результат для Игрока 1
    >>> f6 = f5(20, 47) # Игрок 1 получает 12 очков; недостаточно для рекорда
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 очка(ов)! Лучший результат для Игрока 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 очка(ов)! Лучший результат для Игрока 1
    """
    assert who == 0 or who == 1, 'Аргумент who должен идентифицировать игрока.'
    # НАЧАЛО ЗАДАЧИ 7
    "*** ТВОЙ КОД ЗДЕСЬ ***"
    # КОНЕЦ ЗАДАЧИ 7


######################
# Часть 3: Стратегии #
######################


def always_roll(n):
    """Возвращает стратегию, в которой всегда бросается N костей.

    Стратегия — это функция, принимающая два аргумента: количество очков
    текущего игрока и количество очков противника. Возвращает число бросков
    костей для текущего хода игрока.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(fn, num_samples=1000):
    """Возвращает функцию, которая возвращает среднее значение от NUM_SAMPLES
    вызовов функции FN.

    Для создания этой функции потребуется использовать синтаксис *args, который
    не был рассмотрен на лекциях. Так что смотри описание проекта.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # НАЧАЛО ЗАДАЧИ 8
    "*** ТВОЙ КОД ЗДЕСЬ ***"
    # КОНЕЦ ЗАДАЧИ 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Возвращает число бросков (от 1 до 10), которое приведет в среднем
    к максимальному количеству очков за ход. Функция многократно вызывает
    roll_dice с заданной костью DICE.
    Считай, что кость DICE всегда возвращает положительные результаты.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # НАЧАЛО ЗАДАЧИ 9
    "*** ТВОЙ КОД ЗДЕСЬ ***"
    # КОНЕЦ ЗАДАЧИ 9


def winner(strategy0, strategy1):
    """Возвращает 0, если strategy0 выигрывает против strategy1, иначе 1."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """
    Возвращает усреднённую долю побед (от 0 до 1) стратегии STRATEGY против
    другой стратегии BASELINE. Усреднение учитывает, что начинает игру любая
    из стратегий.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Запускает набор экспериментов со стратегией и выводит информацию
    о результатах."""
    if False:  # Измени на False, когда закончишь вопрос про max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Наиболее выгодное количество бросков для шестигранной кости:', six_sided_max)

    if False:  # Измени на True для теста always_roll(6)
        print('Доля побед для always_roll(6):', average_win_rate(always_roll(6)))

    if False:  # Измени на True для теста bacon_strategy
        print('Доля побед для bacon_strategy:', average_win_rate(bacon_strategy))

    if False:  # Измени на True для теста swap_strategy
        print('Доля побед для swap_strategy:', average_win_rate(swap_strategy))

    if True:  # Измени на True для теста final_strategy
        print('Доля побед для final_strategy:', average_win_rate(final_strategy))

    "*** Тут можешь добавить дополнительные эксперименты, если хочешь ***"


def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """
    Эта стратегия запустит 0 костей, если можно получить по крайней мере
    MARGIN очков, в противном случае вернёт NUM_ROLLS.
    """
    # НАЧАЛО ЗАДАЧИ 10
    return 4  # Замени эту инструкцию
    # КОНЕЦ ЗАДАЧИ 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """Эта стратегия запустит 0 костей, если она сработала как выгодный
    переворот. Также она запустит 0 костей, если можно получить по крайней мере
    MARGIN очков и не использовать невыгодный переворот. Иначе запустит
    NUM_ROLLS костей.
    """
    # НАЧАЛО ЗАДАЧИ 11
    return 4  # Замени эту инструкцию
    # КОНЕЦ ЗАДАЧИ 11


def final_strategy(score, opponent_score):
    """Напиши краткое описание твоей финальной стратегии.

    *** ТВОЁ ОПИСАНИЕ ЗДЕСЬ ***
    """
    # НАЧАЛО ЗАДАЧИ 12
    return 4  # Замени эту инструкцию
    # КОНЕЦ ЗАДАЧИ 12

##############################
# Интерфейс командной строки #
##############################

# Учти: Функции в этой секции не должны меняться. Здесь используются возможности
#       Python выходящие за рамки курса.

def run(*args):
    """Считывает аргументы командной строки и вызывает соответствующие
    функции.

    Эта функция использует возможности Python выходящие за пределы курса.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Игра в Свинью")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Запускает эксперименты со стратегиями')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    run(*args)
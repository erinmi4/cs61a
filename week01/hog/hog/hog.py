"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    sum = 0 
    sow_sad = 0 
    i = 1 
    """
    在这里其实有一个问题，如果不使用 x = dice()的结果
    只是使用dice()的结果来比较的话，因为每次调用dice函数之后，都会修改index的数值
    这样就会导致结果不同
    """
    while i <= num_rolls :
        i +=  1 
        x = dice()
        if x == 1 :
            sow_sad = 1
        else : 
            sum += x
    if sow_sad == 1 : 
        sum = 1 
    return sum
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.
    <<<boar_brawl(72,29)
    1
    <<<boar_brawl(12,14)
    3
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    player_score = player_score % 10 
    opponent_score = (opponent_score // 10) % 10 
    i  = 3 * abs(player_score - opponent_score)
    if i == 0: 
        return 1 
    else:
        return i 
    # END PROBLEM 2

# 获得的点数
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.
# 返回获得的点数,同时考虑到了播种忧伤和野猪冲撞
    >>>take_turn(2,7,21,make_test_dice(4,5,1))
    9
    >>>take_turn(2,7,21,make_test_dice(4,5,1))
    1
    >>>take_turn(0,7,21,make_test_dice(4,5,1))
    15
    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls != 0 :
        point = roll_dice(num_rolls,dice)
    else: 
        point = boar_brawl(player_score, opponent_score)
    return point
    # END PROBLEM 3

# 考虑前面两个规则之后，获得的总点数
def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

# 规则2
def num_factors(n):
    """Return the number of factors of N, including 1 and N itself.
    >>> num_factors(10)
    4
    看能否实现整除,
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    num , i = 0 , 1  
    while i <= n   :
        if n % i == 0 : 
            num += 1 
        i += 1 
    return num 
    # END PROBLEM 4

# 在当前策略下，考虑到所有规则可以得到的点数
def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule.
    >>> sus_points(64)
    64 
    >>> sys_points(10)
    11
    >>> sus_points(21)
    23   
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if num_factors(score) in [3,4] :
        while is_prime(score) != 1 : 
            score +=  1
            
    return score 
    # END PROBLEM 4

# 考虑到前面的所有规则得到的结果 （修改后的总点数）
def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    返回总得分，需要考虑到之前的所有情况，还有应用simple_update
    >>> sus_update(0,15,37)
    23
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    ## 经历前两个条件
    score = simple_update(num_rolls, player_score, opponent_score, dice)
    score = sus_points(score)
    return score
    # END PROBLEM 4

# 策略 ： 总是丢五个
def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # 返回的是本轮结束后 双方各自的点数
    who = 0 # 一开始是 选手 0 ，然后是选手 1 ， 1 - who
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 = update(strategy0(score0, score1), score0, score1, dice)
        else:
            score1 = update(strategy1(score1, score0), score1, score0, dice)
        who = 1 - who
    # END PROBLEM 5
    return score0, score1



#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def roll_nums(point , opponent_point):
        return  n
    return  roll_nums
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # 本质意思是 ，扔到任意一种结果都是等可能的
    num_dice = strategy(0, 0)
    for i in range(goal):
        for j in range(goal):
            if strategy(i, j) != num_dice:
                return False

    return True
    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    返回的是，对于一种方案，执行sample_count 次数后，  对其求平均值 ，
    特别注意，对于返回的函数的参数，实际上也是original_function 的参数 。

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def averaged(*args) :
        i = 0
        result = 0
        while i < samples_count :
            result += original_function(*args) # 如果 函数是 dice_roll 则会返回通过骰子计算的点数
            i += 1
        return result/samples_count
    return averaged
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    max_score = 0
    averaged_dice = make_averaged(roll_dice, samples_count)
    best_dice_num = 0
    for i in range(1, 11):
        averaged_score = averaged_dice(i, dice)
        if averaged_score > max_score:
            best_dice_num = i
            max_score = averaged_score
    return best_dice_num
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    at_least = boar_brawl(score,opponent_score) # 求保底
    if at_least >= threshold : # 取保底
        return  0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    score_after_boar = score + boar_brawl(score, opponent_score)
    if sus_points(score_after_boar) - score >= threshold:
        return 0
    return num_rolls  # Remove this line once implemented.    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
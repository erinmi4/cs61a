"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact
from hog import boar_brawl,roll_dice

GOAL = 100  # The goal of Hog is to score 100 points.

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
    Fuss rule is in effect.# 使用所有规则

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.    # 策略返回的是玩家将要投掷的次数 

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).sus 或者 simple 
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # 从 0 开始 who = 0 , 下一个玩家是 1 ，所以是 who = 1 - who
    # 判断本轮的对象是谁
    while score0 < goal and score1 < goal :
        who = 0  
        print(score0 , score1 )

        if who == 0 : 
            strategy = strategy0
            player = score0
            opponent = score1
        else: 
            strategy = strategy1
            player = score1
            opponent = score0

        # 对who 迭代
        who = 1 - who 
        
        # 不同的规则有不同的情况
        if update == simple_update : 
            player+=simple_update(strategy,player, opponent, dice)
        else : 
            player+=sus_update(strategy,player, opponent, dice)

        
    # END PROBLEM 5
    return score0, score1

play(5, 5, sus_update)
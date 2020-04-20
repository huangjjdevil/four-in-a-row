# 这是我们自己编写的代码，所有的函数在完整实现后请复制到这里，在所有人的工作完成之后，这个文件的代码应能在AIGAMEING上直接运行。

## _____                  ___            _      ____
# |  ___|__  _   _ _ __  |_ _|_ __      / \    |  _ \ _____      __
# | |_ / _ \| | | | '__|  | || '_ \    / _ \   | |_) / _ \ \ /\ / /
# |  _| (_) | |_| | |     | || | | |  / ___ \  |  _ < (_) \ V  V /
# |_|  \___/ \__,_|_|    |___|_| |_| /_/   \_\ |_| \_\___/ \_/\_/
#

botName='demo-defbot'

import json
from random import randint


# These are the only additional libraries available to you. Uncomment them
# to use them in your solution.
#
#import numpy    # Base N-dimensional array package
#import pandas   # Data structures & analysis


# =============================================================================
# This calculateMove() function is where you need to write your code. When it
# is first loaded, it will play a complete game for you using the Helper
# functions that are defined below. The Helper functions give great example
# code that shows you how to manipulate the data you receive and the move
# that you have to return.
#

def calculateMove(gameState):

    # When manipulating the Board remember the positions are as follows
    #
    # 0| -   -   -   -   -   -   -
    # 1| -   -   -   -   -   -   -
    # 2| -   -   -   -   -   -   -
    # 3| -   R   R   Y   Y   -   -
    # 4| -   Y   R   R   R   -   -
    # 5| Y   R   R   Y   Y   -   Y
    # ----------------------------
    #    0   1   2   3   4   5   6
    #
    #
    # 0|-1  -1  -1  -1  -1  -1  -1
    # 1|-1  -1  -1  -1  -1  -1  -1
    # 2|-1  -1  -1  -1  -1  -1  -1
    # 3|-1   1   1   0   0  -1  -1
    # 4|-1   0   1   1   1  -1  -1
    # 5| 0   1   1   0   0  -1   0
    # ----------------------------
    #    0   1   2   3   4   5   6
    #
    # -1 - Empty space
    #  0 - Your disc in this case yellow (Y)
    #  1 - Your opponents disc red (R)

    #print(gameState["Board"])

    #makes a random drop in any column that is not full
    dropColumn=randint(0, len(gameState["Board"][0])-1)
    while isColumnFullX(dropColumn,gameState["Board"]):
        dropColumn=randint(0, len(gameState["Board"][0])-1)

    return {"Column": dropColumn}

def isColumnFullX(dropColumn,board):
    #Check the top row has an empty space
    if len([x[dropColumn] for x in board if x[dropColumn] == -1]) > 0:
        return False

    return True

import copy
from domain import createScore
from validation import validateScore
from utils import addContestant
from utils import listScores
from utils import sortKey
from utils import printList

def addNewContestant(contestantsList, contestantsListHistory, P1, P2, P3):
    '''
    Add new contestant's scores to the list
    '''
    scoresDictionary = createScore(P1, P2, P3)
    validateScore(scoresDictionary)
    addContestant(contestantsList, contestantsListHistory, scoresDictionary)

def insertScores(contestantsList,contestantsListHistory, P1, P2, P3, pos):
    '''
    Inserts the scores P1, P2, P3 to the list of contestants at the given position I
    input:  contestantsList : the list of contestants' scores
            contestantsListHistory : the list of all versions of scores modified before
            scoresDictionary: dictionary containing the 3 scores P1, P2, P3
    output: True : if scores were inserted at given position
            False: if the position is out of range
    '''
    scoresDictionary = createScore(P1, P2, P3)
    if not 0 <= int(scoresDictionary['P1']) <= 10:
        return False
    if not 0 <= int(scoresDictionary['P2']) <= 10:
        return False
    if not 0 <= int(scoresDictionary['P3']) <= 10:
        return False
    if 0 <= pos <= len(contestantsList):
        contestantsList.insert(pos,scoresDictionary)
        contestantsListHistory.append(copy.deepcopy(contestantsList))
        return True
    return False

def removeStartStop(contestantsList,contestantsListHistory,  start, stop):
    '''
    Sets the scores of all participants form start to stop to 0
    input:  contestantsList: the list of the contestants' scores
            contestantsListHistory : the list of all versions of scores modified before
            start, stop: the given positions
    output: True: if the scores were removed
            False: otherwise
    '''
    if(0 <= start < len(contestantsList) - 1 and 0 < stop < len(contestantsList)):
        for i in range(start, stop + 1):
            contestantsList[i] = {'P1': 0, 'P2': 0, 'P3': 0}
        contestantsListHistory.append(copy.deepcopy(contestantsList))
        return True
    return False


def removePosition(contestantsList,contestantsListHistory, pos):
    '''
    Sets the scores of the participant pos to 0
    input:  contestantsList : the list of the contestants
            contestantsListHistory : the list of all versions of scores modified before
            pos: the position of the contestant
    output: True: if the scores were removed
            False: otherwise
    '''
    if(0 <= pos < len(contestantsList)):
        contestantsList[pos] = {'P1':0, 'P2':0, 'P3':0}
        contestantsListHistory.append(copy.deepcopy(contestantsList))
        return True
    return False


def replaceScore(contestantsList, contestantsListHistory, idContestant, problem, newScore):
    '''
    Raplaces the contestant's score at the problem with a new score
    input:  contestantsList: the list of the contestants' scores
            idContestant: the id of the participant
            contestantsListHistory : the list of all versions of scores modified before
            problem : P1, P2 or P3 - the score which must be modified
            newScore: the new value of the score
    output: True: if the score was modified
            False: otherwise
    '''
    if not 0 <= idContestant < len(contestantsList):
        return False
    if not 0 <= newScore <= 10:
        return False
    if problem != "P1" and problem != "P2" and problem != "P3":
        return False
    contestantsList[idContestant].update({problem:newScore})
    contestantsListHistory.append(copy.deepcopy(contestantsList))
    return True


def listScoresCommand(contestantsList, params):
    '''
    Write the participants whose score has different properties.
    '''
    listScores(contestantsList)


def listSortedScores(contestantsList):
    '''
    Prints the list of scores, sorted by the  average score
    input: contestantsList: the list of the contestants
    output:-
    '''
    contestantsList.sort(key=sortKey, reverse=True)
    printList(contestantsList)

def listPropertyScores(contestantsList, averageScore, crit):
    '''
    Lists the scores that satisfly a certain property
    :param contestantsList: the list of contestants
    :param averageScore: the given score
    :param crit: the given property
    :return: -
    '''
    if crit == '=':
        for i in range (0, len(contestantsList)):
            if(int(contestantsList[i]['P1'] + contestantsList[i]['P2'] + contestantsList[i]['P3']) / 3 == averageScore):
                print(contestantsList[i])
    if crit == '>':
        for i in range (0, len(contestantsList)):
            if(int(contestantsList[i]['P1'] + contestantsList[i]['P2'] + contestantsList[i]['P3']) /3 > averageScore):
                print(contestantsList[i])
    if crit == '<':
        for i in range(0, len(contestantsList)):
            if (int(contestantsList[i]['P1'] + contestantsList[i]['P2'] + contestantsList[i]['P3']) /3 < averageScore):
                print(contestantsList[i])

def findAverageScore(contestantsList, start, stop):
    """
    Calculates the average score of the average scores of the contestants between positions start and stop
    :param contestantsList: the list of contestants' scores
    :param start: the starting position
    :param stop: the stop position
    :return: the average score of the average scores of the contestants
    """
    averageScore = 0
    for i in range(start, stop+1):
        x = (contestantsList[i]["P1"] + contestantsList[i]["P2"] + contestantsList[i]["P3"])/3
        averageScore += x
    averageScore /= (stop - start + 1)
    return averageScore


def findMinScore(contestantsList, start, stop):
    """
    Calculates the lowest average score of participants between position start and stop
    :param contestantsList: the list of contestants
    :param start: the start position
    :param stop:  the stop  position
    :return: the lowest average score
    """
    minAverage = 31
    for i in range(start, stop+1):
        x = contestantsList[i]["P1"] + contestantsList[i]["P2"] + contestantsList[i]["P3"]
        if x < minAverage:
            minAverage = x
    minAverage /= 3
    return minAverage

def topContestants(contestantsList, numberOfTopContestants):
    """
    Finds the numberOfTopContestants participants having the highest average score, in descending order of their
    average score.
    :param contestantsList: the list of contestants
    :param numberOfTopContestants: the number of contestants of the top
    :return: the list of the contestants in the top
    """
    topList =[]
    contestantsList.sort(key=sortKey, reverse=True)
    for i in range(0, numberOfTopContestants):
        topList.append(contestantsList[i])
    return topList


def topContestantsProblem(contestantsList, numberOfTopContestants, problem):
    """
    Finds the numberOfTopContestants participants having the highest score on a certain given problem
    :param contestantsList: the list of contestants
    :param numberOfTopContestants: the number of the contestants of the top
    :param problem: the given problem
    return: the list of the top
    """
    topList = []
    contestantsList.sort(key=lambda k: k[problem], reverse=True)
    for i in range (0, numberOfTopContestants):
        topList.append(contestantsList[i])
    return topList

def removeLowerThan(contestantsList, contestantsListHistory, number):
    """
    Sets to 0 all scores, which sum is lower than the given number
    :param contestantsList: the list of contestants
    :param number: the given number
    :param contestantsListHistory:the list of all versions of scores modified before
    :return:True if the changes have been made
            False otherwise
    """
    change = False
    for i in range(0, len(contestantsList)):
        if(int(contestantsList[i]["P1"] + contestantsList[i]["P2"] + contestantsList[i]["P3"])/3 < number):
            contestantsList[i] = {"P1": 0, "P2":0, "P3": 0}
            change = True
    if change:
        contestantsListHistory.append(copy.deepcopy(contestantsList))
        return True
    return False

def removeGreaterThan(contestantsList, contestantsListHistory, number):
    """
    Sets to 0 all scores, which sum is greater than the given number
    :param contestantsList: the list of contestants
    :param number: the given number
    :param contestantsListHistory: the list of all versions of scores modified before
    :return:True if the changes have been made
            False otherwise
    """
    change = False
    for i in range(0, len(contestantsList)):
        if(int(contestantsList[i]["P1"] + contestantsList[i]["P2"] + contestantsList[i]["P3"])/3 > number):
            contestantsList[i] = {"P1": 0, "P2":0, "P3": 0}
            change = True
    if change == True:
        contestantsListHistory.append(copy.deepcopy(contestantsList))
        return True
    else:
        return False

def removeEqualTo(contestantsList, contestantsListHistory, number):
    """
    Sets to 0 all scores, which sum is equal to the given number
    :param contestantsList: the list of contestants
    :param number: the given number
    :param contestantsListHistory: the list of all versions of scores modified before
    :return:True - if changes have been made
            False - otherwise
    """
    change = False
    for i in range(0, len(contestantsList)):
        if(int(contestantsList[i]["P1"] + contestantsList[i]["P2"] + contestantsList[i]["P3"])/3 == number):
            contestantsList[i] = {"P1":0, "P2":0, "P3":0}
            change = True
    if change:
        contestantsListHistory.append(copy.deepcopy(contestantsList))
        return True
    return False

def undo(contestantsListHistory):
    contestantsListHistory.pop()
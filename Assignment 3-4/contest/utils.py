import copy


def addContestant(contestantsList, contestantsListHistory, score):
    contestantsList.append(score)
    contestantsListHistory.append(copy.deepcopy(contestantsList))


def listScores(contestantsList):
    '''
    Prints the entire list
    input: contestantsList -> the list of contestants
    output: -
    '''
    for i in contestantsList:
        print(i)

def sortKey(dict):
    '''
    Generates the key for the sort algorithm
    input: dict -> dictionary
    output: key
    '''
    return dict['P1'] + dict['P2'] + dict['P3']

def printList(contestantsList):
    for i in contestantsList:
        print(i)
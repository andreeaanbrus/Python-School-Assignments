from functionalities import addNewContestant
from functionalities import listScores
from functionalities import listSortedScores
from functionalities import listPropertyScores
from functionalities import insertScores
from functionalities import removePosition
from functionalities import replaceScore
from functionalities import removeStartStop
from functionalities import findAverageScore
from functionalities import findMinScore
from functionalities import topContestants
from functionalities import topContestantsProblem
from functionalities import removeLowerThan
from functionalities import removeGreaterThan
from functionalities import removeEqualTo
from functionalities import undo


def uiChooseInterface(x):
    x = int(input("For comand based press 1.\nFor menu based press 2\n"))
    return x

def uiAddScore(contestantsList, contestantsListHistory, scores):
    x = len(scores)
    if x % 3 != 0:
        print("Invalid input")
        return
    for i in range(0, x, 3):
        if not 0 <= int(scores[i]) <= 100:
            print("Invalid input. Contestant's scores were not added")
            return
        P1 = int(scores[i])
        P2 = int(scores[i + 1])
        P3 = int(scores[i + 2])
        addNewContestant(contestantsList, contestantsListHistory, P1, P2, P3)
        print("Score added!")

def uiInsertScores(contestantsList, contestantsListHistory, params):
    '''
        Insert scores at a position in the list
    '''
    ok = True
    if len(params) < 4 or len(params) > 5:
        print("Invalid input. Scores were not added")
        ok = False
    if (not 0 <= int(params[0]) <= 10):
        print("Invalid input. Scores were not added")
        ok = False
    if (not 0 <= int(params[1]) <= 10):
        print("Invalid input. Scores were not added")
        ok = False
    if (not 0 <= int(params[2]) <= 10):
        print("Invalid input. Scores were not added")
        ok = False
    if ok:
        pos = int(params[4])
        P1 = int(params[0])
        P2 = int(params[1])
        P3 = int(params[2])
        insertScores(contestantsList, contestantsListHistory, P1, P2,P3, pos)
        print("Score inserted!")


def uiRemoveScores(contestantsList,contestantsListHistory, params):
    '''
    Modify the scores from the list
    '''
    if len(params) == 1:
        pos = int(params[0])
        if 0 <= pos < len(contestantsList):
            if removePosition(contestantsList, contestantsListHistory, pos):
                print("The score was removed")
        else:
            print("Invalid input")
    # elif len(params) > 1 and params[1] != "to":
    #     for i in range(0, len(params)):
    #         if 0 <= int(params[i]) < len(contestantsList):
    #             removePosition(contestantsList, int(params[i]))
    elif len(params) > 1 and params[1] == "to":
        start = int(params[0])
        stop = int(params[2])
        if 0 <= start < len(contestantsList) - 1 and 1 <= stop < len(contestantsList):
            if removeStartStop(contestantsList, contestantsListHistory, start, stop):
                print("The scores were removed")
        else:
            print("Invalid input. The scores were not modified.")
    elif len(params) > 1:
        if params[0] == ">" or params[0] == "=" or params[0] == "<":
            number = int(params[1])
            if not 0 < number <= 30:
                print("Invalid input!")
                return
            if params[0] == ">":
                if(removeGreaterThan(contestantsList, contestantsListHistory, number) == True):
                    print("Changes have been made!")
                else:
                    print("There are no scores greater than the given number")
            if params[0] == "<":
                if(removeLowerThan(contestantsList, contestantsListHistory, number)):
                    print("Changes have been made!")
                else:
                    print("There are no scores lower than the given number")
            if params[0] == "=":
                if(removeEqualTo(contestantsList, contestantsListHistory, number)):
                    print("Changes have been made")
                else:
                    print("There are no scores equal to the given number")


def uiReplaceScore(contestantsList, contestantsListHistory, params):
    '''
    Replace the score obtained by a participant at a certain problem with a new given score
    '''
    ok = True
    if len(params) != 4:
        ok = False
    if 0 <= int(params[0]) < len(contestantsList):
        idContestant = int(params[0])
    else:
        ok = False
    if(params[1] == "P1" or params[1] == "P2" or params[1] == "P3"):
        problem = params[1]
    else:
        ok = False
    if 0 <= int(params[3]) <= 10:
        newScore = int(params[3])
    else:
        ok = False
    if ok == True:
            replaceScore(contestantsList,contestantsListHistory, idContestant, problem, newScore)
            print("The score was modified")
    else:
        print("Invalid input. The score was not modified")


def uiListScores(sList, params):
    if(not params):
        listScores(sList)
    elif params[0] == "sorted":
            listSortedScores(sList)
    elif (params[0] == '<' or params[0] == '>' or params[0] == '='):
        if(0 <= int(params[1]) <= 30):
            averageScore = int(params[1])
            crit = '='
            if(params[0] == '<'):
                crit = '<'
            if(params[0] == '>'):
                crit = '>'
            listPropertyScores(sList, averageScore, crit)
        else:
            print("Invalid input")
    else:
        print("Invalid input")


def uiAverageScores(sList, params):
    '''
    Writes the average of the average scores of the participants between positions given
    '''
    if len(params) != 3:
        print("Invalid input")
        return
    startPosition = int(params[0])
    stopPosition = int(params[2])
    if not 0 <= startPosition < len(sList):
        print("Invalid input. Start position not in range")
        return
    if not 0 <= stopPosition < len(sList):
        print("Invalid input. Stop position not in range")
        return
    x = findAverageScore(sList, startPosition, stopPosition)
    print(x)

def uiMinimAverageScore(sList, params):
    """
    Writes the lowest average score of the participants between positions given
    """
    startPosition = int(params[0])
    stopPosition = int(params[2])
    if not 0 <= startPosition < len(sList):
        print("Invalid input. Start position not in range")
        return
    if not 0 <= stopPosition < len(sList):
        print("Invalid input. Stop position not in range")
        return
    x = findMinScore(sList, startPosition, stopPosition)
    print(x)


def uiTop(sList, params):
    """
    Write the n(given) participants having the highest average score, in descending order of their
    average score or write the n(given) participants who obtained the highest score for problem P1, P2 or P3(given), sorted
    descending by that score.
    """
    if len(params) == 1:
        numberOfTopContestants = int(params[0])
        if 1 > numberOfTopContestants:
            print("Invalid input! The number of contestants on too is too low!")
            return
        if numberOfTopContestants > len(sList):
            print("Invalid input! The number of contestants is too high!")
            return
        resList = topContestants(sList, numberOfTopContestants)
        listScores(resList)
    if len(params) == 2:
        numberOfTopContestants = int(params[0])
        problem = params[1]
        if 1 > numberOfTopContestants:
            print("Invalid input! The number of contestants on too is too low!")
            return
        if numberOfTopContestants > len(sList):
            print("Invalid input! The number of contestants is too high!")
            return
        if problem != "P1" and problem != "P2" and problem != "P3":
            print("Invalid input! Problem name inexistent!")
            return
        resList = topContestantsProblem(sList, numberOfTopContestants, problem)
        listScores(resList)


def uiUndo(contestantsListHystory):
    if len(contestantsListHystory) <= 1:
        print("There is no undo possible")
        return
    undo(contestantsListHystory)
    print("The undo was made. Use 'list' to see the scores!")

def uiListHelp():
    '''
    Prints the help menu
    '''
    print("Valid commands:")
    print("\t add <P1 score> <P2 score> <P3 score>")
    print("\t insert <P1 score> <P2 score> <P3 score> at <position>")
    print("\t remove <position>")
    print("\t remove <start position> to <end position>")
    print("\t replace <old score> <P1 | P2 | P3> with <new score>")
    print("\t list")
    print("\t list sorted")
    print("\t list [ < | = | > ] <score>")
    print("\t avg <start position> to <end position>")
    print("\t min <start position> to <end position>")
    print("\t top <number>")
    print("\t top <number> <P1 | P2 | P3>")
    print("\t remove [ < | = | > ] <score>")
    print("\t undo")
    print(" \t help")
    print("\t exit")


def uiListHelpMenu():
    '''
    Prints the help menu
    '''
    print("Valid commands:")
    print("\t 1 <P1 score> <P2 score> <P3 score>")
    print("\t 2 <P1 score> <P2 score> <P3 score> at <position>")
    print("\t 3 <position>")
    print("\t 3 [ < | = | > ] <score>")
    print("\t 3 <start position> to <end position>")
    print("\t 4 <old score> <P1 | P2 | P3> with <new score>")
    print("\t 5 -")
    print("\t 5 sorted")
    print("\t 5 [ < | = | > ] <score>")
    print("\t 6 <start position> to <end position>")
    print("\t 7 <start position> to <end position>")
    print("\t 8 <number>")
    print("\t 8 <number> <P1 | P2 | P3>")

def uiPrintMenu():
    '''
    Prints the menu
    :return: -
    '''
    print("1 -> Add a new contestant")
    print("2 -> Insert score at a given position")
    print("3 -> Remove a position or remove positions from start to stop or remove all scores < > = with a given average")
    print("4 -> Replace old score with new score")
    print("5 -> Print the list, print the list sorted or print the participants having the average score < > = with a given number")
    print("6 -> Print the average of the average scores for participants between positions given")
    print("7 -> Print the lowest average score of the participants between positions given")
    print("8 -> Print the top n-given or print the top n-given participants who obtained the highest score on a certain problem")
    print("9 -> Undo")
    print("10 -> Help")
    print("11 -> Exit")
import copy
from tests import testInit
from ui import uiAddScore
from ui import uiListScores
from ui import uiListHelp
from ui import uiInsertScores
from ui import uiRemoveScores
from ui import uiReplaceScore
from ui import uiAverageScores
from ui import uiMinimAverageScore
from ui import uiTop
from ui import uiChooseInterface
from ui import uiPrintMenu
from ui import uiUndo
from ui import uiListHelpMenu
from tests import runAllTests

def readCommand():
    '''
    Read and parse user comand
    input: -
    output: (comand, params) tuple, where:
            command = user comand
            params = parameters
    '''
    cmd = input("command: ")
    if cmd.find(" ") == -1:
        '''
        No parameters
        '''
        command = cmd
        params = ""
    else:
        '''
        We have parameters
        '''
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(" "):]
        params = params[1:].split(' ')
        for i in range (0, len(params)):
            params[i] = params[i].strip()
    return  (command, params)


def readParams():
    '''
    Read the parameters for the menu based version
    :return:params = parameters
    '''
    params = input("Give the parameters ")
    if len(params) == 0:
        params = ""
    else:
        params = params.split(' ')
        for i in range(0, len(params)):
            params[i] = params[i].strip()
    return params


def start():
    x = 0
    if(uiChooseInterface(x) == 1):
        contestantsList = []
        testInit(contestantsList)
        contestantsListHistory = [copy.deepcopy(contestantsList)]
        while True:
            cmd = readCommand()
            command = cmd[0]
            params = cmd[1]
            if command == 'add':
                uiAddScore(contestantsList, contestantsListHistory, params)
            elif command == 'insert':
                uiInsertScores(contestantsList, contestantsListHistory, params)
            elif command == 'remove':
                uiRemoveScores(contestantsList, contestantsListHistory, params)
            elif command == 'replace':
                uiReplaceScore(contestantsList, contestantsListHistory, params)
            elif command == 'list':
                uiListScores(contestantsList, params)
            elif command == 'avg':
                uiAverageScores(contestantsList, params)
            elif command == 'min':
                uiMinimAverageScore(contestantsList, params)
            elif command == 'top':
                uiTop(contestantsList, params)
            elif command == 'undo':
                uiUndo(contestantsListHistory)
            elif command == 'help':
                uiListHelp()
            elif command == 'exit':
                break
            elif command == 'dbg':
                for i in contestantsListHistory:
                    print(type(i), i)
            else:
                print("Invalid command")
            contestantsList = copy.deepcopy(contestantsListHistory[-1])

    else:
        contestantsList = []
        testInit(contestantsList)
        contestantsListHistory = [copy.deepcopy(contestantsList)]
        while True:
            uiPrintMenu()
            choice = int(input())
            params = readParams()
            if choice == 1:
                uiAddScore(contestantsList, contestantsListHistory, params)
            elif choice == 2:
                uiInsertScores(contestantsList, contestantsListHistory, params)
            elif choice == 3:
                uiRemoveScores(contestantsList, contestantsListHistory, params)
            elif choice == 4:
                uiReplaceScore(contestantsList, contestantsListHistory, params)
            elif choice == 5:
                uiListScores(contestantsList, params)
            elif choice == 6:
                uiAverageScores(contestantsList, params)
            elif choice == 7:
                uiMinimAverageScore(contestantsList, params)
            elif choice == 8:
                uiTop(contestantsList, params)
            elif choice == 9:
                uiUndo(contestantsListHistory)
            elif choice == 10:
                uiListHelpMenu()
            elif choice == 11:
                break
            contestantsList = copy.deepcopy(contestantsListHistory[-1])



start()
#runAllTests()
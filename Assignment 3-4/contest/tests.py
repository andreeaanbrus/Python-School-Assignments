from functionalities import insertScores
from functionalities import removePosition
from functionalities import removeStartStop
from functionalities import replaceScore
from functionalities import removeLowerThan
from functionalities import removeGreaterThan
from functionalities import removeEqualTo

def testInit(contestantsList):
    contestantsList.append({'P1': 0, 'P2': 10, 'P3': 5})
    contestantsList.append({'P1': 2, 'P2': 7, 'P3': 4})
    contestantsList.append({'P1': 2, 'P2': 8, 'P3': 1})
    contestantsList.append({'P1': 2, 'P2': 5, 'P3': 4})
    contestantsList.append({'P1': 9, 'P2': 9, 'P3': 9})
    contestantsList.append({'P1': 4, 'P2': 0, 'P3': 10})
    contestantsList.append({'P1': 2, 'P2': 3, 'P3': 4})
    contestantsList.append({'P1': 5, 'P2': 5, 'P3': 0})
    contestantsList.append({'P1': 3, 'P2': 2, 'P3': 10})
    contestantsList.append({'P1': 10, 'P2': 10, 'P3': 10})


def testInsertScores():
    cList = []
    testInit(cList)
    assert insertScores(cList, 3, 2, 3, 2) == True
    assert insertScores(cList, 30, 20,  30, 5) == False
    assert insertScores(cList, 3, 2, 3, 0) == True


def testRemovePosition():
    cList = []
    testInit(cList)
    assert removePosition(cList, 2) == True
    assert removePosition(cList, 3) == True
    assert removePosition(cList, 10) == False
    assert removePosition(cList, 0) == True


def testRemoveStartStop():
    cList = []
    testInit(cList)
    assert removeStartStop(cList, -1, 5) == False
    assert removeStartStop(cList, 2, 5) == True
    assert removeStartStop(cList, 0, 3) == True
    assert removeStartStop(cList, 5, 10) == False
    assert removeStartStop(cList, 5, 9) == True


def testReplaceScore():
    cList = []
    testInit(cList)
    assert replaceScore(cList, 4, "P2", 3) == True
    assert replaceScore(cList, -1,"P1", 4) == False
    assert replaceScore(cList, 1, "p1", 5) == False
    assert replaceScore(cList, 1, "P3", 12) == False
    assert replaceScore(cList, 9, "P2", 10) == True
    assert replaceScore(cList, 0, "P1", 5) == True

def testRemoveEqualTo():
    cList = []
    testInit(cList)
    assert removeEqualTo(cList, 10) == True
    assert removeEqualTo(cList, 10) == False

def testRemoveLowerThan():
    cList = []
    testInit(cList)
    assert removeLowerThan(cList, 10) == True
    assert removeLowerThan(cList, 10) == True #The sets are 0 < 10

def testRemoveGreaterThen():
    cList = []
    testInit(cList)
    assert removeGreaterThan(cList, 10) == True
    assert removeGreaterThan(cList, 10) == False
    assert removeGreaterThan(cList, 15) == False

def runAllTests():
    testInsertScores()
    testRemovePosition()
    testRemoveStartStop()
    testReplaceScore()
    testRemoveEqualTo()
    testRemoveLowerThan()
    testRemoveGreaterThen()

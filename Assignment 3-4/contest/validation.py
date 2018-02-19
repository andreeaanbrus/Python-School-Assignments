def validateScore(score):
    '''
    Build the string of errors
    input: score -> dictionary, containing score of the contestant
    :return:-
    '''
    errors = ""
    if score["P1"] < 0 and score["P1"] > 10:
        errors += "Invalid input. First problem is not an integer between 0 and 10"
    if score["P2"] < 0 and score["P2"] > 10:
        errors += "Invalid input. Second problem is not an integer between 0 and 10"
    if score["P3"] < 0 and score["P3"] > 10:
        errors += "Invalid input. Third problem is not an integer between 0 and 10"
    if len(errors):
       raise ValueError(errors)
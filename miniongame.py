def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    vowelPoints = 0
    consonantPoints = 0
    stringlength = len(string)
    currentPoints = 0 
    for i in range (stringlength):
        if string[i] in vowels:
            currentPoints = stringlength-i
            vowelPoints = vowelPoints+currentPoints
        if string[i] not in vowels:
            currentPoints = stringlength-i
            consonantPoints = consonantPoints+currentPoints
    if vowelPoints==consonantPoints:
        print "Draw"
    if vowelPoints>consonantPoints:
        print "Kevin", vowelPoints
    else:
        print "Stuart", consonantPoints

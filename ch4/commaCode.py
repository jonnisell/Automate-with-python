spam = ['apples', 'bananas', 'tofu', 'cats']

def listToString( spam ):
    spamstring = ''
    for i in range(len(spam)-1):
        spamstring += str(spam[i] + ', ')
    spamstring += 'and ' + str(spam[-1])
    print(spamstring)

listToString(spam)
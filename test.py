import re

# Test data1
# Notes: 
# Final Word: "minus"

#known1 = ["0", "0", "0", "u", "0"]
known1 = ["0", "i", "n", "u", "s"]

used1 = ["c", "l", "o", "d", "p", "t", "s"]

possibleChars1 = [["i", "n", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

# Test data2
# Notes: 
# Final Word: "vibes"
# 1) Allows "bibes" to be a possible word even though there is only one 'b'
# and its already in the right place
known2 = ["0", "i", "b", "e", "0"]

used2 = ["c", "l", "o", "u", "d", "t", "a", "r", "p", "n", "k", "y", "f", "r"]

possibleChars2 = [["s", "0", "0", "0", "e"]]

# Test data3
# Notes: 
# Final Word: "liked"
known3 = ["0", "i", "0", "0", "d"]

used3 = ["c", "o", "u", "s", "t", "a", "r", "p", "n", "y"]

possibleChars3 = [["0", "l", "0", "0", "0"], ["0", "0", "0", "0", "e"], ["0", "0", "0", "k", "0"]]

# Test data4
# Notes: 
# Final Word: "rhino"
known4 = ["0", "0", "i", "0", "0"]

used4 = ["c", "l", "u", "d", "s", "t", "a", "p", "k", "y"]

possibleChars4 = [["0", "0", "o", "0", "0"], ["0", "0", "0", "r", "0"], ["0", "i", "n", "0", "0"], ["0", "r", "0", "o", "n"]]

#==================================================




# Definitions

def createUsed(used):
    allUsedChars = ""
    for c in used:
        allUsedChars = allUsedChars + "|" + c
    
    return allUsedChars

# ((charSpecExcluded)(allCharExcluded)[a-z])
# ADD PRIOTIES 
def createChar1SpecExcluded(pos):
    char1SpecExcluded = ""
    
    for list in pos:
        if (list[0] != "0"):
            char1SpecExcluded = char1SpecExcluded + "|" + list[0]

    return char1SpecExcluded

def createChar1(known, posChars):
    char1 = ""

    if (known[0] != "0"):
        char1 = char1 + "(" + known[0] + ")"
    else:
        char1Excluded = createChar1SpecExcluded(posChars)
        char1 = "(" + "(?!0" + char1Excluded + ")" + "(?!0" + allUsedChars + ")" "[a-z])"
    
    return char1



def createChar2SpecExcluded(pos):
    char2SpecExcluded = ""

    for list in pos:
        if (list[1] != "0"):
            char2SpecExcluded = char2SpecExcluded + "|" + list[1]
    
    return char2SpecExcluded

def createChar2(known, posChars):
    char2 = ""

    if (known[1] != "0"):
        char2 = char2 + "(" + known[1] + ")"
    else:
        char2Excluded = createChar2SpecExcluded(posChars)
        char2 = "(" + "(?!0" + char2Excluded + ")" + "(?!0" + allUsedChars + ")" "[a-z])"
    
    return char2


def createChar3SpecExcluded(pos):
    char3SpecExcluded = ""

    for list in pos:
        if (list[2] != "0"):
            char3SpecExcluded = char3SpecExcluded + "|" + list[2]
    
    return char3SpecExcluded            

def createChar3(known, posChars):
    char3 = ""

    if (known[2] != "0"):
        char3 = char3 + "(" + known[2] + ")"
    else:
        char3Excluded = createChar3SpecExcluded(posChars)
        char3 = "(" + "(?!0" + char3Excluded + ")" + "(?!0" + allUsedChars + ")" "[a-z])"
    
    return char3

def createChar4SpecExcluded(pos):
    char4SpecExcluded = ""

    for list in pos:
        if (list[3] != "0"):
            char4SpecExcluded = char4SpecExcluded + "|" + list[3]
    
    return char4SpecExcluded 

def createChar4(known, posChars):
    char4 = ""

    if (known[3] != "0"):
        char4 = char4 + "(" + known[3] + ")"
    else:
        char4Excluded = createChar4SpecExcluded(posChars)
        char4 = "(" + "(?!0" + char4Excluded + ")" + "(?!0" + allUsedChars + ")" "[a-z])"
    
    return char4

def createChar5SpecExcluded(pos):
    char5SpecExcluded = ""

    for list in pos:
        if (list[4] != "0"):
            char5SpecExcluded = char5SpecExcluded + "|" + list[4]
    
    return char5SpecExcluded

def createChar5(known, posChars):
    char5 = ""

    if (known[4] != "0"):
        char5 = char5 + "(" + known[4] + ")"
    else:
        char5Excluded = createChar5SpecExcluded(posChars)
        char5 = "(" + "(?!0" + char5Excluded + ")" + "(?!0" + allUsedChars + ")" "[a-z])"
    
    return char5

def validateKnownInput(input):
    validInputRegex = "^((0|[a-z]),(0|[a-z]),(0|[a-z]),(0|[a-z]),(0|[a-z]))$"

    if (input == "/q"):
        return 0
    elif (input == "0"):
        return 2
    elif (len(input) != 9):
        print("Invalid length.\n")
        return -1
    elif (re.fullmatch(validInputRegex, input)):
        return 1
    else:
        print("Invalid form of input.\n")
        return -1
    
def validateUsedInput(input):
    validInputRegex = "^((0|[a-z])(,([a-z]))*)$"

    if (input == "/q"):
        return 0
    elif (re.fullmatch(validInputRegex, input)):
        return 1
    else:
        print("Invalid form of input.\n")
        return -1
    
def validatePossibleCharsInput(input):
    validInputRegex = "^((0|[a-z]),(0|[a-z]),(0|[a-z]),(0|[a-z]),(0|[a-z]))$"

    if (input == "/q"):
        return 0
    elif (input == "0"):
        return 2
    elif (len(input) != 9):
        print("Invalid length.\n")
        return -1
    elif (re.fullmatch(validInputRegex, input)):
        return 1
    else:
        print("Invalid form of input.\n")
        return -1

    

#==================================================






# Main Function

# Read word list from file (one word per line)
with open("combined_wordlist.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]

done = False
# Contionsly run till true
while (not done):
    validKnownInput = -1
    # Continously run till valid knownInput/quit
    while(validKnownInput == -1):
        print("Enter \"/q\" to quit.")
        knownInput = input("Enter known characters: ")
        
        validKnownInput = validateKnownInput(knownInput)
    # end while

    # Check if user wants to quit
    if (validKnownInput == 0): 
        break
    elif (validKnownInput == 2):
        known = ["0", "0", "0", "0", "0"]
    else:
        known = knownInput.split(',')
    
    print(known)
    
    validUsedInput = -1
    while (validUsedInput == -1):
        usedInput = input("Enter used characters: ")

        validUsedInput = validateUsedInput(usedInput)
    # end while

    # Check if user wants to quit
    if (validUsedInput == 0):
        break

    used = usedInput.split(",")
    print(used)

    possibleCharsList = []
    validPosibleCharsInput = -1
    while (validPosibleCharsInput != 0):
        possibleCharsInput = input("Enter possible characters: ")

        validPosibleCharsInput = validateKnownInput(possibleCharsInput)

        if (validPosibleCharsInput == 2):
            possibleCharsList.append(["0", "0", "0", "0", "0"])
            break
        elif (validPosibleCharsInput == 1):
            possibleCharsList.append(possibleCharsInput.split(","))
    # end while
    print("Out of validation.\n")
    print(possibleCharsList)
    print()

    if (validPosibleCharsInput == 0):
        break

    existingLetters = []
    for list in possibleCharsList:
        for c in list:
            if (c != "0" and (c not in existingLetters)):
                existingLetters.append(c)
    
    print(existingLetters)

    done = True
# end while




# Compile regex pattern
allUsedChars = createUsed(used)                                #TO CHANGE USED
char1 = createChar1(known, possibleCharsList)
char2 = createChar2(known, possibleCharsList)
char3 = createChar3(known, possibleCharsList)
char4 = createChar4(known, possibleCharsList)
char5 = createChar5(known, possibleCharsList)

pattern = re.compile("^" + char1 + char2 + char3 + char4 + char5 + "$")

# Filter words that match
#matches = [w for w in words if pattern.match(w)]

matches = []
for w in words:
    addWord = True
    for c in existingLetters:
        if (c not in w):
            addWord = False
            break
    if (pattern.match(w) and addWord):
        matches.append(w)


print(f"Found {len(matches)} matches:")
print(matches[:20])  # show first 20

#==================================================





# Test outputs

#print("allUsedChars: " + allUsedChars)

"""
print("char1: " + char1)
print("char2: " + char2)
print("char3: " + char3)
print("char4: " + char4)
print("char5: " + char5)
"""
#char2Excluded = createChar2SpecExcluded(possibleChars)
#print(char2Excluded)

#==================================================





# Notes:
"""
Regex tests:

Key
WORD - REGEX

tests - "^t[a-rt-z]s[a-z][a-su-z]$"
noses - "^([a-rt-z])([a-df-z])([a-mp-z])([a-mp-z])(s)$"

"""
#==================================================

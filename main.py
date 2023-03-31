#WRITE YOUR CODE IN THIS FILE
def countA(word):
    numA = 0
    for i in range(0,len(word)):   
        if word[i] == "a":
            numA = numA + 1
    return numA

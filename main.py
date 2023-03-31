#WRITE YOUR CODE IN THIS FILE
def countA(word):
    for i in range(0,len(word)):
        numA = 0    
        if word[i] == "a":
            numA = numA + 1
        return numA



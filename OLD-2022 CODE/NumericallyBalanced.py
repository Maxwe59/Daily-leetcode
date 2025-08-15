'''
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!


'''



#notes: identify n-next biggest prime balanced, after the number gets 1+ bigger than prime Balanced num, it changes +1 digit
#notes: if the lowest range value is 3 digits long it can only have numbers 1-3

#22,122,212,221,333,1333,3133,3313,3331,4444


def ListToInt(l=list): #45321
    string = ""
    Int = 0
    for i in l:
        string = string + (str(i)*(int(str(i))))
    Int = int(string)
    return Int



def Identify(n=int):
    DictPermutate = {3:[1,2],4:[3,1],5:[[2,3],[1,4]],6:[[2,4],[1,5],[1,2,3]],7:[[3,4],[1,2,4],[1,6],[5,2]],8:[[3,5],[1,3,4],[1,7],[1,2,5],[2,6]],9:[[1,2,3,4],[2,3,4],[1,2,6],[4,5],[1,8],[2,7],[3,6]]} #all possible permutations of nums 1-9 {"9":"5,4", "8":"5,3","7":"4,3","6":"4,2","5":"3,2","4":"3,1","3":"2,1"}
    PrimeBalancedInt = [1,22,333,4444,55555,666666,7777777,88888888,999999999] #["","1","22","333","4444","55555","666666","7777777","88888888","999999999"]
    HighestPoint = 0
    nStr = str(n)
    count = 0
    FinalNum = 0
    FinalNumList = []

    if(n==0):
        return 1
    
    if(n>=1 and n<=21):
        return 22
    
    if(22<=n and n<101):
        nStr = str(100)


    count2 = 0

    while(count2!=len(DictPermutate[len(nStr)])): #goes through specific dict based on length of num
        if(len(nStr)==3 or len(nStr)==4):

            FinalNum = ListToInt(DictPermutate[len(nStr)])
            FinalNumList.append(FinalNum)

        else:
            FinalNum = ListToInt(DictPermutate[len(nStr)][count2])
            FinalNumList.append(FinalNum)

        count2 = count2 + 1

    #questionable if needed
    if(len(str(n)) < len(str(min(FinalNumList)))): #checks if length of n is smaller than the smallest minimum number in final num list
        FinalNum = min(FinalNumList) #makes finalnum equal to smallest possible number in final num list
    
    print(FinalNumList)

    for num in FinalNumList:
        for perm in num:
            
            FinalNumList.append() 
        


Identify(34322)

"""

    while(count+1!=9):

        if(n==PrimeBalancedInt[count]):
            HighestPoint = PrimeBalancedInt[count+1]
            break

        if(n<PrimeBalancedInt[count]):
            HighestPoint = PrimeBalancedInt[count]
            break

        count = count + 1

    LowPoint = int((10**len(str(HighestPoint)))/10)
    count = 0

    if(LowPoint<n): # if 122 and 100, 100 wins by default, this fixes
        LowPoint = n + 1


    print("range: " + str(LowPoint) +", " + str(HighestPoint))
"""

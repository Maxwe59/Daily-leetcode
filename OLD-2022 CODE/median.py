'''
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!


'''



def algorithm(list1, list2):
    val = list1 + list2
    returned_val = []
    repeat = len(val)

    for i in range(repeat): 
        biggestnum = max(val)
        returned_val.insert(0,biggestnum)
        val.remove(biggestnum) #index
    
    returned_median = None

    if((repeat)/2 == int((repeat)/2)):
        returned_median = ((returned_val[int((repeat)/2)]) + (returned_val[int(((repeat)/2)-1)]))/2
    
    if((repeat)/2 != int((repeat)/2)):
        returned_median = returned_val[int((repeat)/2)]

        
    
    return returned_median




testcase1 = [3,5,6]
testcase2 = [1]
print(algorithm(testcase1,testcase2))
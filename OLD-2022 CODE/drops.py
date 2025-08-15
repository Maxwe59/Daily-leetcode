'''
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!


'''


#takes an input of a list of numbers, each number equates to the vector of blocks, for example 1,0,1 is 1 block then 0 block then 1 block.
#program figures out where rain water would fit in. for example [5,1,3] output = 2
def algorithm(vector):

    filler = 0 #number that is returned based on how many blocks would be filled in (NUMBER OF DROPS)
    count = 0 #(INDEX)
    filler_temp = 0 #used to detect [3,1,0] instance where there is no fills. (NUMBER OF DROPS)
    starting_num = count #detects highest number in list so far. (INDEX)

    while(count!=len(vector)-1):            

        if(vector[starting_num]>=vector[count+1]): #detects if starting num is bigger than next number
            filler_temp += (vector[starting_num]-vector[count+1])

        if(vector[starting_num]<=vector[count+1]): #checks there is a new bigger number
            starting_num = count+1
            filler += filler_temp
            filler_temp = 0

        count +=1


    count = len(vector) - 1 
    filler_temp = 0 
    starting_num = count 

    while(count!=0):            

        if(vector[starting_num]>=vector[count-1]): #detects if starting num is bigger than number before it
            filler_temp += (vector[starting_num]-vector[count-1])

        if(vector[starting_num]<vector[count-1]): #checks there is a new bigger number
            starting_num = count-1
            filler += filler_temp
            filler_temp = 0

        count -=1

    return filler       


testcase = [7,4,7]
print(algorithm(testcase))
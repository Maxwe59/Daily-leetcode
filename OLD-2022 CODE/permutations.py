'''
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!
!!!OLD CODE FROM 2023!!!


'''



import numpy

#account for duplicate num
class Solution(object):

    def factorial(self,nums=int): 

        count = nums-1
        while(count!=1):

            nums = nums * (count)
            count = count - 1
        
        return nums
    
    def LenList(self,nums):
        count = 0
        for i in nums:
            count += 1
        
        return count
    
    def ListToNum(self,nums):
        Fnum = ""
        for num in nums:
            Fnum += str(num)
        return int(Fnum)
  


        
    def permute(self,nums):
        intN = self.ListToNum(nums)

        
        return 





list1 = [4,3,5,11] #change to 43511 = int, then to 11345, then to 11354, then to 11435, then to 11453, ect 
print(Solution().ListToNum(list1))
#print(Solution().permute(list1))




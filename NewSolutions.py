from collections import defaultdict
import random as rand
from random import randint



class Solutions:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        hash_map = {}
        for string in strs:
            new = "".join(sorted(string))
            if not new in hash_map:
                hash_map[new] = [string]
            elif new in hash_map:
                hash_map[new].append(string)
                
        for key in hash_map:
            arr.append(hash_map[key])
            
        return arr

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            elif total < target:
                left += 1

    def maxNumberOfBalloons(self, text: str) -> int:
        map = {"b": 0, "a": 0, "l": 0, "o": 0, "n":0}
        for c in text:
            if c == "b":
                map["b"] += 1
            elif c == "a":
                map["a"] += 1
            elif c == "l":
                map["l"] += 1
            elif c == "o":
                map["o"] += 1
            elif c == "n":
               map["n"] += 1
        
        print(map)
        min_single: int = map["b"]
        min_double: int = map["l"]
        for key in map:
            if key == "o" or key== "l":
                min_double = min_double if map[key] > min_double else map[key]
            else:
                min_single = min_single if map[key] > min_single else map[key]
        
        if min_double<= 1 or min_single==0:
            return 0
            
        if min_double%2 !=0:
            min_double -= 1
            
        if min_double/2 > min_single:
            return min_single
            
        else: 
            return int(min_double/2)
            
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if not num in nums_dict:
                nums_dict[num] = True
            
            else:
                return True
        
        return False


    def isAnagram(self, s: str, t: str) -> bool:
        t_dict = {}
        s_dict = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if not s[i] in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            if not t[i] in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
                

 
        for key in s_dict:
            if not key in t_dict:
                return False
            if not s_dict[key] == t_dict[key]:
                return False
        
        return True
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r_set = set()

        while len(nums) > 1: #fix later
            current = nums[0]
            left = 1
            right = len(nums) -1
            while left < right: #fix later
                total = nums[right] + nums[left] + current

                if total == 0:
                    arr = (current, nums[left], nums[right])
                    r_set.add(arr)
                    right -= 1
                    left += 1
                
                elif total > 0:
                    right -= 1
                elif total <0:
                    left += 1
                
            nums.pop(0)

        result = []
        for item in r_set:
            result.append(list(item))

        return result

    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        res = arr2[0]
        res_arr = []
        for i in range(1, len(arr2)):
            res = res ^ arr2[i]

        for item in arr1:
            res_arr.append(item & res)
        
        
        
        final = res_arr[0]
        for i in range(1, len(res_arr)):
            final = (final ^ res_arr[i])
            
        return final
    

    def trap(self, height: List[int]) -> int:
        output = 0

        high_index = 0
        current_dip =0
        for index,block in enumerate(height):
            if block >= height[high_index]:
                output += current_dip
                current_dip = 0
                high_index = index
            
            elif block < height[high_index]:
                current_dip += (height[high_index] - block)

        high_index = len(height) - 1
        current_dip = 0
        for index in reversed(range(len(height))):
            if height[index] > height[high_index]:
                output += current_dip
                current_dip = 0
                high_index = index

            elif height[index] < height[high_index]:
                current_dip += (height[high_index]- height[index])
                

        return output

    def isValid(self, s: str) -> bool:
        mapping = {"{":"}", "[":"]", "(":")"}
        stack = []
        if len(s)%2 != 0:
            return False
            
        for char in s:  
            if char in mapping.keys(): #if there is a left mapping
                stack.append(char)
            
            elif char in mapping.values(): #if there is a right mapping
                if len(stack) == 0:
                    return False
                top = stack[len(stack) - 1]
                if mapping[top] != char:
                    return False
                elif mapping[top] == char:
                    stack.pop(len(stack) - 1)

        if len(stack) != 0:
            return False

        return True

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operators: #integer
                stack.append(token)
            
            elif token in operators:
                num1,num2 = stack.pop(), stack.pop()
                calc = int(eval(f"{num2}{token}{num1}"))
                stack.append(calc)

        return int(stack[0])


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)

        result = []

        total = nums[0]
        for i in range(1, len(nums)):
            left_arr[i] *= total
            total *= nums[i]   
            
        total = nums[-1]
        for i in reversed(range(0, len(nums)-1)):
            right_arr[i] *= total
            total *= nums[i]
        
        
        for i in range(len(nums)):
            result.append(left_arr[i] * right_arr[i])
            
        return result


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        predicted_arr = None
        while left <= right:
            mid = (left + right)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                predicted_arr = mid
                break
            
            elif matrix[mid][-1] < target:
                left = mid + 1
            
            elif matrix[mid][0] > target:
                right = mid - 1

        if predicted_arr == None:
            return False

        left = 0
        right = len(matrix[predicted_arr]) - 1
        while left <= right:
            mid = (left + right) //2

            if matrix[predicted_arr][mid] == target:
                return True

            elif matrix[predicted_arr][mid] > target:
                right = mid - 1
            elif matrix[predicted_arr][mid] < target:
                left = mid + 1
        
        return False
    
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        arr = [0] * n
        arr[0], arr[1] =  1,1

        for n in range(2, len(arr)):
            arr[n] = arr[n-1] + arr[n-2]

        return arr[n-1] + arr[n]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        res_arr = []    
        def backtrack(arr):
            if len(arr) == 0 or arr in res:
                return
            
            res.add(arr[:])
            for i in range(len(arr)):
                new_arr = arr[:i] + arr[i+1:]
                backtrack(new_arr)
        
        backtrack(tuple(nums[:]))
        
        for item in res:
            res_arr.append(list(item))
        res_arr.append([])
        return res_arr
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[left]:
                left = i
            
            else:
                res = max(res, (prices[i] - prices[left]))
        
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hash_ = {}
        if len(s) == 1 or len(s) == 0:
            return len(s)

        for i in range(len(s)):
            if not s[i] in hash_:
                hash_[s[i]] = i
                res = max(res, len(hash_))
            
            else:
                res = max(res, len(hash_))
                delete_to = hash_[s[i]]
                hash_[s[i]] = i
                new_hash = {}
                for item in hash_:
                    if not hash_[item] <= delete_to:
                        new_hash[item] = hash_[item]
                hash_ = new_hash
        return res

test = Solutions()

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


test = Solutions()

from collections import defaultdict
import random as rand
from random import randint

class Solutions:
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




test = Solutions()

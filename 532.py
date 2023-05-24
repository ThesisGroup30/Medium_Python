from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        count = 0

        for num in counter:
            if k > 0 and num + k in counter:
                count += 1
            elif k == 0 and counter[num] > 1:
                count += 1

        return count

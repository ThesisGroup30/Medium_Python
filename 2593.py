class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        score = 0

        def mark(index):
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < n - 1:
                marked[index + 1] = True

        while True:
            min_val = float('inf')
            min_index = -1

            for i in range(n):
                if not marked[i] and nums[i] < min_val:
                    min_val = nums[i]
                    min_index = i

            if min_index == -1:
                break

            score += min_val
            mark(min_index)

        return score

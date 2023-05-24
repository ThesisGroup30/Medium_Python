class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums.sort()
        mex = 0

        for num in nums:
            if num <= mex:
                mex += 1
            else:
                break

        return mex

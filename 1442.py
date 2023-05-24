class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            xor_sum = arr[i]
            for j in range(i+1, n):
                xor_sum ^= arr[j]
                if xor_sum == 0:
                    count += j - i
        return count






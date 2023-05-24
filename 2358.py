class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)  # Sort grades in non-increasing order
        groups = 0
        curr_sum = 0
        curr_count = 0

        for grade in grades:
            curr_sum += grade
            curr_count += 1

            if curr_sum > curr_count:
                groups += 1
                curr_sum = 0
                curr_count = 0

        return groups

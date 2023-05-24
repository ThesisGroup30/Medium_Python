class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        n = len(s1)
        s1_breaks_s2 = True
        s2_breaks_s1 = True
        for i in range(n):
            if s1_sorted[i] < s2_sorted[i]:
                s1_breaks_s2 = False
            if s2_sorted[i] < s1_sorted[i]:
                s2_breaks_s1 = False
            if not s1_breaks_s2 and not s2_breaks_s1:
                return False
        return True

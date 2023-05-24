from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        frequency = Counter(s)

        # Sort the characters based on frequency in descending order
        sorted_chars = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)

        # Construct the sorted string
        sorted_str = ""
        for char in sorted_chars:
            sorted_str += char * frequency[char]

        return sorted_str

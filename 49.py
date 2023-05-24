from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        # Iterate through each string in strs
        for word in strs:
            # Sort the characters of the word to get a unique key for anagrams
            sorted_word = ''.join(sorted(word))
            # Append the word to the corresponding anagram group
            anagram_groups[sorted_word].append(word)

        # Convert the dictionary values to a list
        result = list(anagram_groups.values())

        return result

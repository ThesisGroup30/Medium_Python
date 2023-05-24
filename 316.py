class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}  # Store the last occurrence index of each character
        seen = set()  # Store the characters already seen in the stack
        stack = []  # Store the characters in the final result

        # Find the last occurrence index of each character
        for i, char in enumerate(s):
            last_occurrence[char] = i

        for i, char in enumerate(s):
            # If the character is already in the stack, skip it
            if char in seen:
                continue

            # Remove characters from the stack if:
            # 1. The current character is smaller than the top of the stack
            # 2. The top of the stack has more occurrences later in the string
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                seen.remove(removed_char)

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

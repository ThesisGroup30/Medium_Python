class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}  # Store the last occurrence index of each character

        # Iterate through the string to find the last occurrence index of each character
        for i, char in enumerate(s):
            last_occurrence[char] = i

        partitions = []  # Store the sizes of the partitions
        start = 0  # Initialize the start index of the current partition
        end = 0  # Initialize the end index of the current partition

        # Iterate through the string again to find the end index of each partition
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Update the end index if necessary

            # If the current index reaches the end index of the current partition
            if i == end:
                partitions.append(end - start + 1)  # Add the size of the partition to the list
                start = i + 1  # Update the start index for the next partition

        return partitions

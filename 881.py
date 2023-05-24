class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sort the people array in ascending order

        left, right = 0, len(people) - 1  # Initialize two pointers at the start and end of the array
        boats = 0  # Initialize the number of boats

        while left <= right:
            if people[left] + people[right] <= limit:
                # If the sum of the weights of the lightest and heaviest person is less than or equal to the limit,
                # they can be on the same boat
                left += 1  # Move the left pointer to the right (lighter person embarked)
                right -= 1  # Move the right pointer to the left (heavier person embarked)
            else:
                # If the sum of the weights exceeds the limit, the heaviest person must be on a separate boat
                right -= 1  # Move the right pointer to the left (heavier person embarked)

            boats += 1  # Increment the number of boats

        return boats

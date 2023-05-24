class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, time) to represent each car
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        
        # Sort the cars based on their positions in descending order
        cars.sort(key=lambda x: x[0], reverse=True)
        
        fleets = 0
        max_time = 0
        
        # Iterate through the cars and count the fleets
        for car in cars:
            if car[1] > max_time:
                # A new fleet is formed
                fleets += 1
                max_time = car[1]
        
        return fleets

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def evaluate(left: List[int], right: List[int], operator: str) -> List[int]:
            results = []
            for l in left:
                for r in right:
                    if operator == '+':
                        results.append(l + r)
                    elif operator == '-':
                        results.append(l - r)
                    elif operator == '*':
                        results.append(l * r)
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                results.extend(evaluate(left, right, expression[i]))

        return results

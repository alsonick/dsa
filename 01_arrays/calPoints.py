from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        output = 0
        for operation in operations:
            match operation:
                case "C":
                    scores.pop()
                case "D":
                    previous_score = scores[len(scores) - 1]
                    scores.append(int(previous_score) * 2)
                case "+":
                    score_one = scores[len(scores) - 1]
                    score_two = scores[len(scores) - 2]
                    computation = int(score_one) + int(score_two)
                    scores.append(computation)
                case _:
                    scores.append(int(operation))
        for score in scores:
            output += score
        
        return output

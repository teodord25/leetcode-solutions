from typing import List


class Solution:
    """
    Pretty simple.
    Working solution: 3 minutes
    NOTE: I don't think theres a solution thats much faster? 
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)

        count = 0
        for w in words:
            legal = False
            for c in w:
                if c not in a:
                    legal = False
                    break
                else:
                    legal = True

            if legal:
                count += 1
                legal = False

        return count

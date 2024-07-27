from typing import List


class Solution:
    """
    Took me 30 minutes to come up with a decent naive idea, took me 2 and a
    half hours to actually implement the recursive algorithm and it was too
    slow... Took me another hour and a hint to realize that my first idea to
    use sets somehow was ok and that's the final solution. Still very ass but
    it passes...

    NOTE: need more practice on recursion it still confuses me
    NOTE: dont jump to recursion unless obvious (trees n stuff)
    """

    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums = set([0 for _ in mat[0]])

        for i, row in enumerate(mat):
            new = set()
            for j, val in enumerate(row):
                for s in sums:
                    new_val = s + val
                    if i == len(mat) - 1 and new_val == target:
                        return 0

                    new.add(new_val)
            sums = new

        return min([abs(s - target) for s in sums])

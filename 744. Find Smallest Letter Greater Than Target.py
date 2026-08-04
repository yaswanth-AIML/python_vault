class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for a in letters:
            if a>target:
                return a
        return letters[0]

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(2):
            num+=t
        return num
        
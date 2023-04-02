class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        output = []
        left, right = 0, len(skill) - 1
        skill.sort()
        target = skill[0] + skill[-1]
        while left <= right:  
            if skill[left] + skill[right] == target:
                chemistry = skill[left] * skill[right]
                output.append(chemistry)
            else:
                return -1
            left += 1
            right -= 1
        return sum(output)
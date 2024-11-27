class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
        return not stack
        
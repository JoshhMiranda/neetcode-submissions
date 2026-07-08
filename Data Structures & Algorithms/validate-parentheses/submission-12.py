class Solution:
    def isValid(self, s: str) -> bool:
        # mapping = {
        #     ")": "(",
        #     "}": "{",
        #     "]":"["
        # }
        # stack = []
        
        # for char in s:
        #     if char in mapping.values():
        #         stack.append(char)
        #     elif char in mapping:
        #         if not stack or stack[-1] != mapping[char]:
        #             return False
        #         stack.pop()

        # return len(stack) == 0
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}","")
            s = s.replace("[]", "")

        return s == ""





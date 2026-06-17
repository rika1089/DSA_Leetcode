class Solution: 
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        opened = 0
        for ch in s :
            if ch == '(' :
                if stack :
                    ans+=ch
                stack.append(ch)
            else :
                stack.pop()
                if stack :
                   ans += ch

        return ans

        return ans


        
from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        in_stack = set()
        
        # freq = {ch: 0 for ch in s}
        

        # for ch in s:
        #     freq[ch] += 1

        for ch in s :
            freq[ch] -= 1
            if ch in in_stack :
                continue 
            
            while stack and stack[-1] > ch and freq[stack[-1]] > 0 :
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(ch)
            in_stack.add(ch)

        return "".join(stack)
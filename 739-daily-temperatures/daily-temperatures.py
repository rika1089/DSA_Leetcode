class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 0 :
            return []
        if n == 1 :
            return [0]
        
        #stack = [temperatures[0]]
        stack = list()
        res = [0] * n

        for i in range(n) :
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            else :
                stack.append(i)
        
        return res


        
        
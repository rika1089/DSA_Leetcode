class Solution:
    def isValid(self, s: str) -> bool:
        # i = 0
        # stack = []

        # for i in range(len(s)) :
        #     if s[i] =='(' or s[i] =='{' or s[i] == '[' :
        #         stack.append(s[i])
            
        #     else :
        #         if not stack :
        #             return False
                
        #         top  = stack.pop()
        #         if s[i] == ')' and top != '(' :
        #             return False
        #         if s[i] == '}' and top != '{' :
        #             return False
        #         if s[i] == ']' and top != '[' :
        #             return False
        # return len(stack) == 0

        Map = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        stack = []
        if s == "" :
            return True
        if len(s) % 2 == 1 :
            return False
        for i in range(len(s)) :
            if s[i] in Map :
                    if not stack or  Map[s[i]] != stack.pop() :
                        return False
            elif s[i] in Map.values():
                stack.append(s[i])
            else :
                return False
        
        return len(stack) == 0


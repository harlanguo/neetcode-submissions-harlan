class Solution:
    def decodeString(self, s: str) -> str:
        curStr = ''
        curNum = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                curNum = curNum * 10 + int(ch)
            
            elif ch == '[':
                stack.append((curStr, curNum))
                curStr = ''
                curNum = 0
            
            elif ch == ']':
                prevStr, num = stack.pop()
                curStr = prevStr + num * curStr
            
            else:
                curStr += ch
        
        return curStr
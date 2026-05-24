class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        lineLen = 0

        for word in words:
            if lineLen + len(word) + len(line) > maxWidth:
                spaces = maxWidth - lineLen

                if len(line) == 1:
                    res.append(line[0] + " " * spaces)
                else:
                    curLine = ''
                    gaps = len(line) - 1
                    evenSpace = spaces // gaps
                    extraSpace = spaces % gaps

                    for i in range(len(line) - 1):
                        curLine += line[i]
                        curLine += ' ' * (evenSpace + (1 if i < extraSpace else 0))
                    curLine += line[-1]
                    res.append(curLine)
                
                line = []
                lineLen = 0
            
            line.append(word)
            lineLen += len(word)

        lastLine = ' '.join(line)
        lastLine += ' ' * (maxWidth - len(lastLine))
        res.append(lastLine)

        return res
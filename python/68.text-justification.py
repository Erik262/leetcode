#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
from typing import List
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        ch_count = 0

        for word in words:
            if ch_count + len(word) + len(line) <= maxWidth:
                line.append(word)
                ch_count += len(word)
            else:
                total_spaces = maxWidth - ch_count
                gaps = len(line) - 1

                if gaps == 0:
                    result.append(line[0] + " " * total_spaces)
                else:
                    base = total_spaces // gaps
                    extra = total_spaces % gaps

                    s = ""
                    for i in range(len(line)):
                        s += line[i]
                        if i < gaps:
                            s += " " * (base + (1 if i < extra else 0))

                    result.append(s)

                line = [word]
                ch_count = len(word)

        s = " ".join(line)
        s += " " * (maxWidth - len(s))
        result.append(s)

        return result 
# @lc code=end
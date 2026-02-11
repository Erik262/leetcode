#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
from typing import List
# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        seen_twice = set()

        for i in range(len(s)):
            dna_seq = s[i:i+10]

            if dna_seq in seen:
                seen_twice.add(dna_seq)
            else:
                seen.add(dna_seq)

        return list(seen_twice)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(s))


# @lc code=end


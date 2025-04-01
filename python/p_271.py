class Solution:

    def encode(self, strs: list[str]) -> str:
        l = ""
        for w in strs:
            w = w + ";"
            l += w

        return l

    def decode(self, s: str) -> list[str]:
        l = []
        w = ""
        for c in s:
            if c == ';':
                l.append(w)
                w = ""
                continue
            w += c

        return l

strs = ["neet","code","love","you"]
enc = Solution().encode(strs)
print(enc)
print(Solution().decode(enc)) 
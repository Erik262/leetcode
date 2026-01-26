#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import hashlib

class Codec:
    def __init__(self) -> None:
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_key = 'https://tin.e/' + hashlib.md5(longUrl.encode()).hexdigest()
        self.urls[hash_key] = longUrl
        return hash_key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
    

tiny = Codec()

encoded = tiny.encode("Erik")
print(encoded)

decoded = tiny.decode(encoded)
print(decoded)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end


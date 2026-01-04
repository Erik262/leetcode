#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
from typing import List
# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()

        for mail in emails:
            mail = mail.split('@')
            l_mail = mail[0].replace('.', '').split('+')[0]
            d_mail = mail[1]

            mails.add((l_mail, d_mail))

        return len(mails)
    
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] # 2

print(Solution().numUniqueEmails(emails))
        
# @lc code=end


--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes With at Least 5 Students
--

-- @lc code=start
# Write your MySQL query statement below
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(class) >= 5
-- @lc code=end


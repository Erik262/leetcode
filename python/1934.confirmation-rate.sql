--
-- @lc app=leetcode id=1934 lang=mysql
--
-- [1934] Confirmation Rate
--

-- @lc code=start
# Write your MySQL query statement below
SELECT s.user_id, ROUND(
    IFNULL(SUM(c.action = 'confirmed') / COUNT(c.action), 0), 2)
     AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id
-- @lc code=end


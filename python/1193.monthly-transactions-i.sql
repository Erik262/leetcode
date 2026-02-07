--
-- @lc app=leetcode id=1193 lang=mysql
--
-- [1193] Monthly Transactions I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DATE_Format(trans_date, '%Y-%m') AS month, country,
COUNT(*) AS trans_count,
SUM(state = 'approved') AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(amount * (state = 'approved')) AS approved_total_amount
FROM transactions
GROUP BY DATE_Format(trans_date, '%Y-%m'), country;
-- @lc code=end


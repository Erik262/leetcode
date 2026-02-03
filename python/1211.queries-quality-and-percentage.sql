--
-- @lc app=leetcode id=1211 lang=mysql
--
-- [1211] Queries Quality and Percentage
--

-- @lc code=start
# Write your MySQL query statement below
SELECT q1.query_name, ROUND(AVG(q1.rating / q1.position), 2) AS quality,
ROUND((
    SELECT COUNT(*)
    From queries q2
    WHERE q2.rating < 3 AND q1.query_name = q2.query_name
) * 100 / COUNT(*), 2) AS poor_query_percentage
FROM queries q1
GROUP BY q1.query_name
-- @lc code=end


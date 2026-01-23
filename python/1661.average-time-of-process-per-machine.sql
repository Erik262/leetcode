--
-- @lc app=leetcode id=1661 lang=mysql
--
-- [1661] Average Time of Process per Machine
--

-- @lc code=start
# Write your MySQL query statement below
SELECT a1.machine_id, ROUND(AVG(ABS(a1.timestamp - a2.timestamp)),3) AS processing_time
FROM activity a1
JOIN activity a2
ON a1.machine_id = a2.machine_id
WHERE a1.process_id = a2.process_id AND a1.activity_type != a2.activity_type
GROUP BY a1.machine_id
-- @lc code=end


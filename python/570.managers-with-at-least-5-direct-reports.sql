--
-- @lc app=leetcode id=570 lang=mysql
--
-- [570] Managers with at Least 5 Direct Reports
--

-- @lc code=start
# Write your MySQL query statement below
SELECT e1.name 
FROM Employee e1
JOIN Employee e2
ON e1.id = e2.managerID 
GROUP BY e2.managerID
HAVING COUNT(*) >= 5;
-- @lc code=end


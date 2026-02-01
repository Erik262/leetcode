--
-- @lc app=leetcode id=1075 lang=mysql
--
-- [1075] Project Employees I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT p.project_id, ROUND(SUM(e.experience_years) / COUNT(*), 2) AS average_years
FROM project p
JOIN employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id
-- @lc code=end


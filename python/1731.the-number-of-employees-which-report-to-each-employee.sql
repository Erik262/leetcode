--
-- @lc app=leetcode id=1731 lang=mysql
--
-- [1731] The Number of Employees Which Report to Each Employee
--

-- @lc code=start
# Write your MySQL query statement below
SELECT e1.employee_id, e1.name, 
COUNT(e1.employee_id) AS reports_count, 
ROUND(AVG(e2.age)) AS average_age
FROM employees e1
JOIN employees e2
    ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
ORDER BY e1.employee_id
-- @lc code=end


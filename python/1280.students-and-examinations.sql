--
-- @lc app=leetcode id=1280 lang=mysql
--
-- [1280] Students and Examinations
--

-- @lc code=start
# Write your MySQL query statement below
SELECT stu.student_id, student_name, sub.subject_name, COUNT(ex.subject_name) as attended_exams
FROM students stu
JOIN subjects sub
LEFT JOIN examinations ex ON stu.student_id = ex.student_id AND sub.subject_name = ex.subject_name
GROUP BY stu.student_id, sub.subject_name
ORDER BY stu.student_id
-- @lc code=end


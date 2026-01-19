--
-- @lc app=leetcode id=1148 lang=mysql
--
-- [1148] Article Views I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT author_id as id FROM views
Where author_id = viewer_id
ORDER BY id ASC
-- @lc code=end


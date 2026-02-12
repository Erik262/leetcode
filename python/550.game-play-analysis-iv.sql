--
-- @lc app=leetcode id=550 lang=mysql
--
-- [550] Game Play Analysis IV
--

-- @lc code=start
# Write your MySQL query statement below
SELECT ROUND(
    COUNT(DISTINCT a1.player_id) /
    (
        SELECT COUNT(DISTINCT player_id)
        FROM activity
    ), 2
) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id

) first
JOIN activity a1
ON a1.player_id = first.player_id
AND DATEDIFF(a1.event_date, first.first_login) = 1

-- @lc code=end


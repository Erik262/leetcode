--
-- @lc app=leetcode id=1068 lang=mysql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT product_name, year, price FROM product p
JOIN sales s
ON p.product_id = s.product_id
-- @lc code=end


# Write your MySQL query statement below
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) as Rank
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) Init
ORDER BY Score DESC;

# Write your MySQL query statement below
select w1.Id from Weather w1, Weather w2 where w1.Temperature > w2.Temperature AND TO_DAYS(w1.DATE)-TO_DAYS(w2.DATE)=1;

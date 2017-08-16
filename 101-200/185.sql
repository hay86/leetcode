# Write your MySQL query statement below
select d1.Name as Department, e1.Name as Employee, e1.Salary as Salary
from Employee e1, Department d1
where e1.DepartmentId = d1.Id
and (select count(distinct(Salary)) from Employee e2 where e2.DepartmentId = e1.DepartmentId and e2.Salary > e1.Salary) < 3
ORDER by e1.DepartmentId, e1.Salary DESC;

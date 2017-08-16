# Write your MySQL query statement below
select d1.Name as Department, e1.Name as Employee, e1.Salary as Salary
from Employee e1, Department d1
where e1.DepartmentId = d1.Id
and e1.Salary = (
select Max(Salary) 
from Employee e2
where e2.DepartmentId = d1.Id
)

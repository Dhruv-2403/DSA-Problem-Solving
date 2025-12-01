# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary as Salary from Employee e join Department d on d.id=e.departmentId where (SELECT COUNT(DISTINCT(salary)) from employee e2 where e2.departmentId=e.departmentId and e2.salary>=e.salary ) <=3
order by salary desc

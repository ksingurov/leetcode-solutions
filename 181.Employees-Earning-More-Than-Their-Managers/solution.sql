select
    t1.name as Employee
from Employee t1
left join Employee t2 on t1.managerId = t2.id
where t1.salary > t2.salary

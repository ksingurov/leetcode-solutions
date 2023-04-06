select
    t1.employee_id
from Employees t1
left join Employees t2
on t1.manager_id = t2.employee_id
where t1.salary < 30000 and t1.manager_id is not null and t2.employee_id is null
order by employee_id

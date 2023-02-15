WITH customers_with_orders as (
    select distinct customerId
    from orders
)

select
    t1.name as Customers
from customers t1
left join customers_with_orders t2
on t1.id = t2.customerId
where t2.customerId is null

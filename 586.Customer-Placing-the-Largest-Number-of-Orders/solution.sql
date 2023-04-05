select
    customer_number
    # ,count(*) as order_count
from Orders
group by customer_number
# order by order_count desc
order by count(*) desc
limit 1

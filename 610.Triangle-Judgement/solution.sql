select
    *
    ,case
        when x+y<=z or x+z<=y or z+y<=x then 'No'
        else 'Yes'
    end as triangle
from Triangle

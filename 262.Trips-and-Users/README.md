# SQL Server Solutions for Trips and Users

This directory contains solutions for [`Trips and Users`](https://leetcode.com/problems/trips-and-users/description/) problem from `LeetCode`.

## Files

### 1. `trips_and_users_sqlserver_solution1.sql`
- **Description**: This solution uses `INNER JOIN` to filter out banned users (both clients and drivers) before processing the trip data.
- **Key Features**:
  - Filters banned users using `INNER JOIN`.

### 2. `trips_and_users_sqlserver_solution2.sql`
- **Description**: This solution uses `EXISTS` to filter out banned users (both clients and drivers) before processing the trip data.
- **Key Features**:
  - Filters banned users using `EXISTS` subqueries.

## Common Features
Both solutions:
- Focus on trips requested between `2013-10-01` and `2013-10-03`.
- Exclude trips involving banned users.
- Calculate the cancellation rate as `cancelled_trips_per_day / trips_per_day`, rounded to two decimal places.

## Notes
- The choice between `INNER JOIN` and `EXISTS` depends on your database's performance characteristics and the size of the data.
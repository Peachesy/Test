-- Person表
-- personId   firstName   lastName
-- 1          Wang        Allen
-- 2          Alice       Bob
-- ________________________________
-- Address表
-- addressId   personId   city              state
-- 1			2		   New York City     New York
-- 2           3          Leetcode          California


select p.firstName as first name,p.lastName as last name,a.city,a.state
from Person as p 
left join Address as a
on p.personId = a.personId




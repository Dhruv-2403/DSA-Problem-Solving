# Write your MySQL query statement below
with game as(
    select player_id , min(event_date) as login from Activity group by player_id
)

select round(sum(datediff(event_date,g.login)=1)/count(distinct a.player_id),2) as fraction from Activity a join game g on g.player_id=a.player_id

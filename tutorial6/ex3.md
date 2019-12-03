
### 3.2

executes those queries one by one to get a better feeling how `exists` works
```sql

select id, leg, leg - row_number() over (partition by id order by leg) section
from trails
where not exists (
	select * from completed c where
    trails.id = c.trail_id and trails.leg = c.leg 
);

```

```sql 

select id, section, count(*) from (
  select id, leg, leg - row_number() over (partition by id order by leg) section
  from trails
  where not exists (
      select * from completed c where
      trails.id = c.trail_id and trails.leg = c.leg 
  )
) group by id, section

```

```sql
select id, section, min(leg) firstLeg, max(leg) lastLeg, count(*) c from (
  select id, leg, leg - row_number() over (partition by id order by leg) section
  from trails
  where not exists (
      select * from completed c where
      trails.id = c.trail_id and trails.leg = c.leg 
  )
) 
group by id, section
having count(*) >= 3
```


#### Version with `except`

Equivalent query using "set" syntax.

```sql
select min(leg), max(leg), max(leg) - min(leg) + 1 from (
select id, leg, leg - row_number () over
( partition by id order by leg ) section
from (
select * from trails
except
select * from completed
)) group by id, section
```
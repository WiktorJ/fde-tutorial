#### In command list (mac)

* get data into the right format
`iconv -f iso-8859-1 -t utf-8 < actors.list > actors.list.utf`

* use head/tail to trim like that:
`head -n 20494548 actors.list.utf > actors.list.utf.trimmed`  or using `vim`

* run: `python transform.py ./actors.list.utf.trimmed`

#### In psql
```sql
create table playedin_text (
actor_name text not null ,
movie_name text not null );
```

```
\copy playedin_text from file.csv delimiter ',' CSV;
```
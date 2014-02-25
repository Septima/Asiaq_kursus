# Ad hoc queries

## Formål

Afprøve at lave dynamiske SQL forspørgsler i DBManger og få vist resultatet som et lag i QGIS.

Links: http://postgis.net/docs/manual-2.1/reference.html#Geometry_Constructors


1. Åben DBmanager->SQL Window
2. Copy/paste følgende SQL

```sql
select * from att0902.bygninger where "Info" = 'B-857'
```

3. Klik Excecute (f5) og se resultatet. Klik "store" og gem SQL med et sigende navn
4. Check af i ""load as new layer
5. Vælg kolonne med geometri og en id kolonne fra resultatet
6. Giv laget et navn
7. Klik Excecute (f5) igen og der burde være et nyt lag i kortet med de udvalgte objekter.
8. Prøv flere SQL forespørglser og find selv på nye. 
9

###Eksempler

Bygninger over 18 meter:

```sql
SELECT *from att0902.bygninger WHERE "Z" >18;
```

Bygninger med buffer:

```sql
select id, st_buffer(geom, 20) FROM att0902.bygninger
```

Bygninger uden B-nummer:

```sql
  SELECT * 
  FROM   att0902.bygninsnumre 
  WHERE  'info' IS NULL 
          OR 'info' = '';

```
Bygninger tæt på veje:

```sql
WITH vejmidte_buffer AS (

select id, st_buffer(geom, 10) as geom from att0902.vejmidte
), byg as
(
select * from att0902.bygninger
)
select DISTINCT  byg.* from vejmidte_buffer, byg where st_intersects(vejmidte_buffer.geom, byg.geom)
``
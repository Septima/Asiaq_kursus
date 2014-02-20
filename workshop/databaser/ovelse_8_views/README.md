# Brug af views

```sql
CREATE OR REPLACE VIEW att0902.ingen_b_nr AS 
 SELECT bygninsnumre.id, 
    bygninsnumre.geom, 
    bygninsnumre."Info", 
    bygninsnumre."Objekttype", 
    bygninsnumre."Z", 
    bygninsnumre."Konverteret"
   FROM att0902.bygninsnumre
  WHERE bygninsnumre."Info" IS NULL OR bygninsnumre."Info"::text = ''::text;
  ```

```sql
CREATE OR replace VIEW att0902.ingen_b_nr 
AS 
  SELECT * 
  FROM   att0902.bygninsnumre 
  WHERE  "info" IS NULL 
          OR "info" = '';

```
    

```sql


DROP VIEW att0902.byg_close_to_road ;
CREATE OR REPLACE VIEW att0902.byg_close_to_road AS
WITH vejmidte_buffer AS (

select id, st_buffer(geom, 10) as geom from att0902.vejmidte
), byg as
(
select * from att0902.bygninger
)
select DISTINCT  byg.* from vejmidte_buffer, byg where st_intersects(vejmidte_buffer.geom, byg.geom)

```
# Brug af views

## Formål

Deltageren afprøver at lave views som spatielle analyser i PostGIS og ser hvorledes ændringer i data dynamisk afspejlesi QGIS.



1. Sørg for at tabellerne bygninger og vejmidte er indlæst schemaet att0902
2. Åben enten Pgadmin eller i DBmanager SQL window og eksekvéwr følgebde sql:


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


Ovnstående view består af alle de bygninger,som er indenfor 10 meter af en vejmidte.

3. Åben nu att0902.byg_close_to_road, att0902.bygninger, att0902.vejmidte i QGIS. 
5.  Sørg for at att0902.byg_close_to_road er øverst i listen med anden farve end att0902.vejmidte.
6. Redigér nu vejmidte tabellen med nye vejsegmenter i nærheden af af bygninger og se laget att0902.byg_close_to_road dynamisk ændre sig.
7. Prøv selv at tænke i dynamiske analyser med egne data og diskutér, hvordan et views kan etableres til formålet.

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
  WHERE  'info' IS NULL 
          OR 'info' = '';

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
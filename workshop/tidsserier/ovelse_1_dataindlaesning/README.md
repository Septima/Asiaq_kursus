# Dataindlæsning

## Formål
Deltagerens skal afprøve teknikker til at indlæse data i QGIS med henblik på visualisering i Anita Grasers Timemanager plugin.


1. Gem data som CSV fil. Derefter konverteres data til shapefil som åbnes 
2. Kontrollér at data er korrekt konverteret. Ser data stemplet korrekt ud?
3. Opret ny tidskolonne og beregn nyt tidsformat til TimeManager:
Følgende udtryk kan bruges i field calculator pg kan bruges til at beregne ny kolonne med dato.

Expression/udtryk i field calculator

    '20' || substr("Acquisit_2", 7, 2) || '-' || substr("Acquisit_2", 0, 3) || '-' || substr("Acquisit_2", 4, 2) ||' ' ||    substr("Acquisit_2", 10, 5)||':00'


4. Alternativ konverteres shapefilen til databsaen med DBmanager. Defefter kan der oprettes en ny kopi af tabellen , hvor datokolonnen er "castet" korrekt.

Eksempel på cast af kolonne til andet datoformat
```sql
CREATE TABLE "time".test1 AS
select acquisition_date_time::timestamp without time zone as test ,*  from "time".caribou_613847;
```

Nu er data parat til anvendelse i TimeManager plug-in






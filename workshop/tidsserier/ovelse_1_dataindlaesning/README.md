# Dataindlæsning

## Formål
Deltagerens skal afprøve teknikker til at indlæse data i QGIS med henblik på visualisering i Anita Grasers Timemanager plugin.


1. Gem data som CSV fil. Åben layer->add delimted text layer
2. Vælg om det er semikolon eller komma, der anvendes som separator
3. Nu vælges hvilke kolonner, der skal bruges til koordinater
4. Kontrollér at data er korrekt konverteret. Ser data stemplet korrekt ud?
5. Opret ny tidskolonne og beregn nyt tidsformat til TimeManager:
Følgende udtryk kan bruges i field calculator pg kan bruges til at beregne ny kolonne med dato. Der skal vælges "create new field" og "width" skal mindst 20 og typen af kolonnen skal være "string"

Eksempel på Expression/udtryk i field calculator

    '20' || substr("Acquisit_2", 7, 2) || '-' || substr("Acquisit_2", 0, 3) || '-' || substr("Acquisit_2", 4, 2) ||' ' ||    substr("Acquisit_2", 10, 5)||':00'

Tilpas expression til egne data så tidsformatet er yyyy-mm-dd hh:mm

6. Endelig konverteres data til shapefil som åbnes 
7. Alternativ konverteres shapefilen til databasen med DBmanager. Derefter kan der oprettes en ny kopi af tabellen , hvor datokolonnen er "castet" korrekt.

Eksempel på cast af kolonne til andet datoformat
```sql
CREATE TABLE "time".test1 AS
select acquisition_date_time::timestamp without time zone as test ,*  from "time".caribou_613847;
```

Nu er data parat til anvendelse i TimeManager plug-in






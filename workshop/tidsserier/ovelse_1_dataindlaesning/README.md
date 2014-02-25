# Dataindlæsning

## Formål
Deltagerens skal afprøve teknikker til at indlæse data i QGIS med henblik på visualisering i Anita Grasers Timemanager plugin.


1. konvertér data til shapefil eller til database
2. Kontrollér at data er korrekt konverteret. Ser data stemplet korrekt ud?
3. Opret ny tidskolonne og beregn nyt tidsformat til TimeManager:
Følgende udtryk kan bruges i field calculator kan bruges til at beregne ny kolonne.

'20' || substr("Acquisit_2", 7, 2) || '-' || substr("Acquisit_2", 0, 3) || '-' || substr("Acquisit_2", 4, 2) ||' ' ||    substr("Acquisit_2", 10, 5)||':00'






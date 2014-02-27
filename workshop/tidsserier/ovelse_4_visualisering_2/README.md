# Avanceret visualisering

## Formål

Deltageren afprøver teknikker til at avanceret visualsieringer af tidsserier. Der arbejdes med timing af forskellige lag med "offset" funktionalitet samt grafiske "blending modes" e wikipedia for mere om blending modes

Der skal oprettes 2 lag:

permanent: Vises permanent efter at punktet er vist og vises 10 sekunder forskudt (offset=10)
flash: Vises midlertidigt når et punkt vises, men aktiveres efter 20 sekunder

1. Indlæs laget igen to gange og omdøb tl hhv. permanent og flash
2. Redigér stylen på flash og vælg et stort symbol
3. Vælg "multiply" som feature blending mode
4. Redigér stylen på permanent til en diskret og lille style
5. Tilføj ny kolonne (create new field) med navnet "forever" med field calculator med en dato langt frem i tiden. Expression er blot en streng med en dato : *'2020-01-01 20:00'*. Husk at vælge 20 "width" og typen "string". 
6. Åben begge lag i timemanager og for laget permanent vælges den nye kolonne "forever" som  "End Time". Sæt offset til 20 sekunder
7. Afspil visualisering
8. Herefter bruges resten af tiden på at "lege" med blending modes og offsets.
UTM-transformation i QGIS
=======================================

Som udgangspunkt benytter QGIS i forbindelse med transvers mercator en transformationsalgoritme, der giver relativt store fejl, når der transformeres til/fra koordinater, som ligger relativt langt uden for UTM-zonens definitionsområde.

Opsætning af QGIS
---------------------------------------
Version 2.0 af QGIS kan bringes til at foretage korrekt transformation af grønlandske UTM-data ved at sætte en system-variabel.

Dette kan gøres som følger (De præcise navne kan afhænge af Windows-versionen):

  1 Åbn Windows´ kontrol-panel
  2 Vælg 'System og Sikkerhed'
  3 Vælg 'System'
  4 Vælg 'Avancerede systemindstillinger'
  5 Vælg 'Miljøvariable'
  6 Under 'Systemvariable' vælges 'Ny'
  7 I 'Variabelnavn' indtastes `OSR_USE_ETMERC` og i 'Variabelværdi' indtastes `YES`

QGIS lukkes og startes igen og herefter skulle den foretage korrekte transformation.

OBS: Benyt nedenstående script til at kontrollere, at QGIS rent faktisk transformerer korrekt. Det er nok en god idé at lade scriptet være installeret altid, så det opdages øjeblikkeligt, hvis transformationer af den ene eller anden årsag ikke virker.

### Angående QGIS versioner større end 2.0
Under besøget hos Asiaq blev det testet, hvorvidt QGIS version 2.2 fungerer med ovenstående miljøvariabel. Resultatet af undersøgelsen var, at det gør den _ikke_. Det er ikke undersøgt hvorfor, eller om der er alternative metoder til at opnå samme effekt.

Kontrolscript
---------------------------------------
Hvis scriptet (`startup.py`)[https://github.com/Septima/Asiaq_kursus/raw/master/OSR_test/startup.py] installereres som startup script i QGIS vil det under hver opstart af programmet vise en lille dialog, der fortæller, om den pågældende installation af QGIS kan transformere korrekt til/fra UTM.

Rent praktisk transformerer scriptet en koordinatet i UTM19 til UTM24 og tilbage til UTM19. Derefter beregnes afstanden mellem den originale UTM19-koordinat og den transformerede UTM19-koordinat. Hvis afstanden er mindre end 0,1 mm anses transformationen for at være 'korrekt'.

### Installation af scriptet
Installation kan foregå ved at downloade scriptet og kopiere det ind i python-mappen under QGIS´ bruger-specifikke mappe.

Denne findes typisk på en sti a la
`c:\\Brugere\\BRUGERNAVN\\.qgis\\python`

I nogle tilfælde findes der ikke en `python`-mappe under `.qgis`-mappen. Er dette tilfældet, oprettes mappen `python`-manuelt.

Findes der allerede et `startup.py`-script på ovennævnte sti, må indholdet flyttes over i dette script manuelt. Åbn begge filer i en tekst-editor og indsæt hele indholdet øverst i den eksisterende fil.

### Verfifikation af installation
Efter installationen lukkes QGIS og startes igen. I forbindelse med opstarten skulle der nu komme en dialog-boks med en besked om QGIS´ evne til at transformere grønlandske data.
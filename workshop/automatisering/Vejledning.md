Indledning
============================================
Der er adskillige måder, hvormed man kan "automatisere" opgaver i QGIS. Nogle metoder kræver programmering mens andre kan konfigureres i brugergrænsefladen.

Er du ikke interesseret i programmering vil det nok være relevant at kigge på opgaverne i Processing Toolbox og i Atlas.

Er du interesseret i programmering vil de øvrige opgaver også have interesse.

Processing Toolbox
=============================================
Aktivér Processing Toolbox (Klik Processing -> Toolbox).

Nu skulle der gerne være dukket et nyt panel op i højre side af skærmen. I dette panel er alle tilgængelige algoritmer listet. Øverst i panelet er der en indtastningsbox, som filtrerer listen efter det indtastede. Prøv eksempelvis at skrive "Fill sinks".

Nederst i panelet er der en rullegardin, hvor man skifte mellem "Simplified interface" og "Advanced interface". I det forsimplede interface er algoritmerne forsøgt kategoriseret efter deres anvendelse. Dette interface indeholder til gengæld ikke alle algoritme! I det avancerede interface er alle algoritmer med, men de er arrangeret efter deres oprindelse (kommer algoritmen fra SAGA, GRASS eller GDAL-projektet), hvilket gør det noget mere besværligt at lede efter relevante algoritmer.

Prøv at kigge  algoritmerne igennem. Læg mærke til, at der kan findes flere algoritmer, som gør det samme eller næsten det samme.


Case hydrologisk beregning
---------------------
Som eksempel ønsker vi at lave en Processing model, der kan beregne en grid DTM ud fra et sæt højdekurver.

Først gennemgås processens enkelte trin. Derefter bygger vi en model, der samler trinene til én ny Processing Algoritme.

Indlæs kurver_samlet.shp

Aktivér Processing algoritmen "Shapes to grid". Den findes under SAGA og kan kun findes i "Advanced interface". Denne algoritme opretter en raster og sætter celleværdierne i rasteren til en attributværdi et vektorlag. Som input "Shapes" vælges laget "kurver_samlet". Som input "Attribute" vælges "Z"-attributten fra kurver_samlet-laget. "Preferred Target Grid Type" sættes til "[3] Floating point (4 byte)" og "Cell size" sættes til 1.0. Under "Grid" vælges et output bibliotek, som du kan finde igen, og giv output filen navnet "rasteriseret.tif".

Kør algortimen. Det burde tage nogle få sekunder.

Kig på data i rasteriseret.tif. Brug eventuelt "info"-værktøjet til at udlæse nogle celleværdier.

Celler under højdekurverne skulle gerne have samme celleværdi som højdekurvens Z-værdi. Der, hvor der ikke er højdekurver, skulle rasteren gerne have "no data".

Vi vil nu interpolere nogle Z værdier for alle cellerne, der har "no data". Der findes et utal af algoritmer i Processing til interpolation. Den mest egnede i dette tilfælde er nok "r.surf.contour", men den er meget, meget lang ti om at beregne. Derfor benytter vi i denne øvelse algoritmen "Fill nodata", som er meget hurtig, men som også giver et noget ringere resultat.

Aktivér algoritmen "Fill nodata", som findes under "GDAL Analysis".

Som "Input layer" vælges den netop rasteriserede fil ("rasteriseret.tif"). "Search distance" sættes til 1000. "Smooth iterations" forbliver 0 (I min udgave fungerer andre værdier ikke!). I "Output layer" vælger du at gemme filen i mappen fra før. Giv filen navnet "Attu_DEM.tif".

Kør algoritmen. Den burde blive færdig på nogle sekunder.

Kig på data. Output skulle gerne være ligne en højdemodel. Dvs alle celler har en værdi, som nogenlunde svarer til Z-værdien i virkelighedens verden.

Automatisering af workflowet
------------------------------
Nu skal ovenstående lille workflow bestående af algoritmerne "Shapes to grid" og "Fill nodata" bygges ind i vores egen algoritme, som kan eksekveres i ét enkelt trin.

Åben Processing Toolboxens grafiske model-værktøj (Klik Processing -> Graphical modeler).

I det grafiske model-værktøj er der to faner. I fanen "Inputs" defineres de inputs, som algoritmen kan tage imod. I fanen "Algorithms" sammensættes den nye algoritmes workflow ud fra eksisterende algorimer, scripts osv.

Øverst i modelværktøjet findes en række knapper til at åbne og gemme algoritmer, og til at køre og skrive hjælp til den aktuelle algoritme. Øverst findes også tekst-bokse til at angive et model-navn og en model-gruppe. Indtast "Højdekurver til DEM" i "model name" og "Terræn" i "group name".

Vores workflow tager i første omgang følgende input: et vektorlag med højdekurver og en angivelse af hvilken attribut, der indheloder Z-værdierne.

I inputfanen dobbeltklikkes på "vector layer". I Parameter definition-dialogen angives parameterens navn "Højdekurver", at input skal være linier, og at dette input er påkrævet "Required" = "Yes". Klik OK.

Derefter tilføjes en "Table field"-input-parameter. Parameternavnet kunne feks være "Z" og "Parent layer" er den netop oprettede input vektorlag "Højdekurver". Klik OK.

I "Algorithms" fanen fremfindes nu "Shapes to grid"-algoritmen. Dobbeltklik på algoritmen i listen. Nu fremkommer samme dialog, som da vi brugte algoritmen direkte fra Processing Toolbox lige før. Den eneste forskel er, at vi ikke kan vælge de lag, som er åbne i QGIS som input. I stedet kan vi kun kan vælge de vektorlag og attributter, som vi lige har defineret i "Input"-fanen. Således sættes "Shapes" til "Højdekurver" og "Attribute" sættes til "Z". Som ovenfor sættes "Preferred Target Grid Type" til "[3] Floating point (4 byte)" og "Cell size" sættes til 1.0. Klik OK.

Nu skulle modelværktøjet gerne vise en slags flowdiagram, hvor input-parametrene er forbundet med "In" på algoritmen "Shapes to grid".

Nu er det på tide at få gemt et mellemresultat. Klik på "Save"-ikonet. Kontrollér at filen bliver gemt i et bibliotek, som hedder noget i retningen af "C:\Users\Asger\.qgis2\processing\models\". Dette er stedet, hvor alle hjemmebyggede modeller skal ligge. Kald filen "Kurver_til_DEM.model" og gem.

TIP: Algoritmen kan udveksles med andre brugere af QGIS ved at kopiere denne fil.

Nu skal vi have tilføjet "Fill nodata" til vores algoritme. I "Algorithms"-fanen findes og dobbeltklikkes på "Fill nodata"-algoritmen. Som input til algoritmen vælges outpu fra forrige skridt. Dette hedder formodentlig noget i retningen af "Grid from algorithm 0(Shapes to grid)". "Search distance" sættes til 1000 og "Output layer" kaldes "DEM". Klik OK.

Nu skulle flowdiagrammet gerne være opdateret den nye algoritme, som har et output kaldet "DEM".

Gem algoritmen.

KLik på "Edit model help"-knappen i toppen af modelværktøjet. Her kan algoritmen dokumenteres og hjælp til brugeren skrives. Indtast en smule hjælp. "Algorithm description" kunne feks være 'Grid DEM fra Højdekurver. Bemærk, at interpolationsmetoden er dårligt egnet til formålet.' Indtast kort beskrivelse af input og output. Klik OK.

Gem algoritmen og luk modelværktøjet.

Tilbage i QGIS sørger du for at "Kurver_samlet.shp" er indlæst.

I Processing Toolbox findes nu algoritmen, som du lige har gemt. Har du brugt det foreslåede navn, hedder den "Højderkurver til DEM". Aktivér algoritmen, se at der står hjælp i "Help"-fanen og kør algoritmen på højdekurverne.

Kontrollér at output er som forventet.

Prøv nu at lave følgende ændring i "Højdekurver til DEM"-algoritmen: Det skal være muligt at angive cellestørrelsen ("Cellsize" i "Shapes to grid"), som inputparameter. Prøv at køre den opdaterede algoritme.

Batchkørsel af processing algoritmer
------------------------------------
Processing algoritmer kan eksekveres på mange filer ved at højreklikke på algoritmen og vælge "Execute as batch process".

I batch processing vinduet kan man tilføje filer enten en ad gangen, eller man kan vælge flere filer på én gang. Der kommer så en linie i tabellen for hver fil. Output-filer kan enten angives manuelt, ellers kan man (når den første output-fil er angivet) få QGIS til at give output-filerne navn efter input-fil, en parameterværdi eller blot med et fortløbende nummer.

TIP: Prøv at højreklikke på den nye algortime i Procesing Toolbox og vælg "Save as Python script". Kig på det gemte python script. Dette script kan ændres, eller det kan fungere som inspiration for helt nye scripts. 

Python console
=========================================
QGIS har en interaktiv Python konsol. Den aktiveres ved at klikke Plugins -> Python Console.

Der findes en "kogebog" til brug af Python i QGIS. Den hedder PyQGIS Cookbook og findes på QGIS´ [dokumentationsside] (http://qgis.org/en/docs/index.html#). På samme side findes også links til API-dokumenation som kan være nyttig/nødvendig, hvis man går dybere ind i python-udvikling til QGIS.

I konsollen kan man direkte skrive python-kode, som bland andet kan interagere med QGIS. Prøv først at skrive 
```python
a = 1
b = 2
print a + b
```

I Pythonkonsollen kan man få noget information om objekter ved at skrive ```help(OBJEKTNAVN)```.

Indlæs en Bygningerne fra grundkortet og gør laget aktivt i logkontrollen.

I pythonkonsollen kan vi nu få fat i laget via objektet ```iface```. Prøv at skrive

```python
help(iface)
```

Og se på output.

Prøv nu

```python
layer = iface.activeLayer()
print layer
```
Output af ovenstående er noget i retningen af ```<qgis.core.QgsVectorLayer object at 0x114594f80>```.

Nu kan vi ved at skrive ```help(layer)```få at vide, hvad vi kan gøre med layer-objektet. Vi kan feks:

```python
layer.name()
layer.featureCount()
layer.source()
```

Vi kan også tage fat i features fra laget:
```python
layer = iface.activeLayer()
for feature in layer.getFeatures():
  print feature.id()
  geom = feature.geometry()
  print geom.area()
  attrs = feature.attributes()
  print attrs
```

Lad os sige, at vi er interesserede i det samlede antal koordinater i bygningstemaet. Dette vill kunne beregnes således:

```python
layer = iface.activeLayer()
numpoints = 0
for feature in layer.getFeatures():
  geom = feature.geometry()
  if geom.type() == QGis.Polygon:
    x = geom.asPolygon()
    for ring in x:
      numpoints += len(ring)
      print numpoints
  else:
    print "Ups dette er ikke en polygon"
```

Python scripts
================================

Har man brug for den samme kode flere gange, kan man i stedet for at taste den ind i konsollen eksekvere den som et script. 

Installere "ScriptRunner" pluginet.

Gem følgende i en fil, som du kalder "CountPoints.py":
```python
from qgis.core import QGis
def run_script(iface):
  layer = iface.activeLayer()
  if not layer:
    print "Intet aktivt lag"
    return
  numPts = 0
  for feature in layer.getFeatures():
    geom = feature.geometry()
    if geom.type() == QGis.Point:
      x = geom.asPoint()
    elif geom.type() == QGis.Line:
      x = geom.asPolyline()
    elif geom.type() == QGis.Polygon:
      x = geom.asPolygon()
    else:
      raise Exception("Unknown geometry type")
    for sub in x:
      numPts += len(sub)
  print numPts
```

Aktiver ScriptRunner, tilføj det ovenfor oprettede script og kør scriptet i ScriptRunner.

En anden måde at genbruge python-kode på er at tilføje den til filen
```c:\Users\BRUGERNAVN\.qgis2\python\startup.py``` (Hvor Users\BRUGERNAVN afhænger af Windowsversion og brugernavn). Kode i denne fil eksekveres ved opstart af QGIS. Ovenstående funktionalitet kunne således tilføjes med et andet metodenavn til startup.py, hvorefter den ville være tilgængelig i konsollen.

Custom expressions
==================================
Man kan også lave sine egne funktioner til Expression builderen (er tilgængelig feks i Field Calculator, Label motoren og flere andre steder).

Lad os sige, at vi har brug for at kunne sætte antallet af koordinater i geometrien på som label. 

I startup.py tilføjes følgende:

```python
from qgis.utils import qgsfunction
from qgis.core import QGis

@qgsfunction(0, "Python")
def numpoints(values, feature, parent):
    geom = feature.geometry()
    if not geom:
        return None
    numPts = 0
    if geom.type() == QGis.Point:
      x = geom.asPoint()
    elif geom.type() == QGis.Line:
      x = geom.asPolyline()
    elif geom.type() == QGis.Polygon:
      x = geom.asPolygon()
    else:
      raise Exception("Unknown geometry type")
    for sub in x:
      numPts += len(sub)
    return numPts
```

Genstart QGIS. Nu skulle funktionen "numpoints" være tilgængelige under kategorien "python" i expression builder, alle de steder den bruges. Prøv feks at sætte labels på et lag, hvor lablen indeholder antallet af punkter i geometrien.

Plugins
==========================
Den nemmeste måde at komme i gang med at bygge plugins er, at installere pluginet "Plugin Builder". Dette plugin danner et rammeværk af filer, som skal til for at bygger sit eget plugin. Derefter er det "bare" at fylde sin egen kode ind.

En meget effektiv måde at lære hvordan plugins kodes er ved at kigge på de eksisterende plugins. Disse findes i et bibliotek a la
```c:\Users\BRUGERNAVN\.qgis2\python\plugins```

Hvis du ikke allerede har installeret plugins, så er nu et godt tidspunkt. Kig derefter i filerne i ovenstående mappe med en textedit (feks notepad).

TIP: Står man nu med et konkret kodeproblem, man ikke kan løse, kan man kigge efter et plugin, som formodentlig har løst problemet, installere pluginnet og derefter kigge i dets kode. Dette er nok den mest effektive måde at blive klog på.

For at kunne redigere i GUI for plugins, skal man have programmet Qt Creator installeret. Det kan downloades på (QT Projects hjemmeside)[https://qt-project.org/downloads]. Deres online installer fungerer fint. Der kan installeres en masse mere, end hvad der er brug for - der er kun brug for QT Creator.

Pluginet (eller måske rettere det bibliotek, som indeholder pluginet) placeres i mappen ```c:\Users\BRUGERNAVN\.qgis2\python\plugins```. Efter en genstart af QGIS er pluginet til rådighed i QGIS.

TIP: I stedet for at genstarte, kan man installere pluginet "Plugin Reloader". Med dette plugin kan ens plugin genindlæses ved et tryk på en knap, og der spares en genstart af QGIS.

Atlas
==========================
Atlas er en måde at automatisere "print" af et kort for hver feature i et lag. Antag eksempelvis, at vi ønsker at printe et kort for hvert B-nummer, der opfylder et bestemt kriterium, således at printet eksempelvis kan sendes til ejerne.

Prøv at indlæse data fra grundkortet og lav en symbolisering af lagene.

Lav en ny Print Composer.

Lav en passende opsætning af denne print composer.

Når alt er klart klikkes på fanen "Atlas generation" til højre i composeren. Her aktiveres "Generate an atlas", "Composer map" sættes til hovedkortvinduet (ofte "Map 0") og "Coverage layer" sættes til det lag, der indeholder de features, som skal have et kort hver. I dette tilfælde kunne det være Bygningsnumre. Er coverage laget et polygon- eller linielag, kan kortudsnittet enten defineres ved en fast scale (som defineres i hovedkortet) eller ved geometriens bbox + X%. For punkter kan der kun benyttes en fast scala.

Når alt er klart trykkes på PDF-eksport-knappen. Composeren vil nu spørge efter i bibliotek, hvor PDF'erne skal placeres og derefter laver Composeren forhåbentlig en PDF per bygning i denne mappe.
Analyser på DTM/DSM
=====================================
Data:

Til første del anvendes data i mappen Kolding
* DTM
* DSM
* Bygninger

Basale rasterfunktioner
-------------------
Indlæs DSM.

Zoom lidt rundt i rasteren. Højreklik på laget og vælg "Strech using current extent".

Højreklik på laget og vælg "Zoom to best scale".

Højreklik på laget og vælg "Properties". Herefter undersøges mulighederne i properties dialogen:

Prøv at symbolisere DSM'en på forskellige måder. Udforsk især muligheden for selv at definere farver for forskellige højdeintervaller. 

Udforsk hvad forskellen er på de tre "Color interpolation"-indstillinger.

Prøv forskellige "color ramps". Prøv også de forskellige muigheder under "New Color Ramp".

Afprøv muligheder for at definere transparens.

Byg pyramider på rasteren (Også kaldet overviews på DSM).

Kig på histogrammet og se, hvad der står af informationer i "Metadata".


Udlæse værdier fra rasteren
----------------------
Indlæs både DTM og DSM.

### Info
Prøv at klikke på rasteren med "Info"-værktøjet.

### Value tool
Installér pluginet "Value Tool". (Klik Plugins -> Manage and install plugins... -> Get more. Indtast "Value tool" i søgeboksen).

Nu kommer der et ekstra panel under lagkontrollen. (Hvis ikke kan det slås til under View -> Panels -> Value Tool).

I Value Tool panelet sættes et flueben i "Active". Prøv at føre musen rundt over rasteren i kortvinduet.

### Profile tool
Installér pluginet "Profile tool". (Klik Plugins -> Manage and install plugins... -> Get more. Indtast "Profile tool" i søgeboksen)

Aktivér profil-værktøjet ved at klikke på ikonet i værktøjslinien. Nu dukker der et panel op i bunden af skærmen. Sørg for at både DTM og DSM er aktive lag i Profil toolet og giv dem forskellige farver i toolet.

Profile toolet tillader at tegne en linie i kortvinduet, hvorefter der vises en profil for hver aktiv raster i grafen. Man kan også udpege en eksisterende linie. Prøv at zoome ind og ud i grafen.

I profiltoolets "Table"-tab kan man få profilet i tabel-format.

Se under "Settings"-tabben og bemærk, at "Profile tool" som udgangspunkt ikke nødvendigvis anvender rasterens fulde opløsning!

Simple afledte data
----------------------
Indlæs både DTM og DSM.

Beregn højdekurver med 10m ækvidistance for DTM. (Klik Raster -> Extraction -> Contour). Kig på resultatet. (Der findes i øvrigt adskillige andre værktøjer til at beregne højdekurver i Processing toolboxen.)

Beregn et skyggekort (Hillshade) for DSM. (Klik Raster -> Analysis -> DEM (Terrain models)). Kig på resultatet. Skyggekortet kan være nyttigt til hurtigt at danne sig et indtryk af en højdemodel. Prøv eventuelt at regne flere skyggekort, hvor der anvendes forskellige værdier for overhøjde (Z factor) og lys-vinkler (Azimuth og Altitude).


Map Algebra
------------------------
Indlæs både DTM og DSM.

Nu ønsker vi at danne en raster, der indeholder differencen mellem Z-værdierne fra DSM og DTM - en såkaldt NDSM. Vi skal altså trække DTM-værdien fra DSM-værdien i hver celle.

Åbn "Raster Calculator" (Klik Raster -> Raster calculator).

Alle rastere, der er indlæst i QGIS er nu tilgængelige som input for vores beregning. Kontrollér at både DSM og DTM er til rådighed i listen "Raster bands". (Hvis ikke, må du ud og åbne dem i QGIS først).

Nu skal vi definere formlen, som skal beregnes for hver celle:
Dobbeltklik på DSM i listen. Klik på minus-operatoren og dobbeltklik på DTM i listen.

Under "Result layer" skal du vælge en placering og et filnavn til output. Man kan også justere på opløsning og bbox for output-laget. Vi anvender blot samme opløsning og bbox som inputlagene.

Kør processen.

Kig på resultatet. Prøv at symbolisere det. Prøv især at sætte celler med værdien 0.0 til at være gennemsigtig.

TIP: Har du brug for at lave en raster, som har samme opløsning og bbox som eksisterende raster men med en konstant værdi, så kan du bruge den eksisterende raster som input i Raster Calculator og blot benytte den konstante værdi i formlen.

TIP: Der kan også laves sammenligninger i Raster Calculator. Ønsker man eksempelvis at erstatte DSM-værdien med DTM-værdien, hvis forskellen på de to er mindre end 1 meter, kan følgende formel benyttes:

(("DSM@1" - "DTM@1") < 1) * "DTM@1" + (("DSM@1" - "DTM@1") >= 1) * "DSM@1"

Her udnyttes det, at et falsk udtryk evaluerer til værdien 0 (nul) og et sandt til værdien 1.

Der findes i øvrigt et endnu stærkere Map Algebra værktøj kaldet r.mapcalculator i Processing Toolboxen.

Rasterisering af vektorer
-------------------------
Indlæs DTM, DSM og bygninger.

Vi ønsker nu en DTM, som er mere egnet til at lave hydrologiske beregninger på. I den udleverede DTM er bygningerne editeret bort, og vandet kan derfor frit strømme, hvor det i virkeligheden blokeres af en bygning.

Strategien i denne øvelse er, at vi vil kopiere DSM-værdien ind i DTM'en, der hvor vi ved, der er en bygning.

Først laver vi en raster, som har 0 (nul) i alle celler, og som har samme opløsning og bounding box, som vores DTM og DSM.

Dette gøres med Raster calculator, som beskrevet ovenfor.

Dernæst skal alle celler, som er inden for en bygningspolygon sættes til en anden værdi end nul.

Dette gøres med "Rasterize"-værktøjet. (Klik Raster -> Conversion -> Rasterize). Vælg en attribut, som har værdier større end nul. Som output raster peges på den ovenfor dannede raster (Dette er et af de sjældne tilfælde, hvor output ikke skrives til en ny raster men skrives ind i en eksisterende).

Nu har vi så en raster med 0 uden for bygninger og X (hvor X > 0) inden for bygninger.

Nu kan vi med "Raster calculator" lave et output, hvor cellværdien kommer fra DTM, hvis "bygningsrasteren" er 0 og ellers kommer celleværdien fra DSM. Prøv selv at regne ud, hvordan formlen skal se ud.

TIP: Raseterisering af vektorlag kan bruges til at "håndeditere" terrænmodeller. Vil man eksempelvis indsætte en dæmning, kan man lave en linie, som har dæmningens top-kote som attribut.

TIP: Hvis man rasteriserer et linie- eller punkt-lag, som har Z-værdier på koordinaterne, så kan man rasterizere Z-værdien i stedet for en attribut-værdi.

Processing Toolbox
-------------------------
Der findes adskillige algoritmer til at regne på vand og terrænmodeller. De gemmer sig alle i "Processing Toolbox".

Aktivér Processing Toolbox (Klik Processing -> Toolbox).

Nu skulle der gerne være dukket et nyt panel op i højre side af skærmen. I dette panel er alle tilgængelige algoritmer listet. Øverst i panelet er der en indtastningsbox, som filtrerer listen efter det indtastede. Prøv eksempelvis at skrive "Fill sinks".

Nederst i panelet er der en rullegardin, hvor man skifte mellem "Simplified interface" og "Advanced interface". I det forsimplede interface er algoritmerne forsøgt kategoriseret efter deres anvendelse. Dette interface indeholder til gengæld ikke alle algoritme! I det avancerede interface er alle algoritmer med, men de er arrangeret efter deres oprindelse (kommer algoritmen fra SAGA, GRASS eller GDAL-projektet), hvilket gør det noget mere besværligt at lede efter relevante algoritmer.

Prøv at kigge efter algoritmer til hydrologiske beregninger.

TIP: I Det simplificerede interface er der nogle under Geoalgorithms -> Domain specific -> Hydrology og under Geoalgorithms -> Domain specific -> Terrain Analyis and geomorphometry.
TIP: I det avancerede er de spredt lidt rundt omkring. SAGA har interessante algoritmer i flere underkategorier under Terrain Analysis. I GRASS ligger de hulter til bulter under "Raster".

Det er tanken, at hver algoritme er dokumenteret i Processing Toolbox, men man kommer ofte ud for at dokumentationen er tom. I det tilfælde må man søge dokumentationen i det projekt, som algoritmen stammer fra SAGA/GDAL/GRASS/R etc, eller helt simpelt gennem Google.

Wang & Liu
--------------------------
Åbn DTM eller alternativt den nyligt fremstillede DTM med bygninger inkluderet.

I Processing Toolbox aktiveres algoritmen "Fill sinks (wang & liu)" (OBS: Der er flere algoritmer med næsten ens navne!)

Læg mærke til at "Help" er tom for denne algoritme.

Fra nettet findes:

>This module uses an algorithm proposed by Wang and Liu (2006) to identify and fill surface depressions in DEMs. The method was enhanced to allow the creation of hydrologically sound elevation models, i.e. not only to fill the depressions but also to preserve a downward slope along the flow path. If desired, this is accomplished by preserving a minimum slope gradient (and thus elevation difference) between cells. This is the fully featured version of the module creating a depression-free DEM, a flow path grid and a grid with watershed basins. If you encounter problems processing large data sets (e.g. LIDAR data) with this module try the basic version (xxl.wang.lui.2006).

Vælg din DTM som input og sørg for at outputs bliver skrevet til en mappe, som du kan finde, og som beskriver algoritmen (Feks "wangliu"). Vi får især brug for outputtet "Filled DEM" senere.

Kør algoritmen. Den bør blive færdig på ca to minutter.

Kig på output. Symbolisér dem.

Output kaldet "Filled DEM" fra Wang & Liu er en udgave af input DTM, hvor alle afløbsløse lavninger er fyldt op, således at der fra en vilkårlig celle i modellen er vej til kanten af rasteren hvor celleværdierne er konstant faldende.

Man kan se de områder, som algoritmen har fyldt op ved at bruge "Raster calculator" og trække input DTM fra "Filled DEM". Disse områder kaldes også "Blue spots". "Blue spots" kan være en udmærket måde at kontrollere sin DTM på. I nogle tilfælde vil fejl i modellen give sig meget tydligt til kende i blue spot kortet. Er der feks en dyb blue spot oven i en sø, kan der være noget galt med modellen omkring afløbet af søen. Sådanne fejl kan i øvrigt fixes med brug rasterisering af linier.

Catchment Area (Parallel)
-----------------------------
Åbn "Filled DEM" fra ovenstående.


I Processing toolbox aktiveres algoritmen "Catchment Area (Parallel)" (OBS: Igen er der flere med ensklingende navne).

I "Elevation" vælges som input "Filled DEM"-rasteren. De øvrige input forbliver default-værdier.

Output kaldet "Catchment Area" (også kaldet accumulated flow) skal du gemme et sted, du kan finde. De øvrige output kan du blot lade være midlertidige filer.

Kør algoritmen. Den bør blive færdig på et par minutter.

Kig på outputs. Prøv at symbolisere "Catchment area". Hver celle i denne raster fortæller, hvor mange celler, der ligger opstrøms, så celleværdierne er absolut ikke uniformt fordelt. Brug eventuelt 

Channel Network
-----------------------------
Åbn "Filled DEM" og "Catchment Area" fra ovenstående.

I Processing toolbox aktiveres algoritmen "Channel Network".

Input "Elevation" sættes ti "Filled DEM", "Initiation Grid" sættes til "Catchment Area", "Initiation Type" sættes til "[2] Greater than" og "Initiation Threshold" til 10000.

Sørg for at gemme "Channel Network" output (Der er to med samme navn, vi skal især bruge den første.)

Watershed basins
-----------------------------
Åbn "Filled DEM" og "Channel Network" fra ovenstående.

I Processing toolbox aktiveres algoritmen "Watershed Basins".

"Elevation" sættes til "Filled DEM" og "Channel Network" til "Channel Network" fra ovenstående.

Kør processen og se på output.

TIP: Oplandene kan vektoriseres på flere måder i QGIS. Feks med Processing Algoritmen "Vectorising grid classes"

Processing model
-----------------------------
Særligt interesserede kan kigge på Processing algoritmen "Watershed from DEM and Threshold", som samler ovenstående trin i én algoritme.

Yderligere analyser
-----------------------------
Prøv eventuelt at kigge på viewshedanalysen i Processing Algoritmen "r.los".

Med ovenstående metoder til rasterisering og beregninger med map algebra kan der i kombination med pluginet "Zonal statistics" laves mere eller mindre komplicerede volumenbereginger. Prøv eventuelt at udføre en volumenberegning.

Grønlandske data
=============================
UTM
-----------------------------
Som sikkert bekendt kan transformation til/fra UTM-koordinater langt uden for UTM-zonens definitionsområde være forbundet med relativt store fejl. Vi har set fejl på op til 1000m ved transformation af koordinater frem og tilbage mellem zone 19 og zone 24.

I QGIS kan dette problem undgås ved at anvende en brugerdefineret udgave af UTM-projektionen i stedet for QGIS' indbyggede.

Klik Settings -> Custom CRS...

I Custom CRS-dialogen klikkes "Add new CRS". Det nye koordinatreferencesystem gives et navn og parametrene indtastes. Eksempel for UTM zone 22:

```
+proj=etmerc +lat_0=0 +lon_0=-51 +k=0.9996 +units=m +x_0=500000 +datum=WGS84 +nodefs +wktext
```
Navnet på dette CRS kunne feks være ```UTM22N WGS84 Engsager Extended```

Der oprettes et custom CRS for hver UTM-zone, der ønskes benyttet. I parametrene ovenfor ændres blot parameterværdien lon_0 til zonens midtmeridian.

Attu
-----------------------------
Til denne del af øvelsen anvendes data fra mappen Attu.

Indlæs Attu_by_interpoleret.tif og gimpdem1_2_compress.tif.

Attu_by_interpoleret.tif har 1m opløsning og er dannet ved interpolation af 2-meter-kurverne fra Attu ved brug af algoritmen "r.surf.contour". Dette er gjort forud, da det tager meget lang tid.

Højreklik på begge lag, vælg Properties og se i General-tabben, at de to lag har forskellige CRS (Notér også gimpdems EPSG-kode). QGIS reprojicerer således et af de to lag on the fly, således at de kan overlejres. For at undgå ovennævnte transformationsfejl sættes både projektets og Attu-rasterens CRS til det ovenfor oprettede ```UTM22N WGS84 Engsager Extended```. Lagets CRS sættes ved at højreklikke på laget og vælge "Set layer CRS". Projektets kan bla sættes ved at klikke Project -> Prject Properties.

Først transformeres gimpdem til UTM22. Klik Raster -> Projections -> Warp. Vælg gimpdem som input og vælg et passende outputnavn eks "gimpdem_utm22.tif". Source CRS sættes til gimpdems EPSG-kode. I Target CRS vælges UTM22 med Engsager Extended. Resampling method vælges Bilinear. Klik Ok. Det burde tage under et minut.

Nu ønsker vi at klippe et passende område omkring Attu ud af gimpdem_utm22. Feks 389500,7536300 : 393600,7539200. Derudover resampler vi til 1m opløsning. I Processing Toolbox aktiveres algoritmen "r.resamp.interp". Som input vælges gimpdem_utm22. Interpolation method sættes til bilinear. GRASS region extent sættes til "389500,393600,7536300,7539200" og Cellsize sættes til 1.0. Vælg et passende output navn eksempelvis "gimpdem_utm22_attu.tif". Kør algoritmen. Det burde tage under et minut.

Kig på data.

Nu har vi to DEMs fra Attu-området. Attu_by_interpoleret fra byområdet og gimpdem_utm22_attu i det åbne land. Begge er i UTM22 og har 1m opløsning.

Der er flere metoder til at kombinere de to rastere. Her bruger vi en såkaldt VRT-fil (Virtual Raster). Sørg for at kun de to ønskede rastere er indlæst og sørg for at Attu_by_interpoleret ligger neders i lagkontrollen. Klik Raster -> Miscellaneous -> Build Virtual Raster (Catalog). Markér "Use visible raster layers for input", vælg en passende output fil. Klik Ok. Dette tager under et sekund.

Kig på output filen med en texteditor. QGIS opfatter denne fil som en raster på lige fod med alle andre rastere. Prøv feks at indlæse filen i QGIS.

TIP: VRT-filer er et ekstremt kraftfuldt værktøj til rasterhåndtering.

OBS: Prøv at trække gimp-DEM fra Attu-by-DEM. Kig på differensrasteren under Properties -> Metadata ses det, at fifferensen gennemsnitligt er ca 25m. Er der tale om et egentligt offset, er det nemt fixet med Raster Calculator. Prøv det eventuelt.

Analyser på Attu data
------------------------------------
Prøv eventuelt at udføre analyser på den kombinerede DEM.

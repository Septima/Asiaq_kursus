
Processing modeller
 - Byg flere
 - Hvor gemmes?
 - Udveksle
 - Save as python script
 - Batch afvikling

Processing scripts

Python console

Brugerdef funktioner som er tilgængelige i expression builder

Plugin builder



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












SKRALD
----------------------
userfunctions.getlogin.func(None, None, None)
#Eksportér til video fil


# Formål
Deltageren prøver at eksportere visaliseringen til .avi video format.

1.Installér Mplayer
MAC: brew install mplayer

WIN
http://oss.netfarm.it/mplayer-win32.php/

2. Klik på "Export Video" og vælg en placering for videofilen. Vent til TimeManager er helt færdig.
3. I kommandopromten navigeres hen til der, hvor filerne er placeret.
4. Indtast denne kommando:
mencoder "mf://*.PNG" -mf fps=10 -o output.avi -ovc lavc -lavcopts vcodec=mpeg4


Når kommandoen er færdig åbnes output.avi i din videoafspiller f.eks. VLC Player

Note: MPlayer er gratis. Der findes formentlig mange værktøjer til dette formål.
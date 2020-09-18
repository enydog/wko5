import math
from numpy import log as ln


awc=8000
MAP=420
Pmax =470
tte=1853
cp=270
slope=198
seg = 0
frc=0


tau = awc/Pmax #Pmax constante
#Peronnet Thibault:
#slope = slope de la MAP
if seg <= tte :
 Pdc = awc / seg * (1-math.exp(-seg/tau)) + MAP * (1-math.exp(-seg/tau))
else: 
 Pdc = awc / seg * (1-math.exp(-seg/tau)) + MAP * (1-math.exp(-seg/tau)) – slope*ln(seg/tte)

#slope = slope de la MAP
#Tmap es la duraccion maxima que la MAP se puede aguantar.

Pmax=497     #pmax(meanmax(power)) 
frc=8000     #awc:=athleterange(date-89, date, frc(meanmax(power))),
FTP=270      #ftp:=athleterange(date-89, date, ftp(meanmax(power))),
tau=frc/Pmax #Pmax variable de WKO5

#wko5 estimation
if (seg <=tte):
  pdc = frc / seg * (1-math.exp(-seg/tau)) + FTP * (1-math.exp(-seg/tau))
else:  
  pdc = frc / seg * (1-math.exp(-seg/tau)) + FTP * (1-math.exp(-seg/tau)) – slope*ln(seg/slope*ln(seg/tte))


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import aseegg as ag

dane= pd.read_csv('C:/Users/Oliwier/Desktop/data.csv')

df = pd.DataFrame(dane)
df.columns = ['kol1','kol2','kol3','kol4','kol5','kol6']
syg = dane['kol2']


filtr1=ag.pasmowozaporowy(df['kol2'], 200, 49, 51)

filtr2=ag.pasmowoprzepustowy(filtr1, 200, 1, 50)

t = np.linspace(0, syg.size/200, syg.size)

plt.subplot(2, 1, 1)
plt.plot(t, syg)
plt.xlabel('czas [s]')
plt.ylabel('amplituda [μV]')
plt.title('Wykres przed filtracją')
plt.subplot(2, 1, 2)
plt.tight_layout()
plt.xlabel('czas [s]')
plt.ylabel('amplituda [μV]')
plt.title('Wykres po filtracji filtrem pasmowo-zaporowym i pasmowo-przepustowym')
plt.plot(t,filtr2)
plt.show()


numery=[]

ogr = 1

for i in range(len(df)):
	if df['kol2'][i] > ogr:
		numery.append(df['kol6'][i])
		
print ('Osoba badana „wymrugała” w pięciu seriach kod :',set(numery))

import csv, os, runtime
from fuzzywuzzy import fuzz

starttime=runtime.starttime()
# os.chdir('C:\\Users\\caspe\\OneDrive\\Prog\\Aksje prosjekt\\WIP')
cwd = os.getcwd()

header = ['År','Antall','Type']
print(cwd)

# Vurder at lave et sjekk om fil eksistere

new=[]
count = 0
newlst=[]
lst=[]
# Definer funksjon til å s skrive til den nye liste

with open('ansatte.csv', 'r', newline='', encoding= 'utf-8-sig') as ansat_lst, open('scrape_lst.csv', 'r', newline='', encoding= 'utf-8-sig') as scrape_lst:
    ansat_lst = csv.reader(ansat_lst)
    scrape_lst = csv.reader(scrape_lst) 
    ansat_lst = list(ansat_lst)
    scrape_lst = list(scrape_lst)
    
    for ansat in ansat_lst:
        name = str(ansat[1]+' '+ansat[2]).upper()
        
        
        for scrape in scrape_lst:
            comp = fuzz.token_sort_ratio(scrape[0], name)
            if scrape[0] == '':
                continue
            if comp == 100:
                new.extend(ansat)
                new.extend(scrape[4:6])
                # Sjekk for a eller b aksje
                checknumb= int(scrape[5])
                quot,rem=divmod(int(checknumb),10)
                if checknumb > 412:
                    new.append('A')
                elif checknumb<410 and rem==0:
                    new.append('A')
                else:
                    new.append('B')
            
            elif 78 < comp < 100 :
                x = scrape[0]
                x = x.split()
                y = name.split()
                lenght = min(len(x),len(y))
                namecount = 0
                for n in range(lenght):
                    if x[n].upper() in y[n].upper():
                        namecount += 1
                    if namecount/lenght == 1:
                        # print('Der er et match yeahh!!! Navnet er: ',scrape[0], ' ; ', name,'%.1f' % comp,'\\n')
                        new.extend(ansat)
                        new.extend(scrape[4:6])
                        # Sjekk for a eller b aksje
                        if scrape[5] !=None:
                            new.append('B')
                        
with open('resultat_long.csv', 'w', newline ='', encoding='utf-8-sig') as fhand:    
    f= csv.writer(fhand)   
    header=['Ansattnr','Etternavn','Fornavn','E-Post','Avdeling','Gruppe','Kontor','Inntektskategori','Utdannet år','Stillingsprosent','Type','Startet','Sluttet','Tjenestetid', 'År','Antal','Type aksje']
    header.reverse()
    for i in header:
        new.insert(0,i)
    for i in range(0,len(new),17):            
        f.writerow(new[i:i+17])
         
stoptime = runtime.stoptime(starttime) 

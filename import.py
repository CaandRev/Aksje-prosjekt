import csv, os, runtime
# from bs4.element import ProcessingInstruction
from fuzzywuzzy import fuzz
# from fuzzywuzzy import process

starttime=runtime.starttime()
cwd = os.getcwd()

# thisyear=datetime.datetime.now().year
# years=range(2015,thisyear+1,1)
header = ['År','Antall']
print(cwd)

# Vurder at lave et sjekk om fil eksistere

names = []
employes = []
newans=[]
count = 0
compcount = 0
con=1
newlst=[]
lst=[]
# Definer funksjon til å s skrive til den nye liste

with open('ansatte.csv', 'r', newline='', encoding= 'utf-8-sig') as ansatt_lst, open('scrape_lst.csv', 'r', newline='', encoding= 'utf-8-sig') as scrape_lst:
    ansatt_lst = csv.reader(ansatt_lst)
    scrape_lst = csv.reader(scrape_lst) 
    ansatt_lst = list(ansatt_lst)
    scrape_lst = list(scrape_lst)
    
    for writes in ansatt_lst:
        name = str(writes[1]+' '+writes[2]).upper()
        
        for reads in scrape_lst:
            comp = fuzz.token_sort_ratio(reads[0], name)
            if reads[0] == '':
                continue
            if comp == 100:
                # print('Der er et match yeahh!!! Navnet er: ',reads[0], ' ; ', name,'%.1f' % comp,'\n')
                newans.append(writes)
                newans[count].extend(reads[4:6])
                newname = name = str(writes[1]+' '+writes[2]).upper()
                count += 1
            elif 78 < comp < 100 :
                x = reads[0]
                x = x.split()
                y = name.split()
                lenght = min(len(x),len(y))
                namecount = 0
                for n in range(lenght):
                    
                    if x[n].upper() in y[n].upper():
                        namecount = namecount + 1
                    if namecount/lenght == 1:
                        # print('Der er et match yeahh!!! Navnet er: ',reads[0], ' ; ', name,'%.1f' % comp,'\n')
                        newans.append(writes)
                        newans[count].extend(reads[4:6])
                        newname = name = str(writes[1]+' '+writes[2]).upper()
                        count+=1


with open('newfile.csv', 'w', newline ='', encoding='utf-8-sig') as fhand:    
    f= csv.writer(fhand)
   
    newlst=[['Ansattnr','Etternavn','Fornavn','E-Post','Avdeling','Gruppe','Kontor','Inntektskategori','Utdannet år','Stillingsprosent','Type','Startet','Sluttet','Tjenestetid', header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1],header[0],header[1]]]
    for i in newans:            
        if i not in newlst:
            newlst.append(i)
    
    f.writerows(newlst)

with open('newfile.csv', 'r', newline='', encoding='utf-8-sig') as f:
    count = 0
    fhand = csv.reader(f)
    for i in fhand:
        count+=1
        lenght=len(i)
            
        if lenght < 42:
            item = i[14:lenght+1]
            del i[14:lenght+1]
            for j in range(42-lenght):
                i.append('N/A')
            for j in item:
                i.append(j)
            lst.append(i)
            # print(i,len(i))
        else:
            lst.append(i)
       
with open('resultat.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fhand = csv.writer(f)   
    fhand.writerows(lst)
delpath = cwd+'\\newfile.csv'
os.remove(delpath)
stoptime = runtime.stoptime(starttime) 

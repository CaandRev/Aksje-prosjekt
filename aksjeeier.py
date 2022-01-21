#Import libraries
import urllib.request, urllib.parse, ssl
from bs4 import BeautifulSoup
import datetime,csv, os.path

# Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#Definitions
baseurl="https://www.aksjeeiere.no/"
url = "https://www.aksjeeiere.no/?utf8=%E2%9C%93&year=2014&q=Norconsult+holding+AS"
htmllst=[]
thisyear=datetime.datetime.now().year
years=range(2015,thisyear+1,1)
count=0

# Promter bruker for filnavn og undersøker om den eksistere og giver mulighed for å stoppe
filename = input('Indtast file navn du ønsker på resultatfilen: ')
if os.path.isfile(filename + '.csv'): 
    owrite = input('Ønsker du at overskrive filen[Y/n]?')
    if owrite.upper() == 'N':
        print('vi stopper her')
        quit()
    elif len(owrite) < 1:
        quit()
    else: 
        print('forsetter...')
    
    
# Gets the date from the webpage
for year in years:
    while True:
    # while count < 2:

        html= urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all("td")

        for tag in tags:
        ##        print(tag.get_text())
            htmllst.append(tag.get_text())

        nexttag = soup.find(rel="next")

        if nexttag is None:
            break

        url = baseurl + nexttag.get("href", None)
        print(baseurl + nexttag.get("href", None))
        count = count + 1
    url = "https://www.aksjeeiere.no/?utf8=%E2%9C%93&year=" + str(year) + "&q=Norconsult+holding+AS"

#Prints list to csv in chunks
with open(filename + '.csv', "w", newline ='', encoding='utf-8-sig') as fhand:
    writer = csv.writer(fhand)
    for i in range(0,len(htmllst),7):
        writer.writerow(htmllst[i:i+7])
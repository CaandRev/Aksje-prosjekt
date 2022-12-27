import csv

def get_name_lst(file):
    name_lst = []
    with open(str(file), newline='', encoding='utf-8-sig') as names:
        names = csv.DictReader(names)

        for i in names:
            if i['Ansattnr'] not in name_lst:
                name_lst.append(i['Ansattnr'])
            else:
                continue
    return name_lst


x = get_name_lst('resultat_long.csv')
print(x)
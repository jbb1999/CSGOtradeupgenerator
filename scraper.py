import requests
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "csgotradeup"
)
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()

types=["consumer grade","industrial grade","mil-spec","restricted","classified","covert"]
temp_id=1435
url_main=f"https://csgostash.com/skin/"

def extract(html, ids, quality_term, case_type):
    html = html.split('\n')
    temp = 2
    if 'StatTrak' in html[1] or 'StatTrak' in html[2]:
        stattrak = True
        temp = 3
    else:
        stattrak = False
    wear = html[temp].replace('<span class="pull-left">','').replace('</span>','').replace('<span class="pull-left price-details-st">','')
    price = html[temp+1].replace('<span class="pull-right">','').replace('</span>','').replace('<span class="pull-left">','').replace('£','').replace('$','')
    if price == "No Recent Price":
        price=0000
    else:
        price = price[3:].strip()
        price = price.replace(",",".")
    if stattrak == False and wear == "Factory New":
        if quality_term != None:
            if quality_term == "classified":
                print(f"{ids}:{quality_term}:{case_type}:{wear}:{price}")
                mycursor.execute("INSERT INTO classified(ID, SKIN_ID, QUALITY, PRICE, COLLECTION) VALUES (%s, %s, %s, %s, %s)", (None, int(ids), str(quality_term), str(price), str(case_type)))
                mydb.commit()
            elif quality_term == "consumer":
                print(f"{ids}:{quality_term}:{case_type}:{wear}:{price}")
                mycursor.execute("INSERT INTO consumer(ID, SKIN_ID, QUALITY, PRICE, COLLECTION) VALUES (%s, %s, %s, %s, %s)", (None, int(ids), str(quality_term), str(price), str(case_type)))
                mydb.commit()
            elif quality_term == "covert":
                print(f"{ids}:{quality_term}:{case_type}:{wear}:{price}")
                mycursor.execute("INSERT INTO covert(ID, SKIN_ID, QUALITY, PRICE, COLLECTION) VALUES (%s, %s, %s, %s, %s)", (None, int(ids), str(quality_term), str(price), str(case_type)))
                mydb.commit()
            elif quality_term == "industrial":
                print(f"{ids}:{quality_term}:{case_type}:{wear}:{price}")
                mycursor.execute("INSERT INTO industrial(ID, SKIN_ID, QUALITY, PRICE, COLLECTION) VALUES (%s, %s, %s, %s, %s)", (None, int(ids), str(quality_term), str(price), str(case_type)))
                mydb.commit()
            elif quality_term == "milspec":
                print(f"{ids}:{quality_term}:{case_type}:{wear}:{price}")
                mycursor.execute("INSERT INTO milspec(ID, SKIN_ID, QUALITY, PRICE, COLLECTION) VALUES (%s, %s, %s, %s, %s)", (None, int(ids), str(quality_term), str(price), str(case_type)))
                mydb.commit()
            elif quality_term == "restricted":
                print(f"{ids}:{quality_term}:{case_type}:{wear}:{price}")
                mycursor.execute("INSERT INTO restricted(ID, SKIN_ID, QUALITY, PRICE, COLLECTION) VALUES (%s, %s, %s, %s, %s)", (None, int(ids), str(quality_term), str(price), str(case_type)))
                mydb.commit()
            else:
                mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(f"quality term is not matched by any on libary {quality_term}")))
                mydb.commit()

        else:
            pass
    else:
        return
    return [stattrak,wear,price]
def check_type(types, line):
    for type in types:
        if type.lower() in line.lower():
            print(line[:-2])


def csgostash(ids):
    prices = []
    response = requests.get(f"https://csgostash.com/skin/{ids}")
    quality = response.text.split('<div class="quality color-')
    case_thingy = response.text.split('<p class="collection-text-label">The ')
#    print(response.text)
    try:
        case_thingy = case_thingy[1].split('\n')[0]
        if "collection" in case_thingy or "Collection" in case_thingy:
            case_thingy=case_thingy[:case_thingy.index("Collection")+10]
#            print(case_thingy)

    except Exception as error:
        try:
            mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(error)))
            mydb.commit()
        except:
            pass

    try:
        lines=quality[1].split('\n')
    except Exception as error:
        try:
            mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(error)))
            mydb.commit()
        except:
            pass
    quality_term=None
    try:
        for line in lines:
            line=line.lower()
            if "classified" == line[:-2] or "restricted" == line[:-2] or "milspec" == line[:-2] or "industrial" == line[:-2] or "consumer" == line[:-2] or "covert" == line[:-2]:
                quality_term=line[:-2]
        r = response.text.split('<div class="btn-group-sm btn-group-justified">')
    except Exception as error:
        try:
            print(error)
            mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(error)))
            mydb.commit()
        except:
            pass
    try:
        if '<span class="pull-left price-details-st">StatTrak</span>' in r[2].split('\n'):
            for i in range(2,2+10):
                try:
                    values = r[i].split('</a>')[0]
                except Exception as error:
                    print(error)
                    try:
                        mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)",(int(ids), str(error)))
                        mydb.commit()
                    except:
                        pass
                prices.append(extract(values, ids, quality_term, case_thingy))
        else:
            for i in range(2,2+5):
                try:
                    values = r[i].split('</a>')[0]
                except Exception as error:
                    print(error)
                    try:
                        mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)",(int(ids), str(error)))
                        mydb.commit()
                    except:
                        pass
                prices.append(extract(values, ids, quality_term, case_thingy))
    except Exception as error:
        try:
            print(error)
            mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(error)))
            mydb.commit()
        except:
            pass




csgostash(temp_id)

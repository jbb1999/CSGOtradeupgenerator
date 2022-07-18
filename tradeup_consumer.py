import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "csgotradeup"
)
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
def str_float(price_str):
  if " " in price_str:
    price_list = (price_str.split())
    price = price_list[0] + price_list[1]
    price = (float(price))
    return price
  else:
    price = (float(price_str))
    return price
temp1 = 1
def collection_outcome(collection_1,collection_2,collection_3,collection_4,collection_5, current):
  price_profitability_temp = None
  price_sum_temp = None
  sql = "SELECT * FROM industrial WHERE COLLECTION = %s"
  collection = collection_1[0][4],
  mycursor.execute(sql, collection)
  collection_1_outcome = mycursor.fetchall()
  sql = "SELECT * FROM industrial WHERE COLLECTION = %s"
  collection = collection_2[0][4],
  mycursor.execute(sql, collection)
  collection_2_outcome = mycursor.fetchall()
  sql = "SELECT * FROM industrial WHERE COLLECTION = %s"
  collection = collection_3[0][4],
  mycursor.execute(sql, collection)
  collection_3_outcome = mycursor.fetchall()
  sql = "SELECT * FROM industrial WHERE COLLECTION = %s"
  collection = collection_4[0][4],
  mycursor.execute(sql, collection)
  collection_4_outcome = mycursor.fetchall()
  sql = "SELECT * FROM industrial WHERE COLLECTION = %s"
  collection = collection_5[0][4],
  mycursor.execute(sql, collection)
  collection_5_outcome = mycursor.fetchall()
#  print(collection_1_outcome,"\n",collection_2_outcome,"\n",collection_3_outcome,"\n",collection_4_outcome,"\n",collection_5_outcome,"\n")
  try:
    prices = [collection_1_outcome[0][3], collection_2_outcome[0][3], collection_3_outcome[0][3],
              collection_4_outcome[0][3], collection_5_outcome[0][3]]
    prices_list = []
    for price in prices:
      if price != "Possible" or 0:
        prices_list.append(str_float(price) * 2)
      else:
        prices.remove(price)
    prices_ingrediantes = [collection_1[0][3], collection_2[0][3], collection_3[0][3], collection_4[0][3],
                           collection_5[0][3]]
    #    print("test2")
    #    print(prices_ingrediantes, "\n")
    #    print(collection_1,"\n", collection_2,"\n", collection_3,"\n", collection_4,"\n",collection_5)
    prices_ingrediants_list = []
    for price in prices_ingrediantes:
      if price != "Possible" or 0:
        prices_ingrediants_list.append(str_float(price) * 2)
      else:
        if price in prices:
          prices.remove(price)
        else:
          pass
    prices_ingrediants_list_sum = sum(prices_ingrediants_list)
    price_sum = sum(prices_list) / 10
    if price_sum != 0:
      price_sum_temp = price_sum
      #      print(price_sum)
      price_profitability_temp = price_sum / int(prices_ingrediants_list_sum)
    else:
      #      print("no recent prices on any items\n")
      pass
    print(current)
  except Exception as error:
    try:
      mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(error)))
      mydb.commit()
    except:
      pass
  try:
    if price_profitability_temp > 0.6:
      if collection_1[0][3] != "Possible" and collection_2[0][3] != "Possible" and collection_3[0][3] != "Possible" and collection_4[0][3] != "Possible" and collection_5[0][3] != "Possible":
        mycursor.execute(
          "INSERT INTO tradeup (profitability, cost_ingredient, cost_resault, skin_id_1, skin_cost_1, skin_id_2, skin_cost_2, skin_id_3, skin_cost_3, skin_id_4, skin_cost_4, skin_id_5, skin_cost_5, from_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
          (price_profitability_temp, prices_ingrediants_list_sum, price_sum_temp, collection_1[0][1], collection_1[0][3],
           collection_2[0][1], collection_2[0][3],
           collection_3[0][1], collection_3[0][3], collection_4[0][1], collection_4[0][3], collection_5[0][1],
           collection_5[0][3], "consumer-industrial"))
        mydb.commit()
      else:
        pass
  except Exception as error:
    try:
      mycursor.execute("INSERT INTO error (ID, ERROR) VALUES (%s, %s)", (int(ids), str(error)))
      mydb.commit()
    except:
      pass



sql = "SELECT ID FROM consumer ORDER BY ID DESC LIMIT 1;"
mycursor.execute(sql)
amount_of_data = mycursor.fetchall()
amount_of_data = amount_of_data[0][0]


def tradeup_consumer():
  for i in range(1,amount_of_data+1):
    for o in range(1,amount_of_data+1):
      for p in range(1,amount_of_data+1):
        for a in range(1,amount_of_data+1):
          for s in range(1,amount_of_data+1):
            sql="SELECT * FROM consumer WHERE ID = %s"
            id=i,
            mycursor.execute(sql, id)
            item_1 = mycursor.fetchall()
            sql = "SELECT * FROM consumer WHERE ID = %s"
            id=o,
            mycursor.execute(sql, id)
            item_2 = mycursor.fetchall()
            sql = "SELECT * FROM consumer WHERE ID = %s"
            id=p,
            mycursor.execute(sql, id)
            item_3 = mycursor.fetchall()
            sql = "SELECT * FROM consumer WHERE ID = %s"
            id=a,
            mycursor.execute(sql, id)
            item_4 = mycursor.fetchall()
            sql = "SELECT * FROM consumer WHERE ID = %s"
            id=s,
            mycursor.execute(sql, id)
            item_5 = mycursor.fetchall()
            collection = [item_1[0][4],item_2[0][4],item_3[0][4],item_4[0][4],item_5[0][4]]
            prices = [item_1[0][3],item_2[0][3],item_3[0][3],item_4[0][3],item_5[0][3]]
            prices_list = []
            for price in prices:
              if price != "Possible":
                 prices_list.append(str_float(price)*2)
              else:
                prices.remove(price)
            price_sum=sum(prices_list)
            current = f"{i}-{o}-{p}-{a}-{s}"
            collection_outcome(item_1,item_2,item_3,item_4,item_5, current)







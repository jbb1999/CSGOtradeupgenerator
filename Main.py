from scraper import extract, csgostash
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "csgotradeup"
)
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()




temp1=int(input("What do you wish to do. \n1. run scraper \n2. run scraper and clear database\n3. check database for profitability trade up.\n"))
temp2=None
if temp1 == 1:
    for i in range(100, 1534):
        csgostash(i)
elif temp1 == 2:
    temp2=int(input("are you sure you want to clear the database. This can crash your pc and is ireversable. 1 for reset. 0 for ignore"))
    if temp2 == 1:
        mycursor.execute("DELETE FROM `classified`")
        mycursor.execute("ALTER TABLE classified AUTO_INCREMENT = 1")
        mycursor.execute("DELETE FROM `consumer`")
        mycursor.execute("ALTER TABLE consumer AUTO_INCREMENT = 1")
        mycursor.execute("DELETE FROM `covert`")
        mycursor.execute("ALTER TABLE covert AUTO_INCREMENT = 1")
        mycursor.execute("DELETE FROM `industrial`")
        mycursor.execute("ALTER TABLE industrial AUTO_INCREMENT = 1")
        mycursor.execute("DELETE FROM `milspec`")
        mycursor.execute("ALTER TABLE milspec AUTO_INCREMENT = 1")
        mycursor.execute("DELETE FROM `restricted`")
        mycursor.execute("ALTER TABLE restricted AUTO_INCREMENT = 1")
        mycursor.execute("DELETE FROM `tradeup`")
        mydb.commit()
        for i in range(100, 1534):
            csgostash(i)
    else:
        print("reset canceled")
elif temp1 == 3:
    sql = "select profitability,cost_ingredient,cost_resault,skin_id_1,skin_id_2,skin_id_3,skin_id_4,skin_id_5,from_to from tradeup order by profitability desc limit 1,10;"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    for i in data:
        print(i)





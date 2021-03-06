from scraper import extract, csgostash
from functions import database_size, name_scraper
from tradeup_consumer import tradeup_consumer
from tradeup_industrial import tradeup_industrial
from tradeup_classified import tradeup_classified
from tradeup_restricted import tradeup_restricted
import mysql.connector
import time
from threading import Thread
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "csgotradeup"
)
mycursor = mydb.cursor()



temp1=int(input("What do you wish to do. \n1. run scraper \n2. run scraper and clear database\n3. check database for profitability trade up.\n4. check database total size.\n5. check database total size and display sperate table size.\n6. run trade up bots.\n"))
temp2=None
if temp1 == 1:
    for i in range(100, 1534):
        csgostash(i)
elif temp1 == 2:
    temp3=int(input("DO you wish to delete(makes a log but can crash and generates log files for every single deleted row, for tradeup table this can cause the database to time out. Recomend trucate. 0 delete, 1 trucate.\n"))
    if temp3==0:
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
    else:
        temp2 = int(input("are you sure you want to clear the database. This is ireversable. 1 for reset. 0 for ignore"))
        if temp2 == 1:
            mycursor.execute("TRUNCATE TABLE classified")
            mycursor.execute("ALTER TABLE classified AUTO_INCREMENT = 1")
            mycursor.execute("TRUNCATE TABLE consumer")
            mycursor.execute("ALTER TABLE consumer AUTO_INCREMENT = 1")
            mycursor.execute("TRUNCATE TABLE covert")
            mycursor.execute("ALTER TABLE covert AUTO_INCREMENT = 1")
            mycursor.execute("TRUNCATE TABLE industrial")
            mycursor.execute("ALTER TABLE industrial AUTO_INCREMENT = 1")
            mycursor.execute("TRUNCATE TABLE milspec")
            mycursor.execute("ALTER TABLE milspec AUTO_INCREMENT = 1")
            mycursor.execute("TRUNCATE TABLE restricted")
            mycursor.execute("ALTER TABLE restricted AUTO_INCREMENT = 1")
            mycursor.execute("TRUNCATE TABLE tradeup")
            mydb.commit()
        else:
            pass



elif temp1 == 3:
    sql = "select profitability,cost_ingredient,cost_resault,skin_id_1,skin_id_2,skin_id_3,skin_id_4,skin_id_5,from_to from tradeup order by profitability desc limit 1,10;"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print("NOTE: These resaults can be wrong and its recomended to always double check them with a site such as csgofloat.")
    print("DATA is sorted by PROFITABILITY, Cost, Resault, skin id 1, skin id 2, skin id 3, skin id 4, skin id 5, and from-to")
    time.sleep(5)
    for i in data:
        print(i)
        print(name_scraper(i[3]))
        print(name_scraper(i[4]))
        print(name_scraper(i[5]))
        print(name_scraper(i[6]))
        print(name_scraper(i[7]))





elif temp1 == 4:
    database_size_total_1, unused = database_size("csgotradeup", "tradeup")
    database_size_total_2, unused = database_size("csgotradeup", "classified")
    database_size_total_3, unused = database_size("csgotradeup", "consumer")
    database_size_total_4, unused = database_size("csgotradeup", "covert")
    database_size_total_5, unused = database_size("csgotradeup", "error")
    database_size_total_6, unused = database_size("csgotradeup", "industrial")
    database_size_total_7, unused = database_size("csgotradeup", "milspec")
    database_size_total_8, unused = database_size("csgotradeup", "restricted")
    database_size_total = database_size_total_1 + database_size_total_2 + database_size_total_3 + database_size_total_4 + database_size_total_5 + database_size_total_6 + database_size_total_7 + database_size_total_8
    print(database_size_total)
elif temp1 == 5:
    database_size_total_1, print_command_1 = database_size("csgotradeup", "tradeup")
    for item in print_command_1:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_2, print_command_2 = database_size("csgotradeup", "classified")
    for item in print_command_2:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_3, print_command_3 = database_size("csgotradeup", "consumer")
    for item in print_command_3:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_4, print_command_4 = database_size("csgotradeup", "covert")
    for item in print_command_4:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_5, print_command_5 = database_size("csgotradeup", "error")
    for item in print_command_5:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_6, print_command_6 = database_size("csgotradeup", "industrial")
    for item in print_command_6:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_7, print_command_7 = database_size("csgotradeup", "milspec")
    for item in print_command_7:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total_8, print_command_8 = database_size("csgotradeup", "restricted")
    for item in print_command_8:
        print(item[0], "Size in MB: ", item[-1])
    database_size_total = database_size_total_1 + database_size_total_2 + database_size_total_3 + database_size_total_4 + database_size_total_5 + database_size_total_6 + database_size_total_7 + database_size_total_8
    print(f"Total database size MB: {database_size_total}")
elif temp1 == 6:
    thread1 = Thread(target=tradeup_consumer)
    thread1.start()
    thread2 = Thread(target=tradeup_industrial)
    thread2.start()
    thread3 = Thread(target=tradeup_classified)
    thread3.start()
    thread4 = Thread(target=tradeup_restricted)
    thread4.start()














CSGO trade up generator/CSGO TUG
====

CSGO trade up generator is a generator that generates all possible trade ups and deems their profitability. It uses a data scraper to first make a db list, then start generating.



Installation
------------

CSGO TUG requires Python 3.6 or newer.

Use pip:

``pip install requests``
``pip install mysql.connector``


CSGO TUG relies on a database to function. You can setup a mysql database on a server, or use mysql with something like xampp. I recomend xampp as its easy to setup and doesnt reqire anything special and will work out of the box.


Basic Usage
-----------
1. Import the .sql file into mysql.
2. run main.py and run the data scraper (press 1)
3. wait for it to finish
4. run trade up by pressing 6
5. after a while you can run main.py and check profitability by pressing 3
ALSO note that this code is inspired by similar projects and might contain ways of doing things similar to other projects.



Support
-------

If you need support for CSGO TUG, contact me on discord. Jbb#0001



Features
--------

CSGO TUG supports the following features:
 - price and skin scraping
 - trade up generation
 - profitability caulculator
 - datbase logging for both skins and trade ups
 - database size checker
 - multi threading(sort of)
 - db structure file.

Features to come
--------

I am working on these atm and may come down the line.
 - excel sheet alternative to DB
 - web UI
 - price limiter
Note that i have no eta for these and might not add them at all.

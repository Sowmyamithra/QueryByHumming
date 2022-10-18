# creating a database of songs

import psycopg2;                               # import psycopg2 library

conn = psycopg2.connect(database="Songs", user='postgres', password='123456', host='127.0.0.1', port= '5432');          # establishing the connection
conn.autocommit = True;
cursor = conn.cursor();                        # Creating a cursor object using the cursor() method
#sql = '''CREATE database Songs''';            # Preparing query to create a database
#cursor.execute(sql);                          # Creating a database
#print("Database created successfully........");
cursor.execute("DROP TABLE IF EXISTS SONGS");  # drop the table if it already exists
q1 = '''CREATE TABLE SONGS(
   SONG_NAME VARCHAR(40),
   SINGERS VARCHAR(40),
   MOVIE VARCHAR(40),
   YEAR INTEGER,
   PATH VARCHAR(50),
   PRIMARY KEY(SONG_NAME))''';
cursor.execute(q1);
# insertng data
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES('JabilliKosam' , 'S. P. Balasubrahmanyam' , 'Manchi Manasulu' , 1992 , 'Original_Songs\JabilliKosam.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('JaamuRathiri' , 'S. P. Balasubrahmanyam;K. S. Chitra' , 'Kshana Kshanam' , 1991 , 'Original_Songs\JaamuRathiri.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('MaateManthramu' , 'S. P. Balasubrahmanyam;S. P. Shailaja' , 'Seethakoka Chiluka' , 1982 , 'Original_Songs\MaateManthramu.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('NaaCheliRojave' , 'S. P. Balasubrahmanyam;Sujatha' , 'Roja' , 1992 , 'Original_Songs\NaaCheliRojave.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('Kannanule' , 'K. S. Chitra' , 'Bombay' , 1995 , 'Original_Songs\Kannanule.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('Nuvvadiginadhe' , 'Anirudh Ravichander' , 'Jersey' , 2019 , 'Original_Songs\Nuvvadiginadhe.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('TharaganiBaruvaina' , 'Ananya Bhat' , 'KGF Chapter 1' , 2018 , 'Original_Songs\TharaganiBaruvaina.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('Gunjukunna' , 'Shaktisree Gopalan' , 'Kadali' , 2013 , 'Original_Songs\Gunjukunna.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('AakasamYenatido' , 'S. Janaki' , 'Nireekshana' , 1982 , 'Original_Songs\AakasamYenatido.mp3')''');
cursor.execute('''INSERT INTO SONGS(SONG_NAME , SINGERS , MOVIE , YEAR , PATH) VALUES ('Mandaara' , 'Shreya Ghoshal' , 'Bhagamathi' , 2018 , 'Original_Songs\Mandaara.mp3')''');
conn.commit();                                # Commit your changes in the database
print("Table created and data inserted successfully........");
conn.close();                                 # Closing the connection
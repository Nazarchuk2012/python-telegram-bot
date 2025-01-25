import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()


# cur.execute("CREATE TABLE user(name, year, title)")


#cur.execute('''CREATE TABLE example1(
#        id INTEGER PRIMARY KEY,
#        name TEXT DEFAULT 'user',
#        age INTEGER DEFAULT 0,
#        title TEXT NOT NULL
#     );''')

#cur.execute('''INSERT INTO user (name, yar, title)
#    VALUES ('Назар', '2092', 'Учень 90а класу')
#    ;''')

#for i in range(100):
#    cur.execute('''INSERT INTO user (name, yar, title)
#            VALUES (?, ?, ?)
#        ''',('Назар', i, f'212312 {i}'))
#    con.commit()

cur.execute("UPDATE user SET name='Тарас' WHERE yar=0;")
con.commit()


con.close()


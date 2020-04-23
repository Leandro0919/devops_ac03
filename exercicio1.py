import sqlite3
conn = sqlite3.connect('exercicio1.db')

c = conn.cursor()

c.execute('''CREATE TABLE exercicio1(
                id integer,
                nome text not null,
                email text)'''
                )

c.execute("INSERT INTO exercicio1 VALUES (1,'Leandro','leandro@123.com')")

conn.commit()

conn.close()
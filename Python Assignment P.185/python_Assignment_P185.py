import os
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS find_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")
conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
        
with conn:
        cur = conn.cursor()
for file in fileList:
        if file.endswith(".txt"):
                cur.execute("INSERT INTO find_file(file_name) VALUES (?)", (file,))
        conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
        cur = conn.cursor()
        cur.execute("SELECT file_name FROM find_file")
        results = cur.fetchall()
        print(results)

        conn.commit()
conn.close()

 

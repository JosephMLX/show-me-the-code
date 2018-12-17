# written by Joseph Meng 2018
# mlx7.xyz

from generate import generate_promotion_code
import pymysql


code_list = generate_promotion_code(200)

conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='promotion')
cur = conn.cursor()

for index, code in enumerate(code_list):
    cur.execute("INSERT INTO Getcode(code) VALUES (%s)", (code))
    conn.commit()

conn.close()


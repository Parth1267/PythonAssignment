import sqlite3
con = sqlite3.connect('hello.db')
cur = con.cursor()

# cur.execute("CREATE TABLE stud (id INTEGER PRIMARYKEY, name TEXT)")
# print("table created")

# cur.execute("INSERT INTO test (id, name)VALUES(2,'jaydeep')")
# print("data inserted ")
# for row in cur.execute("SELECT * FROM stud "):
#     print(row)

# cur.execute("CREATE TABLE test (id INTEGER PRIMARYKEY, name TEXT)")
# print("table created")

# print('drop')
# cur.execute("DROP TABLE test")

# for row in cur.execute("SELECT * FROM test"):
#     print(row)

con.commit()
con.close()

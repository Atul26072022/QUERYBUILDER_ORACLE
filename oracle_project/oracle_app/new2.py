import cx_Oracle

dict2 = {
    "TableName" : "qqabc",
    "Coloumn" : {
        "a" : "x",
        "b" : "y",
        "c" : "z",
        'd' : 'r',
        'e' : 'q'
    }
}

# print(dict2["Coloumn"].values())

l1 = []
l2 = []
with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
    print("Connected")
    cur=co.cursor()
    # print(cur)
    cur.execute(" SELECT table_name FROM all_tables WHERE owner='C##ABC' ")
    x = cur.fetchall()

    for i in x:
        l1.append(i[0])

    if dict2["TableName"].upper() in l1:
        cur.execute(f"select * from C##ABC.{dict2['TableName']}")
        col_names = [row[0] for row in cur.description]
        print(col_names)
        for i in dict2["Coloumn"].values():
            if i.upper() not in col_names:
                l2.append(i)
        if len(l2) > 0:
            for i in l2:
                cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} ADD {i} VARCHAR2(50)")
            print("Table Altered")
        print("Table and coloumn already created")
    else:
    
        cur.execute(f"CREATE TABLE C##ABC.{dict2['TableName']}(id int NOT NULL)")
        # print(dict2)
        for key in dict2["Coloumn"].values():
            cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} ADD {key} VARCHAR2(50)")
        print("Table Created")
    



    # print(l2)
    # print(len(l2))
                

    # else:
    #     print("NO")     
    # cur.execute(f"CREATE TABLE C##ABC.{dict2['TableName']}(id int NOT NULL)")
    # print(dict2)
    # for key in dict2["Coloumn"].values():
    #     cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} ADD {key} VARCHAR2(50)")
    # print("Table Created")
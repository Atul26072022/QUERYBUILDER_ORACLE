import cx_Oracle

dict2 = {
    "TableName" : "qqabc",
    "Coloumn" : {
        "a" : "x",
        "b" : "y",
        "c" : "z",
        
        'e' : 'ff'
    }
}

# print(dict2["Coloumn"].values())

table_name = []
coloumn_name = []
existing_coloumn_name = []
with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
    print("Connected")
    cur=co.cursor()
    # print(cur)
    cur.execute(" SELECT table_name FROM all_tables WHERE owner='C##ABC' ")
    x = cur.fetchall()

    for i in x:
        table_name.append(i[0])

    if dict2["TableName"].upper() in table_name:
        cur.execute(f"select * from C##ABC.{dict2['TableName']}")
        col_names = [row[0] for row in cur.description]
    
        for i in dict2["Coloumn"].values():
            existing_coloumn_name.append(i.upper())
            if i.upper() not in col_names:
                coloumn_name.append(i)
        if len(coloumn_name) > 0:
            for i in coloumn_name:
                cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} ADD {i} VARCHAR2(50)")
        for i in col_names:
            if i not in existing_coloumn_name:
                if i != 'ID':
                    cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} DROP column {i}")
        print("Table Altered")
        print("Table and coloumn already created")
    else:
    
        cur.execute(f"CREATE TABLE C##ABC.{dict2['TableName']}(id int NOT NULL)")
        # print(dict2)
        for key in dict2["Coloumn"].values():
            cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} ADD {key} VARCHAR2(50)")
        print("Table Created")
    



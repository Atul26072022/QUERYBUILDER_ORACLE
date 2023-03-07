import cx_Oracle

dict1 = {
    "id" : 12,
    "name" : "rahul11",
    "age" : 23
}

l1 = []
try:
    with cx_Oracle.connect('system/1234') as co:
        print("Connected")
        cur = co.cursor()


        cur.execute("SELECT * FROM ORACLE_APP_STUDENT")
        col_names = [row[0] for row in cur.description]
        # print(col_names)
        # print(col_names[0])
        # print(col_names[1])
        # print(col_names[2])
        x = cur.fetchall()

     
        for i in x:

            # print(i[0])
            # print(i[1])
            # print(i[2])
            l1.append({
                col_names[0] : i[0],
                col_names[1] : i[1],
                col_names[2] : i[2]
            })
        cur.close()
        print("DATA FETCHED")
    print(l1)
        
except Exception as e:
    print("Error: ",str(e))

import cx_Oracle

dict1 = {
    "id" : 12,
    "name" : "rahul11",
    "age" : 23
}


try:
    with cx_Oracle.connect('system/1234') as co:
        print("Connected")      
        cur = co.cursor()


        cur.execute("INSERT INTO ORACLE_APP_STUDENT VALUES (:1,:2,:3)",[dict1["id"],dict1["name"],dict1["age"]])
        # cur.execute("INSERT INTO ORACLE_APP_STUDENT VALUES (?,?,?)",(dict1["id"],dict1["name"],dict1["age"]))
        # cur.execute(f"INSERT INTO ORACLE_APP_STUDENT VALUES ({dict1['id']},{dict1['name']},{dict1['age']})")
        # cur.execute('SELECT * FROM ORACLE_APP_STUDENT')
        # x = cur.fetchall()
        # print(x)
        co.commit()
        cur.close()
        print("DATA INSERTED")
    
        
        
        
except Exception as e:
    print("Error: ",str(e))

        
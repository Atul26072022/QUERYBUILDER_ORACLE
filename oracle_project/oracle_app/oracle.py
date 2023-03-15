import cx_Oracle

dict1 = [{
        "id" : 17,
        "name" : "rahulaaa",
        "age" : 23
    },
    {
        "id" : 18,
        "name" : "rahulbbb",
        "age" : 23
    
    }
    ]



try:
    with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
        print("Connected")      
        cur = co.cursor()

        for i in dict1:
            cur.execute("INSERT INTO ORACLE_APP_STUDENT VALUES (:1,:2,:3)",[i["id"],i["name"],i["age"]])
            # cur.execute("INSERT INTO ORACLE_APP_STUDENT VALUES (?,?,?)",(dict1["id"],dict1["name"],dict1["age"]))
            # cur.execute(f"INSERT INTO ORACLE_APP_STUDENT VALUES ({dict1['id']},{dict1['name']},{dict1['age']})")
            # cur.execute('SELECT * FROM ORACLE_APP_STUDENT')
            # x = cur.fetchall()
            # print(x)
        co.commit()
            
        print("DATA INSERTED")
        
            
            
        
except Exception as e:
    print("Error: ",str(e))

            
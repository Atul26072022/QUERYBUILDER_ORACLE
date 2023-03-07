import cx_Oracle
l1 = []
try:
    with cx_Oracle.connect('C##ABC/1234') as co:
        print("Connected")
        cur = co.cursor()


        cur.execute("SELECT table_name FROM user_tables")
        
        x = cur.fetchall()
        for i in range(0,len(x)):
            # print(x[i][0])

            a = "student"
            cur.execute(f"select * from {x[i][0]}")
            col_names = [row[0] for row in cur.description]
            # print(col_names)
            l1.append({
                x[i][0] : col_names
            })
        
        print(l1)
        
        # cur.close()
        print("DATA FETCHED")
        
except Exception as e:
    print("Error: ",str(e))
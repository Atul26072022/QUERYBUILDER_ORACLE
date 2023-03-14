import cx_Oracle
l1 = []
try:
    # with cx_Oracle.connect('C##ABC/abcd@//localhost:1521/XE') as co:
    # with cx_Oracle.connect('C##ABC/abcd') as co:
    with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
    # with cx_Oracle.connect('system/1234') as co:
        print("Connected")
        cur = co.cursor()
        # print(co)



        # cur.execute("SELECT table_name FROM user_tables@TOTESTSYSTEM")
        # cur.execute("SELECT * FROM dba_pdbs")
        cur.execute(" SELECT table_name FROM all_tables WHERE owner='C##ABC' ")
        
        x = cur.fetchall()
        # print(x)
        for i in range(0,len(x)):
            # print(x[i][0])

            # a = "student"
            # cur.execute(f"select * from {x[i][0]}")
            cur.execute(f"select * from C##ABC.{x[i][0]}")
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
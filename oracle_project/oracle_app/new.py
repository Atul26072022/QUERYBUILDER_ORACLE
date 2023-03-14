import cx_Oracle

# def Oracle_connection(self):
#         with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
#             print("Connected")
#             cur = co.cursor()
#             return cur


class Oracleopration:

    
            

    def Oracle_fetch_data(self):
        l1 = []
        try:
            with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
                print("Connected")
                cur = co.cursor()


                cur.execute(" SELECT table_name FROM all_tables WHERE owner='C##ABC' ")
                
                x = cur.fetchall()
                for i in range(0,len(x)):

                    cur.execute(f"select * from C##ABC.{x[i][0]}")
                    col_names = [row[0] for row in cur.description]
                    l1.append({
                        x[i][0] : col_names
                    })
                
                print(l1)

            return ({"Message : Data Fetched successfully"})
                
        except Exception as e:
            print("Error: ",str(e))
            return ({"Message : Data Not Fetched"})
        


    def Oracle_create_table(self,dict2):
        l1 = []
        l2 = []
        try:
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
            
        except Exception as e:
            print("Error: ",str(e))
            return ({"Message : Table not created Something went wrong"})
            

    
        
    
    def Oracle_drop_table(self,table_name):

        try:
            with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
                print("Connected")
                cur = co.cursor()


                cur.execute(f" DROP TABLE C##ABC.{table_name}")
                
            return ({"Message : Table Deleted Successfully"})
                
        except Exception as e:
            print("Error: ",str(e))
            return ({"Message : Table not deleted"})


    




dict3 = {
    "TableName" : "rrrabc",
    "Coloumn" : {
        "a" : "x",
        "b" : "y",
        "c" : "z"
    }
}


a = Oracleopration()
# print(a.Oracle_drop_table("XYAC"))
# a.Oracle_connection()
a.Oracle_fetch_data()

# print(a.Oracle_create_table(dict3))

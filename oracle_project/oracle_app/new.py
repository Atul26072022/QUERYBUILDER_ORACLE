import cx_Oracle

# def Oracle_connection(self):
#         with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
#             print("Connected")
#             cur = co.cursor()
#             return cur


class Oracleopration:

    
            

    def Oracle_fetch_data(self):
        required_data = []
        try:
            with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
                # print("Connected")
                cur = co.cursor()


                cur.execute(" SELECT table_name FROM all_tables WHERE owner='C##ABC' ")
                
                x = cur.fetchall()
                for i in range(0,len(x)):

                    cur.execute(f"select * from C##ABC.{x[i][0]}")
                    col_names = [row[0] for row in cur.description]
                    required_data.append({
                        x[i][0] : col_names
                    })
                
                print(required_data)

            return ({"Message" : "Data Fetched successfully"})
                
        except Exception as e:
            print("Error: ",str(e))
            return ({"Message" : "Data Not Fetched"})
        


    def Oracle_create_table(self,dict2):
        table_name = []
        coloumn_name = []
        existing_coloumn_name = []
        try:
            with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
                # print("Connected")
                cur=co.cursor()
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
                    return ({"Message" : "Table Altered"})
                else:
                
                    cur.execute(f"CREATE TABLE C##ABC.{dict2['TableName']}(id int NOT NULL)")

                    for key in dict2["Coloumn"].values():
                        cur.execute(f"ALTER TABLE C##ABC.{dict2['TableName']} ADD {key} VARCHAR2(50)")
                    return ({"Message" : "Table Created"})
                
        except Exception as e:
            # print("Error: ",str(e))
            return ({"Message" : "Table not created Something went wrong"})
            

    
        
    
    def Oracle_drop_table(self,table_name):

        try:
            with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
                # print("Connected")
                cur = co.cursor()


                cur.execute(f" DROP TABLE C##ABC.{table_name}")
                
            return ({"Message" : "Table Deleted Successfully"})
                
        except Exception as e:
            print("Error: ",str(e))
            return ({"Message" : "Table not deleted"})
        

    def oracle_data_insertion(self , list1):

        try:
            with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
                print("Connected")      
                cur = co.cursor()

                for i in list1:
                    cur.execute("INSERT INTO ORACLE_APP_STUDENT VALUES (:1,:2,:3)",[i["id"],i["name"],i["age"]])
                    
                co.commit()
                    
                return ({"Message" : "Data Inserted Successfully" })
                
            
            
                
        except Exception as e:
            # print("Error: ",str(e))
            return ({"Message" : "Data not inserted successfully something went wrong"})


    




dict3 = {
    "TableName" : "rrrabc",
    "Coloumn" : {
        "a" : "x",
        "c" : "u",
        "d" : "v",
        "e" : "gg"
    }
}

list2 = [{
        "id" : 21,
        "name" : "rahulaaa",
        "age" : 23
    },
    {
        "id" : 22,
        "name" : "rahulbbb",
        "age" : 23
    
    }
    ]

a = Oracleopration()
# print(a.Oracle_drop_table("XYAC"))
# a.Oracle_connection()
# a.Oracle_fetch_data()

# print(a.Oracle_create_table(dict3))
print(a.oracle_data_insertion(list2))
import cx_Oracle


dict2 = {
    "name" : "xyz",
    "Company" :  "Antino",
    "emp" : "employee_id" }


# def create_table(self,dict2):
    


try:
    # with cx_Oracle.connect('C##ABC/abcd')as co:
    with cx_Oracle.connect('system/1234@//localhost:1521/XE') as co:
    # with cx_Oracle.connect('system/1234') as co:
        print("Connected")
        cur=co.cursor()
        cur.execute(f"CREATE TABLE C##ABC.{dict2['name']}( {dict2['Company']} varchar2(10), {dict2['emp']} varchar2(10))")
        print("Table Created")
        cur.close()
    # return ({"msg : Table Created successfully"})
                
except Exception as e:
    print("Error: ",str(e))
    # return ({"msg" : "Table not created", "error" : str(e)})

    
import cx_Oracle

with cx_Oracle.connect('C##ABC/abcd@Hitachi') as co:
    print("Connected")
    cur = co.cursor()
    print(cur)
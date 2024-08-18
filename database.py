#Database management banking
import mysql.connector as sql
mydb= sql.connect(
          host= "localhost",
          user="root",
          passwd="24359940",
          database="BANK"
)
cursor=mydb.cursor()
def createcustomertable():cursor.execute('''CREATE TABLE IF NOT EXISTS customers
            (Username varchar(20),
            password varchar(20),
            name varchar(20),
            age integer,
            city varchar(20),
            account_number integer,
            status boolean)
''')
mydb.commit()

if __name__ == "__main__":
    createcustomertable()

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall
    return result
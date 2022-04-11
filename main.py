import mysql.connector as connector
class DatabaseHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='*******',database='databaseName')
        query='create table if not exists user(user_id int primary key,user_name varchar(50),phone varchar(13))'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created Successfully...!!!');
    def insertData(self,user_id,user_name,phone):
        query='insert into user(user_id,user_name,phone) values({},"{}","{}")'.format(user_id,user_name,phone)
        cursor=self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('Data save successfully....!!!');
    def getAllData(self):
        query="select * from user";
        cursor=self.con.cursor();
        cursor.execute(query);
    
        for data in cursor:
            print(data)
    def getSingleData(self,user_id):
        query="select * from user where user_id={}".format(user_id);
        cursor=self.con.cursor();
        cursor.execute(query);
        self.con.commit()
        for x in cursor:
            print(x);
    def deleteOne(self,user_id):
        query="delete from user where user_id={}".format(user_id);
        cursor=self.con.cursor();
        cursor.execute(query);
        self.con.commit()
        print('Deleted Successfully...!!!');
    
    def update(self,user_id,new_name):
        query="update user set user_name='{}' where user_id={}".format(new_name,user_id);
        cursor=self.con.cursor();
        cursor.execute(query);
        self.con.commit();
     
        print('Updated Successfully...!!!');




helper=DatabaseHelper();
helper.getAllData();
helper.update(4,'rizwan iqbal')
# helper.deleteOne(3);
# helper.getSingleData(3)

# helper.insertData(2,'rabeeb aqdas khan','03131057073');
# helper.insertData(3,'abdul hai  khan','03131057074');
# helper.insertData(4,'umar farooq','03131057076');
# helper.insertData(5,'ali umair','03131057078');







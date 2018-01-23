# from flask_sqlalchemy import SQLAlchemy
import pymysql
# db=SQLAlchemy()

class Users():
    # __tablename__='user'
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(80), unique=True)
    # password = db.Column(db.String(80), unique=True)

    def __init__(self):
        # self.__username = username
        # self.__password = password
        self.__conn=pymysql.connect(user='*******',password='******',host='*********',port=3306,db='flaskPractice',use_unicode=True, charset="utf8")
        self.__cursor=self.__conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        # self.__cursor.close()
        self.__conn.close()

    def insert_user(self,username,password):
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("insert into user(username,password) values (%s,%s)",(username,password))
        self.__conn.commit()
        self.__cursor.close()

    def select_user(self,name):
        self.__cursor = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            self.__cursor.execute("select * from user where username = %s",name)
            result = self.__cursor.fetchone()
        finally:
            self.__cursor.close()
            return result

    def __repr__(self):
        return '<User %r>' % self.username





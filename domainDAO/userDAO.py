import psycopg2
from config.dbconfig import DATABASE_URL


class UserDAO:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
            # self.connection = psycopg2.connect(user=heroku_config['user'], password=heroku_config['password'],
            #                                    host=heroku_config['host'], database=heroku_config['dbname'])
            cursor = self.connection.cursor()

            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL database in heroku", error)

    def get_all_users(self):
        result = list()
        cursor = self.connection.cursor()
        query = "Select * from Users"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_user_by_id(self, uid):
        cursor = self.connection.cursor()
        query = "Select * from Users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert_user(self, uusername, upassword, uemail, uphone):
        cursor = self.connection.cursor()
        query = "Insert into Users(uusername, upassword, uemail, uphone) values " \
                "(%s, %s, %s, %s) returning uid;"
        cursor.execute(query, (uusername, upassword, uemail, uphone))
        uid = cursor.fetchone()[0]  # Fetchone retorna un row, y nosotros queremos el elemento 0
        self.connection.commit()  # Esta linea es SOLO cuando alteras algo en el DB (ej, insert, delete, update).
        cursor.close()
        return uid

    def get_user_by_username(self, uusername):
        cursor = self.connection.cursor()
        query = "select * from Users where uusername = %s"
        cursor.execute(query, (uusername,))
        result = cursor.fetchone()
        return result

    def get_user_by_email(self, uemail):
        cursor = self.connection.cursor()
        query = "select * from Users where uemail = %s"
        cursor.execute(query, (uemail,))
        result = cursor.fetchone()
        return result

    def delete_user_by_id(self, uid):
        cursor = self.connection.cursor()
        query = "delete from Users where uid = %s"
        cursor.execute(query, (uid,))
        self.connection.commit()
        return uid

    def update_user(self, uusername, upassword, uemail, uphone):
        cursor = self.connection.cursor()
        query = "Update Users Set uusername=%s, upassword=%s, uemail=%s, uphone=%s where uid = %s;"
        cursor.execute(query, (uusername, upassword, uemail, uphone))
        self.connection.commit()
        cursor.close()

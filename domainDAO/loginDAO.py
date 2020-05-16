import psycopg2
from config.dbconfig import DATABASE_URL


class LoginDAO:
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

    # def get_all_users(self):
    #     result = list()
    #     cursor = self.connection.cursor()
    #     query = "Select * from Users"
    #     cursor.execute(query)
    #     for row in cursor:
    #         result.append(row)
    #     cursor.close()
    #     return result

    def get_login_by_id(self, lid):
        cursor = self.connection.cursor()
        query = "Select * from login where lid = %s;"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_login_by_username_and_password(self, uusername, upassword):
        cursor = self.connection.cursor()
        query = "Select * from login where uusername = %s and upassword = %s;"
        cursor.execute(query, (uusername, upassword,))
        result = cursor.fetchone()[3]
        cursor.close()
        return result

    def insert_login(self, uusername, upassword, uid):
        cursor = self.connection.cursor()
        query = 'Insert into login(uusername, upassword, uid) values ' \
                '(%s, %s, %s) returning lid;'
        cursor.execute(query, (uusername, upassword, uid))
        result = cursor.fetchone()[0]  # Fetchone retorna un row, y nosotros queremos el elemento 0
        self.connection.commit()  # Esta linea es SOLO cuando alteras algo en el DB (ej, insert, delete, update).
        cursor.close()
        return result

    def delete_login_by_id(self, lid):
        cursor = self.connection.cursor()
        query = "delete from login where lid = %s"
        cursor.execute(query, (lid,))
        self.connection.commit()
        result = cursor.fetchone()[0]
        cursor.close()
        return result

    def delete_login_by_uid(self, uid):
        cursor = self.connection.cursor()
        query = "delete from login where uid = %s"
        cursor.execute(query, (uid,))
        self.connection.commit()
        result = cursor.fetchone()[0]
        cursor.close()
        return result

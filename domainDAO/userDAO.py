import psycopg2
from config.dbconfig import heroku_config


class UserDAO:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user=heroku_config['user'], password=heroku_config['password'],
                                               host=heroku_config['host'], database=heroku_config['dbname'])
            cursor = self.connection.cursor()

            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL database in heroku", error)

    def get_all_users(self):
        result = []
        cursor = self.connection.cursor()
        query = "Select * from Users"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

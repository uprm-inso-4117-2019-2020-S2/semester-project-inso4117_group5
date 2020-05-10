import psycopg2
from config.dbconfig import heroku_config


class ProviderDAO:
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

    def get_all_providers(self):
        result = list()
        cursor = self.connection.cursor()
        query = "Select * from Provider"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_provider_by_id(self, pid):
        cursor = self.connection.cursor()
        query = "Select * from Provider where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert_provider(self, puser, prequest):
        cursor = self.connection.cursor()
        query = "Insert into Provider(puser, prequest) values " \
                "(%s, %s) returning pid;"
        cursor.execute(query, (puser, prequest))
        pid = cursor.fetchone()[0]  
        self.connection.commit()  
        cursor.close()
        return pid

    def get_provider_by_user(self, puser):
        cursor = self.connection.cursor()
        query = "select * from Provider where puser = %s"
        cursor.execute(query, (puser,))
        result = cursor.fetchone()
        return result
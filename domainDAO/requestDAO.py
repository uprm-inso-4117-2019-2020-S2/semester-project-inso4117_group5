import psycopg2
from config.dbconfig import DATABASE_URL


class RequestDAO:
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

    def get_all_requests(self):
        result = list()
        cursor = self.connection.cursor()
        query = "select * from request;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_request_by_id(self, rid):
        cursor = self.connection.cursor()
        query = "select * from request where rid = %s;"
        cursor.execute(query,(rid,))
        result = cursor.fetchone()
        return result

    def get_request_by_title(self, rtitle):
        cursor = self.connection.cursor()
        query = "select * from request where rtitle = %s;"
        cursor.execute(query, (rtitle,))
        result = cursor.fetchone()
        return result

    def get_request_by_location(self, rlocation):
        cursor = self.connection.cursor()
        query = "select * from request where rlocation = %s;"
        cursor.execute(query, (rlocation,))
        result = cursor.fetchone()
        return result

    def get_requests_by_user_id(self, ruser):
        result = []
        cursor = self.connection.cursor()
        query = "select * from request where ruser = %s;"
        cursor.execute(query, (ruser,))
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_requests_by_user_status(self, ruser,status):
        result = []
        cursor = self.connection.cursor()
        query = "select * from request where ruser = %s and rstatus= %s;"
        cursor.execute(query, (ruser,rstatus,))
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_request_by_status(self, rstatus):
        result = []
        cursor = self.connection.cursor()
        query = "select * from request where rstatus = %s;"
        cursor.execute(query, (rstatus,))
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def insert_request(self, rtitle, rdescription, rlocation, ruser):
        cursor = self.connection.cursor()
        query = "insert into request(rtitle, rdescription, rlocation, rstatus, ruser)"\
                " values(%s, %s, %s, 0 , %s) returning rid;"
        cursor.execute(query, (rtitle, rdescription, rlocation, rstatus, ruser))
        rid = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()
        return rid

    def delete_request_by_id(self, rid):
        cursor = self.connection.cursor()
        query = "delete from request where rid = %s;"
        cursor.execute(query, (rid,))
        self.connection.commit()
        return rid

    def update_request_by_id(self, rid, rtitle, rdescription, rlocation, rstatus, ruser):
        cursor = self.connection.cursor()
        query = "update request set rtitle = %s, rdescription = %s, rlocation = %s, rstatus = %s, ruser = %s"\
                " where rid = %s;"
        cursor.execute(query, (rid, rtitle, rdescription, rlocation, rstatus, ruser))
        self.connection.commit()
        cursor.close()
        return rid

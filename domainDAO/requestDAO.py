import psycopg2
from config.dbconfig import DATABASE_URL


class RequestDAO:
    def __init__(self):
        while True:
            try:
                self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
                # self.connection = psycopg2.connect(user=heroku_config['user'], password=heroku_config['password'],
                #                                    host=heroku_config['host'], database=heroku_config['dbname'])
                cursor = self.connection.cursor()

                # Print PostgreSQL version
                cursor.execute("SELECT version();")
                record = cursor.fetchone()
                print("You are connected to - ", record, "\n")
                break
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL database in heroku", error)

    def get_all_requests(self) -> list:
        result = list()
        cursor = self.connection.cursor()
        query = "select * from request;"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_request_by_id(self, rid: int) -> tuple:
        cursor = self.connection.cursor()
        query = "select * from request where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_request_by_title(self, rtitle: str) -> list:
        results = list()
        cursor = self.connection.cursor()
        query = "select * from request where rtitle = %s;"
        cursor.execute(query, (rtitle,))
        for row in cursor:
            results.append(row)
        cursor.close()
        return results

    def get_request_by_location(self, rlocation: str) -> list:
        results = list()
        cursor = self.connection.cursor()
        query = "select * from request where rlocation = %s;"
        cursor.execute(query, (rlocation,))
        for row in cursor:
            results.append(row)
        cursor.close()
        return results

    def get_requests_by_user_id(self, ruser: int) -> list:
        result = list()
        cursor = self.connection.cursor()
        query = "select * from request where ruser = %s;"
        cursor.execute(query, (ruser,))
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_requests_by_user_status(self, ruser: int, rstatus: str) -> list:
        result = list()
        cursor = self.connection.cursor()
        query = "select * from request where ruser = %s and rstatus = %s;"
        cursor.execute(query, (ruser, rstatus,))
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_request_by_status(self, rstatus: int) -> list:
        result = list()
        cursor = self.connection.cursor()
        query = "select * from request where rstatus = %s;"
        cursor.execute(query, (rstatus,))
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def insert_request(self, rtitle, rdescription, rlocation, rstatus, ruser) -> int:
        cursor = self.connection.cursor()
        query = "insert into request(rtitle, rdescription, rlocation, rstatus, ruser)"\
                " values(%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rtitle, rdescription, rlocation, rstatus, ruser))
        rid = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()
        return rid

    def delete_request_by_id(self, rid: int) -> int:  # returns the number of rows deleted in whole DB
        cursor = self.connection.cursor()
        count = 0
        query = "DELETE FROM provider WHERE prequest IN (SELECT %s request);"
        cursor.execute(query, (rid,))
        count += cursor.rowcount
        query = "DELETE FROM request WHERE rid = %s RETURNING *;"
        cursor.execute(query, (rid,))
        count += cursor.rowcount
        self.connection.commit()
        cursor.close()
        return count

    def update_request_by_id(self, rid, rtitle, rdescription, rlocation, rstatus, ruser) -> int:
        cursor = self.connection.cursor()
        query = "update request set rtitle = %s, rdescription = %s, rlocation = %s, rstatus = %s, ruser = %s"\
                " where rid = %s RETURNING rid;"
        cursor.execute(query, (rtitle, rdescription, rlocation, rstatus, ruser, rid))
        result = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()
        return result

from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def get_car(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM car"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'car_id': row['car_id'],
                'car_brand': row['car_brand'],
                'car_name': row['car_name'],
                'car_type': row['car_type'],
                'car_trans': row['car_trans'],
                'car_year': row['car_year'],
                'car_seats': row['car_seats'],
                'car_lugg': row['car_lugg'],
                'car_price': row['car_price'],
                'provider_id': row['provider_id']
            })
        cursor.close()
        return result

    def __del__(self):
        self.connection.close()


class Database(DependencyProvider):

    connection_pool = None

    def __init__(self): 
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='localhost',
                database='rental_db',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())

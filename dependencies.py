from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error

MODEL_DATA = {
    'car': ['car_id', 'car_brand', 'car_name', 'car_type', 'car_trans', 'car_year', 'car_seats', 'car_lugg', 'car_price', 'provider_id'],
    'driver': ['driver_id', 'driver_name', 'driver_gender', 'driver_age', 'driver_phone'],
    'provider': ['provider_id', 'provider_name', 'provider_loc', 'provider_phone']
}

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    # Function untuk get all
    def fetch_all(self, table):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = f"SELECT * FROM {table}"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({field: row[field] for field in MODEL_DATA[table]})
        cursor.close()
        return result
    
    # Function untuk get by id
    def fetch_by_id(self, table, id_field, id_value):
        cursor = self.connection.cursor(dictionary=True)
        sql = f"SELECT * FROM {table} WHERE {id_field} = %s"
        cursor.execute(sql, (id_value,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return {field: row[field] for field in MODEL_DATA[table]}
        return None

    # Car
    def get_car(self):
        return self.fetch_all('car')
    
    def get_car_by_id(self, car_id):
        return self.fetch_by_id('car', 'car_id', car_id)
    
    def check_carID(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT car_id FROM car WHERE car_id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()  # Use fetchall to get all rows
        cursor.close()

        if result:
            return result
        else:
            return False

    def add_car(self, car_brand, car_name, car_type, car_trans, car_year, car_seats, car_lugg, car_price, provider_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "INSERT INTO car (car_brand, car_name, car_type, car_trans, car_year, car_seats, car_lugg, car_price, provider_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (car_brand, car_name, car_type, car_trans, car_year, car_seats, car_lugg, car_price, provider_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
        


    # Provider
    def get_provider(self):
        return self.fetch_all('provider')
    
    def get_provider_by_id(self, provider_id):
        return self.fetch_by_id('provider', 'provider_id', provider_id)
    
    def check_provID(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT provider_id FROM provider WHERE provider_id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()  # Use fetchall to get all rows
        cursor.close()

        if result:
            return result
        else:
            return False
            
    def add_provider(self, provider_name, provider_loc, provider_phone):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "INSERT INTO provider (provider_name, provider_loc, provider_phone) VALUES (%s, %s, %s)"
            cursor.execute(sql, (provider_name, provider_loc, provider_phone))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
    

    # Driver
    def get_driver(self):
        return self.fetch_all('driver')

    def get_driver_by_id(self, driver_id):
        return self.fetch_by_id('driver', 'driver_id', driver_id)
    
    def check_driverID(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT driver_id FROM driver WHERE driver_id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()  # Use fetchall to get all rows
        cursor.close()

        if result:
            return result
        else:
            return False
            
    def add_driver(self, driver_name, driver_gender, driver_age, driver_phone):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "INSERT INTO driver (driver_name, driver_gender, driver_age, driver_phone) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (driver_name, driver_gender, driver_age, driver_phone))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
    

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

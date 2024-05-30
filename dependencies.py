from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    # Car
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


    # Provider
    def get_provider(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM provider"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'provider_id': row['provider_id'],
                'name': row['provider_name'],
                'location': row['provider_loc'],
                'phone': row['provider_phone']
                # Add other fields as needed
            })
        cursor.close()
        return result
    
    

    # Driver
    def get_driver(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM driver"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'driver_id': row['driver_id'],
                'name': row['driver_name'],
                'gender': row['driver_gender'],
                'age': row['driver_age'],
                'phone': row['driver_phone']
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

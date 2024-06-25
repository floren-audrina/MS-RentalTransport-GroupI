from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from datetime import datetime

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError, EndpointConnectionError

MODEL_DATA = {
    'car': ['car_id', 'car_brand', 'car_name', 'car_type', 'car_transmission', 'car_year', 'car_seats', 'car_luggages', 'car_price', 'driver_id'],
    'driver': ['driver_id', 'driver_name', 'driver_gender', 'driver_age', 'driver_phone'],
    'booking': ['booking_id', 'tanggal_mulai', 'tanggal_selesai', 'with_driver', 'total_harga', 'car_id']
}

class DatabaseWrapper:

    connection = None
    
    BUCKET_NAME = 'car-image-soa'
    s3 = boto3.client('s3')

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
    
    def get_available_cars(self, start, end):
        try:
            start = datetime.strptime(start, "%Y-%m-%d").date()
            end = datetime.strptime(end, "%Y-%m-%d").date()
        except ValueError:
            return 400, {"error": "Invalid date format. Expected format: 'YYYY-MM-DD'"}

        cursor = self.connection.cursor(dictionary=True)

        sql = 'SELECT DISTINCT car_id FROM car WHERE car_id NOT IN (SELECT car_id FROM booking WHERE (%s BETWEEN tanggal_mulai AND tanggal_selesai) OR (%s BETWEEN tanggal_mulai AND tanggal_selesai) OR (tanggal_mulai BETWEEN %s AND %s) OR (tanggal_selesai BETWEEN %s AND %s))'
        cursor.execute(sql, (start, end, start, end, start, end))
        available_cars = [row['car_id'] for row in cursor.fetchall()]
        
        cursor.close()
        return available_cars
    
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

    def add_car(self, car_brand, car_name, car_type, car_transmission, car_year, car_seats, car_luggages, car_price, driver_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "INSERT INTO car (car_brand, car_name, car_type, car_transmission, car_year, car_seats, car_luggages, car_price, driver_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (car_brand, car_name, car_type, car_transmission, car_year, car_seats, car_luggages, car_price, driver_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
        
    def edit_car(self, car_id, car_brand, car_name, car_type, car_transmission, car_year, car_seats, car_luggages, car_price, driver_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            updates = []
            params = []

            if car_brand != "-":
                updates.append("car_brand = %s")
                params.append(car_brand)
            if car_name != "-":
                updates.append("car_name = %s")
                params.append(car_name)
            if car_type != "-":
                updates.append("car_type = %s")
                params.append(car_type)
            if car_transmission != "-":
                updates.append("car_transmission = %s")
                params.append(car_transmission)
            if car_year != "-":
                updates.append("car_year = %s")
                params.append(car_year)
            if car_seats != "-":
                updates.append("car_seats = %s")
                params.append(car_seats)
            if car_luggages != "-":
                updates.append("car_luggages = %s")
                params.append(car_luggages)
            if car_price != "-":
                updates.append("car_price = %s")
                params.append(car_price)
            if driver_id != "-":
                updates.append("driver_id = %s")
                params.append(driver_id)
            
            if not updates:
                return False  # Nothing to update

            sql = "UPDATE car SET " + ", ".join(updates) + " WHERE car_id = %s"
            params.append(car_id)

            cursor.execute(sql, tuple(params))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False

    def delete_car(self, id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "DELETE FROM car WHERE car_id = {}".format(id)
            cursor.execute(sql)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False

    # Car Image
    def get_car_image_s3(self):
        result = None
        try:
            response = self.s3.list_objects_v2(Bucket=self.BUCKET_NAME)
            result = []
            for obj in response['Contents']:
                # print(obj)
                key = obj['Key'].replace(" ", "+")
                url = "https://{0}.s3.amazonaws.com/{1}".format(self.BUCKET_NAME, key)
                result.append(url)
        except NoCredentialsError:
            result = {"error": "No AWS credentials were provided."}
        except PartialCredentialsError:
            result = {"error": "Incomplete AWS credentials provided."}
        except EndpointConnectionError:
            result = {"error": "Could not connect to the specified endpoint."}
        except ClientError as e:
            # Handle any client error thrown by boto3
            result = {"error": str(e)}
        except Exception as e:
            # Catch any other exceptions
            result = {"error": str(e)}
        # print(result)
        return result
    
    def get_car_image_s3_by_id(self, id):
        result = None
        try:
            response = self.s3.list_objects_v2(Bucket=self.BUCKET_NAME)            
            obj = response['Contents'][id-1]
            # print(obj)
            key = obj['Key'].replace(" ", "+")
            url = "https://{0}.s3.amazonaws.com/{1}".format(self.BUCKET_NAME, key)
            result = url
        except NoCredentialsError:
            result = {"error": "No AWS credentials were provided."}
        except PartialCredentialsError:
            result = {"error": "Incomplete AWS credentials provided."}
        except EndpointConnectionError:
            result = {"error": "Could not connect to the specified endpoint."}
        except ClientError as e:
            # Handle any client error thrown by boto3
            result = {"error": str(e)}
        except Exception as e:
            # Catch any other exceptions
            result = {"error": str(e)}
        # print(result)
        return result

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
        
    def edit_driver(self, driver_id, driver_name, driver_gender, driver_age, driver_phone, car_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            updates = []
            params = []

            if driver_name != "-":
                updates.append("driver_name = %s")
                params.append(driver_name)
            if driver_gender != "-":
                updates.append("driver_gender = %s")
                params.append(driver_gender)
            if driver_age != "-":
                updates.append("driver_age = %s")
                params.append(driver_age)
            if driver_phone != "-":
                updates.append("driver_phone = %s")
                params.append(driver_phone)
            if car_id != "-":
                updates.append("car_id = %s")
                params.append(car_id)
            
            if not updates:
                return False  # Nothing to update

            sql = "UPDATE driver SET " + ", ".join(updates) + " WHERE driver_id = %s"
            params.append(driver_id)

            cursor.execute(sql, tuple(params))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False

    
    def delete_driver(self, id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "DELETE FROM driver WHERE driver_id = {}".format(id)
            cursor.execute(sql)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
        
    
    
    # Booking
    def get_booking(self):
        return self.fetch_all('booking')

    def get_booking_by_id(self, booking_id):
        return self.fetch_by_id('booking', 'booking_id', booking_id)
    
    def check_bookingID(self, booking_id):
        if self.get_booking_by_id(booking_id) :
            return True
        else :
            return False
    
    def add_booking(self, tanggal_mulai, tanggal_selesai, with_driver, total_harga, car_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "INSERT INTO booking (tanggal_mulai, tanggal_selesai, with_driver, total_harga, car_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (tanggal_mulai, tanggal_selesai, with_driver, total_harga, car_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
        
    def edit_booking(self, booking_id, start_date, end_date, with_driver, total_price, car_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            updates = []
            params = []

            if start_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                updates.append("tanggal_mulai = %s")
                params.append(start_date)
            if end_date:
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                updates.append("tanggal_selesai = %s")
                params.append(end_date)
            if with_driver is not None:
                updates.append("with_driver = %s")
                params.append(with_driver)
            if total_price:
                updates.append("total_harga = %s")
                params.append(total_price)
            if car_id is not None:
                updates.append("car_id = %s")
                params.append(car_id)
            
            if not updates:
                return False  # Nothing to update

            sql = "UPDATE booking SET " + ", ".join(updates) + " WHERE booking_id = %s"
            params.append(booking_id)

            cursor.execute(sql, tuple(params))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            cursor.close()
            return False
    
    # Check 
    def check_booking_is_done(self, booking_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT tanggal_mulai, tanggal_selesai FROM booking WHERE booking_id = %s"
        cursor.execute(sql, (booking_id,))
        row = cursor.fetchone()
        cursor.close()

        if not row:
            return {"status": "error", "message": f"Booking with ID {booking_id} does not exist."}

        tanggal_mulai = row['tanggal_mulai']
        tanggal_selesai = row['tanggal_selesai']

        from datetime import datetime

        current_date = datetime.now().strftime("%Y-%m-%d")  # format harus sesuai dengan format tanggal di database

        if current_date > tanggal_selesai:
            return {"status": "done", "message": "Booking is done."}
        elif current_date < tanggal_mulai:
            return {"status": "not_started", "message": "Booking has not started yet."}
        else:
            return {"status": "in_progress", "message": "Booking is in progress."}
        
    def delete_booking(self, id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            sql = "DELETE FROM booking WHERE booking_id = {}".format(id)
            cursor.execute(sql)
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
        if not self.connection:
            self.connect()
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT provider_name, provider_address, provider_city, provider_num, policy, information, map FROM provider"
        cursor.execute(query)
        provider = cursor.fetchall()
        cursor.close()
        return provider
    
    def edit_provider(self, provider_name=None, provider_address=None, provider_city=None, provider_num=None, policy=None, information=None, map=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            updates = []
            params = []

            # Add provided fields to updates and params
            if provider_name is not None:
                updates.append("provider_name = %s")
                params.append(provider_name)
            if provider_address is not None:
                updates.append("provider_address = %s")
                params.append(provider_address)
            if provider_city is not None:
                updates.append("provider_city = %s")
                params.append(provider_city)
            if provider_num is not None:
                updates.append("provider_num = %s")
                params.append(provider_num)
            if policy is not None:
                updates.append("policy = %s")
                params.append(policy)
            if information is not None:
                updates.append("information = %s")
                params.append(information)
            if map is not None:
                updates.append("map = %s")
                params.append(map)
            
            # If no updates, return False
            if not updates:
                return False

            # Join updates list into a single string
            sql = "UPDATE provider SET " + ", ".join(updates)

            # Execute the SQL query with the parameters
            cursor.execute(sql, tuple(params))
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
                # database='rental_db',
                database='jayamahe_easy_ride_jakarta',
                # database='moovby_driverless_jakarta',
                # database='arasya_jakarta',
                # database='empat_roda_jogja',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
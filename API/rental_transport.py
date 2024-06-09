from nameko.rpc import rpc

import dependencies as dependencies

class RentalService:
    name = 'rental_service'
    database = dependencies.Database()
    
    # Car
    @rpc
    def get_car(self):
        return self.database.get_car()
    
    @rpc
    def get_car_by_id(self, car_id):
        return self.database.get_car_by_id(car_id)
    
    @rpc
    def get_available_cars(self, start, end):
        return self.database.get_available_cars(start, end)

    @rpc
    def add_car(self, car_list):
        response = []
        driver_id = car_list.get('driver_id')
        if self.database.check_driverID(driver_id):
            car_brand = car_list.get('car_brand')
            car_name = car_list.get('car_name')
            car_type = car_list.get('car_type')
            car_transmission = car_list.get('car_transmission')
            car_year = car_list.get('car_year')
            car_seats = car_list.get('car_seats')
            car_luggages = car_list.get('car_luggages')
            car_price = car_list.get('car_price')
            driver_id = car_list.get('driver_id')
            self.database.add_car(car_brand,car_name,car_type,car_transmission,car_year,car_seats,car_luggages,car_price,driver_id)
            response.append({"status": "success", "message": "Car added successfully."})
        else:
            response.append({"status": "error", "message": f"Driver with ID {driver_id} does not exist."})
        return response
    
    @rpc
    def delete_car(self, car_id):
        if self.database.check_carID(car_id):
            self.database.delete_car(car_id)
            return {"status": "success", "message": f"Car with ID {car_id} has been deleted."}
        else:
            return {"status": "error", "message": f"Car with ID {car_id} does not exist."}

    # Driver
    @rpc
    def get_driver(self):
        return self.database.get_driver()
    
    @rpc
    def get_driver_by_id(self, driver_id):
        return self.database.get_driver_by_id(driver_id)
    
    @rpc
    def add_driver(self, driver_list):
        response = []
        driver_name = driver_list.get('driver_name')
        driver_gender = driver_list.get('driver_gender')
        driver_age = driver_list.get('driver_age')
        driver_phone = driver_list.get('driver_phone')
        self.database.add_driver(driver_name,driver_gender,driver_age,driver_phone)
        response.append({"status": "success", "message": "Driver added successfully."})
        return response
    
    @rpc
    def delete_driver(self, driver_id):
        if self.database.check_driverID(driver_id):
            self.database.delete_driver(driver_id)
            return {"status": "success", "message": f"Driver with ID {driver_id} has been deleted."}
        else:
            return {"status": "error", "message": f"Driver with ID {driver_id} does not exist."}
        
        
    # Booking
    @rpc
    def get_booking(self):
        return self.database.get_booking()
    
    @rpc
    def get_booking_by_id(self, booking_id):
        return self.database.get_booking_by_id(booking_id)

    @rpc
    def add_booking(self, booking_data):
        response = []
        car_id = booking_data.get('car_id')
        if self.database.check_carID(car_id):
            tanggal_mulai = booking_data.get('tanggal_mulai')
            tanggal_selesai = booking_data.get('tanggal_selesai')
            with_driver = booking_data.get('with_driver')
            total_harga = booking_data.get('total_harga')
            car_id = booking_data.get('car_id')
            self.database.add_booking(tanggal_mulai,tanggal_selesai,with_driver,total_harga,car_id)
            response.append({"status": "success", "message": "Booking added successfully."})
        else:
            response.append({"status": "error", "message": f"Car with ID {car_id} does not exist."})
        return response
    
    @rpc
    def check_booking_is_done(self, booking_id):
        return self.database.check_booking_is_done(booking_id)
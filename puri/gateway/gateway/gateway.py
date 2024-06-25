import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from datetime import datetime, date


class GatewayService:
    name = 'gateway'
    rental_rpc = RpcProxy('puri_bali')

    # Car
    @http('GET', '/car')
    def get_car(self, request):
        result = self.rental_rpc.get_car()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Car not found"})
        
    @http('GET', '/car/<int:car_id>')
    def get_car_by_id(self, request, car_id):
        result = self.rental_rpc.get_car_by_id(car_id)
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Car not found"})
        
    # resource example : http://localhost:8000/available_cars/2024-06-02/2024-06-09
    @http('GET', '/available_cars/<string:tanggal_mulai>/<string:tanggal_selesai>')
    def get_available_cars(self, request, tanggal_mulai, tanggal_selesai):
        # start = request.args.get('tanggal_mulai')
        # end = request.args.get('tanggal_selesai')

        if not tanggal_mulai or not tanggal_selesai:
            return 400, json.dumps({"error": "tanggal_mulai and tanggal_selesai parameters are required"})
        if not all(isinstance(field, str) for field in [tanggal_mulai, tanggal_selesai]):
            return 400, {"error": "tanggal_mulai and tanggal_selesai must be a string so it can be parsed to date"}
        
        result = self.rental_rpc.get_available_cars(tanggal_mulai, tanggal_selesai)

        if isinstance(result, dict) and "error" in result:
            return 400, json.dumps(result)
        
        result_list = list(result)
        
        if result_list:
            return 200, json.dumps(result_list)
        else:
            return 404, json.dumps({"error": "No available cars"})

    @http('POST', '/car_add')
    def add_car(self, request):
        req = request.get_data(as_text=True)
        try:
            car_list = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(car_list, dict):
            return 400, json.dumps({"error": "Expected a list of car details"})

        # for car_details in car_list:
        car_brand = car_list.get('car_brand', None)
        car_name = car_list.get('car_name', None)
        car_type = car_list.get('car_type', None)
        car_transmission = car_list.get('car_transmission', None)
        car_year = car_list.get('car_year', None)
        car_seats = car_list.get('car_seats', None)
        car_luggages = car_list.get('car_luggages', None)
        car_price = car_list.get('car_price', None)
        driver_id = car_list.get('driver_id', None)

        # Check if any required field is None
        if None in (car_brand, car_name, car_type, car_transmission, car_year, car_seats, car_luggages, car_price, driver_id):
            return 400, json.dumps({"error": "All car details fields are required and cannot be None"})

        # Validate types
        if not all(isinstance(field, str) for field in [car_brand, car_name, car_type, car_transmission]):
            return 400, json.dumps({"error": "car_brand, car_name, car_type, and car_transmission must be strings"})

        if not all(isinstance(field, int) for field in [car_year, car_seats, car_luggages]):
            return 400, json.dumps({"error": "car_year, car_seats, and car_luggages must be integers"})

        if not isinstance(car_price, (int, float)):
            return 400, json.dumps({"error": "car_price must be a number"})

        if not isinstance(driver_id, int):
            return 400, json.dumps({"error": "driver_id must be an integer"})

        # All entries are valid, proceed with adding cars
        responses = self.rental_rpc.add_car(car_list)
        return 200, json.dumps(responses)
    
    @http('PUT', '/car_edit')
    def edit_car(self, request):
        req = request.get_data(as_text=True)
        try:
            car_details = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(car_details, dict):
            return 400, json.dumps({"error": "Expected a dictionary of car details"})

        # Extract car details
        car_id = car_details.get('car_id', None)
        car_brand = car_details.get('car_brand', "-")
        car_name = car_details.get('car_name', "-")
        car_type = car_details.get('car_type', "-")
        car_transmission = car_details.get('car_transmission', "-")
        car_year = car_details.get('car_year', "-")
        car_seats = car_details.get('car_seats', "-")
        car_luggages = car_details.get('car_luggages', "-")
        car_price = car_details.get('car_price', "-")
        driver_id = car_details.get('driver_id', "-")

        # Check if car_id is provided and valid
        if car_id is None or not isinstance(car_id, int):
            return 400, json.dumps({"error": "car_id is required and must be an integer"})

        # Validate fields
        if car_brand != "-" and not isinstance(car_brand, str):
            return 400, json.dumps({"error": "car_brand must be a string"})
        if car_name != "-" and not isinstance(car_name, str):
            return 400, json.dumps({"error": "car_name must be a string"})
        if car_type != "-" and not isinstance(car_type, str):
            return 400, json.dumps({"error": "car_type must be a string"})
        if car_transmission != "-" and not isinstance(car_transmission, str):
            return 400, json.dumps({"error": "car_transmission must be a string"})
        if car_year != "-" and not isinstance(car_year, int):
            return 400, json.dumps({"error": "car_year must be an integer"})
        if car_seats != "-" and not isinstance(car_seats, int):
            return 400, json.dumps({"error": "car_seats must be an integer"})
        if car_luggages != "-" and not isinstance(car_luggages, int):
            return 400, json.dumps({"error": "car_luggages must be an integer"})
        if car_price != "-" and not isinstance(car_price, (int, float)):
            return 400, json.dumps({"error": "car_price must be a number"})
        if driver_id != "-" and not isinstance(driver_id, int):
            return 400, json.dumps({"error": "driver_id must be an integer"})

        # if all validated
        responses = self.rental_rpc.edit_car(car_details)
        return 200, json.dumps(responses)


    @http('DELETE', '/car_delete/<int:car_id>')
    def delete_car(self, request, car_id):
        if not isinstance(car_id, int) or car_id <= 0:
            return 400, json.dumps({"error": "Invalid car ID"})
        
        result = self.rental_rpc.delete_car(car_id)
    
        if result.get("status") == "error":
            return 404, json.dumps({"error": result.get("message")})
        else:
            return 200, json.dumps({"message": "Car deleted successfully"})

    # Driver
    @http('GET', '/driver')
    def get_driver(self, request):
        result = self.rental_rpc.get_driver()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Driver not found"})
        
    @http('GET', '/driver/<int:driver_id>')
    def get_driver_by_id(self, request, driver_id):
        result = self.rental_rpc.get_driver_by_id(driver_id)
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Driver not found"})
    
    @http('POST', '/driver_add')
    def add_driver(self, request):
        req = request.get_data(as_text=True)
        try:
            driver_list = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(driver_list, dict):
            return 400, json.dumps({"error": "Expected a list of driver details"})

        driver_name = driver_list.get('driver_name', None)
        driver_gender = driver_list.get('driver_gender', None)
        driver_age = driver_list.get('driver_age', None)
        driver_phone = driver_list.get('driver_phone', None)

        # Check if any required field is None
        if None in (driver_name,driver_gender,driver_age,driver_phone):
            return 400, json.dumps({"error": "All driver details fields are required and cannot be None"})
        
        if not all(isinstance(field, str) for field in [driver_name,driver_gender]):
            return 400, json.dumps({"error": "driver_name and driver_gender] must be strings"})

        if not all(isinstance(field, int) for field in [driver_age,driver_phone]):
            return 400, json.dumps({"error": "driver_age and driver_phone must be integers"})
        
        responses = self.rental_rpc.add_driver(driver_list)
        return 200, json.dumps(responses)
    
    @http('PUT', '/driver_edit')
    def edit_driver(self, request):
        req = request.get_data(as_text=True)
        try:
            driver_details = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(driver_details, dict):
            return 400, json.dumps({"error": "Expected a dictionary of driver details"})

        # Extract driver details
        driver_id = driver_details.get('driver_id', None)
        driver_name = driver_details.get('driver_name', "-")
        driver_gender = driver_details.get('driver_gender', "-")
        driver_age = driver_details.get('driver_age', "-")
        driver_phone = driver_details.get('driver_phone', "-")
        car_id = driver_details.get('car_id', "-")

        # Check if driver_id is provided and valid
        if driver_id is None or not isinstance(driver_id, int):
            return 400, json.dumps({"error": "driver_id is required and must be an integer"})

        # Validate fields
        if driver_name != "-" and not isinstance(driver_name, str):
            return 400, json.dumps({"error": "driver_name must be a string"})
        if driver_gender != "-" and not (driver_gender == 'M' or driver_gender == 'F'):
            return 400, json.dumps({"error": "driver_gender must be 'M' or 'F'"})
        if driver_age != "-" and not isinstance(driver_age, int):
            return 400, json.dumps({"error": "driver_age must be an integer"})
        if driver_phone != "-" and not isinstance(driver_phone, str):
            return 400, json.dumps({"error": "driver_phone must be a string"})
        if car_id != "-" and not (isinstance(car_id, int) or car_id is None):
            return 400, json.dumps({"error": "car_id must be an integer or None"})

        # If all validated
        responses = self.rental_rpc.edit_driver(driver_details)
        return 200, json.dumps(responses)

    
    @http('DELETE', '/driver_delete/<int:driver_id>')
    def delete_driver(self, request, driver_id):
        if not isinstance(driver_id, int) or driver_id <= 0:
            return 400, json.dumps({"error": "Invalid driver ID"})
        
        result = self.rental_rpc.delete_driver(driver_id)
    
        if result.get("status") == "error":
            return 404, json.dumps({"error": result.get("message")})
        else:
            return 200, json.dumps({"message": "Driver deleted successfully"})
    
    # Booking
    @http('GET', '/booking')
    def get_booking(self, request):
        result = self.rental_rpc.get_booking()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Booking not found"})
        
    @http('GET', '/booking/<int:booking_id>')
    def get_booking_by_id(self, request, booking_id):
        result = self.rental_rpc.get_booking_by_id(booking_id)
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Booking not found"})
        
    @http('POST', '/booking_add')
    def add_booking(self, request):
        req = request.get_data(as_text=True)
        try:
            booking_data = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(booking_data, dict):
            return 400, json.dumps({"error": "Expected a list of booking data"})

        # for car_details in car_list:
        tanggal_mulai = booking_data.get('tanggal_mulai', None)
        tanggal_selesai = booking_data.get('tanggal_selesai', None)
        with_driver = booking_data.get('with_driver', None)
        total_harga = booking_data.get('total_harga', None)
        car_id = booking_data.get('car_id', None)

        # Check if any required field is None
        if None in (tanggal_mulai,tanggal_selesai,with_driver,total_harga,car_id):
            return 400, json.dumps({"error": "All booking data fields are required and cannot be None"})

        # Validate types
        if not all(isinstance(field, int) for field in [with_driver, total_harga, car_id]):
            return 400, json.dumps({"error": "with_driver, total_harga, and car_id must be integers"})

        if not all(isinstance(field, str) for field in [tanggal_mulai, tanggal_selesai]):
            return 400, {"error": "tanggal_mulai and tanggal_selesai must be a string so it can be parsed to date"}
        
        # Parse string dates into date objects
        try:
            tanggal_mulai = datetime.strptime(tanggal_mulai, "%Y-%m-%d").date()
            tanggal_selesai = datetime.strptime(tanggal_selesai, "%Y-%m-%d").date()
        except ValueError:
            return 400, json.dumps({"error": "Invalid date format. Expected format: YYYY-MM-DD"})

        # All entries are valid, proceed with adding cars
        responses = self.rental_rpc.add_booking(booking_data)
        return 200, json.dumps(responses)
        
    @http('PUT', '/booking_edit')
    def edit_booking(self, request):
        req = request.get_data(as_text=True)
        try:
            booking_details = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(booking_details, dict):
            return 400, json.dumps({"error": "Expected a dictionary of booking details"})

        # Extract booking details
        booking_id = booking_details.get('booking_id', None)
        start_date = booking_details.get('tanggal_mulai', "-")
        end_date = booking_details.get('end_date', "-")
        with_driver = booking_details.get('with_driver', "-")
        total_price = booking_details.get('total_harga', "-")
        car_id = booking_details.get('car_id', "-")

        # Check if booking_id is provided and valid
        if booking_id is None or not isinstance(booking_id, int):
            return 400, json.dumps({"error": "booking_id is required and must be an integer"})
        
        # Validate types
        if any(not isinstance(field, int) for field in [with_driver, total_price, car_id]) and (with_driver != "-" or total_price != "-" or car_id != "-"):
            return 400, json.dumps({"error": "with_driver, total_harga, and car_id must be integers"})  
        if any(not isinstance(field, str) for field in [start_date, end_date]) and (start_date != "-" or end_date != "-"):
            return 400, {"error": "tanggal_mulai and tanggal_selesai must be a string so it can be parsed to date"}

        # If all validated
        responses = self.rental_rpc.edit_booking(booking_details)
        return 200, json.dumps(responses)


    @http('GET', '/booking/check/<int:booking_id>')
    def check_booking_is_done(self, request, booking_id):
        result = self.rental_rpc.check_booking_is_done(booking_id)
        return 200, json.dumps(result)
    
    @http('DELETE', '/booking_delete/<int:booking_id>')
    def delete_car(self, request, booking_id):
        if not isinstance(booking_id, int) or booking_id <= 0:
            return 400, json.dumps({"error": "Invalid car ID"})
        
        result = self.rental_rpc.delete_car(booking_id)
    
        if result.get("status") == "error":
            return 404, json.dumps({"error": result.get("message")})
        else:
            return 200, json.dumps({"message": "Booking deleted successfully"})


    # Provider
    @http('GET', '/provider')
    def get_provider(self, request):
        result = self.rental_rpc.get_provider()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Provider not found"})
        
    @http('PUT', '/provider_edit')
    def edit_provider_http(self, request):
        req = request.get_data(as_text=True)
        try:
            provider_details = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})

        if not isinstance(provider_details, dict):
            return 400, json.dumps({"error": "Expected a dictionary of provider details"})

        # Extract provider details
        provider_name = provider_details.get('provider_name')
        provider_address = provider_details.get('provider_address')
        provider_city = provider_details.get('provider_city')
        provider_num = provider_details.get('provider_num')
        policy = provider_details.get('policy')
        information = provider_details.get('information')
        map = provider_details.get('map')

        # Validate types
        if not all(isinstance(field, str) for field in [provider_name, provider_address, provider_city, provider_num, policy, information, map] if field is not None):
            return 400, json.dumps({"error": "provider_name, provider_address, provider_city, policy, information, and map must be strings"})

        # If all validated, call the edit_provider method
        success = self.edit_provider(provider_name, provider_address, provider_city, provider_num, policy, information, map)
        if success:
            return 200, json.dumps({"message": "Provider updated successfully"})
        else:
            return 500, json.dumps({"error": "Failed to update provider"})
import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'
    rental_rpc = RpcProxy('rental_service')

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
        
    @http('GET', '/available_cars')
    def get_available_cars(self, request):
        result = self.rental_rpc.get_available_cars()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "No available cars found"})

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

    @http('DELETE', '/car_delete')
    def delete_car(self, request):
        req = request.get_data(as_text=True)
        try:
            data = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})
        car_id = data.get('car_id')
        
        if not isinstance(car_id, int):
            return 400, json.dumps({"error": "car_id must be an integer"})
        
        if car_id not in self.rental_rpc:
            return 404, json.dumps({"error": "Car not found"})
        del self.rental_rpc.delete_car[car_id]
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
    
    @http('DELETE', '/driver_delete')
    def delete_driver(self, request):
        req = request.get_data(as_text=True)
        
        try:
            data = json.loads(req)
        except json.JSONDecodeError:
            return 400, json.dumps({"error": "Invalid JSON format"})
        driver_id = data.get('driver_id')
        
        if not isinstance(driver_id, int):
            return 400, json.dumps({"error": "driver_id must be an integer"})
        
        if driver_id not in self.rental_rpc:
            return 404, json.dumps({"error": "Driver not found"})
        del self.rental_rpc.delete_driver[driver_id]
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
        
        
        
    @http('GET', '/booking/check/<int:booking_id>')
    def check_booking_is_done(self, request, booking_id):
        result = self.rental_rpc.check_booking_is_done(booking_id)
        return 200, json.dumps(result)
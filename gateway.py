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

    @http('POST', '/car')
    def add_car(self, request):
        req = request.get_data(as_text=True)
        try:
            car_list = json.loads(req)
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON format"}), 400

        if not isinstance(car_list, list):
            return json.dumps({"error": "Expected a list of car details"}), 400

        # for car_details in car_list:
        car_brand = car_list.get('car_brand', None)
        car_name = car_list.get('car_name', None)
        car_type = car_list.get('car_type', None)
        car_trans = car_list.get('car_trans', None)
        car_year = car_list.get('car_year', None)
        car_seats = car_list.get('car_seats', None)
        car_lugg = car_list.get('car_lugg', None)
        car_price = car_list.get('car_price', None)
        provider_id = car_list.get('provider_id', None)

        # Check if any required field is None
        if None in (car_brand, car_name, car_type, car_trans, car_year, car_seats, car_lugg, car_price, provider_id):
            return json.dumps({"error": "All car details fields are required and cannot be None"}), 400

        # Validate types
        if not all(isinstance(field, str) for field in [car_brand, car_name, car_type, car_trans]):
            return json.dumps({"error": "car_brand, car_name, car_type, and car_trans must be strings"}), 400

        if not all(isinstance(field, int) for field in [car_year, car_seats, car_lugg]):
            return json.dumps({"error": "car_year, car_seats, and car_lugg must be integers"}), 400

        if not isinstance(car_price, (int, float)):
            return json.dumps({"error": "car_price must be a number"}), 400

        if not isinstance(provider_id, int):
            return json.dumps({"error": "provider_id must be an integer"}), 400

        # All entries are valid, proceed with adding cars
        responses = self.rental_rpc.add_car(car_list)
        return json.dumps(responses), 200

    # Provider
    @http('GET', '/provider')
    def get_provider(self, request):
        result = self.rental_rpc.get_provider()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Provider not found"})

    @http('POST', '/provider')
    def add_porvider(self, request):
        req = request.get_data(as_text=True)
        try:
            prov_list = json.loads(req)
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON format"}), 400

        if not isinstance(prov_list, list):
            return json.dumps({"error": "Expected a list of provider details"}), 400

        provider_name = prov_list.get('provider_name', None)
        provider_loc = prov_list.get('provider_loc', None)
        provider_phone = prov_list.get('provider_phone', None)

        # Check if any required field is None
        if None in (provider_name,provider_loc,provider_phone):
            return json.dumps({"error": "All provider details fields are required and cannot be None"}), 400
        
        if not all(isinstance(field, str) for field in [provider_name,provider_loc]):
            return json.dumps({"error": "provider_name and provider_loc must be strings"}), 400

        if not all(isinstance(field, int) for field in [provider_phone]):
            return json.dumps({"error": "provider_phone must be integers"}), 400
        
        responses = self.rental_rpc.add_provider(prov_list)
        return json.dumps(responses), 200
    

    # Driver
    @http('GET', '/driver')
    def get_driver(self, request):
        result = self.rental_rpc.get_driver()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Driver not found"})
    
    @http('POST', '/driver')
    def add_driver(self, request):
        req = request.get_data(as_text=True)
        try:
            driver_list = json.loads(req)
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON format"}), 400

        if not isinstance(driver_list, list):
            return json.dumps({"error": "Expected a list of driver details"}), 400

        driver_name = driver_list.get('driver_name', None)
        driver_gender = driver_list.get('driver_gender', None)
        driver_age = driver_list.get('driver_age', None)
        driver_phone = driver_list.get('driver_phone', None)

        # Check if any required field is None
        if None in (driver_name,driver_gender,driver_age,driver_phone):
            return json.dumps({"error": "All driver details fields are required and cannot be None"}), 400
        
        if not all(isinstance(field, str) for field in [driver_name,driver_gender]):
            return json.dumps({"error": "driver_name and driver_gender] must be strings"}), 400

        if not all(isinstance(field, int) for field in [driver_age,driver_phone]):
            return json.dumps({"error": "driver_age and driver_phone must be integers"}), 400
        
        responses = self.rental_rpc.add_provider(driver_list)
        return json.dumps(responses), 200

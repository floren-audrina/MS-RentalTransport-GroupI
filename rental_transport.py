from nameko.rpc import rpc

import dependencies

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
    def add_car(self, car_list):
        response = []
        provider_id = car_list.get('provider_id')
        if self.database.check_provID(provider_id):
            car_brand = car_list.get('car_brand')
            car_name = car_list.get('car_name')
            car_type = car_list.get('car_type')
            car_trans = car_list.get('car_trans')
            car_year = car_list.get('car_year')
            car_seats = car_list.get('car_seats')
            car_lugg = car_list.get('car_lugg')
            car_price = car_list.get('car_price')
            provider_id = car_list.get('provider_id')
            self.database.add_car(car_brand,car_name,car_type,car_trans,car_year,car_seats,car_lugg,car_price,provider_id)
            response.append({"status": "success", "message": "Car added successfully."})
        else:
            response.append({"status": "error", "message": f"Provider with ID {provider_id} does not exist."})
        return response
    
    @rpc
    def delete_car(self, car_id):
        if self.database.check_carID(car_id):
            self.database.delete_car(car_id)
            return {"status": "success", "message": f"Car with ID {car_id} has been deleted."}
        else:
            return {"status": "error", "message": f"Car with ID {car_id} does not exist."}

    
    # Provider
    @rpc
    def get_provider(self):
        return self.database.get_provider()
    
    @rpc
    def get_provider_by_id(self, provider_id):
        return self.database.get_provider_by_id(provider_id)
    
    @rpc
    def add_provider(self, prov_list):
        response = []
        provider_name = prov_list.get('provider_name', None)
        provider_loc = prov_list.get('provider_loc', None)
        provider_phone = prov_list.get('provider_phone', None)
        self.database.add_provider(provider_name,provider_loc,provider_phone)
        response.append({"status": "success", "message": "Provider added successfully."})
        return response
    
    @rpc
    def delete_provider(self, provider_id):
        if self.database.check_provID(provider_id):
            self.database.delete_provider(provider_id)
            return {"status": "success", "message": f"Provider with ID {provider_id} has been deleted."}
        else:
            return {"status": "error", "message": f"Provider with ID {provider_id} does not exist."}
        
    
    
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

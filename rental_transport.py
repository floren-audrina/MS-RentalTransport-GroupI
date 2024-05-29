from nameko.rpc import rpc

import dependencies

class RentalService:
    name = 'rental_service'
    database = dependencies.Database()
    
    @rpc
    def get_car(self):
        return self.database.get_car()

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
        else:
            response.append({"status": "error", "message": f"Provider with ID {provider_id} does not exist."})
        
        return response
#     @rpc
#     def edit_car(self, num):
        
#     @rpc
#     def del_car(self, num):

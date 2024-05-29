from nameko.rpc import rpc

import dependencies

class RentalService:
    name = 'car_service'
    database = dependencies.Database()
    
    @rpc
    def get_car(self):
        return self.database.get_car()

#     @rpc
#     def add_car(self, num, r_type):

    
#     @rpc
#     def edit_car(self, num):
        
#     @rpc
#     def del_car(self, num):

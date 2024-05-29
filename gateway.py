import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'
    car_rpc = RpcProxy('car_service')

    @http('GET', '/car')
    def get_car(self, request):
        result = self.car_rpc.get_car()
        if result:
            return 200, json.dumps(result)
        else:
            return 404, json.dumps({"error": "Car not found"})
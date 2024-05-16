import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    hotel_rpc = RpcProxy('room_service')

    @http('GET', '')
    # def get_rooms(self, request):
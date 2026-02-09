import grpc

from kirt08_contracts.auth import auth_pb2, auth_pb2_grpc


class AuthClient:
    def __init__(self, host : str):
        self.channel = grpc.aio.insecure_channel(host)
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    async def telegram_complete(self, session_id: str, phone: str):
        request = auth_pb2.TelegramCompleteRequest(
            session_id = session_id,
            phone = phone,
        )
        response = await self.stub.TelegramComplete(request)
        return response
    
    async def telegram_consume(self, session_id: str):
        request = auth_pb2.TelegramConsumeRequest(
            session_id = session_id
        )
        response = await self.stub.TelegramConsume(request)
        return response
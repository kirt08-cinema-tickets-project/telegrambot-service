from pydantic import BaseModel

class GrpcConfig(BaseModel):
    host : str = ""
    port : str = ""
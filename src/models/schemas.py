from pydantic import BaseModel

class UserQuery(BaseModel):
    user_id: str
    query: str

class ChatResponse(BaseModel):
    response_id: str
    message: str
    timestamp: str
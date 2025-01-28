from typing import Optional
from target.pydantic import BaseModel


class MsgPayload(BaseModel):
    msg_id: Optional[int]
    msg_name: str

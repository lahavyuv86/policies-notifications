from typing import Mapping

from pydantic import BaseModel


class ActionMessage(BaseModel):
    # tenantId?
    # properties, some defined id? notification_id ?

    class Config:
        orm_mode = True


class Event(BaseModel):
    dataId: str
    text: str

    class Config:
        orm_mode = True


class Action(BaseModel):
    tenantId: str
    properties: Mapping[str, str]
    # event: Event (needs to be reduced Event)

    class Config:
        orm_mode = True


class Notification(BaseModel):
    tenantId: str
    insightId: str
    tags: Mapping[str, str]
    triggers: Mapping[str, str]

# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr

class EventTodoEntity(BaseModel):
    """
    EventTodoEntity
    """
    id: StrictFloat = ...
    title: StrictStr = ...
    color: Optional[StrictStr] = ...
    checked: StrictBool = ...
    event_id: Optional[StrictFloat] = Field(..., alias="eventId")
    __properties = ["id", "title", "color", "checked", "eventId"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EventTodoEntity:
        """Create an instance of EventTodoEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if color (nullable) is None
        # and __fields_set__ contains the field
        if self.color is None and "color" in self.__fields_set__:
            _dict['color'] = None

        # set to None if event_id (nullable) is None
        # and __fields_set__ contains the field
        if self.event_id is None and "event_id" in self.__fields_set__:
            _dict['eventId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventTodoEntity:
        """Create an instance of EventTodoEntity from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EventTodoEntity.parse_obj(obj)

        _obj = EventTodoEntity.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "color": obj.get("color"),
            "checked": obj.get("checked"),
            "event_id": obj.get("eventId")
        })
        return _obj

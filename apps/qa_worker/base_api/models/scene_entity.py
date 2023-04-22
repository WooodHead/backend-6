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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictFloat, StrictStr, conlist

class SceneEntity(BaseModel):
    """
    SceneEntity
    """
    id: StrictFloat = ...
    name: StrictStr = ...
    alias: conlist(StrictStr) = ...
    description: Optional[StrictStr] = ...
    deleted: Optional[datetime] = ...
    super_id: Optional[StrictFloat] = Field(..., alias="superId")
    project_id: StrictFloat = Field(..., alias="projectId")
    __properties = ["id", "name", "alias", "description", "deleted", "superId", "projectId"]

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
    def from_json(cls, json_str: str) -> SceneEntity:
        """Create an instance of SceneEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if deleted (nullable) is None
        # and __fields_set__ contains the field
        if self.deleted is None and "deleted" in self.__fields_set__:
            _dict['deleted'] = None

        # set to None if super_id (nullable) is None
        # and __fields_set__ contains the field
        if self.super_id is None and "super_id" in self.__fields_set__:
            _dict['superId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SceneEntity:
        """Create an instance of SceneEntity from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SceneEntity.parse_obj(obj)

        _obj = SceneEntity.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "alias": obj.get("alias"),
            "description": obj.get("description"),
            "deleted": obj.get("deleted"),
            "super_id": obj.get("superId"),
            "project_id": obj.get("projectId")
        })
        return _obj


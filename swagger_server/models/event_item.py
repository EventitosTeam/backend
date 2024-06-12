# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util
from swagger_server.database import db



class EventItem(db.Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    __tablename__ = 'event_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desciption = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    event_place_lat = db.Column(db.String(100), nullable=False)
    event_place_lon = db.Column(db.String(100), nullable=False)
    people_limit = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, date, event_place_lat, event_place_lon, people_limit):
        self.name = name
        self.desciption = description
        self.date = date
        self.event_place_lat = event_place_lat
        self.event_place_lon = event_place_lon
        self.people_limit = people_limit

    # def __init__(self, name: str=None, desciption: str=None, _date: str=None, event_place_lat: str=None, event_place_lon: str=None, people_limit: int=None):  # noqa: E501
    #     """EventItem - a model defined in Swagger

    #     :param name: The name of this EventItem.  # noqa: E501
    #     :type name: str
    #     :param desciption: The desciption of this EventItem.  # noqa: E501
    #     :type desciption: str
    #     :param _date: The _date of this EventItem.  # noqa: E501
    #     :type _date: str
    #     :param event_place_lat: The event_place_lat of this EventItem.  # noqa: E501
    #     :type event_place_lat: str
    #     :param event_place_lon: The event_place_lon of this EventItem.  # noqa: E501
    #     :type event_place_lon: str
    #     :param people_limit: The people_limit of this EventItem.  # noqa: E501
    #     :type people_limit: int
    #     """
    #     self.swagger_types = {
    #         'name': str,
    #         'desciption': str,
    #         '_date': str,
    #         'event_place_lat': str,
    #         'event_place_lon': str,
    #         'people_limit': int
    #     }

    #     self.attribute_map = {
    #         'name': 'name',
    #         'desciption': 'desciption',
    #         '_date': 'date',
    #         'event_place_lat': 'eventPlaceLat',
    #         'event_place_lon': 'eventPlaceLon',
    #         'people_limit': 'peopleLimit'
    #     }
    #     self._name = name
    #     self._desciption = desciption
    #     self.__date = _date
    #     self._event_place_lat = event_place_lat
    #     self._event_place_lon = event_place_lon
    #     self._people_limit = people_limit

    # @classmethod
    # def from_dict(cls, dikt) -> 'EventItem':
    #     """Returns the dict as a model

    #     :param dikt: A dict.
    #     :type: dict
    #     :return: The EventItem of this EventItem.  # noqa: E501
    #     :rtype: EventItem
    #     """
    #     return util.deserialize_model(dikt, cls)

    # @property
    # def name(self) -> str:
    #     """Gets the name of this EventItem.

    #     Nombre del evento  # noqa: E501

    #     :return: The name of this EventItem.
    #     :rtype: str
    #     """
    #     return self._name

    # @name.setter
    # def name(self, name: str):
    #     """Sets the name of this EventItem.

    #     Nombre del evento  # noqa: E501

    #     :param name: The name of this EventItem.
    #     :type name: str
    #     """
    #     if name is None:
    #         raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

    #     self._name = name

    # @property
    # def desciption(self) -> str:
    #     """Gets the desciption of this EventItem.

    #     Descripcion del evento  # noqa: E501

    #     :return: The desciption of this EventItem.
    #     :rtype: str
    #     """
    #     return self._desciption

    # @desciption.setter
    # def desciption(self, desciption: str):
    #     """Sets the desciption of this EventItem.

    #     Descripcion del evento  # noqa: E501

    #     :param desciption: The desciption of this EventItem.
    #     :type desciption: str
    #     """
    #     if desciption is None:
    #         raise ValueError("Invalid value for `desciption`, must not be `None`")  # noqa: E501

    #     self._desciption = desciption

    # @property
    # def _date(self) -> str:
    #     """Gets the _date of this EventItem.

    #     Fecha del evento  # noqa: E501

    #     :return: The _date of this EventItem.
    #     :rtype: str
    #     """
    #     return self.__date

    # @_date.setter
    # def _date(self, _date: str):
    #     """Sets the _date of this EventItem.

    #     Fecha del evento  # noqa: E501

    #     :param _date: The _date of this EventItem.
    #     :type _date: str
    #     """
    #     if _date is None:
    #         raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

    #     self.__date = _date

    # @property
    # def event_place_lat(self) -> str:
    #     """Gets the event_place_lat of this EventItem.

    #     Latitud del evento  # noqa: E501

    #     :return: The event_place_lat of this EventItem.
    #     :rtype: str
    #     """
    #     return self._event_place_lat

    # @event_place_lat.setter
    # def event_place_lat(self, event_place_lat: str):
    #     """Sets the event_place_lat of this EventItem.

    #     Latitud del evento  # noqa: E501

    #     :param event_place_lat: The event_place_lat of this EventItem.
    #     :type event_place_lat: str
    #     """
    #     if event_place_lat is None:
    #         raise ValueError("Invalid value for `event_place_lat`, must not be `None`")  # noqa: E501

    #     self._event_place_lat = event_place_lat

    # @property
    # def event_place_lon(self) -> str:
    #     """Gets the event_place_lon of this EventItem.

    #     Longitud del evento  # noqa: E501

    #     :return: The event_place_lon of this EventItem.
    #     :rtype: str
    #     """
    #     return self._event_place_lon

    # @event_place_lon.setter
    # def event_place_lon(self, event_place_lon: str):
    #     """Sets the event_place_lon of this EventItem.

    #     Longitud del evento  # noqa: E501

    #     :param event_place_lon: The event_place_lon of this EventItem.
    #     :type event_place_lon: str
    #     """
    #     if event_place_lon is None:
    #         raise ValueError("Invalid value for `event_place_lon`, must not be `None`")  # noqa: E501

    #     self._event_place_lon = event_place_lon

    # @property
    # def people_limit(self) -> int:
    #     """Gets the people_limit of this EventItem.

    #     Limite de la cantidad de personas que puede acceder a un evento  # noqa: E501

    #     :return: The people_limit of this EventItem.
    #     :rtype: int
    #     """
    #     return self._people_limit

    # @people_limit.setter
    # def people_limit(self, people_limit: int):
    #     """Sets the people_limit of this EventItem.

    #     Limite de la cantidad de personas que puede acceder a un evento  # noqa: E501

    #     :param people_limit: The people_limit of this EventItem.
    #     :type people_limit: int
    #     """
    #     if people_limit is None:
    #         raise ValueError("Invalid value for `people_limit`, must not be `None`")  # noqa: E501

    #     self._people_limit = people_limit

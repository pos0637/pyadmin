# -*- coding: UTF-8 -*-

from field import Field


class Entity:
    """
    实体
    """

    def __init__(self):
        # 索引
        self.id = ''

        # 名称
        self.name = ''

        # 父实体
        self.parent = ''

        # 字段
        self.fields = []

    def readFromJson(dict):
        entity = Entity()
        entity.__dict__ = dict.copy()
        entity.fields = []
        for item in dict['fields']:
            entity.fields.append(Field.readFromJson(item))

        return entity

    def writeToJson(self):
        return self.__dict__

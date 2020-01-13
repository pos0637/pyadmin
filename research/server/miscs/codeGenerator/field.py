# -*- coding: UTF-8 -*-


class Field:
    """
    字段
    """

    fieldType = {
        'int': 'IntegerField',
        'bigint': 'BigIntegerField',
        'float': 'FloatField',
        'varchar': 'CharField',
        'text': 'TextField',
        'blob': 'BinaryField',
        'date': 'DateField'
    }

    def __init__(self):
        # 索引
        self.id = ''

        # 名称
        self.name = ''

        # 类型
        self.type = ''

        # 选项
        self.options = []

        # 关系
        self.relationship = []

    def getType(self):
        """
        获取类型

        Returns:
            [string] -- 类型
        """
        return Field.fieldType[self.type]

    def getOptions(self):
        """
        获取选项

        Returns:
            [string] -- 选项
        """
        return ''

    def readFromJson(dict):
        field = Field()
        field.__dict__ = dict.copy()
        return field

    def writeToJson(self):
        return self.__dict__

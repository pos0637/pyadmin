# -*- coding: UTF-8 -*-

import json
from jinja2 import Environment, FileSystemLoader
from codeGenerator import CodeGenerator
from entity import Entity


class DjangoModelGenerator(CodeGenerator):
    """
    Django模型代码生成器
    """

    def generate(self, content):
        """
        生成代码

        Arguments:
            content {string} -- 序列化内容
        """
        entities = []
        list = json.loads(content)
        for item in list:
            entities.append(Entity.readFromJson(item))

        env = Environment(loader=FileSystemLoader('./'))
        tpl = env.get_template('model_template.py')
        for entity in entities:
            render_content = tpl.render(entity=entity)
            print(render_content)

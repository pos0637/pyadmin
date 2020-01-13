# -*- coding: UTF-8 -*-

import json
from entity import Entity
from field import Field
from djangoModelGenerator import DjangoModelGenerator

entities = []
for i in range(0, 10):
    entity = Entity()
    entity.name = f'entity{i}'
    for j in range(0, 3):
        field = Field()
        field.id = '123'
        field.name = f'field{j}'
        field.type = 'bigint'
        field.options = ['1', '2']
        entity.fields.append(field)
    entities.append(entity)

content = json.dumps(entities, default=lambda o: o.writeToJson())
print(content)

generator = DjangoModelGenerator()
generator.generate(content)

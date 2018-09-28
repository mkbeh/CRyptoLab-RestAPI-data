# -*- coding: utf-8 -*-
import json
import functools

import hug
import utils

from pymongodb.pymongodb import MongoDB


@hug.get('/api')
def api():
    return {'status': 'ok'}


@hug.get('/news/{parser_name}&limit={limit}&skip={skip}')
def news(parser_name: str, limit: int, skip: int):
    mongo = MongoDB(parser_name)

    # Get day obj and date.
    from datetime import datetime
    day = datetime.today().day
    date = datetime.today().strftime('{}.%m.%Y')

    # Find documents.
    documents = mongo.find({'date': date.format(day)}, 'news', limit, skip)

    if not documents:
        documents = mongo.find({'date': date.format(day - 1)}, 'news', limit, skip)

    mongo.finish()

    return json.dumps(list(map(functools.partial(utils.del_dict_item, key_name='_id'), documents)))


@hug.get('/ico/{parser_name}&cat={cat}&limit={limit}&skip={skip}')
def ico(parser_name: str, cat: str, limit: int, skip: int):
    mongo = MongoDB(parser_name)
    documents = mongo.find({}, cat, limit, skip)
    mongo.finish()

    return json.dumps(list(map(functools.partial(utils.del_dict_item, key_name='_id'), documents)))

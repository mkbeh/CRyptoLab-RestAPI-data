# -*- coding: utf-8 -*-


def del_dict_item(dict_, key_name):
    """
    Func which delete specific dict item by key.
    :param dict_:
    :param key_name:
    :return:
    """
    dict_copy = dict_.copy()

    for key in dict_copy:
        if key == key_name:
            del dict_[key]

    return dict_

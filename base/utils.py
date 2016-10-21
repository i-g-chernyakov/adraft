# $Id: utils.py 7464 2016-10-13 13:16:03Z milde $
# Author: Igor Chernyakov <i.g.chernyakov@yandex.ru>
# Copyright: This module has been placed in the public domain.

"""
Set of functions

"""

__docformat__ = 'restructuredtext'

#import markups


def get_class_name_plural(object):
    """ Return of instance

    :param object:
    :return: plural form for class name of object
    """
    return '{1}s'.format(object.__class__.__name__.lower())

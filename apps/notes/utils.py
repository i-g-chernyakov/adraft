def get_class_name_plural(instance):
    """ Return of instance

    :param instance:
    :return: plural form for class name of object
    """
    return '{}s'.format(instance.__class__.__name__.lower())

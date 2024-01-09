import math


def NULL_not_found(object: any) -> int:
    type_object = type(object)
    if type_object is type(None):
        print('Nothing:', object, type_object)
    elif type_object == float and math.isnan(object):
        print('Cheese:', object, type_object)
    elif object == 0:
        print('Zero:', object, type_object)
    elif type_object == str and len(object) == 0:
        print('Empty:', type_object)
    elif object is False:
        print('Fake:', object, type_object)
    else:
        print('Type not found')
        return 1
    return 0

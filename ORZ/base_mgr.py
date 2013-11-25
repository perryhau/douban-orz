from functools import wraps

class OrmItem(object):
    def __init__(self, field_name):
        self.field_name = field_name

    def __set__(self, obj, value):
        value = int(value) if type(value) == bool else value

        if not obj._initted:
            setattr(obj, "hidden____org_" + self.field_name, value)
        else:
            obj.dirty_fields.add(self.field_name)

        setattr(obj, "hidden____" + self.field_name, value)

    def __get__(self, obj, objtype):
        return getattr(obj, "hidden____" + self.field_name, None)


class OrzField(object):
    class KeyType(object):
        NOT_INDEX, DESC, ASC, AD = range(4)

    def __init__(self, as_key=KeyType.NOT_INDEX, default=None):
        self.name = None
        self.as_key = as_key
        self.default = default

# def orz_custom_cache(*related_key_names):
#     def __(func):
#        def _(cls, *a, **kw):
#            return cls.objects.gets_custom(func, a, kw)
#        _.related_key_names = related_key_names
#        return _
#     return __

def orz_get_multi(func):
    @wraps(func)
    def __(self_or_cls, *a, **kw):
        return self_or_cls.objects.get_multiple_ids(func(self_or_cls, *a, **kw))
    return __

if __name__=='__main__':
    pass
    # for i in A.__dict__:
    #     print i
    # A.name = OrmItem('name')
    # a = A()
    # a.name = 10
    # print a.name
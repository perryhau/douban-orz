# -*- coding:utf8 -*-

def create(cls, **kwargs):
    ins = cls.objects.create(kwargs)
    return ins


def delete(self):
    return self.objects.delete(self)


def save(self):
    return self.objects.save(self)


def create_transactionally(cls, **kwargs):
    ins = cls.objects.create(kwargs, True)
    return ins


def delete_transactionally(self):
    return self.objects.delete(self, True)


def save_transactionally(self):
    return self.objects.save(self, True)


def getstate(self):
    ret = {'dict': self.__dict__.copy(), 'db_fields': {}}

    for i in self.db_fields:
        ret['db_fields'][i] = getattr(self, i)

    return ret

def exist(cls, **conditions):
    ret = cls.count_by(**conditions)
    return ret > 0


def setstate(self, state):
    self.__dict__.update(state['dict'])
    self._initted = False
    for i in self.db_fields:
        setattr(self, i, state['db_fields'][i])
    self._initted = True


def init(self, to_create=True, *a, **kw):
    self.to_create = to_create
    self._initted = False
    self.dirty_fields = set()
    for i in self.db_fields:
        val = kw.pop(i)
        setattr(self, i, val)
    self._initted = True

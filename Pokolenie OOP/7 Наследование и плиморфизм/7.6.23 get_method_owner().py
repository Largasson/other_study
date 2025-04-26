def get_method_owner(cls, method):
    for mro_cls in cls.mro():
        if method in mro_cls.__dict__:
            return mro_cls


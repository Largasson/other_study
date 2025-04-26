class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.__mro__)

    @staticmethod
    def class_by_index(cls, index=0):
        return cls.mro()[index]

    @staticmethod
    def index_by_class(child, parent):
        return child.__mro__.index(parent)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.index_by_class(D, A))
# from functools import wraps
# def decorator(deco):
#     def act_deco(func):
#         @wraps(func)
#         def new_func(*args, **kwargs):
#             return deco(func, *args, **kwargs)
#
#         return new_func
#
#     return act_deco
#
#
@decorator
def introduce(f, *args, **kwargs):
    print(f.__name__)
    return f(*args, **kwargs)

@introduce
def identity(x):
    return x


print(identity(31415))
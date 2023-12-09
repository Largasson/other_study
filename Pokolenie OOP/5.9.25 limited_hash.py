def limited_hash(left, right, hash_function=hash):
    def fun(obj):
        obj = hash_function(obj)
        if left <= obj <= right:
            return obj
        elif obj > right:
            return left + (obj-right - 1) % (right - left + 1)
        elif obj < right:
            return right - (left - obj - 1) % (right - left + 1)
    return fun

#вариант 2
# def limited_hash(left, right, hash_function=hash):
#     def inner_hash_function(x):
#         return left + (hash_function(x) - left) % (right - left + 1)
#     return inner_hash_function
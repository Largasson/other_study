from functools import wraps


def introduce(*dec_args, **dec_kwargs):
    def act_introduce(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            num = dec_kwargs['repeat']
            print(f'Запуск функции: {func.__name__}\n' * num)
            return func(*args, **kwargs)

        return wrapper

    return act_introduce

@introduce()
def identify(x):
    return x


print(identify(456))
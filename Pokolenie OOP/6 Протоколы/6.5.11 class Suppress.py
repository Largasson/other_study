class Suppress:
    def __init__(self, *args):
        self.exc = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exc:
            self.exception = exc_val
            return True
        return False

with Suppress() as context:
    print('All success!')

print(context.exception)
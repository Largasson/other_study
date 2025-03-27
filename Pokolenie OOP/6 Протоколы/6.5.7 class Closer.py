class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.obj, 'close'):
            self.obj.close()
        else:
            print("Незакрываемый объект")

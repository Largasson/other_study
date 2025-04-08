class EasyDict(dict):
    def __getattr__(self, attr):
        return self[attr]


easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)
class Tripleton(type):
    _instances: dict
    counter = 0

    def __call__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        if args:
            obj_n = args[0]
            if isinstance(obj_n, int) and 1 <=obj_n<=3:
                del cls._instances[obj_n]
                cls._instances[obj_n] = super().__call__(*args, **kwargs)
                return cls._instances[obj_n]
            else:
                raise Exception(f'{obj_n} is not allowed')
        c = cls.__class__.counter
        c += 1
        while c < 3:
            cls._instances[c] = super().__call__(cls.__name__, (),  {})
        return cls._instances[c]

    
class Tri(metaclass = Tripleton):
    _instances = dict(zip(range(1, 4), [None for _ in range(3)]))
    def __init__(self, n=None):
        print(n)
        print("Initialising...")

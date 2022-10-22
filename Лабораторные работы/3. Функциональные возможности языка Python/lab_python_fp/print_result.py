def print_result(f):
    def wrapper(*args, **kwargs):
        print(f.__name__)

        res = f(*args, **kwargs)
        if type(res) == list:
            for i in res: 
                print(i)
        elif type(res) == dict:
            for k,v in res.items():
                print(k, '=', v)
        else:
            print(res)

        print()

        return res

    return wrapper 

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


@print_result
def test_5(a, b):
    return a + b

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5(10, 15)
import random

def gen_random(count, begin, end):
    for _ in range(count):
        yield random.randint(begin, end)

if __name__ == '__main__':
    gen_f = gen_random(5, 1, 3)
    for i in gen_f:
        print(i)
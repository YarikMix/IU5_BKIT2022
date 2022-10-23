class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.r = []
    
        if ignore_case:
            items = [i.lower() for i in items]

        for i in items:
            if i not in self.r:
                self.r.append(i)

    def __next__(self):
        if self.begin < len(self.r):
            x = self.r[self.begin]
            self.begin += 1
            return x
        else:
            raise StopIteration

    def __iter__(self):
        self.begin = 0
        return self

def print_test(data, ignore_case=False):
    print("-" * 50)
    for i in Unique(data, ignore_case):
        print(i)

if __name__ == '__main__':
    data = [1, 4, 87, 3, 5, 7, 2, 4, 6, 4, 3, 6, 3, 4, 2]
    test = Unique(data)
    print_test(test)

    data = ['A', 'a', 'B', 'b']
    test = Unique(data)
    print_test(data)

    test = Unique(data, ignore_case=True)
    print_test(data)

def hello_world():
    print('Hello world')


def summ(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    hello_world()
    print(summ(10, 12))

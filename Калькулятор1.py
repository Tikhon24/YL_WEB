import sys

try:
    if len(sys.argv) != 3:
        raise BaseException
    numbers = [int(sys.argv[-2]), int(sys.argv[-1])]
    print(sum(numbers))
except BaseException:
    print(0)


import itertools

if __name__ == '__main__':

    print("*" * 80)
    for each in itertools.product("abc", "xy"):
        print(each)

    print("*" * 80)
    for each in itertools.product("abc", repeat=2):
        print(each)

    print("*" * 80)
    for each in itertools.permutations("abc", 2):
        print(each)

    print("*" * 80)
    for each in itertools.combinations("abc", 2):
        print(each)

    print("*" * 80)
    for each in itertools.combinations_with_replacement("abc", 2):
        print(each)

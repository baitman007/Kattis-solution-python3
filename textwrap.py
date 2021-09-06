def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        x = string[i:i + max_width]
        if len(x) == max_width:
            print(x)
        else:
            return x


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

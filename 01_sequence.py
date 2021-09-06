def Seq():
    User_input = input().strip()
    inversions, count, zeros = 0, 1, 0
    for i in reversed(User_input):
        if i == "1":
            inversions += zeros
        elif i == "0":
            zeros += count
        else:
            inversions += inversions + zeros
            zeros += zeros + count
            count += count
        inversions = inversions % 1000000007
        zeros = zeros % 1000000007
        count = count % 1000000007
    print(inversions)


if __name__ == "__main__":
    Seq()

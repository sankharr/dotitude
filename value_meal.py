numTests = int(input())
for i in range(numTests):
    list = [int(x) for x in input().split()]
    sum = (list[0] + list[1]) - list[2]
    print(sum)
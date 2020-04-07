firstInput = "1 2 3 8 2"
secondInput = "0 0"
firstInput = input()
secondInput = input()

firstInputList = firstInput.split()
secondInputList = secondInput.split()

i = 0
for x in firstInputList:
    temp = int(x,10)
    firstInputList[i] = temp
    # print(type(temp))
    i += 1

i = 0
for y in secondInputList:
    temp = int(y,10)
    secondInputList[i] = temp
    # print(type(temp))
    i += 1
# print(type(list))

#ad
# if secondInputList[0] == 0:
#     ad = firstInputList[0] + firstInputList[3]
#     ace = firstInputList[0] + firstInputList[2] + firstInputList[4]
#     if (ad < ace):
#             print(str(ad) + ' Walukarama Road')
#     else:
#         print(str(ace) + ' Mahanama Road')
# else:
#     be = firstInputList[1] + firstInputList[4]
#     print(str(be) + ' Galle Road')

ad = firstInputList[0] + firstInputList[3]
ace = firstInputList[0] + firstInputList[2] + firstInputList[4]
be = firstInputList[1] + firstInputList[4]

minutesList = [ad, ace, be]
minutesList.sort()
minimum = min(minutesList)

def testfunc(val):
    if val == ad:
        if (secondInputList[0] == 0):
            print(str(ad) + ' Walukarama Road')
            return 0
        else:
            return -1
    elif val == ace:
        if (secondInputList[0] == 0 & secondInputList[1] == 0):
            print(str(ace) + ' Mahanama Road')
        else:
            return -1
    else:
        if secondInputList[1] == 0:
            print(str(be) + ' Galle Road')
        else:
            return -1

if testfunc(minutesList[0]) == -1:
    if testfunc(minutesList[1]) == -1:
        result = testfunc(minutesList[2])

# if (secondInputList[0] == 0 & secondInputList[1] == 0):
#     if minimum == ad:
#         print(str(ad) + ' Walukarama Road')
#     elif minimum == ace:
#         print(str(ace) + ' Mahanama Road')
#     else:
#         print(str(be) + ' Galle Road')
#     # if ad < ace:
#     #     if ad < be:
#     #         print(str(ad) + ' Walukarama Road')
#     #     else:
#     #         print(str(be) + ' Galle Road')
#     # else:
#     #     if ace < be:
#     #         print(str(ace) + ' Mahanama Road')
#     #     else:
#     #         print(str(be) + ' Galle Road')
#
# elif secondInputList[0] == 0 & secondInputList[1] == 1:
#     print(str(ad) + ' Walukarama Road')
#     #
#     # # ad = firstInputList[0] + firstInputList[3]
#     # # ace = firstInputList[0] + firstInputList[2] + firstInputList[4]
#     # if (ad < ace):
#     #     print(str(ad) + ' Walukarama Road')
#     # else:
#     #     print(str(ace) + ' Mahanama Road')
# else:
#     # be = firstInputList[1] + firstInputList[4]
#     print(str(be) + ' Galle Road')
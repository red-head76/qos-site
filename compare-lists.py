import re

list1_raw = []
list2_raw = []
list1 = []
list2 = []
with open("./non-website-publikationen.txt", 'r') as readlist1:
    list1_raw = (readlist1.readlines())

for item in list1_raw:
    item = item.translate({ord(i): None for i in "1234567890"})[1:-1]

    if len(item.replace(' ', '')) != 0:
        if item[-1] == ' ':
            item = item[:-1]
        # print(item)
        list1.append(item)

with open("./non-website-publikationen2.org", 'r') as readlist2:
    list2_raw = (readlist2.readlines())


for item in list2_raw:
    item = item.replace("* TODO ", '')
    item = item.replace('\n', '')
    if len(item.replace(' ', '')) != 0:
        list2.append(item)

not_in_1 = []
not_in_2 = []

for item in list1:
    if item not in list2:
        not_in_2.append(item)

for item in list2:
    if item not in list1:
        not_in_1.append(item)

# print(not_in_1)
# print('\n')
# print('\n')
# print('\n')
# print(not_in_2)

final = (list1 + not_in_1)# .sort(key=str.lower)

print(len(list1), '\n', len(not_in_1), '\n', len(final))
# with open("./non-website-publikationen-final.txt", 'w') as finallist:
#     finallist.writelines(final)

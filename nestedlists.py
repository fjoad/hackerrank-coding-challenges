grades_dict = {}
list1 = []
list2 = []
list3 = []
temp =""
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    grades_dict.update({score:name})
list1 = sorted(grades_dict)
i = 0
while list1[i]==list1[i+1]:
    i=i+1
i=i+1
for j in range (6):
    list2.append(list1[i])
    if list1[i]==list1[i+1]:
        i = i+1
    else:
        break
for q in list2:
    temp = grades_dict[q]
    list3.append(temp)
for r in list3:
    print r
    

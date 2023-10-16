list1 = ["Malika", 1, True]
list2 = ["Bhavya", 2, True]
print(list1)

list:list = []
list.append("Malika")
print(list)

attendees = ["Malika","Bhavya","Lakshmi"]
attendees.insert(1,"Yasshu")
print(attendees)

attendees = ["malika","bhavya","bharath"]
print(attendees.index("bharath"))

attendees=["bhavya","malika","bharath","malika","malika"]
print(attendees.count("malika"))

attendees=["bhavya","malika","bharath"]
print(attendees.count("priyam"))

attendees = ["malika","priyam","bhavya","prasaduu"]
attendees[3]= "prasad"
print(attendees)

attendees = ["malika","priyam","bhavya"]
attendees1 = ["lakshmi","bharath","mani"]
attendees.extend(attendees1)
print(attendees,attendees1)

attendees=["malika","priyam","bhavya"]
attendees.remove("priyam")
print(attendees)

attendees = ["malika","priyam","bhavya","prasad"]
attendees.pop(0)
print(attendees)

attendees = ["malika","bhavya","prasad","priyam"]
attendees.pop()
print(attendees)



my_dict={"name":"alice","age":"24","location":"Tennesse"}
print(my_dict)

print(my_dict['name']) #'name'이라는 키가 가지고 있는 값은?
print(my_dict['age'])

user1={"name":"Bob", "age":30, "location":"Busan"}
print(user1['name'])

user1["age"]=31
print(user1['age'])

user1["car"]="Mustang"
print(user1['car'])

#키값 지움
del user1['car']
print(user1)

print(user1.keys())
print(user1.values())
print(user1.items())

user_items=user1.items()
useritem_list=list(user_items)
print(useritem_list)
print(useritem_list[1])
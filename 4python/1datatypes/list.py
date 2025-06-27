my_list= [0,1,2,3,4]
another_list = [7,8,9]

print(my_list[0:6])

my_list.append(6)
print(my_list)
my_list.insert(2,10)
print(my_list)

my_list.extend(another_list)
print(my_list)

my_list.remove(10) #리스트에서 10이라는 숫자 삭제
print(my_list)

my_list.pop(3) #리스트에서 인덱스 3의 숫자 삭제
print(my_list)

my_list.pop() #리스트에서 마지막 인덱스의 숫자 삭제
print(my_list)

my_list.clear() #리스트 날리기
print(my_list)

print('-'*10)
my_list=[1,2,3,4,5,6,3,2,1]

print(my_list.index(3)) #숫자 3의 인덱스는?
print(my_list.count(3)) #숫자 2의 개수는?

sorted_list=sorted(my_list) #return 있음, 원본 변경 x
print(sorted_list)

my_list.sort() #return값 없음
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse() #현재 리스트를 역순으로 전환
print(my_list)

my_list2=my_list.copy() #리스트 복제
print(my_list2)

#리스트 컴프리헨션
#리스트 안에 반복문 또는 조건문으 ㄹ통해 리스트 안에 채워질 요소 정의하는 문법
numbers=[x for x in range(10)]
print(numbers)

numbers=[num for num in range(1,11)] #1~10
print(numbers)

numbers=[num for num in range(1,11) if num%2 == 0] #짝수만
print(numbers)
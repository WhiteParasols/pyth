my_list= (0,1,2,3,4)

print(my_list)

#my_list[2]=5 #오류

my_list = list(my_list)
my_list[2]=5
print(my_list)

#튜플 언패킹= 튜플안의 데이터를 여러개의 변수로 나눠 담을수 있음
a,b,c=(1,2,3) #받아와서 안쓸 변수를 _로 표시
print(c)

a,b,_=(1,2,3) #받아와서 안쓸 변수를 _로 표시
print(a)
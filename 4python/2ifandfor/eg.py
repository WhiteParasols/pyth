numbers=[1,2,3,4,5,6,7,8,9,10]

def evenNumber(numbers):
    even_numbers=[]
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
    return even_numbers

even=evenNumber(numbers)
print("짝수", even)

students={
    'aa':70,
    'bb':80,
    'cc':70,
    'dd':68,
    'ee':99,
    'ff':76,
    'gg':61,
    'hh':85,
}
Astudent=[];
for student,grade in students.items():
    if int(grade)>90:
        Astudent.append(student)

print(Astudent)

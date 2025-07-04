#기본수학연산
import math

print(math.pi)

#원의 넓이를 구하려면
radius=5
area=math.pi*radius**2
area2=math.pi*math.pow(radius,2)
print(f"반지름이 {radius}인 원 넓이 {area2:.2f}")
print(f"반지름이 {radius}인 원 넓이 {area2:<10.2f}")
print(f"반지름이 {radius}인 원 넓이 {area2:>10.2f}")

text='hi'
print(f"[{text:<10}]")
print(f"[{text:>10}]")
print(f"[{text:^10}]")
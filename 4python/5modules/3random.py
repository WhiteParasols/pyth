import random
print("랜덤 숫자: ", random.randint(1,100)) #1부터 100까지의 양수

#주사위
def roll_dice():
    return random.randint(1,6)
print(f"주사위 던진 결과: {roll_dice()}")

counts=[0,0,0,0,0,0]
def roll_dices(numbers):
    for i in range(numbers):
        n=roll_dice()  
        counts[n-1]+=1      

roll_dices(10_000)
for i in range(6):
    print(f"{i+1}나온 횟수:{counts[i]} 확률: {counts[i]/sum(counts)}")

# counts2 ={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
counts2={i:0 for i in range(1,7)}
print(counts2)

def roll_dice2(numbers):
    for _ in range(numbers):
        result=roll_dice()
        counts2[result]+=1

roll_dice2(100)

for dice_num, dice_count in counts2.items():
    print(f"주사위 수 {dice_num} 횟수  {dice_count}")
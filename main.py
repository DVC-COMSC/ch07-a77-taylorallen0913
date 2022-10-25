
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************

num3 = []
counter = 0

final_len = len(num1) + len(num2)

while len(num3) <= final_len:
    if len(num1) == 0:
        num3 = num3 + num2
        break
    elif len(num2) == 0:
        num3 = num3 + num1
        break

    if counter % 2 == 0:
        num3.append(num1.pop(0))
    elif counter % 2 == 1:
        num3.append(num2.pop(0))

    counter += 1

print(num3)
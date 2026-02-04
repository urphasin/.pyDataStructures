import math
import random

print("🏀 Basketball Shot Trainer")



perfectAngle = random.randint(35, 55)
perfectPower = random.randint(40, 80)

number_of_rounds = 10

for i in range(number_of_rounds):
    angle = int(input("Enter shot angle: "))
    power = int(input("Enter shot power: "))

    error = math.sqrt((angle - perfectAngle)**2 + (power - perfectPower)**2)

    if(error == 0 or error <= 1):
        print("✅Swish! Perfect shot!")
        break
    elif(error <= 2):
        print("So close!")
    elif(error <= 5):
        print("Close")
    else:
        print("Way off")
    print("❌Miss — error score:",error, " | shots left:", number_of_rounds - 1 - i)

print("Perfect Angle:", perfectAngle)
print("Perfect Power:", perfectPower)
print("                                        Welcome to the game of Quiz ")
print("There are five questions adn each answer are 10 points so USE YOUR BRAIN")
points = 0

print("A. What is the smallest country in the world?\n 1. Nepal \n 2. Tibet \n 3. Vatican City \n 4. Berlin")
num = int(input())
if num == 3:
    points += 10
    print("Your answer is write")
else:
    print("Your answer is wrong")


print("B.What is the largest animal on the planet? \n 1. Elephant \n 2. Giraffe \n 3. Blue Whale \n 4. Rhino")
num = int(input())
if num == 3:
    points += 10
    print("Your answer is write")
else:
    print("Your answer is wrong")
print("C.What is the hottest continent on the earth? \n 1.America  \n 2. Asia \n 3. Europe \n 4. Africa")
num = int(input())
if num == 4:
    points += 10
    print("Your answer is write")
else:
    print("Your answer is wrong")
print("C.What is the longest river on the earth? \n 1.Karnali \n 2. Nile \n 3. Amazon \n 4. Ganga ")
num = int(input())
if num == 2:
    points += 10
    print("Your answer is write")
else:
    print("Your answer is wrong")
print("C.How many continent are there in the earth? \n 1.5 \n 2. 7 \n 3. 6 \n 4. 9 ")
num = int(input())
if num == 2:
    points += 10
    print("Your answer is write")
else:
    print("Your answer is wrong")

print(f"(Your total points is : {points})")
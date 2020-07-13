# Guessing game two players prototype

arr = []
output = int(input("enter the length of the character for words: "))
print("Enter the Alphabets: ")
for i in range(output):
    data = str(input())
    arr.append(data)

n = 5
while n > 0:
    arr1 = []
    output1 = int(input("enter the length of the character for words: "))
    print("Enter the Alphabets: ")
    for j in range(output1):
        data1 = str(input())
        arr1.append(data1)
    if arr1[j] != arr[i]:
        print("try again")
        n = n - 1
    elif arr1[j] == arr[i]:
        print("YOU WON!!")
        break
if arr1[j] != arr[i]:
    print("GAME OVER,YOU LOST!!")
else:
    pass



# Another prototype
   word = "naresh"
turns = 5

while turns > 0:
    output = input("\nenter the guess: ")
    for char in word:
        if char in output:
            print(char, end= " ")
            temp = char

        else:
            print("_", end= " ")

    turns = turns - 1
    if output == word:
        print("\nyou won")


        break
    else:
        print("\ntry again")
    print("\n", temp)

print("you lose the game")





# Guessing game two players prototype
#
# arr = []
# output = int(input("enter the length of the character for words: "))
# print("Enter the Alphabets: ")
# for i in range(output):
#     data = str(input())
#     arr.append(data)
#
# n = 5
# while n > 0:
#     arr1 = []
#     output1 = int(input("enter the length of the character for words: "))
#     print("Enter the Alphabets: ")
#     for j in range(output1):
#         data1 = str(input())
#         arr1.append(data1)
#     if arr1[j] != arr[i]:
#         print("try again")
#         n = n - 1
#     elif arr1[j] == arr[i]:
#         print("YOU WON!!")
#         break
# if arr1[j] != arr[i]:
#     print("GAME OVER,YOU LOST!!")
# else:
#     pass



# Another prototype
    for char in word:
        if char in guess:
            print(char, end= " ")
        else:
            print("_", end= " ")
    turns = turns - 1
    if guess == word:
            print("\nYOU WON!!")
            break
    else:

word = "secret"
guess = input("ENTER YOUR GUESSES: ")
turns = 5
while turns > 0:
        guess = input("\nENTER YOUR GUESSES: ")


if guess != word:
    print("you lost!! game over")
else:
    pass







num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even...")
else:
    print(f"{num} is odd...")
    

def palindrome(word):
    return word == word[::-1]

def square_n_cube(num):
    return num ** 2, num ** 3

def greet():
    print("good afternoon")
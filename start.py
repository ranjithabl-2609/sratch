num = int(input("Enter a number: "))
if num % 2 != 0:
    print(f"{num} is odd...")
else:
    print(f"{num} is even...")
    

def palindrome(word):
    return word == word[::-1]

def square_n_cube(num):
    return num ** 2, num ** 3

# pyramid with number - pola 1

print("----------------------------")

print("\nPOLA 1")

number = 10

for num in range(number):

    for i in range(num):

        print(num, end=' ') 

    print('\n')

print("----------------------------")




# pyramid with number - pola 2

print("\nPOLA 2\n")

number = 9

for i in range(number):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

print("----------------------------")


# pyramid with number - pola 3

print("\nPOLA 3")

number = 9

for i in range(num, -1, -1):
    for j in range(number, i, -1):
        print(j, end=" ")
    print("\n")

print("----------------------------")

# pyramid with number - pola 4

print("\nPOLA 4\n")

number = 9

for num in range(number, 0, -1):
    # j = number
    for i in range(num, number+1):
        print(num, end=" ")
    print("\n")

print("----------------------------")


# pyramid with number - pola 5

print("\nPOLA 5\n")

number = 9

k = 0

for i in range(number, 0, -1):
    k += 1
    for j in range(1, i + 1):
        print(k, end=' ')
    print('\n')

print("----------------------------")


# pyramid with number - pola 6

print("\nPOLA 6\n")

number = 9

for i in range(number, 0, -1):

    for j in range(1, i + 1):
        print(j, end=' ')
        
    print('\n')

print("----------------------------")


# pyramid with number - pola 7

print("\nPOLA 7\n")

number = 9

for i in range(0, number):

    for j in range(number, i, -1):
        print(j, end=' ')
        
    print('\n')

print("----------------------------")



# pyramid with number - pola 8

print("\nPOLA 8\n")

number = 9

for i in range(number, 0, -1):  
    n = i   
    for j in range(0, i):  
        print(n, end=' ')  
    print("\n")  

print("----------------------------")

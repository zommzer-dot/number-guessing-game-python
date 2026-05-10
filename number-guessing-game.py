import random
name=input("whats your name")
print(name+" Iam guessing a number between 1 and 10")
secret_number = random.randint(1, 10)
attempts=5
guess_count=0
while guess_count < attempts:
    num = int(input("Enter a number: "))
    guess_count += 1

    if num < secret_number:
        print("Your guess is too low")

    elif num > secret_number:
        print("Your guess is too high")
    elif num == secret_number:
        print("you guessed the correct number "+str(guess_count)+" tries")
        break
    else :
        print("sorry no more attempts "+str(guess_count)+" tries")
        break
    

    
    
    
    
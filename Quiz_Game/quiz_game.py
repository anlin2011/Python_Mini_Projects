print("Welcome to Computer Fundamental Quiz!")

playing = input("Do you want to play?(yes/no): ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

answer = input("1. What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("2. Who is known as the Father of Computer? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("3. What does RAM stands for? ")
if answer.lower() == 'random access memory':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("4. What is the Brain of a Computer System called? ")
if answer.lower() == 'cpu':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("5. What is known as Temporary Memory or Volatile Memory? ")
if answer.lower() == 'ram':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("6. What does ALU stand for in the context of computers? ")
if answer.lower() == 'arithmetic logic unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("7. What is meant by GUI in Computers? ")
if answer.lower() == 'graphical user interface':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("8. The data or an instruction given to a computer system is particularly called? ")
if answer.lower() == 'input':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("9. The Collection of 8 bits makes: ")
if answer.lower() == 'byte':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("10. What is the full form of USB? ")
if answer. lower() == 'universal serial bus':
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
    
    

    

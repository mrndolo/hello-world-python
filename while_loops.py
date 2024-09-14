#while loops - execute block of code multiple tims
'''
while condotion:
,,,
'''
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

#guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry, you've failed!")
'''
begin = input('>')
if begin.lower() == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
    car_status = input(">")
    if car_status == "start":
        print("Car started... Ready to go!")
        car_status = input(">")
    elif car_status == "stop":
        print("Car stopped!...")
        car_status = input(">")
    elif car_status == "quit":
        print("Ended!...")

else:
    print("I don't understand that...")
'''
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped!...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that.")
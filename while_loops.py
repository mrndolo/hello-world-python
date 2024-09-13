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
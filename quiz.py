print('Hello, welcome to a trivia game!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 7

if ans.lower() == 'yes':
    ans = input('1. what is my favorite color? ')
    if ans.lower() == 'blue':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans = input('2. what is 56÷4=? ')
    if ans == '14':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans = input('3. which programing language do I use ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')       


    ans = input('4. Do I like coding? ')
    if ans.lower() == 'yes':
        score += 1
        print('Correct')
    else:
        print('Incorrect')       


    ans = input('5. Do I have a dog ')
    if ans.lower() == 'yes':
        score += 1
        print('Correct')
    else:
        print('Incorrect')       


    ans = input('6. Who is my favorite viedeo game character ')
    if ans.lower() == 'kaine':
        score += 1
        print('Correct')
    else:
        print('Incorrect')       
    

ans = input('7. what computer do I use? ')
if ans.lower() == 'pc':
        score += 1
        print('Correct')
else:
        print('Incorrect')


print('Thank you for playing, you got ', score, " questions correct.")
percentage = (score/total_q) * 100

print('Score ', percentage)
print('Goodbye')
    
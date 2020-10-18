#simplest game using python (Trivia)
#basic use of if-else statement
print('Hello, Welcome to Trivia\n')

ans=input('Are you ready to play ? (yes/no)\n')
score=0
total_q=5
if ans.lower()=='yes':
    ans=input('1. Which programming language does this game use ?\n')
    if ans.lower()=='python':
        score+=1
        print('Correct ;)')
    else:
        print('Incorrect ;(')

    ans=input('2. what do you call son of javascript ?\n')
    if ans.lower()=='json':
        score+=1
        print('Correct ;)')
    else:
        print('Incorrect ;(')
    ans=input('3. Which is mutable in nature list or tuple ?\n')
    if ans.lower()=='list':
        score+=1
        print('Correct ;)')
    else:
        print('Incorrect ;(')
    ans=input('4. What is better a 1050ti or a 1060 (graphic card) ?\n')
    if ans.lower()=='1050ti':
        score+=1
        print('Correct ;)')
    else:
        print('Incorrect ;(')
    ans=input('5. Is python is language or snake or both ?\n')
    if ans.lower()=='both':
        score+=1
        print('Correct ;)')
    else:
        print('Incorrect ;(')

print('You have successfuly completed the Trivia.')
print('Your got',score,'questions correct')
mark =(score/total_q)*100

print('Marks',str(mark)+'%')
print('Goodbye ;)')

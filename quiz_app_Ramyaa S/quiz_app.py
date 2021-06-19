import json
import random


def quiz_play():
    print("\n *******QUIZ*******")
    score = 0
    with open("assets/questions.json",'r+')as f:
        j = json.load(f)
        for i in range(10):
            no_of_questions = len(j)
            ch = random.randint(0, no_of_questions - 1)
            print(f'\nQ{i+1} {j[ch]["question"]}\n')
            for option in j[ch]["options"]:
                print(option)
            answer = input("\n Enter your answer: ")
            if j[ch]["answer"][0] == answer[0].upper():
                print("\n Your answer is correct")
                score += 1
            else:
                print("\n Your answer is incorrect")
            del j[ch]
        print(f'\n Final Score is: {score}')

def game_rules():
    print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.''')


if __name__ == "__main__":
    choice = 1
    while choice != 3:
        print("\n*****WELCOME QUIZ MASTER*****")
        print("1. PLAY THE QUIZ")
        print("2. ABOUT THE RULES")
        print("3. EXIT")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            quiz_play()
        
        elif choice == 2:
            game_rules()

        elif choice == 3:
            break

        else:
            print("INVALID OPTION")
        

#### Output
'''
*****WELCOME QUIZ MASTER*****
1. PLAY THE QUIZ  
2. ABOUT THE RULES
3. EXIT
Enter your choice:1

 *******QUIZ*******

Q1 When does India celebrate Independence Day?

A. 15th August
B. 2nd October
C. 26th January
D. 4th July

 Enter your answer: A

 Your answer is correct

Q2 Nobel prize is awarded for which of the following disciplines?

A. Literature, peace and economics
B. Medicine or Physiology
C. Chemistry and Physics
D. All the above

 Enter your answer: d

 Your answer is correct

Q3 Galileo was an astronomer who

A. Developed the telescope
B. Discovered four satellites of Jupiter
C. discovered that the movement of pendulum produces a regular time measurement
D. All the above

 Enter your answer: b

 Your answer is correct

Q4 In a Database Management System(DBMS) the content and the location of data is identified by ?

A. Subdata
B. Sequence Data
C. Beta Data
D. Meta Data

 Enter your answer: d

 Your answer is correct

Q5 'LIBRA' an alternative of existing cryptocurrency like bitcoin is being developed by?

A. Facebook
B. Google
C. Microsoft
D. None of the above

 Enter your answer: a

 Your answer is correct

Q6 Entomology studies what?

A. Behavior of human beings
B. Insects
C. The origin and history of technical and scientific terms
D. The formation of rocks

 Enter your answer: b

 Your answer is correct

Q7 Headquater of International Olympic Committee is situated at?

A. Athens
B. Lausanne
C. Dubai
D. None of the above

 Enter your answer: b

 Your answer is correct

Q8 Who is the father of geometry?

A. Aristotle
B. Euclid
C. Pythagoras
D. Kepler

 Enter your answer: b

 Your answer is correct

Q9 'The Coalition Years' is the autobiography of?

A. L.K Advani
B. Pranab Mukherjee
C. Atal Behari Vajpayee
D. Sonia Gandhi

 Enter your answer: b

 Your answer is correct

Q10 Which is the first search engine of the internet?

A. Yahoo
B. Wais
C. Archie
D. Mozilla

 Enter your answer: c

 Your answer is correct

 Final Score is: 10

*****WELCOME QUIZ MASTER*****
1. PLAY THE QUIZ
2. ABOUT THE RULES
3. EXIT
Enter your choice:2

==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.

*****WELCOME QUIZ MASTER*****
1. PLAY THE QUIZ
2. ABOUT THE RULES
3. EXIT
Enter your choice:3
'''


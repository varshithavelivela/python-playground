
print("WELCOME TO THE KBC")
print("ANSWER THE QUESTIONS CORRECTLY AND EARN MONEY")


questions = [
    "1.What is the capital of India?",
    "2.How many continents are there in the world?",
    "3.Which planet is known as Red Planet?",
    "4.What does CPU stand for?",
    "5.Which language is mainly used for web page structure?",
   "6. What does SQL stand for?",
    "7.Which instrument has six strings and is often used in pop songs?",
    "8.Who is known as the “King of Bollywood”?"
]

options = [
    ["A.New Delhi", "B.Hyderabad", "C.Mumbai","D.Kolkata"],
    ["A.Five","B. Six", "C. Seven","D.Eight"],
    ["A.Venus","B.Jupiter", "C.Mars","D.Saturn"],
    ["A.Central Processing Unit","B.Computer Power Utility", "C.Control Program Unit","D.Core Processing Utility"],
     ["A.CSS","B.HTML", "C.JavaScript","D. Python"],
     ["A.Simple Query Language","B.Structured Query Language", "C.Sequential Query Logic","D.Standard Quick Language"],
     ["A.Violin","B.Guitar", "C.Piano","D. Flute"],
     ["A.Salman Khan","B.Shah Rukh Khan", "C.Amitabh Bachchan","D.Aamir Khan "],

]

answers = ["A","C","C","A","B","B","B","B"]
score = 0
prize_money=[100,200,300,400,500,1000,5000,10000]
total_money = 0

for i in range(len(questions)):
    print('\n' + "=" *40)
    print(questions[i])
    for option in options[i]:
        print(option)


    user=input("Enter your answer: ").upper()

    if (user == answers[i]):
                print("Yes your answer is correct")
                score +=1
                print("You won Rs.",prize_money[i])
                total_money = prize_money[i]
                
    else:
               print("It is a wrong answer, the correct answer is",answers[i])
print("\n" + "="*40)               
print("Game is over!!!!")
print("Your score is: ",score)
print("Total prize is: ",total_money)
print("\n" + "="*40) 
               
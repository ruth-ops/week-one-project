#list of questions
questions =[
    "what is the first deaddly game in squid game?",
    "what is the name of the main character in squid game?",
    "what shape is on the lowest-ranked mask in squid game?",
    "what is the name of the game where the players have to cross a bridge made of glass?",
]
# list of choices for each question
choices =[
    ["a) Red Light, Green Light", "b) Dalgona Candy", "c) Marbles", "d) Glass Bridge"],
    ["a) Seong Gi-hun", "b) Cho Sang-woo", "c) Kang Sae-byeok", "d) Abdul Ali"],
    ["a) Circle", "b) Triangle", "c) Square", "d) Star"],
    ["a) Red Light, Green Light",  "b) Dalgona Candy", "c) Marbles", "d) Glass bridge"]
]
# list of correct answers for each question
answers = ["a", "a", "a", "d"]

#variable to run the quiz
def run_quiz():
    score = 0
    # outer loop question for i in range
    for i in range(len(questions)):
        print(questions[i])
     # inner loop for j in range   
        for j in range(len(choices[i])):
            print(choices[i][j])
            
        answer = input("enter your answer (a,b,c,d):")
        if answer == answers[i]:
            score += 1

    # showing total score
    total_questions = len(questions)
    print(f"your final score is:{score}/{total_questions}:")
    
    if score == total_questions:
        print("execellent")
    elif score >= total_questions:
        print("good")
    else:
        print("try again")

run_quiz()

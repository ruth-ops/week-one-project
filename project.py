import random

def run_quiz():
    print("========================================")
    print("   WELCOME TO THE SQUID GAME TRIVIA!    ")
    print("========================================")
    print("Test your survival knowledge. Answer with A, B, C, or D.\n")

    # 1. List of question dictionaries
    questions = [
        {
            "question": "What is the name of the very first deadly game the contestants play?",
            "choices": [
                "A. Tug of War", 
                "B. Red Light, Green Light", 
                "C. Ddakji", 
                "D. Marbles"
            ],
            "answer": "B"
        },
        {
            "question": "What is the total final prize money accumulated in the giant piggy bank?",
            "choices": [
                "A. 10 billion won", 
                "B. 30.5 billion won", 
                "C. 45.6 billion won", 
                "D. 100 billion won"
            ],
            "answer": "C"
        },
        {
            "question": "What is the player number assigned to the main protagonist, Seong Gi-hun?",
            "choices": [
                "A. Player 067", 
                "B. Player 001", 
                "C. Player 218", 
                "D. Player 456"
            ],
            "answer": "D"
        },
        {
            "question": "What geometric shape is marked on the masks of the lowest-ranking Squid Game guards (soldiers)?",
            "choices": [
                "A. Circle", 
                "B. Triangle", 
                "C. Square", 
                "D. Star"
            ],
            "answer": "A"
        }
    ]

    # 2. Randomize the question order using random.shuffle()
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    # 3. For loop to cycle through each question
    for index, q in enumerate(questions, 1):
        print(f"\nQuestion {index}: {q['question']}")
        for choice in q['choices']:
            print(choice)

        # 4. Input handling with .upper() and try/except validation
        while True:
            try:
                user_answer = input("\nEnter your choice (A, B, C, or D): ").strip().upper()
                
                # Check if input is valid
                if user_answer not in ["A", "B", "C", "D"]:
                    raise ValueError("Invalid selection! You must enter A, B, C, or D.")
                break # Exit the while loop if input is valid
                
            except ValueError as error:
                print(f"⚠️ {error} Please try again.")

        # Check if the user's answer is correct
        if user_answer == q["answer"]:
            print("✅ Correct! You survived this round.")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

    # 5. Score keeping and final feedback based on score
    print("\n========================================")
    print("               GAME OVER                ")
    print("========================================")
    print(f"Your final score: {score}/{total_questions}")

    if score == total_questions:
        print("Feedback: Excellent! You are the ultimate Squid Game champion! 🏆")
    elif score >= total_questions / 2:
        print("Feedback: Good! You survived, but keep sharp for next time. 👍")
    else:
        print("Feedback: Try Again! Eliminated! Better luck next time... 💀")

# Run the quiz program
if __name__ == "__main__":
    run_quiz()
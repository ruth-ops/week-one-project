import random

# list of 5 Squid Game questions
questions = [
    {
        "question": "What is the title of the first deadly game players play?",
        "choices": ["A. Tug of War", "B. Red Light, Green Light", "C. Ddakji", "D. Marbles"],
        "answer": "B"
    },
    {
        "question": "What game is played in the honeycomb challenge?",
        "choices": ["A. Tug of War", "B. Dalgona Candy", "C. Hopscotch", "D. Rock Paper Scissors"],
        "answer": "B"
    },
    {
        "question": "What is player 456's real name?",
        "choices": ["A. Cho Sang-woo", "B. Kang Sae-byeok", "C. Oh Il-nam", "D. Seong Gi-hun"],
        "answer": "D"
    },
    {
        "question": "What geometric shape is on the masks of the lowest-ranking soldiers?",
        "choices": ["A. Circle", "B. Triangle", "C. Square", "D. Star"],
        "answer": "A"
    },
    {
        "question": "What is the total final prize money in the giant piggy bank?",
        "choices": ["A. 10 billion won", "B. 30.5 billion won", "C. 45.6 billion won", "D. 100 billion won"],
        "answer": "C"
    }
]

# Randomizing question order
random.shuffle(questions)

score = 0
total_questions = len(questions)

# The for loop to cycle through each question
for q in questions:
    print("\n" + q["question"])
    
    # Print out each choice in the list
    for choice in q["choices"]:
        print(choice)
        
    #  Input validation using while and try/except
    while True:
        try:
            user_answer = input("Enter your choice (A, B, C, or D): ").strip().upper()
            
            # If they type something that isn't A, B, C, or D, raise an error
            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError("Invalid option! Please enter A, B, C, or D.")
            break # Exit the while loop if input is valid
            
        except ValueError as err:
            print(f"⚠️ {err}")

    # Step 5: Check if the answer is correct
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was {q['answer']}.")

# Step 6: Final score keeping and feedback based on score[cite: 1]
print(f"\n==============================")
print(f"Game Over! Your final score is: {score}/{total_questions}")

if score == total_questions:
    print("Feedback: Excellent!")
elif score >= 3:
    print("Feedback: Good!")
else:
    print("Feedback: Try Again!")
print(f"==============================")
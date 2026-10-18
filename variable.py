import random

# Step 1:list of 5 Squid Game questions
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

# Step 2: Randomize the question order
random.shuffle(questions)

score = 0

# Step 3: The for loop to cycle through each question
for q in questions:
    print("\n" + q["question"])
    
    # Print out each choice in the list
    for choice in q["choices"]:
        print(choice)
        
    # Get the user's input
    user_answer = input("Enter your choice (A, B, C, or D): ").strip().upper()
    
    # Check if the answer is correct
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was {q['answer']}.")

print(f"\nGame Over! Your final score is: {score}/5")
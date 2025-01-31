import random
questions = [
    {
        "question": "The length of a transition curve depends on the rate of change of ?",
        "options": ["A) distance ", "B) centrifugal acceleration", "C)speed", "D)tangential acceleration "],
        "answer": "B"
    },
    {
        "question": "Which of these is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "A"
    },
    {
        "question": "The unit of measurement is square metres in case of ?",
        "options": ["A)cement concrete in foundation ", "B)R.C.C. structure ", "C) pointing work ", "D)hollow concrete block wallaching "],
        "answer": "C"
    },
    {
        "question": ".The most accurate method used in a laboratory for the determination of water content is ?",
        "options": ["A)oven drying method", "B)sand bath method", "C)calcium carbide method", "D)Radiation method"],
        "answer": "A"
    },
    {
        "question": ".The submerged weight of soil solids per unit volume is ?",
        "options": ["A)wet unit weight", "B)saturated unit weight", "C)dry unit weight", "D)buoyant unit weight "],
        "answer": "D"
    }
]

# Shuffle the questions to randomize their order
random.shuffle(questions)

# Function to display the quiz and handle input
def start_quiz():
    score = 0  # Initialize score
    total_questions = len(questions)

    # Loop through the shuffled questions
    for q in questions:
        print(f"\n{q['question']}")
        for option in q['options']:
            print(option)

        # Input validation: Only allow A, B, C, or D
        while True:
            user_answer = input("Please enter your answer (A, B, C, D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid answer. Please enter one of the following options: A, B, C, D.")

        # Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {q['answer']}")

    # Display the final score
    print(f"\nYour final score is: {score} out of {total_questions}")

# Start the quiz
start_quiz()

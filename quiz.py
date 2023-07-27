import random

# Quiz questions and their corresponding answers
quiz_questions = {
    "What is the capital of France?": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
    "Which planet is known as the 'Red Planet'?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"],
    "Who painted the Mona Lisa?": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"],
    "What is the chemical symbol for water?": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"]
}

# Correct answers for each question
correct_answers = {
    "What is the capital of France?": "A",
    "Which planet is known as the 'Red Planet'?": "B",
    "What is the largest mammal in the world?": "B",
    "Who painted the Mona Lisa?": "A",
    "What is the chemical symbol for water?": "A"
}

def print_question(question, options):
    print(question)
    for option in options:
        print(option)

def get_user_choice():
    while True:
        choice = input("Enter the letter of your answer (A, B, C, or D): ").upper()
        if choice in ["A", "B", "C", "D"]:
            return choice
        print("Invalid input. Please enter a valid option (A, B, C, or D).")

def run_quiz():
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        options = quiz_questions[question]
        print_question(question, options)
        user_choice = get_user_choice()

        if user_choice == correct_answers[question]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answers[question]}.\n")

    print(f"You answered {score} out of {len(questions)} questions correctly.")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("Test your knowledge with these multiple-choice questions.")
    run_quiz()
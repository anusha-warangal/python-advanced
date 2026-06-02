questions = {
    "What is the capital of India?": "Delhi",
    "Which language is used for AI and Data Science?": "Python",
    "How many days are there in a week?": "7"
}

score = 0

print("===== SIMPLE QUIZ APPLICATION =====")

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {answer}\n")

print("===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))

import random

questions = {
    "What is the full form of IT?": {
        "choices": ["Information Technology", "Intelligence Technology", "Internet Technology",
                    "Intelligent Technology"],
        "answer": "1"
    },
    "What is the purpose of a computer network?": {
        "choices": ["To connect computers together", "To share resources", "To provide access to the internet",
                    "All of the above"],
        "answer": "4"
    },
    "What is the difference between hardware and software?": {
        "choices": ["Hardware is physical, software is intangible",
                    "Hardware is used to perform tasks, software is used to control hardware",
                    "Hardware is slow, software is fast", "Hardware is expensive, software is cheap"],
        "answer": "1"
    },
    "What is the purpose of a firewall?": {
        "choices": ["To protect a computer from unauthorized access",
                    "To prevent viruses and malware from entering a computer",
                    "To control the flow of traffic on a network", "All of the above"],
        "answer": "4"
    },
    "What is a web browser?": {
        "choices": ["A software program that allows you to access the internet",
                    "A hardware device that connects you to the internet",
                    "A network of computers that share information", "A type of website"],
        "answer": "1"
    },
    "What is the difference between a website and a web page?": {
        "choices": ["A website is a collection of web pages, a web page is a single document",
                    "A website is a static document, a web page can be interactive",
                    "A website is expensive to create, a web page is cheap to create",
                    "A website is slow to load, a web page is fast to load"],
        "answer": "1"
    },
    "What is the purpose of a search engine?": {
        "choices": ["To help you find information on the internet", "To organize and index information on the internet",
                    "To sell products and services online", "None of the above"],
        "answer": "1"
    },
    "What is the difference between email and instant messaging?": {
        "choices": ["Email is synchronous, instant messaging is asynchronous",
                    "Email is text-based, instant messaging can include audio and video",
                    "Email is private, instant messaging is public", "Email is slow, instant messaging is fast"],
        "answer": "1"
    },
    "What is the purpose of social media?": {
        "choices": ["To connect with friends and family", "To share information and news",
                    "To promote businesses and products", "All of the above"],
        "answer": "4"
    },
    "What is the future of IT?": {
        "choices": ["Artificial intelligence", "Big data", "Cloud computing", "All of the above"],
        "answer": "4"
    }
}

marks_list = []


def start_game(name):
    marks = 0
    correct_answers = 0
    incorrect_answers = 0

    questions_list = list(questions.items())
    random.shuffle(questions_list)

    for count, (question, value) in enumerate(questions_list, start=1):
        print(f"\nQuestion {count}: {question}")
        print("\nChoices:")
        for i, choice in enumerate(value["choices"], start=1):
            print(f"{i}. {choice}")

        user_answer = input("Enter your answer (1-4): ").strip()

        if user_answer == value["answer"]:
            print("Correct!!")
            marks += 10
            correct_answers += 1
        else:
            print(f"Wrong Answer!! The correct answer is {value['answer']}.")
            incorrect_answers += 1

    print("\n--- Game Over ---")
    print(f"Your marks: {marks}")
    print(f"{name}, Your Correct answers: {correct_answers}")
    print(f"Your Incorrect Answers: {incorrect_answers}")

    marks_list.append(marks)
    highest_marks = max(marks_list)
    print(f"Highest marks: {highest_marks}")

    if marks == highest_marks:
        print(f"Congrats, {name}! You are the highest scorer for now!")


def end_game(name):
    exit_confirm = input("Do you want to exit? (y/n): ").strip().lower()
    if exit_confirm == "y":
        print(f"Thank you {name} for playing!")
        exit()


def main():
    while True:
        print("\nWelcome to the Quiz Game!!!")
        name = input("Enter your name: ").strip()
        start = input(f"Hi, {name}! To begin the game, please enter 1: ").strip()

        if start == "1":
            start_game(name)
        end_game(name)


if __name__ == "__main__":
    main()

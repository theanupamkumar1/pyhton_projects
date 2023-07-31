import random

name = input("Enter your name: ").capitalize()
print("Welcome to KBC", name)
print(
    """ *******************************\n
    You will be asked 10 questions in a row. You have to answer them.\nFor each correct answer, 100 points will be awarded.\n
    You have to type the option number to give the answer.
    If you want to exit, press 'e' or 'E'. \n*******************************"""
)

questionBank = {
    # Fill in the questions and options here
    # Example:
    # "What is the capital of France?": ["1. London", "2. Paris", "3. Berlin", "4. Madrid"],
    # "Which planet is closest to the sun?": ["1. Venus", "2. Mercury", "3. Mars", "4. Jupiter"],
    "what is the smallest country in the world": [
        "vatican city",
        "monaco",
        "liechtenstein",
        "san marino",
    ],
    "which is the longest river in the world": [
        "nile",
        "amazon",
        "yangtze",
        "mississippi",
    ],
    "who invented the lightbulb": [
        "thomas edison",
        "nikola tesla",
        "benjamin franklin",
        "albert einstein",
    ],
    "what is the rarest blood type": [
        "AB-negative",
        "AB-positive",
        "B-negative",
        "A-negative",
    ],
    "where are the 2022 winter olympics being held": [
        "beijing, china",
        "pyeongchang, south korea",
        "sochi, russia",
        "torino, italy",
    ],
    "who painted the mona lisa": [
        "leonardo da vinci",
        "vincent van gogh",
        "pablo picasso",
        "claude monet",
    ],
    "what is the diameter of a basketball hoop": [
        "18 inches",
        "20 inches",
        "16 inches",
        "22 inches",
    ],
    "who discovered penicillin": [
        "alexander fleming",
        "louis pasteur",
        "robert koch",
        "edward jenner",
    ],
    "what is the most common eye color": ["brown", "blue", "green", "hazel"],
    "who was the first woman to win a nobel prize": [
        "marie curie",
        "rosalind franklin",
        "dorothy hodgkin",
        "irene joliot-curie",
    ],
    "which is the largest continent": [
        "asia",
        "africa",
        "north america",
        "south america",
    ],
    "how many sides does a hexagon have": ["6", "5", "7", "8"],
    "what element has the chemical symbol O": [
        "oxygen",
        "carbon",
        "hydrogen",
        "nitrogen",
    ],
    "who invented the telephone": [
        "alexander graham bell",
        "elisha gray",
        "antonio meucci",
        "guglielmo marconi",
    ],
    "what is the hardest natural substance": ["diamond", "graphite", "quartz", "topaz"],
    "what is the national sport of canada": [
        "lacrosse",
        "ice hockey",
        "curling",
        "soccer",
    ],
    "which country has won most FIFA World Cups": [
        "brazil",
        "germany",
        "italy",
        "argentina",
    ],
    "how many degrees are in a circle": ["360", "180", "90", "270"],
    "what is the rarest M&M color": ["brown", "yellow", "red", "blue"],
    "what is the smallest ocean in the world": [
        "arctic ocean",
        "indian ocean",
        "southern ocean",
        "atlantic ocean",
    ],
    "where were the first modern Olympic games held": [
        "athens, greece",
        "paris, france",
        "berlin, germany",
        "rome, italy",
    ],
    "which planet is closest to the sun": ["mercury", "venus", "mars", "jupiter"],
    "what is the largest organ in the human body": ["skin", "liver", "heart", "brain"],
    "how many days are there in a leap year": ["366", "365", "364", "367"],
    "what is the square root of 144": ["12", "10", "14", "16"],
    "how many elements are there in the periodic table": ["118", "92", "103", "110"],
    "what is the currency of Switzerland": [
        "swiss franc",
        "euro",
        "pound sterling",
        "us dollar",
    ],
    "which country has the most natural lakes": ["canada", "finland", "russia", "usa"],
    "where is the coldest place on earth": [
        "antarctica",
        "siberia",
        "greenland",
        "northern canada",
    ],
    "what does URL stand for": [
        "uniform resource locator",
        "unified resource language",
        "universal reference link",
        "user-friendly resource library",
    ],
    "how many years are there in a millennium": ["1000", "100", "500", "2000"],
    "who was the first woman in space": [
        "valentina tereshkova",
        "sally ride",
        "yuri gagarin",
        "neil armstrong",
    ],
    "which continent has the largest population": [
        "asia",
        "africa",
        "europe",
        "north america",
    ],
    "what is the national animal of India": [
        "bengal tiger",
        "elephant",
        "lion",
        "peacock",
    ],
    "what is the hardest substance in the human body": [
        "tooth enamel",
        "bone",
        "cartilage",
        "nail",
    ],
    "how many players are there in a basketball team": ["5", "6", "7", "8"],
    "what is the smallest ocean": [
        "arctic ocean",
        "indian ocean",
        "southern ocean",
        "atlantic ocean",
    ],
    "how many degrees does a straight angle have": ["180", "90", "360", "270"],
    "what is the currency of Denmark": ["krone", "euro", "dollar", "pound"],
    "which planet has the most moons": ["jupiter", "saturn", "neptune", "mars"],
    "where is the great barrier reef located": [
        "australia",
        "hawaii",
        "maldives",
        "fiji",
    ],
    "who painted the Sistine Chapel": [
        "michelangelo",
        "leonardo da vinci",
        "raphael",
        "donatello",
    ],
    "what is the hottest planet in the solar system": [
        "venus",
        "mercury",
        "mars",
        "jupiter",
    ],
    "which country produces the most coffee in the world": [
        "brazil",
        "colombia",
        "vietnam",
        "indonesia",
    ],
    "how many colors are there in a rainbow": ["7", "6", "5", "8"],
}

no_of_que = int(input("Type the number of questions for the game: ").capitalize())
if no_of_que <= 0:
    print("Number of questions is too low.")
elif no_of_que > 50:
    print("Number of questions is too much. Keep it between 1 and 50.")
else:
    # main quiz program
    score = 0
    asked_questions = set()

    def quiz():
        global score
        global active_que

        for _ in range(no_of_que):
            question = random.choice(list(questionBank.keys()))

            if question in asked_questions:
                continue

            asked_questions.add(question)
            options = questionBank[question]
            print(f"Question no: {active_que}")
            print(question)

            for option in options:
                print(option)

            user_answer = input("Your answer (Type option number or 'e' to exit): ")

            if user_answer.lower() == "e":
                break

            if (
                not user_answer.isdigit()
                or int(user_answer) < 1
                or int(user_answer) > len(options)
            ):
                print("Invalid input. Skipping this question.")
                continue

            user_answer = int(user_answer)
            if (
                options[user_answer - 1] == options[0]
            ):  # Compare with the correct option at index 0
                score += 100

            active_que += 1

    quiz()
    total_possible_score = no_of_que * 100
    print(f"\n{name}, Your Final Score: {score}")

    if score >= 0.9 * total_possible_score:
        print("Congratulations! You are now a crorepati.")
    else:
        print("Try again, you can do this.")

# end of program

import random

name = input("Enter your name: ").capitalize()
print("Welcome to KBC", name)
print(
    """ *******************************\n
    You will be asked 10 questions in a row. You have to answer them.\nFor each correct answer, 100 points will be awarded.\n
    You have to type the option number to give the answer.
    If you want to exit, press 'e' or 'E'. \n*******************************"""
)


question_bank = {
    "what is the smallest country in the world": {
        "options": ["vatican city", "monaco", "liechtenstein", "san marino"],
        "ans": "vatican city",
    },
    "which is the longest river in the world": {
        "options": ["nile", "amazon", "yangtze", "mississippi"],
        "ans": "nile",
    },
    "who invented the lightbulb": {
        "options": [
            "thomas edison",
            "nikola tesla",
            "benjamin franklin",
            "albert einstein",
        ],
        "ans": "thomas edison",
    },
    "what is the rarest blood type": {
        "options": ["AB-negative", "AB-positive", "B-negative", "A-negative"],
        "ans": "AB-negative",
    },
    "where are the 2022 winter olympics being held": {
        "options": [
            "beijing, china",
            "pyeongchang, south korea",
            "sochi, russia",
            "torino, italy",
        ],
        "ans": "beijing, china",
    },
    "who painted the mona lisa": {
        "options": [
            "leonardo da vinci",
            "vincent van gogh",
            "pablo picasso",
            "claude monet",
        ],
        "ans": "leonardo da vinci",
    },
    "what is the diameter of a basketball hoop": {
        "options": ["18 inches", "20 inches", "16 inches", "22 inches"],
        "ans": "18 inches",
    },
    "who discovered penicillin": {
        "options": [
            "alexander fleming",
            "louis pasteur",
            "robert koch",
            "edward jenner",
        ],
        "ans": "alexander fleming",
    },
    "what is the most common eye color": {
        "options": ["brown", "blue", "green", "hazel"],
        "ans": "brown",
    },
    "who was the first woman to win a nobel prize": {
        "options": [
            "marie curie",
            "rosalind franklin",
            "dorothy hodgkin",
            "irene joliot-curie",
        ],
        "ans": "marie curie",
    },
    "which is the largest continent": {
        "options": ["asia", "africa", "north america", "south america"],
        "ans": "asia",
    },
    "how many sides does a hexagon have": {"options": ["6", "5", "7", "8"], "ans": "6"},
    "what element has the chemical symbol O": {
        "options": ["oxygen", "carbon", "hydrogen", "nitrogen"],
        "ans": "oxygen",
    },
    "who invented the telephone": {
        "options": [
            "alexander graham bell",
            "elisha gray",
            "antonio meucci",
            "guglielmo marconi",
        ],
        "ans": "alexander graham bell",
    },
    "what is the hardest natural substance": {
        "options": ["diamond", "graphite", "quartz", "topaz"],
        "ans": "diamond",
    },
    "what is the national sport of canada": {
        "options": ["lacrosse", "ice hockey", "curling", "soccer"],
        "ans": "ice hockey",
    },
    "which country has won most FIFA World Cups": {
        "options": ["brazil", "germany", "italy", "argentina"],
        "ans": "brazil",
    },
    "how many degrees are in a circle": {
        "options": ["360", "180", "90", "270"],
        "ans": "360",
    },
    "what is the rarest M&M color": {
        "options": ["brown", "yellow", "red", "blue"],
        "ans": "brown",
    },
    "what is the smallest ocean in the world": {
        "options": ["arctic ocean", "indian ocean", "southern ocean", "atlantic ocean"],
        "ans": "arctic ocean",
    },
    "where were the first modern Olympic games held": {
        "options": [
            "athens, greece",
            "paris, france",
            "berlin, germany",
            "rome, italy",
        ],
        "ans": "athens, greece",
    },
    "which planet is closest to the sun": {
        "options": ["mercury", "venus", "mars", "jupiter"],
        "ans": "mercury",
    },
    "what is the largest organ in the human body": {
        "options": ["skin", "liver", "heart", "brain"],
        "ans": "skin",
    },
    "how many days are there in a leap year": {
        "options": ["366", "365", "364", "367"],
        "ans": "366",
    },
    "what is the square root of 144": {
        "options": ["12", "10", "14", "16"],
        "ans": "12",
    },
    "how many elements are there in the periodic table": {
        "options": ["118", "92", "103", "110"],
        "ans": "118",
    },
    "what is the currency of Switzerland": {
        "options": ["swiss franc", "euro", "pound sterling", "us dollar"],
        "ans": "swiss franc",
    },
    "which country has the most natural lakes": {
        "options": ["canada", "finland", "russia", "usa"],
        "ans": "canada",
    },
    "where is the coldest place on earth": {
        "options": ["antarctica", "siberia", "greenland", "northern canada"],
        "ans": "antarctica",
    },
    "what does URL stand for": {
        "options": [
            "uniform resource locator",
            "unified resource language",
            "universal reference link",
            "user-friendly resource library",
        ],
        "ans": "uniform resource locator",
    },
    "how many years are there in a millennium": {
        "options": ["1000", "100", "500", "2000"],
        "ans": "1000",
    },
    "who was the first woman in space": {
        "options": [
            "valentina tereshkova",
            "sally ride",
            "yuri gagarin",
            "neil armstrong",
        ],
        "ans": "valentina tereshkova",
    },
    "which continent has the largest population": {
        "options": ["asia", "africa", "europe", "north america"],
        "ans": "asia",
    },
    "what is the national animal of India": {
        "options": ["bengal tiger", "elephant", "lion", "peacock"],
        "ans": "bengal tiger",
    },
    "what is the hardest substance in the human body": {
        "options": ["tooth enamel", "bone", "cartilage", "nail"],
        "ans": "tooth enamel",
    },
    "how many players are there in a basketball team": {
        "options": ["5", "6", "7", "8"],
        "ans": "5",
    },
    "what is the smallest ocean": {
        "options": ["arctic ocean", "indian ocean", "southern ocean", "atlantic ocean"],
        "ans": "arctic ocean",
    },
    "how many degrees does a straight angle have": {
        "options": ["180", "90", "360", "270"],
        "ans": "180",
    },
    "what is the currency of Denmark": {
        "options": ["krone", "euro", "dollar", "pound"],
        "ans": "krone",
    },
    "which planet has the most moons": {
        "options": ["jupiter", "saturn", "neptune", "mars"],
        "ans": "jupiter",
    },
    "where is the great barrier reef located": {
        "options": ["australia", "hawaii", "maldives", "fiji"],
        "ans": "australia",
    },
    "who painted the Sistine Chapel": {
        "options": ["michelangelo", "leonardo da vinci", "raphael", "donatello"],
        "ans": "michelangelo",
    },
    "what is the hottest planet in the solar system": {
        "options": ["venus", "mercury", "mars", "jupiter"],
        "ans": "venus",
    },
    "which country produces the most coffee in the world": {
        "options": ["brazil", "colombia", "vietnam", "indonesia"],
        "ans": "brazil",
    },
    "how many colors are there in a rainbow": {
        "options": ["7", "6", "5", "8"],
        "ans": "7",
    },
}

no_of_que = int(input("Type the number of questions for the game: ").capitalize())
if no_of_que <= 0:
    print("Number of questions is too low.")
elif no_of_que > 50:
    print("Number of questions is too much. Keep it between 1 and 50.")
else:
    # main quiz program
    score = 0

    asked_questions = []
    for i in range(no_of_que):
        # Get random question
        question = random.choice(list(question_bank.keys()))
        while question in asked_questions:
            question = random.choice(list(question_bank.keys()))

        asked_questions.append(question)

        # Print question
        print(f"Question {i+1}: {question}")

        # Shuffle and print options
        options = question_bank[question]["options"]
        random.shuffle(options)

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        while True:
            user_ans = input("Your answer: ")

            # Validate input
            if user_ans.lower() == "e":
                print("You have exited the game.")
                break
            if not user_ans:
                print("Cannot be blank")
                continue

            if not user_ans.isdigit():
                print("Must enter a number")
                continue

            # Input is valid, convert and process
            try:
                user_ans = int(user_ans)
            except ValueError:
                print("Invalid number entered")
                continue

            if user_ans < 1 or user_ans > len(options):
                print("Number must be between 1 and", len(options))
                continue

            # Input is good, break loop
            break

        # Get user's actual choice from options list
        user_choice = options[user_ans - 1]

        # Validate against answer
        if user_choice == question_bank[question]["ans"]:
            print("Correct!")
            score += 100
        else:
            print("Oops, wrong answer!")

    total_possible_score = no_of_que * 100
    print(f"\n{name}, Your Final Score: {score}")

    if score >= 0.9 * total_possible_score:
        print("Congratulations! You are now a crorepati.")
    else:
        print("Try again, you can do this.")

# end of program

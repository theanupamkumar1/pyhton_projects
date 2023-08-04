import random


def encode():
    pass


def decode():
    pass


alphabets = "abcdefghijklmnopqrstuvwxyz"

sentance = ""


# funtion for encoding the user sentance
def encode():
    # while True
    global encoded_sentance
    global words
    sentance = input(
        "enter any " + "english ".upper() + " sentance to ENCODE in ANU-CRYPTION  :"
    )
    words = sentance.split()
    encoded_sentance = ""
    if sentance == "q":
        exit()
    else:
        for x in words:
            if (
                len(x) >= 3
            ):  # in this whole for loop "x" stands for the index of the list named "word"
                last_letter = x[0]
                # words[0] = last_letter
                start_letters = ""
                for _ in range(3):
                    start_letters += random.choice(alphabets)

                end_letters = ""
                for _ in range(3):
                    end_letters += random.choice(alphabets)

                # encoded_sentance +={start_letters}{ x[1:]}{last_letter}{end_letters}

                # print(f"{start_letters}{ x[1:]}{last_letter}{end_letters}")
                encoded_sentance += (
                    f"{start_letters}{ x[1:]}{last_letter}{end_letters} "
                )
            elif len(x) < 3:
                # print(x[::-1])
                encoded_sentance += f"{x[::-1]} "

        print("\n" + encoded_sentance)

        return encode()


# fn for decoding the sentance


def decode():
    global decoded_sentance
    global start_letters
    global end_letters

    sentance = input("enter any " + "sentance to DECODE FROM ANU-CRYPTION to ENGLISH :")
    words = sentance.split()
    decoded_sentance = ""
    if sentance == "q":
        exit()
    else:
        for word in words:
            if len(word) >= 9:
                # Slice encoded word

                start_letters = word[:3]
                end_letters = word[-3:]
                decoded_word = word[3:-3]
                first_letter = decoded_word[-1]

                # Reverse encoding

                decoded_word = f"{first_letter}{decoded_word[:-1]} "
                decoded_sentance += decoded_word

            #   decoded_word = encoded_word[1:] + encoded_word[0]

            else:
                decoded_sentance += f"{word[::-1]} "
        # Reverse short words
        #   words[words.index(word)] = word[::-1]

    # print("\n" + decoded_sentance)
    return decode()


def exit():
    print("thank you for using ANU-CRYPTION")


while True:
    choice = input(
        """
        WELCOME TO ANU-CRYPTION!!!!
        What would you like to use ENCODE or DECODE?
        Type "0" for ENCODING
        Type "1" for DECODING
        Type "e" to EXIT
        Enter your choice: """
    )

    if choice == "0":
        encode()
    elif choice == "1":
        decode()
    elif choice == "e":
        print("Thank you for using ANU-CRYPTION")
        break
    else:
        print("Invalid input")

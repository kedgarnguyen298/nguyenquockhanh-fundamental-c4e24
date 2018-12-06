ques = {
    "Which is the next number of 3? ": [4,5,6,7],
    "Who is lecture of C4E 24? ": ["Khanh", "Duc", "Huy", "Techkids"],
    "What is capital of Viet Nam? ": ["Ha Noi", "HCM", "Da Nang", "Ca Mau"],

}

anss = {
    "Which is the next number of 3? ": "1",
    "Who is lecture of C4E 24? ": "3",
    "What is capital of Viet Nam? ": "1",
}

point = 0

for que in ques:
    print(que)
    chos = ques[que]
    for i, cho in enumerate(ques[que], 1):
        print(i, cho, sep = ".")
    user = input("Your choice: ")
    if user == anss[que]:
        print("Bingo !")
        point += 1
    else:
        print(":(")

print("Your correct answer:", point, "of", len(ques), "question!" )


# score = 0
# question
# print("When was GTBank founded? ")
# print("a) 1994 \n b) 1894 \n c) 1990 \n d) 1978")
# response =  input("Enter Answer ")
# result= response.upper()

# if result == "C":
#     print('Correct')
#     score += 1
# else:
    # print('wrong')

questions = ['3\n', '2', '1']
answers = ['a', 'b', 'c' ]

score = 0

for index in range(len(questions)):
    answer = input(questions[index])
    if answers[index] == answer:
        score = score + 1

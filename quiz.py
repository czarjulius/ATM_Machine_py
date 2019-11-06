score = 0
print("When was GTBank founded? ")
print("a) 1994 \n b) 1894 \n c) 1990 \n d) 1978")
response =  input("Enter Answer ")
result= response.upper()

if result == "C":
    print('Correct')
    score += 1
else:
    print('wrong')

print("What is GTBank logo colour? ")
print("\n a) Orange \nb) Blue \nc) Purple \nd) Red")
response =  input("Enter Answer ")
result= response.upper()

if result == "A":
    print('Correct')
    score += 1
else:
    print('wrong')

print("Where is GTBank head office located? ")
print("\n a) VI \nb) Obalende \nc) Yaba \n d) Ikeja")
response =  input("Enter Answer ")
result= response.upper()

if result == "A":
    print('Correct')
    score += 1
else:
    print('wrong')

total_score = score

print('Your total score', total_score)
# first create a list of questions and store it into the list 
# then create a dictionary that containes the correct answer for the given question 
# if the answer is correct then point will increase then it will not 



# question list 

questionsList = [
	"How many Continent are there ? \n \n 1. Five 2. Size 3. Four 4.Seven",
	"Who is the current President of Nepal ? \n \n1. Sher B. Thapa 2. Bidya D. Bhandari 3. KP Oli 4.Puspa K. Dahal",
	"What is the club Ronaldo Playing for ? \n \n1. Real Madrid 2. Juventus 3. ManUtd 4. PSG",
	"What is the longest River ? \n \n 1. Ganga 2. Nile 3. Karnali 4.Amazon",
]

# correct answer where key -> question and value -> answer
correctAnswer = {
	0 : 4, 
	1 : 2,
	2 : 2,
	3 : 2
}

# initial score
score = 0

# it checks the answer of the quiz

def checkAnswer(answer, index):
	global score
	if answer == correctAnswer[index]:
		score += 1
		print("Correct Answer")
	else:
		print("Wrong Answer")
		
# main program

def main():
	global score
	print("       WELCOME TO THE GAME OF QUIZ.\n")
	print("Answer the following quiz questions: \n")
	for i in range(len(questionsList)):
		print(questionsList[i])
		answer = int(input("Enter Answer : "))
		checkAnswer(answer , i)
		
	print(score)


if __name__ == '__main__':
	main()
	
#!/usr/local/bin/python3

import random
import operator

class number:
	# Just to not have to put "number" in the IntegOfInput() func
	pass

def AskToReturn():
	# Asks User if They Want to Leave
	keepGoing = input("Do you want to keep going? (y/n)\nChoice: ")
	IntegOfInput(keepGoing, str)
	keepGoing = keepGoing.capitalize()

	if keepGoing == "Y":
		print("Good choice!")
		return
	elif keepGoing == "N":
		print("Good luck failing!")
		quit()
	else:
		print("[ERR]: BAD INPUT!")
		quit()

def RandomQuestion():
	# Creates a random problem
	ops = {"x": operator.mul,
		"/": operator.truediv}

	num1 = random.uniform(0.1, 12)
	num1 = '%.3f'%(num1)
	num1 = str(num1)

	num2 = random.uniform(0.1, 12)
	num2 = '%.3f'%(num2)
	num2 = str(num2)

	op = random.choice(list(ops.keys()))
	question = num1 + " " + op + " " + num2

	return question

def quiz(num):
	# Gives User a Quiz
	print("Truncate to 3 decimal places.")
	score = 0
	for i in range(0, num):
		print("Your score: {}".format(score))
		problem = RandomQuestion()
		realAns = SolveProblem(problem)
		ans = input("The problem is {}.\nAnswer: ".format(problem))
		IntegOfInput(ans)

		if ans.find(".") == -1:
			ans = ans + ".000"		

		if len(ans.split(".")[1]) == 1:
			ans = ans + "00"
		elif len(ans.split(".")[1]) == 2:
			ans = ans + "0"
		else:
			ans = float(ans)
			ans = '%.3f'%(ans)

		ans = float(ans)
		ans = '%.3f'%(ans)

		realAns = float(realAns)
		realAns = '%.3f'%(realAns)

		if float(realAns)-0.001 <= float(ans) <= float(realAns):
			score += 1
			print("You are correct!")
		else:
			print("You are incorrect! The real answer was: {}.".format(realAns))

	print("Your score is: {} out of {}.".format(score, num))

	AskToReturn()
	return

def WalkThrough(problemType, problem=None):
	# Walks User Through Problem
	if problemType == "1": # Spec
		specRealAns = SolveProblem(problem)
		ans = input("The problem is {}.\nAnswer: ".format(problem))
		IntegOfInput(ans)

		if ans == specRealAns:
			print("You are correct!")
		else:
			print("You are incorrect! The real answer was: {}.".format(specRealAns))
			
		AskToReturn()
		return

	elif problemType == "2": # Rand
		print("Truncate to 3 decimal places.")
		randProblem = RandomQuestion()
		randRealAns = SolveProblem(randProblem)
		randRealAns = '%.3f'%(randRealAns)

		ans = input("The problem is {}.\nAnswer: ".format(randProblem))
		IntegOfInput(ans)

		if ans.find(".") == -1:
			ans = ans + ".000"		

		if len(ans.split(".")[1]) == 1:
			ans = ans + "00"
		elif len(ans.split(".")[1]) == 2:
			ans = ans + "0"
		else:
			ans = float(ans)
			ans = '%.3f'%(ans)

		ans = float(ans)
		randRealAns = float(randRealAns)

		if ans == randRealAns:
			print("You are correct!")
		else:
			print("You are incorrect! The real answer was: {}.".format(randRealAns))

		AskToReturn()
		return

def SolveProblem(problem):
	# Solves any mult or div problem
	if problem.find("x") != -1:
		problemParts = problem.split("x")
		problemParts = StrToFloatListConv(problemParts)
		ans = problemParts[0] * problemParts[1]
	if problem.find("/") != -1:
		problemParts = problem.split("/")
		problemParts = StrToFloatListConv(problemParts)
		ans = problemParts[0] / problemParts[1]

	return ans

def StrToFloatListConv(_list):
	# Converts any string list into an int list
	for i in range(0, len(_list)):
		_list[i] = float(_list[i])
	return _list

def IntegOfInput(_object, _type=number):
	# Verifies that object is of type
	if _type == number:
		try:
			float(_object)
			return
		except:
			print("[ERR]: BAD INPUT!")
			quit()
	else:
		if type(_object) == _type:
			return
		else:
			print("[ERR]: BAD INPUT!")			
			quit()

while True:	
	choice = input("Make Sure: 1\nQuiz: 2\nChoice: ")
	IntegOfInput(choice)

	if choice == "1":
		print("You chose: Make Sure")
		secondaryChoice = input("Specific Problem: 1\nRandom Problems: 2\nChoice: ")
		IntegOfInput(secondaryChoice)

		if secondaryChoice == "1":
			specProblem = input("What problem?\nChoice: ")
			specProblem = specProblem.replace("*", "x")
			WalkThrough(secondaryChoice, specProblem)
			continue
		elif secondaryChoice == "2":
			WalkThrough(secondaryChoice)
			continue

	elif choice == "2":
		print("You chose: Quiz")
		numQuestions = input("How many questions should there be?\nChoice: ")
		IntegOfInput(numQuestions)
		numQuestions = int(numQuestions)
		quiz(numQuestions)


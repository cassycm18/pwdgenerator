#!/usr/bin/python3
#Usage : password generator
# file create date: 26-May-2022
# last update: 02-Jun-2022
# created by: YN Ng
# Requirement: 
# password length min 12
# password must start with capital and end with digit
# Added ability to save the password into a txt file

# Modules imported
import string
import random
import datetime


## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
alpha_upper = list(string.ascii_uppercase)

#define policy requirement
min_pwdlength = 12
min_alphacount = 1
min_digitscount = 1
min_specialcharacter = 1


#Question to select and to be answer by user.
pwd_choice = 0
alpha_choice = 1
digits_choice = 2
specialcharacter_choice = 3 

#store password filename
filename = "lpassword.txt"

#List questions based on subject(s) to be evaluated 
questions = list(("password length (default 12)" , "alphabets count in password (default 1)" , "digits count in password (default 1)", "special character count in password(default 1)"))

# Function to valid the input values from user
def validate_int(inputvalue, choice, minvalue):

	try: 
		inputvalue = validate_criteria(inputvalue, choice, minvalue)
		#print(" min value should be ", minvalue)
		return inputvalue	
	except ValueError:
		print("Please input integer only...")
		while True:
			try:
				inputvalue = int(input("Enter " + questions[choice]+ ": "))
				#print("user input value should at least ", minvalue)
				return inputvalue		
			except ValueError:
				print("Please input integer only....")
				continue

#Function to check the input value and to enforce meet min policy requirement 
 
def validate_criteria(uservalue, choice, policyvalue):
	uservalue = int(uservalue)
	choice = int(choice)
	policyvalue = int(policyvalue)
	while uservalue < policyvalue:
		print(questions[choice] +  "....")
		uservalue =  validate_int(input("Enter " + questions[choice] + ": "), choice, policyvalue)
		if uservalue >= policyvalue:
			return uservalue		
	#print("value detected from user  is " , uservalue)	
	return uservalue 

def generate_random_password():
	## Get length of password from the user
	pwd_length = validate_int(input("Enter " + questions[pwd_choice] + " : ") or min_pwdlength, pwd_choice, min_pwdlength)
	
	## number of character types
	alphabets_count = validate_int(input("Enter " + questions[alpha_choice] + " : ") or min_alphacount, alpha_choice, min_alphacount)
		
	## number of digits types
	digits_count = validate_int(input("Enter " + questions[digits_choice] + " : ") or min_digitscount, digits_choice, min_digitscount)

	## number of special characters types
	special_characters_count = validate_int(input("Enter " + questions[specialcharacter_choice] + " : ") or min_specialcharacter, specialcharacter_choice, min_specialcharacter)


	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total password length with characters sum count
	## print not valid if the sum is greater than password length
	
	if characters_count > pwd_length:
		print("Characters total count is greater than the password length")
		print("No password being generatored.")
		return


	## initializing the password
	## first store capital
	## last store digit
	## finalpassword with store password begin with Capital and end with digits
	
	password = []
	first = []
	last = []
	finalpassword = []
	
	## picking random uppercase
	random.shuffle(alpha_upper)
	first.append(random.choice(alpha_upper))
	
	## picking random digits for last
	random.shuffle(digits)
	last.append(random.choice(digits))
	
	## picking random alphabets
	for i in range(alphabets_count - 1):
		password.append(random.choice(alphabets))

	## picking random digits
	for i in range(digits_count - 1):
		password.append(random.choice(digits))
	
	## picking random special_characters 
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))
	
	## if total characters count is less than password length
	## add random characters to make it equeal to the length
	if characters_count < pwd_length:
		random.shuffle(characters)
		for i in range(pwd_length - characters_count):
			password.append(random.choice(characters))

	## Shuffling the result password
	random.shuffle(password)
	
	## finalize password must begin with capital, end with digits
	first.extend(password)
	first.extend(last)
	finalpassword = list(first)

	## converting the list to string
	## printing the list
	password_created = "".join(finalpassword)
	#print("".join(finalpassword))
	print("length of the password is ", len(finalpassword))
	#print("password created as ", password_created)


	## Save the password into file
	ans = input("Do you want to save the file (default Yes)? ") or "Y"
	if ans.upper() == "Y" or ans.upper() == "YES":
		today = datetime.datetime.now()

		#create if the file not exit otherwise append into the file
		f = open(filename, "a")
		f.writelines([today.strftime("%d/%m/%Y %X"), "\t", password_created, "\n"])
		f.close()
		
		#Open and read the content after append:
		f = open(filename, "r")
		print("The password save into filename : ", filename, "\n", f.read())		
	else:
		print("the password not save into file")
		print("password generated as asked: ", password_created)
## invoking the function
generate_random_password()

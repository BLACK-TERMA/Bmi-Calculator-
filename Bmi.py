# Bmi-Calculator-

# BMR CALCULATOR 
import time
print ("[>~~~~~Starting BMR Calculator~~~~~<]") 
time.sleep (1)
print ("processing............... ")
time.sleep (1)
print ("   ")
print ("Input necessary data carefully and accurately")
time.sleep(.50)
print ("   ")
print ("{>----------Enter your name----------<}")
name = str(input(" ■ Enter your nickname:> "))
print("Name inputted done $> " + name + " <$")
time.sleep (.5)
print ("   ")
print ("{>----------Enter your age----------<}")
age = int(input(" ■ Enter your age:> "))
time.sleep (.5)
print ("   ")
print ("{>-------Enter your height----------<}")
height = float(input(" ■ Enter your height(cm):> ") )
time.sleep (.5)
print ("   ")
print ("{>----------Enter your weight----------<}")
weight = float(input(" ■ Enter your weight(kg):> "))
time.sleep (.50)
print ("   ")
print ("{>----------Chose your gender----------<}")
print ("》》》》》》》》》》》~>1. Male ")
print ("》》》》》》》》》》》~>2. Female ")
time.sleep(.50)
print ("   ")
gender = int(input(" ■ write your gender : "))
time.sleep(.50)
print ("    ")
print (" 《>>>>>>>> Review your information <<<<<<<<》 ")
print ("○○○○○○《>>your name  :- " + str(name) )
print ("○○○○○○《>>your age   :- " + str(age) )
print ("○○○○○○《>>your weight:- " + str(weight) )
print ("○○○○○○《>>your height:- " + str(height) )
print ("○○○○○○《>>your gender:  " + str(gender) )
print ("   ")
time.sleep(1)
if gender == 2 :
	bmi = (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
	print ("  ■■ Your bmi is:- "+ str(bmi))
	if bmi > 57 :
		print ("I dont know who are you")
	else :
		print(" I don't know who are you")
elif gender > 2 :
	print ("⛔⛔⛔⛔Wrong input")
elif gender < 1 :
	print ("⛔⛔⛔Wrong input")
else :
	bmi1 = (66 + (13.7* weight) + (5 * height) - (6.8 * age))
	print ("  ■■ Your bmi is:- "+ str(bmi1))
	if bmi1 > 57 :
		print ("Trust me I am a boy")
	else :
		print ("Trust me I am a boy")





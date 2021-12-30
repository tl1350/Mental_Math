import random
import copy
import pyinputplus as pyip
import pyttsx3


#Dictionary that stores problems are solutions
info_template = {
    "point": 0,
    "question": "",
    "num1": 0,
    "num2": 0,
    "type":"",
    "answer": 0,
    "formula":""
} 

####initiate voice object
engine = pyttsx3.init()

################1.Function for addition and subtraction ####################################

def add_subt(problem_id):
    # Purpose: Generates addition and subtraction questions based on number range
    # Tactics: Uses a while loop
    # Status: Basics work
    
    lowest_num = -999 #select number range
    highest_num = 999

    #dictionary to store info
    info = copy.deepcopy(info_template)
    info["type"]= "add"

    info["num1"] = random.randint(lowest_num, highest_num)
    info["num2"] = random.randint(lowest_num, highest_num)
    info["answer"] = info["num1"] + info["num2"] 
    info["formula"] = '= {} + {}'.format(info["num1"],info["num2"])
    
    speech = str(info["num1"]) + " plus" + str()
    engine.say(speech)
    engine.say(info["num2"]) ###fix tmw?
    #engine.save_to_file(speech , 'current_problem.mp3')
    engine.runAndWait()
    
    response = None
    score = 0
    
    while response != info["answer"]:
        response = pyip.inputInt(prompt='{}: {} + {} = '.format(problem_id,info["num1"],info["num2"]))
        if response == info["answer"]:
            score += 1
        else:
            score -=1
    
    info["point"] = max(0,score)

    return info

#################Section 2: Multiplication###################################
# Purpose: Generates multiplication problems based on number range (can select to study squares only)
# Tactics: Uses a pyip.inputCustom function
# Status: Basics work

def mult(problem_id, program_type):
  
    lowest_num = 10
    highest_num = 100
    score = 0
    response = None
    
    #dictionary to store info
    info = copy.deepcopy(info_template)
    

    info["num1"] = random.randint(lowest_num, highest_num)

    if program_type == "squares":
        info["num2"] = info["num1"]
        info["type"]= "square"
    else:    
        info["num2"] = random.randint(lowest_num, highest_num)
        info["type"]= "mult"
    
    question = '{}: {} * {} = '.format(problem_id,info["num1"],info["num2"])
    info["answer"] = info["num1"] * info["num2"]
    info["formula"] = '= {} * {}'.format(info["num1"],info["num2"])
    
  

    speech = str(info["num1"]) + " times" + str(info["num2"])
    engine.say(speech)
    #engine.save_to_file(speech , 'current_problem.mp3')
    engine.runAndWait()

    while response != info["answer"]:
        response = pyip.inputInt(prompt=question)
        if response == info["answer"]:
            score += 1
        else:
            score -= 1

    info["point"] = max(0,score)

    return info
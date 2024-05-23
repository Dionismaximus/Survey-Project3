import gspread
from google.oauth2.service_account import Credentials
from collections import Counter

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Popular-Games-Survey')

results = SHEET.worksheet('results')


'''
print("------------------")
print("We are pleased to welcome you to the video game popularity survey. Your answers are very important to us!")
print("------------------")
print("*** SURVEY RULES ***")
print('Please enter only the number corresponding to your correct answer for each individual question and press the ENTER.\nIf you have read the rules and are ready to start the survey, enter 1 and press ENTER.')
'''

def survey_question():
    """
    List of questions which is displayed in the console for the user.
    """
    user_answers = []
    results_sheet = SHEET.worksheet('results')
    questions = results_sheet.get_all_values()
    
    # Question1
    question1 = questions[0][0]

    question1_option1 = '1 - Everyday'
    question1_option2 = '2 - A few times per week'
    question1_option3 = '3 - A few times per month'
    question1_option4 = '4 - A few times per year'
    while True:
        try:
            user_reply1 = int(input(f'{question1}\n{question1_option1}\n{question1_option2}\n{question1_option3}\n{question1_option4}\n----------\n'))
            if user_reply1 > 4 or user_reply1 == 0:
                raise ValueError(
                "Correct value should be from 1 to 4."
            )
            if user_reply1 == 1:
                user_answers.append(question1_option1)
            elif user_reply1 == 2:
                user_answers.append(question1_option2)
            elif user_reply1 == 3:
                user_answers.append(question1_option3)
            else:
                user_answers.append(question1_option4)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")
    print('')

    # Question2
    question2 = questions[0][1]

    question2_option1 = '1 - RPG'
    question2_option2 = '2 - Strategy'
    question2_option3 = '3 - Action/Shooter'
    question2_option4 = '4 - Sport/Simulators'
    question2_option5 = '5 - MOBA/MMORPG'
    question2_option6 = '6 - Horror/Survival'
    question2_option7 = '7 - Adventure'
    while True:
        try:
            user_reply2 = int(input(f'{question2}\n{question2_option1}\n{question2_option2}\n{question2_option3}\n{question2_option4}\n{question2_option5}\n{question2_option6}\n{question2_option7}\n----------\n'))
            if user_reply2 > 7 or user_reply2 == 0:
                raise ValueError(
                "Correct value should be from 1 to 7."
            )
            if user_reply2 == 1:
                user_answers.append(question2_option1)
            elif user_reply2 == 2:
                user_answers.append(question2_option2)
            elif user_reply2 == 3:
                user_answers.append(question2_option3)
            elif user_reply2 == 4:
                user_answers.append(question2_option4)
            elif user_reply2 == 5:
                user_answers.append(question2_option5)
            elif user_reply2 == 6:
                user_answers.append(question2_option6)    
            else:
                user_answers.append(question2_option7)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')

    # Question3
    question3 = questions[0][2]

    question3_option1 = '1 - Buying'
    question3_option2 = '2 - Renting'
    question3_option3 = '3 - Download from internet'
    while True:
        try:
            user_reply3 = int(input(f'{question3}\n{question3_option1}\n{question3_option2}\n{question3_option3}\n----------\n'))
            if user_reply3 > 3 or user_reply3 == 0:
                raise ValueError(
                "Correct value should be from 1 to 3."
            )
            if user_reply3 == 1:
                user_answers.append(question3_option1)
            elif user_reply3 == 2:
                user_answers.append(question3_option2)
            else:
                user_answers.append(question3_option3)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")
    print('')

    # Question4
    question4 = questions[0][3]

    question4_option1 = '1 - PC'
    question4_option2 = '2 - Laptop'
    question4_option3 = '3 - Tablet'
    question4_option4 = '4 - Smartphone'
    question4_option5 = '5 - Console'
    while True:
        try:
            user_reply4 = int(input(f'{question4}\n{question4_option1}\n{question4_option2}\n{question4_option3}\n{question4_option4}\n{question4_option5}\n----------\n'))
            if user_reply4 > 5 or user_reply4 == 0:
                raise ValueError(
                "Correct value should be from 1 to 5."
            )
            if user_reply4 == 1:
                user_answers.append(question4_option1)
            elif user_reply4 == 2:
                user_answers.append(question4_option2)
            elif user_reply4 == 3:
                user_answers.append(question4_option3)
            elif user_reply4 == 4:
                user_answers.append(question4_option4)
            else:
                user_answers.append(question4_option5)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')

    # Question5
    question5 = questions[0][4]

    question5_option1 = '1 - PC'
    question5_option2 = '2 - Console'
    question5_option3 = '3 - neither'
    while True:
        try:
            user_reply5 = int(input(f'{question5}\n{question5_option1}\n{question5_option2}\n{question5_option3}\n----------\n'))
            if user_reply5 > 3 or user_reply5 == 0:
                raise ValueError(
                "Correct value should be from 1 to 3."
            )
            if user_reply5 == 1:
                user_answers.append(question5_option1)
            elif user_reply5 == 2:
                user_answers.append(question5_option2)
            else:
                user_answers.append(question5_option3)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')

    # Question6
    question6 = questions[0][5]

    question6_option1 = '1 - 0 - €50'
    question6_option2 = '2 - €50 - €200'
    question6_option3 = '3 - €200+'
    while True:
        try:
            user_reply6 = int(input(f'{question6}\n{question6_option1}\n{question6_option2}\n{question6_option3}\n----------\n'))
            if user_reply6 > 3 or user_reply6 == 0:
                raise ValueError(
                "Correct value should be from 1 to 3."
            )
            if user_reply6 == 1:
                user_answers.append(question6_option1)
            elif user_reply6 == 2:
                user_answers.append(question6_option2)
            else:
                user_answers.append(question6_option3)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')
    
    # Question7
    question7 = questions[0][6]

    question7_option1 = '1 - GTA series'
    question7_option2 = '2 - The Witcher 3: Wild Hunt'
    question7_option3 = '3 - The Elder Scrolls V: Skyrim'
    question7_option4 = '4 - Total War series'
    question7_option5 = '5 - Minecraft' 
    question7_option6 = '6 - Mass Effect Legendary Edition'
    question7_option7 = '7 - Dark Souls series'
    question7_option8 = '8 - The Sims' 
    question7_option9 = '9 - Forza Horizon series' 
    question7_option10 = '10 - Dragon Age: Origins'
    question7_option11 = '11 - The Last of Us'
    question7_option12 = '12 - Read Dead Redemption 2'
    question7_option13 = '13 - none of those options'
    while True:
        try:
            user_reply7 = int(input(f'{question7}\n{question7_option1}\n{question7_option2}\n{question7_option3}\n{question7_option4}\n{question7_option5}\n{question7_option6}\n{question7_option7}\n{question7_option8}\n{question7_option9}\n{question7_option10}\n{question7_option11}\n{question7_option12}\n{question7_option13}\n----------\n'))
            if user_reply7 > 13 or user_reply7 == 0:
                raise ValueError(
                "Correct value should be from 1 to 13."
            )
            if user_reply7 == 1:
                user_answers.append(question7_option1)
            elif user_reply7 == 2:
                user_answers.append(question7_option2)
            elif user_reply7 == 3:
                user_answers.append(question7_option3)
            elif user_reply7 == 4:
                user_answers.append(question7_option4)
            elif user_reply7 == 5:
                user_answers.append(question7_option5)
            elif user_reply7 == 6:
                user_answers.append(question7_option6)
            elif user_reply7 == 7:
                user_answers.append(question7_option7)
            elif user_reply7 == 8:
                user_answers.append(question7_option8)
            elif user_reply7 == 9:
                user_answers.append(question7_option9)
            elif user_reply7 == 10:
                user_answers.append(question7_option10)
            elif user_reply7 == 11:
                user_answers.append(question7_option11)
            elif user_reply7 == 12:
                user_answers.append(question7_option12)
            else:
                user_answers.append(question7_option13)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')
    
    # Question8
    question8 = questions[0][7]

    question8_option1 = '1 - Lara Croft (Tomb Raider)'
    question8_option2 = '2 - Kratos (God of War)'
    question8_option3 = "3 - Ezio Auditore da Firenze (Assassin's Creed)"
    question8_option4 = '4 - Arthur Morgan (Read Dead Redemption 2)'
    question8_option5 = '5 - Ellie Williams (The Last of Us)' 
    question8_option6 = '6 - Trevor Philips (GTA V)'
    question8_option7 = '7 - Carl Johnson (GTA: San Andreas)'
    question8_option8 = '8 - Shepard (Mass Effect)' 
    question8_option9 = '9 - Link (Legend of Zelda)' 
    question8_option10 = '10 - Morrigan (Dragon Age)'
    question8_option11 = '11 - Mario'
    question8_option12 = '12 - none of those characters'

    while True:
        try:
            user_reply8 = int(input(f'{question8}\n{question8_option1}\n{question8_option2}\n{question8_option3}\n{question8_option4}\n{question8_option5}\n{question8_option6}\n{question8_option7}\n{question8_option8}\n{question8_option9}\n{question8_option10}\n{question8_option11}\n{question8_option12}\n----------\n'))
            if user_reply8 > 12 or user_reply8 == 0:
                        raise ValueError(
                        "Correct value should be from 1 to 12."
                    )
            if user_reply8 == 1:
                user_answers.append(question8_option1)
            elif user_reply8 == 2:
                user_answers.append(question8_option2)
            elif user_reply8 == 3:
                user_answers.append(question8_option3)
            elif user_reply8 == 4:
                user_answers.append(question8_option4)
            elif user_reply8 == 5:
                user_answers.append(question8_option5)
            elif user_reply8 == 6:
                user_answers.append(question8_option6)
            elif user_reply8 == 7:
                user_answers.append(question8_option7)
            elif user_reply8 == 8:
                user_answers.append(question8_option8)
            elif user_reply8 == 9:
                user_answers.append(question8_option9)
            elif user_reply8 == 10:
                user_answers.append(question8_option10)
            elif user_reply8 == 11:
                user_answers.append(question8_option11)
            else:
                user_answers.append(question8_option12)
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")


    return user_answers
    


def update_worksheet(data):
    """
    Receives a list of user answers and update results worksheet
    """
    results_sheet = SHEET.worksheet('results')
    results_sheet.append_row(data)



most_common_response_sheet = SHEET.worksheet('most_common_response')
most_common_response = []
second_common_response = []
third_common_response = []

def calculate_popular_reply():
    """
    Calculate the most popular response for each question and update those results in most_common_reply worksheet
    """
    #Question 1
    first_column_replies = []
    first_column = results.col_values(1)[1:]

    for i in first_column:
        first_column_replies.append(i[0])

    most_common_answer1 = Counter(first_column_replies).most_common(3)
    index = 0
    user_responses = []
    while index < 3:
        if int(most_common_answer1[index][0]) == 1: 
            percentage = round(100 / (len(first_column) / most_common_answer1[index][1])) 
            user_responses.append(f'Everyday - {percentage}%') 
        elif int(most_common_answer1[index][0]) == 2: 
            percentage = round(100 / (len(first_column) / most_common_answer1[index][1])) 
            user_responses.append(f'A few times per week - {percentage}%') 
        elif int(most_common_answer1[index][0]) == 3: 
            percentage = round(100 / (len(first_column) / most_common_answer1[index][1])) 
            user_responses.append(f'A few times per month - {percentage}%') 
        elif int(most_common_answer1[index][0]) == 4:
            percentage = round(100 / (len(first_column) / most_common_answer1[index][1])) 
            user_responses.append(f'A few times per year - {percentage}%')
        else:
            print('Something gone wrong!')
        index += 1
        
    
    most_common_response.append(user_responses[0])
    second_common_response.append(user_responses[1])
    third_common_response.append(user_responses[2])
    

    #Question 2
    second_column_replies = []
    second_column = results.col_values(2)[1:]

    for i in second_column:
        second_column_replies.append(i[0])

    most_common_answer2 = Counter(second_column_replies).most_common(3)
    index = 0
    user_responses = []

    while index < 3:
        if int(most_common_answer2[index][0]) == 1:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'RPG - {percentage}%') 
        elif int(most_common_answer2[index][0]) == 2:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'Strategy - {percentage}%') 
        elif int(most_common_answer2[index][0]) == 3:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'Action/Shooter - {percentage}%') 
        elif int(most_common_answer2[index][0]) == 4:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'Sport/Simulators - {percentage}%')
        elif int(most_common_answer2[index][0]) == 5:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'MOBA/MMORPG - {percentage}%')
        elif int(most_common_answer2[index][0]) == 6:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'Horror/Survival - {percentage}%')
        elif int(most_common_answer2[index][0]) == 7:
            percentage = round(100 / (len(second_column) / most_common_answer2[index][1])) 
            user_responses.append(f'Adventure - {percentage}%')
        else:
            print('Something gone wrong!')
        index += 1
    most_common_response.append(user_responses[0])
    second_common_response.append(user_responses[1])
    third_common_response.append(user_responses[2])
    

    print(most_common_response)
    print(second_common_response)
    print(third_common_response)



calculate_popular_reply()
update_worksheet(survey_question())













'''
if int(most_common_answer1[0][0]) == 1: 
    percentage = round(100 / (len(first_column) / most_common_answer1[0][1])) 
    most_common_replies.append(f'Everyday - {percentage}%') 
elif int(most_common_answer1[0][0]) == 2: 
    percentage = round(100 / (len(first_column) / most_common_answer1[0][1])) 
    most_common_replies.append(f'A few times per week - {percentage}%') 
elif int(most_common_answer1[0][0]) == 3: percentage = round(100 / (len(first_column) / most_common_answer1[0][1])) 
    most_common_replies.append(f'A few times per month - {percentage}%') 
else:
    percentage = round(100 / (len(first_column) / most_common_answer1[0][1])) 
    most_common_replies.append(f'A few times per year - {percentage}%')
'''
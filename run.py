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



print("------------------")
print("We are pleased to welcome you to the video game popularity survey. Your answers are very important to us!")
print("------------------")


#Survey question options
options1 = ['1 - Everyday', '2 - A few times per week', '3 - A few times per month', '4 - A few times per year']
options2 = ['1 - RPG', '2 - Strategy', '3 - Action/Shooter', '4 - Sport/Simulators', '5 - MOBA/MMORPG', '6 - Horror/Survival', '7 - Adventure']
options3 = ['1 - Buying', '2 - Renting', '3 - Download from internet']
options4 = ['1 - PC', '2 - Laptop', '3 - Tablet', '4 - Smartphone', '5 - Console']
options5 = ['1 - PC', '2 - Console', '3 - neither']
options6 = ['1 - 0 - €50', '2 - €50 - €200', '3 - €200+']
options7 = ['1 - GTA series', '2 - The Witcher 3: Wild Hunt', '3 - The Elder Scrolls V: Skyrim', '4 - Total War series', '5 - Minecraft', '6 - Mass Effect Legendary Edition', '7 - Dark Souls series', '8 - The Sims', '9 - Forza Horizon series', '10 - Dragon Age: Origins', '11 - The Last of Us', '12 - Read Dead Redemption 2', '13 - none of those options']
options8 = ['1 - Lara Croft (Tomb Raider)', '2 - Kratos (God of War)', "3 - Ezio Auditore da Firenze (Assassin's Creed)", '4 - Arthur Morgan (Read Dead Redemption 2)', '5 - Ellie Williams (The Last of Us)', '6 - Trevor Philips (GTA V)', '7 - Carl Johnson (GTA: San Andreas)', '8 - Shepard (Mass Effect)', '9 - Link (Legend of Zelda)', '10 - Morrigan (Dragon Age)', '11 - Mario', '12 - Geralt (Witcher)', '13 - none of those characters']


most_common_response = []
second_common_response = []
third_common_response = []

def start_survey():
    """
    Allows the user to start the survey after reading the rules.
    """
    print("*** SURVEY RULES ***")
    print('Please enter only the number corresponding to your correct answer for each individual question and press the ENTER.\n')
    while True:    
        try:
            start_survey = input('If you have read the rules and are ready to start the survey, enter 1 and press ENTER\n')
            if int(start_survey) == 1:
                break
        except:
            print('Please, ENTER 1 to start the survey.')

def survey_question():
    """
    List of questions which is displayed in the console for the user.
    """
    user_answers = []
    results_sheet = SHEET.worksheet('results')
    questions = results_sheet.get_all_values()
    
    # Question1
    question1 = questions[0][0]

    while True:
        try:
            print('# Question 1')
            user_reply1 = int(input(f'{question1}\n----------\n{options1[0]}\n{options1[1]}\n{options1[2]}\n{options1[3]}\n----------\n'))
            if user_reply1 > 4 or user_reply1 == 0:
                raise ValueError(
                "Correct value should be from 1 to 4."
            )
            if user_reply1 == 1:
                user_answers.append(options1[0])
            elif user_reply1 == 2:
                user_answers.append(options1[1])
            elif user_reply1 == 3:
                user_answers.append(options1[2])
            else:
                user_answers.append(options1[3])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")
    print('')

    # Question2
    question2 = questions[0][1]

    while True:
        try:
            print('# Question 2')
            user_reply2 = int(input(f'{question2}\n----------\n{options2[0]}\n{options2[1]}\n{options2[2]}\n{options2[3]}\n{options2[4]}\n{options2[5]}\n{options2[6]}\n----------\n'))
            if user_reply2 > 7 or user_reply2 == 0:
                raise ValueError(
                "Correct value should be from 1 to 7."
            )
            if user_reply2 == 1:
                user_answers.append(options2[0])
            elif user_reply2 == 2:
                user_answers.append(options2[1])
            elif user_reply2 == 3:
                user_answers.append(options2[2])
            elif user_reply2 == 4:
                user_answers.append(options2[3])
            elif user_reply2 == 5:
                user_answers.append(options2[4])
            elif user_reply2 == 6:
                user_answers.append(options2[5])    
            else:
                user_answers.append(options2[6])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')

    # Question3
    question3 = questions[0][2]

    while True:
        try:
            print('# Question 3')
            user_reply3 = int(input(f'{question3}\n----------\n{options3[0]}\n{options3[1]}\n{options3[2]}\n----------\n'))
            if user_reply3 > 3 or user_reply3 == 0:
                raise ValueError(
                "Correct value should be from 1 to 3."
            )
            if user_reply3 == 1:
                user_answers.append(options3[0])
            elif user_reply3 == 2:
                user_answers.append(options3[1])
            else:
                user_answers.append(options3[2])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")
    print('')

    # Question4
    question4 = questions[0][3]

    while True:
        try:
            print('# Question 4')
            user_reply4 = int(input(f'{question4}\n----------\n{options4[0]}\n{options4[1]}\n{options4[2]}\n{options4[3]}\n{options4[4]}\n----------\n'))
            if user_reply4 > 5 or user_reply4 == 0:
                raise ValueError(
                "Correct value should be from 1 to 5."
            )
            if user_reply4 == 1:
                user_answers.append(options4[0])
            elif user_reply4 == 2:
                user_answers.append(options4[1])
            elif user_reply4 == 3:
                user_answers.append(options4[2])
            elif user_reply4 == 4:
                user_answers.append(options4[3])
            else:
                user_answers.append(options4[4])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')

    # Question5
    question5 = questions[0][4]

    while True:
        try:
            print('# Question 5')
            user_reply5 = int(input(f'{question5}\n----------\n{options5[0]}\n{options5[1]}\n{options5[2]}\n----------\n'))
            if user_reply5 > 3 or user_reply5 == 0:
                raise ValueError(
                "Correct value should be from 1 to 3."
            )
            if user_reply5 == 1:
                user_answers.append(options5[0])
            elif user_reply5 == 2:
                user_answers.append(options5[1])
            else:
                user_answers.append(options5[2])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')

    # Question6
    question6 = questions[0][5]

    while True:
        try:
            print('# Question 6')
            user_reply6 = int(input(f'{question6}\n----------\n{options6[0]}\n{options6[1]}\n{options6[2]}\n----------\n'))
            if user_reply6 > 3 or user_reply6 == 0:
                raise ValueError(
                "Correct value should be from 1 to 3."
            )
            if user_reply6 == 1:
                user_answers.append(options6[0])
            elif user_reply6 == 2:
                user_answers.append(options6[1])
            else:
                user_answers.append(options6[2])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')
    
    # Question7
    question7 = questions[0][6]

    while True:
        try:
            print('# Question 7')
            user_reply7 = int(input(f'{question7}\n----------\n{options7[0]}\n{options7[1]}\n{options7[2]}\n{options7[3]}\n{options7[4]}\n{options7[5]}\n{options7[6]}\n{options7[7]}\n{options7[8]}\n{options7[9]}\n{options7[10]}\n{options7[11]}\n{options7[12]}\n----------\n'))
            if user_reply7 > 13 or user_reply7 == 0:
                raise ValueError(
                "Correct value should be from 1 to 13."
            )
            if user_reply7 == 1:
                user_answers.append(options7[0])
            elif user_reply7 == 2:
                user_answers.append(options7[1])
            elif user_reply7 == 3:
                user_answers.append(options7[2])
            elif user_reply7 == 4:
                user_answers.append(options7[3])
            elif user_reply7 == 5:
                user_answers.append(options7[4])
            elif user_reply7 == 6:
                user_answers.append(options7[5])
            elif user_reply7 == 7:
                user_answers.append(options7[6])
            elif user_reply7 == 8:
                user_answers.append(options7[7])
            elif user_reply7 == 9:
                user_answers.append(options7[8])
            elif user_reply7 == 10:
                user_answers.append(options7[9])
            elif user_reply7 == 11:
                user_answers.append(options7[10])
            elif user_reply7 == 12:
                user_answers.append(options7[11])
            else:
                user_answers.append(options7[12])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")

    print('')
    
    # Question8
    question8 = questions[0][7]

    while True:
        try:
            print('# Question 8')
            user_reply8 = int(input(f'{question8}\n----------\n{options8[0]}\n{options8[1]}\n{options8[2]}\n{options8[3]}\n{options8[4]}\n{options8[5]}\n{options8[6]}\n{options8[7]}\n{options8[8]}\n{options8[9]}\n{options8[10]}\n{options8[11]}\n{options8[12]}\n----------\n'))
            if user_reply8 > 13 or user_reply8 == 0:
                        raise ValueError(
                        "Correct value should be from 1 to 13."
                    )
            if user_reply8 == 1:
                user_answers.append(options8[0])
            elif user_reply8 == 2:
                user_answers.append(options8[1])
            elif user_reply8 == 3:
                user_answers.append(options8[2])
            elif user_reply8 == 4:
                user_answers.append(options8[3])
            elif user_reply8 == 5:
                user_answers.append(options8[4])
            elif user_reply8 == 6:
                user_answers.append(options8[5])
            elif user_reply8 == 7:
                user_answers.append(options8[6])
            elif user_reply8 == 8:
                user_answers.append(options8[7])
            elif user_reply8 == 9:
                user_answers.append(options8[8])
            elif user_reply8 == 10:
                user_answers.append(options8[9])
            elif user_reply8 == 11:
                user_answers.append(options8[10])
            elif user_reply8 == 12:
                user_answers.append(options8[11])    
            else:
                user_answers.append(options8[12])
            break
        except ValueError as e:
            print(f"Invalid data! {e}\nPlease enter only the number of the correct answer for you.\n******")


    return user_answers
    


def update_result_worksheet(data):
    """
    Receives a list of user answers and update results worksheet
    """
    results_sheet = SHEET.worksheet('results')
    results_sheet.append_row(data)




def calculate_popular_reply(column_number, options):
    """
    Counts the most popular, second and third responses for questions
    """
    #Question 1
    column_replies = []
    column = results.col_values(column_number)[1:]

    for i in column:
        column_replies.append(i[0])

    most_common_answer = Counter(column_replies).most_common(3)

    index = 0
    user_responses = []
    while index < len(most_common_answer):
        if int(most_common_answer[index][0]) == 1: 
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[0][4:]} - {percentage}%') 
        elif int(most_common_answer[index][0]) == 2: 
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[1][4:]} - {percentage}%') 
        elif int(most_common_answer[index][0]) == 3: 
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[2][4:]} - {percentage}%') 
        elif int(most_common_answer[index][0]) == 4:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[3][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 5:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[4][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 6:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[5][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 7:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[6][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 8:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[7][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 9:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[8][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 10:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[9][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 11:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[10][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 12:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[11][4:]} - {percentage}%')
        elif int(most_common_answer[index][0]) == 13:
            percentage = round(100 / (len(column) / most_common_answer[index][1])) 
            user_responses.append(f'{options[12][4:]} - {percentage}%')
        else:
            print('Something gone wrong!')
        index += 1
        
    if len(most_common_answer) == 3:
        most_common_response.append(user_responses[0])
        second_common_response.append(user_responses[1])
        third_common_response.append(user_responses[2])
    elif len(most_common_answer) == 2:
        most_common_response.append(user_responses[0])
        second_common_response.append(user_responses[1])
        third_common_response.append('')
    else:
        most_common_response.append(user_responses[0])
        second_common_response.append('')
        third_common_response.append('')



def update_most_common_response_worksheet():
    """
    Update most_common_response worksheet with the most common response, the second common response
    and the third common response. Delete previous data before add new data.
    """

    most_common_response_sheet = SHEET.worksheet('most_common_response')
    print('Saving your responses...')
    most_common_response_sheet.batch_clear(["A2:H4"])
    most_common_response_sheet.append_row(most_common_response)
    most_common_response_sheet.append_row(second_common_response)
    most_common_response_sheet.append_row(third_common_response)

    print('.')
    print('.')
    print('.')
    print('Your responses have been noted and saved. Thank you for your participation!')



def main():
    """
    Run all program function
    """
    start_survey()
    update_result_worksheet(survey_question())

    calculate_popular_reply(1, options1)
    calculate_popular_reply(2, options2)
    calculate_popular_reply(3, options3)
    calculate_popular_reply(4, options4)
    calculate_popular_reply(5, options5)
    calculate_popular_reply(6, options6)
    calculate_popular_reply(7, options7)
    calculate_popular_reply(8, options8)

    update_most_common_response_worksheet()

main()
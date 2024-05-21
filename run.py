import gspread
from google.oauth2.service_account import Credentials

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

data = results.get_all_values()[0][0]

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
    question1_user_reply1 = questions[-1][0]

    question1_option1 = '1 - Everyday'
    question1_option2 = '2 - A few times per week'
    question1_option3 = '3 - A few times per month'
    question1_option4 = '4 - A few times per year'

    user_reply1 = int(input(f'{question1}\n{question1_option1}\n{question1_option2}\n{question1_option3}\n{question1_option4}\n----------\n'))
    if user_reply1 == 1:
        user_answers.append(question1_option1)
    elif user_reply1 == 2:
        user_answers.append(question1_option2)
    elif user_reply1 == 3:
        user_answers.append(question1_option3)
    else:
        user_answers.append(question1_option4)
    
    return user_answers
    


def update_worksheet(data):
    """
    Receives a list of user answers and update results worksheet
    """
    results_sheet = SHEET.worksheet('results')
    results_sheet.append_row(data)

user_answers = survey_question()
update_worksheet(user_answers)


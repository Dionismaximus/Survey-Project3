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

data = results.get_all_values()[1]

print("------------------")
print("We are pleased to welcome you to the video game popularity survey. Your answers are very important to us!")
print("------------------")
print("*** SURVEY RULES ***")
print('Please enter only the number corresponding to your correct answer for each individual question and press the ENTER.\nIf you have read the rules and are ready to start the survey, enter 1 and press ENTER.')


def survey_question():
    """
    List of questions which is displayed in the console for the user.
    """
    question1 = input('How often do you play games?\n1 - Everyday\n2 - A few times per week\n3 - A few times per month\n4 - Few times per year\n')
    print(question1)

survey_question()
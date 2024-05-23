# Popular Games Survey
## Overview
This website is the third project in my Code Institute course.

It showcases various programming skills and methods that I acquired during the course.

Popular Games Survey created with Python, which runs in the Code Institute mock terminal on Heroku.

Link to the live site here: [Popular Games Survey](https://dionismaximus.github.io/rock-paper-scissors/)

![](assets/images/Readme-img/responsivedesign.png)

## Survey rules
You have the chance to take part in a survey about the popularity of computer games.
The survey participant must choose one of the options to the questions on the survey questionnaire.

## Features
### Existing features
- __Start the survey__
  - User must enter 1 indicating that the user is fully aware of the rules and is ready to start the survey.
- __Input data__
  - The app receives input data from the user and save it in the google sheet. 
- __Data storage__
  - After the last question all responses saved in the googlesheet.
- __Data analysis__
  - All previous data received from respondents is analyzed and stored in a separate google spreadsheet.
  - Data in the most_common_response sheet is displays the top three most popular answers for each question, and indicates their relevance as a percentage.
  - All data is updated after each successive survey completed.
- __Input validation and error-checking__
  - User cannot enter number which is beyond the range of possible options.
  - User musts enter only digit number corresponding to the option.

### Future features
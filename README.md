# FeelGood Physio Booking System

## A Command Line Interface Application

![Screenshot of Home screen](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/screenshot_home.png)
**FeelGood Physio is an application built for a fictional physiotherapy clinic, syncronized with Google Calendar and Google sheets.**

[Click here](https://feelgood-physio.herokuapp.com/) to visit the deployed site.

[Here](https://calendar.google.com/calendar/u/0?cid=dXVlcTNzMnRiZ2RsNTdkdm1tdmNwNW9zZDhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) is the link to view the Google Calendar as it is updated. You will have to log in to Google and add it to your subscribed calendars, but it is just as easy to remove it again.

[Here](https://docs.google.com/spreadsheets/d/1tZfgo8_TkdA9EdJyrj58YbFePcTcciv-zyC2UBqY6-g/edit?usp=sharing) is the link to the Google Spreadsheet, to see the updates made.

## Contents

1. [Strategy](#strategy)
    1. [Project Goals](#project-goals)
    2. [Future Goals](#future-goals)
    3. [User Goals](#user-goals)

2. [Structure](#structure)

3. [User Stories](#user-stories)
    1. [User Stories](#user-stories)
    2. [Site Owner Goals](#site-owner-goals)

5. [Surface](#surface)
    1. [Design Choices](#design-choices)

2. [Features](#features)
    1. [Existing Features](#existing-features)
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Applications, Libraries and Platforms](#applications-libraries-and-platforms)

4. [Validation](#validation)
    1. [Performance](#performance)

4. [Testing of User Stories/Site Owner Goals](#testing-of-user-stories/site-owner-goals)
    1. [Testing of User Stories](#testing-of-user-stories)
    2. [Testing of Site Owner Goals](#testing-of-site-owner-goals)

5. [Bugs](#bugs)

6. [Deployment](#deployment)
    1. [GitHub Pages](#github-pages)
    2. [Heroku](#heroku)
    2. [Forking the GitHub Repository](#forking-the-github-repository)
    3. [Making a Local Clone](#making-a-local-clone)

7. [Credits](#credits)

## User Experience

### Strategy
___

#### Project Goals

Project Goals for intended use are:

- Creating a system for managing bookings and patient data for both staff and patients.
- Making this system easy and effective for all users.
- Displaying relevant information so users can easily navigate.

My personal project goals of FeelGood Physio are:

- To build an application that serves the booking needs of both patients and staff
- To explore the possibilities of working with API's
- To gain knowledge of the Python programming language

#### User Goals

Patients should find it simple to book appointments, and not be able to book a timeslot that is not available. Patients should also be made aware if their data is being logged.

Staff should find it easy to access and modify their schedule and patient data.

Target Audience

- A Physiotherapist (or their receptionist)
- Patients


### Structure
___

The FeelGood Physio Booking System relies almost only on user input. There are always options displayed on the screen and users can choose what to do next.
When an input is entered, the application takes the user to the chosen option. All functions are chained together, each depending on the users input.

#### 1. Home Screen

![Screenshot of Home screen](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/screenshot_home.png)

This welcomes the user when they first enter the application, when the task at hand is done or when users choose to exit from whereever they are in the application. From the home screen, there are two options:

- Book appointment - takes users to the booking process
- Staff login - takes users to the staff area

#### 2. Booking process for patient

![Patient booking, month](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_month.png)

This is a long chain of functions resulting in a new appointment and an update to the patient log, if completed. Users input their desired appoinment time and details, and get a confirmation message at the end.

#### 3. Staff area

To access the staff area, users need the staff password. If entered correctly, users can either view the patient log, or access the schedule.

![Staff area](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/staff_area/password.png)

#### 4. Staff Schedule

The schedule, which shows 1 week at a time, can be edited, which also updates the linked Google Calendar.

#### 5. Patient Log

The log, which is a Google Sheet, updates dynamically as users book appointments.


### User Stories
___

As this application has such specific target users, I have adapted my user stories to patients and staff.

#### Patient user stories:

1. I would like to be able to book an appointment at a time of my choosing, should the appointement be available
2. I would like to be alerted if my details are saved before I enter them
3. I would like to be well informed from the application throughout the booking process
4. I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again
5. I would like to be able to confirm the booking right before it is made
6. I would like to view a confirmation of the booking when it is made
7. I would like to at any point cancel my booking during the booking process should I wish to do so

#### Staff member user stories:

8. I would like for users to only be able to book appointments on weekdays between 9 and 17, and when the schedule is free
9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
10. I would like the appointments made by patients dynamically update my Google Calendar
11. I would like the changes made in the applications edit menu to update the events on my Google Calendar
12. I would like to be able to view the patient log
13. I would like to view my schedule for the coming week
14. I would like to navigate between weeks in my schedule
15. I would like to be able to update or remove any appointment viewed in my schedule
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

#### Site owner goals

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does


### Flowchart
___

Below is a flowchart describing the structure of the application, created with [Lucidchart](https://lucid.co/product/lucidchart).

![Flowchart](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/flowchart.png)

### Technology Design
___

#### Data models

I have chosen to use several data models in this project, but rely mainly on dictionaries for managing data. For variation, I have created two classes for this project, and use lists aswell.

Dictionaries have attributes that fit perfectly for this project; for example, I can easily pair a patient number with an ID that Google uses for the specific event. Another example is appointment dictionary, given its values by the user and pushed to the Google Calendar.

Here are the most important objects:

- The appointment list(cal_mod.apt_list) that stores dictionaries of appointments, to be read or edited and then passed through the Google API to the Calendar

- The IncDecWeek class, used to increment the the number of days ahead or in the past to display the schedule from.
- The time format converter class (TimeFConverter), created in four instances for each ty p of conversion it makes.

- The appointment dictionary (app_dict), created in the print_appointment function to pair the Google events specific ID together with numbers, that the user can input to edit that appointment. New numbers from 1 upwards are created each time the function is called.
- apntmnt_to_edit, a dictionary of a single event that the edit_appntmnt function gets from Google Calendar, to edit and then push back to Google with new values.
- The month dictionary (month_dict), used to pair the months three letter abbreviations with their corresponding number of days, accessed when getting date details from user.
- The patient dictionary helps the Google Sheets patient log keep track of patients that have booked appointments, keeping their details as values and assigning (with the help of the get_p_nr function) a unique patient ID. These details can then be displayed to the staff user.

#### User interface

I find it important to be clear to the user on displaying information, especially on an interface where styling is limited. As this project focuses solely on the Python language, I decided not to try to implement graphics and focus on funcionality, even though it was tempting.

I have, however, put lots of time in displaying the information to the user as correctly and as clearly as possible. Each message or piece of data displayed to the user has space around it, separating it from the previous one, for optimal readability.

Some simple formatting has also been done, for example when displaying date time, the time format converter converts it into a format that is easier and more pleasing to read.
Also, when displaying the patient log, I have removed curly braces and apostophes before the patient data is printed to the screen, only needed when managing it.

Messages to clarify what has and has not been done, and what the user's choices are have carefully been created to make the user experience as straightforward as possible.

## Features

### Feature 1 The Patient Booking System

![Patient Booking System](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_month.png)

This is the main feature of the application, getting patient information to make a booking and make a patient log entry.

The patient booking system consists of several steps after the welcome screen. The user can exit the booking process at any time.

- The patient is made aware that their details are saved and have to take action to continue

- The patient is prompted to choose month of the appointment (if the month chosen is june, and it is july at the point of booking, the application will change the year to next year)

- The patient is informed of the month chosen and get to choose date. The date must corrrespond with the days in that month, made sure by the month_dict dictionary.

- The patient is notified of the date chosen and can choose the time of the appointment, 9 - 17. The time must be a weekday and between 9 and 17. After validation, the first API request is made. The application gets data through the Google API if the chosen time slot is available in the Google calendar, and, if so, notifies the user. If the slot is not available, the user has to choose another time.

- If the timeslot is available, the user is prompted to enter their full name. A single name or name with digits is not accepted.

- The user is, if the name is accepted, prompted to enter their email adress, which is validated with a simple regular expression.

- If the email input is correct, the patient is prompted to shortly describe their symptoms. This must b at least 8 characters long, so the user cannot enter nothing or a short word.

- The user is shown the appointment and must confirm the booking.

![Confirm patient booking](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_done.png)

- If the booking is confirmed by the user, two requests are made with the users input; one to push the information to FeelGood Physio's Google calendar and one to make an entry in the Google sheets patient log on Google Drive, all with the help of the Google API.

![Google calendar entry](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/google_cal/g_cal_new.png)

If the user with the same name already exists in the patient log, the patients symptoms are unpdated instead of a row being added. The patient is then notified that the booking has been made and can return to the home screen again.

![Google sheets](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/g_sheets_new.png)

**Patient stories covered:**

1. I would like to be able to book an appointment at a time of my choosing, should the appointement be available
2. I would like to be alerted if my details are saved before I enter them
3. I would like to be well informed from the application throughout the booking process
4. I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again
5. I would like to be able to confirm the booking right before it is made
6. I would like to view a confirmation of the booking when it is made
7. I would like to at any point cancel my booking during the booking process should I wish to do so

**Staff member goals covered**

8. I would like for users to only be able to book appointments on weekdays between 9 and 17, and when the schedule is free
9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
10. I would like the appointments made by patients dynamically update my Google Calendar
11. I would like the changes made in the application to update the events on my Google Calendar

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does


### Feature 2: The Schedule

![The Schedule](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/schedule/schedule.png)

The Schedule is accessed via the staff area, which only users with a password can access. Here, users are initially shown the schedule from the current time and 7 days forward. The appointments are retrieved by an API request to FeelGood Physio's Google Calender, and can be edited and removed, by user inputting number displayed within the appointment.

The user can navigate with keys "n" for next and "b" for back, which will respectively retrieve the schedule for the next or previous week. New numbers are displayed for the user to modify specific appointments. If the user enters "e" for edit, the user gets several choices to edit below:

- Time: edit the date and time of the appointment
- Name: Change the name given in the appointment
- Details: Change the patient's email adress or symptoms description

![The edit menu](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/schedule/edit_apntmnt.png)

Upon changing these parameters and confirming the changes, the appointments are updated in the Google Calendar. The user is notified of this and can return to the staff menu or exit.

**Staff member goals covered**

11. I would like the changes made in the application edit menu to update the events on my Google Calendar
13. I would like to view my schedule for the coming week
14. I would like to navigate between weeks in my schedule
15. I would like to be able to update or remove any appointment viewed in my schedule
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does


### Feature 3: The Patient Log

![Patient Log](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log.png)

This is where staff can access data from patients that have booked via the booking system. The system lets users know before initiating the booking that their data will be logged, and after a successful booking the datails are logged in the Google Sheet via the API as a new entry. If the user already exists, their symptoms are the only thing that will be updated.

![Old patient books new appointment](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log_old_patient.png)

![The Google Sheet with the updated symptoms](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/sheet_update_sympt.png)

Even though the same details are kept in the Google Calendar, the patient log is a way to consolidate information if staff are looking for a specific patient.

**Staff member goals covered:**

9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
12. I would like to be able to view the patient log
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does


### Features to be implemented
___

There are endless possibilities with an application like this. If the clinic were to hire more than one therapist, they could each have their own calendar and log. Patients could have the possibility to add a user account with which they log in to the system, and can reschedule or cancel their appointment. An important feature that the log now lacks is the possibility for staff to edit entries; this will be implemented at a later stage.


## Technologies used

### Languages
___

- [Python 3](https://www.python.org/) - Was used solely to create this project.


### Applications and Libraries


#### Applications

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited, pushed and deployed to Github.

- [Gitpod](https://gitpod.com/) - All code was written and tested using the Gitpod web-based IDE.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [Lucidchart](https://lucid.co/product/lucidchart) - Lucidchart was used to create the [flowchart](#flowchart) of the project.


#### Python Libraries

I have used these third party libraries and Python libraries for this project:

- datetime: As time is of essence when working with calendars, this was essential.

- os: By using os I was able to both have my password in the workspace without pushing it to github, but also use it as a config var on heroku.

- re: to be able to validate using regular expressions

#### Third Party Libraries

- googleapiclient.discovery: needed to work with the Google API

- google.oauth2.service_account: So the application can access the account that the sheet and calendar are on with the credentials

- gspread: so the application can read Google Spreadsheets




## Validation

All Python files passed the [PEP8](http://pep8online.com/) and [Pylint](https://www.pylint.org/) tests with 0 errors.

Click [here](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/validation/validation.md) to view them.



## Testing of patient User Stories

User stories are tested with the features that cover them. All user stories passed the tests.

<details>
  <summary>View patient user story tests</summary>

### Patient user story 1. I would like to be able to book an appointment at a time of my choosing, should the appointement be available
___

**Covered by feature 1: The Patient Booking System**

![User story 1, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_1.png)
*The initial steps of the booking*

- **Actions**:

    * User hits "b" to begin
    * User enters "1" to agree on the application logging the patient data
    * User enters desired month of the appointment (Three letters)
    * User enters desired date (one or two figure numbers both work)
    * User is notified if the date is bookable
    * User enters desired hour of the appointment
    * User is notified if the timeslot is free or not
    * User enters their name
    * User enters their email
    * User enters their symptoms
    * User confirms by hitting "y"
    * User is greeted with their newly made booking
    * User can choose to go back to the beginning

![User story 1, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_2.png)
*Checks if the date is a weekend or if a booking is already made at that time*

![User story 1, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_3.png)
*Lets user know that the booking is made*

 - Expected result: *To Make a successful booking at an available time*

 - Actual result: *Works as intended*


### Patient user story 2. I would like to be alerted if my details are saved before I enter them
___

**Covered by feature 1: The Patient Booking System**

**Action** - *In the welcome screen, user hits "b" to get to the booking screen*

**Expected Result** - *Application displays message about storing data and user needs to confirm this to carry on*

**Actual Result** - *Works as intended*

![User story 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_2.png)


### Patient user story 3. I would like to be well informed from the application throughout the booking process
___

This user story is tested in the steps needed to make an appointment.

**Covered by feature 1: The Patient Booking System**

- **Action**: *User initiates a booking by pressing "b"*

- **Expected Result**: *Application displays message about storing data*

- **Actual Result**: *Works as intended*

![User story 1, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_1.png)

___

**Action** - *User hits "1" to continue*

**Expected Result** - *Application asks user for the month they would like to come*

**Actual Result** - *Works as intended*

___

**Action** - *User enters the three first letters of the month that they want to come*

**Expected Result** - *Application confirms the month entered and asks for the desired appointment date*

**Actual Result** - *Works as intended*

___

**Action** - *User enters the desired appointment date*

**Expected Result** - *Application lets user know if the date is unbookable, (weekends for example) or if it is available to book, in which case the app confirms date and asks user for time of appointment*

**Actual Result** - *Works as intended*

![User story 3, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_2.png)

___

**Action** - *User enters hour of desired appointment time*

**Expected Result** - *Application confirms the time and asks user for name if the desired appoinment time is free and bookable, otherwise lets the user know and user has to choose new time*

**Actual Result** - *Works as intended*

___

**Action** - *User enters their name*

**Expected Result** - *Application Confirms the users name and asks for their email*

**Actual Result** - *Works as intended*

![User story 3, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_3.png)

___

**Action** - *User enters their email*

**Expected Result** - *Application Confirms the users email address and asks user to enter their symptoms*

**Actual Result** - *Works as intended*

___

**Action** - *User enters their symptoms*

**Expected Result** - *Application displays all the patient data retrieved and asks user to confirm appointment*

**Actual Result** - *Works as intended*

___

**Action** - *User confirms appointment*

**Expected Result** - *Application displays confirmation, that patient data is logged and user can return to the main screen*

**Actual Result** - *Works as intended*

![User story 3, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_4.png)



### Patient user story 4. I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again
___

**Covered by feature 1: The Patient Booking System**


**Action** - *User enters invalid value, or date/time that is not free*

**Expected Result** - *Application let user know that the entry is invalid, and the user gets to try again*

**Actual Result** - *Works as intended*

The testing of this user case is best portrayed with the images below. All areas of navigation have passed the tests.

___

*Invalid choices at the welcome screen:*
![User story 4, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_1.png)

___

*Invalid choices when choosing month:*
![User story 4, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_2.png)

___

*Invalid choices when choosing date:*
![User story 4, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_3.png)

___

*Invalid choices when choosing weekend date:*
![User story 4, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_4.png)

___

*Invalid choices when choosing an already booked timeslot:*
![User story 4, 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_5.png)

___

*Invalid choices when entering single word:*
![User story 4, 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_6.png)

___

*Invalid choices when entering invalid email:*
![User story 4, 7](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_7.png)

___

*Invalid choices when entering too short description of symptoms:*
![User story 4, 8](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_8.png)



### User story 5. I would like to be able to confirm the booking right before it is made
___

**Covered by feature 1: The Patient Booking System**

**Action** - *User completes booking and enters valid information throughout the booking process*

**Expected Result** - *User is asked to confirm the booking*

**Actual Result** - *Works as intended*

![User story 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_3.png)


### User story 6. I would like to view a confirmation of the booking when it is made
___

**Covered by feature 1: The Patient Booking System**

**Action** - *User confirms the booking made*

**Expected Result** - *Application displays the details of the booking*

**Actual Result** - *Works as intended*

![User story 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_6.png)
___

**Covered by feature 1: The Patient Booking System**


#### User story 7. I would like to at any point cancel my booking during the booking process should I wish to do so
___

**Covered by feature 1: The Patient Booking System**

**Action** - *User follows instructions to exit on screen*

**Expected Result** - *Booking returns to the home screen or the previous stage*

**Actual Result** - *Works as intended*

![User story 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_6.png)
___

![timer](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/timer.png)

#### User story 8

**As a user, i would like to see an end game screen alerting me of my score and how the quiz went**

**The Quiz Feature**

- Action: *User play quiz, which then ends*

- Expected Result: *A modal covers the screen ending the game*

- Actual Result: *Works as intended*

#### User story 9:

**As a user, i would like to be able to choose to close the end game screen or play again**

- Action: *User play quiz, which then ends*

- Expected Result: *The modal window contains two buttons, one to close and one to play again.*

- Actual Result: *Works as intended*

![modal](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/tablet/tablet_quiz_modal.png)

#### User story 10:

**As a user, i would like to be able to play notes on a piano on the screen and see which tone is being played**

**The Piano Feature**

- Action: *User opens the play page, and plays on the piano keys*

- Expected Result: *The note played is both heard and seen on the screen*

- Actual Result: *Works as intended*

(The piano can be viewed in the images above)

#### User story 11:

**As a user, i would like to be able to play the notes on the computer keyboard**

**The Piano Feature**

- Action: *User opens the play page, and triggers the piano keys with the keyboard*

- Expected Result: *The note played is both heard and seen on the screen*

- Actual Result: *Works as intended*

(The piano can be viewed in the images above)

#### User story 12:

**As a user, i would like to be able to view videos to learn about music theory and sight reading**

**Learn Page Feature**

- Action: *User opens the learn page, and clicks on a video to view it*

- Expected Result: *The video that the user clicks on is viewed in the main window*

- Actual Result: *Works as intended*

![learn](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/laptop/laptop_learn.png)

#### User story 13:

**As a user, i would like to be able to get in touch with the site owner**

**Contact Page Feature**

- Action: *User opens the learn page, and clicks on a video to view it*

- Expected Result: *The video that the user clicks on is viewed in the main window*

- Actual Result: *Works as intended*

![Contact tablet](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/tablet/tablet_contact_landscape.png)

#### User story 14:

**As a user, i would like to view an 404-error page if I have entered an invalid url within the website**

**404 Page Feature**

- Action: User enters an invalid URL within the website

- Expected Result: *The user is taken to the 404-error page, where user can navigate home or elsewhere on the website
*
- Actual Result: *Works as intended*

![404](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/404_iphone.png)

</details>

### Testing of site owner goals

<details>
  <summary>View siteowner goal tests</summary>

#### User story 15:

**As a site owner, i would like to display simple clear options on the home page**

**Home Page Feature**

- Action: *User visits the home page*

- Expected Result: *The options to navigate all the pages of the site are there and clear*

- Actual Result: *Works as intended*

![home iphone](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/home_iphon.png)

#### User story 16:

**As a site owner, i would like to display a menu in a navigation bar or popout menu at the top of the page**

**Nav Menu Feature**

- Action: *User views a page or clicks on the hamburger button*

- Expected Result: *The nav menu appears (if it isn't already visible as on larger screens)*

- Actual Result: *Works as intended*

![nav menu](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/navmenu_iphone.png)

#### User story 17:

**As a site owner, i would like to display a quiz for users to test their knowledge**

**The Quiz Feature**

- Action: *User navigates to the Quiz page and clicks "Let's Play!"*

- Expected Result: *The user is able to play the quiz*

- Actual Result: *Works as intended*

(Quiz images are visible above)

#### User story 18:

**As a site owner, i would like to display a learn page containing the results of a YouTube search dynamically updated, using YouTube API**

**Learn Page Feature**

- Action: *User navigates to the learn page*

- Expected Result: *The Videos list is dynamically updated with YouTube API and loaded into the videos section*

- Actual Result: *Works as intended*

The learn page can be viewed above. It is highly responsive, and works even on the smallest devices.

#### User story 19:

**As a site owner, i would like to display a page where users can play the piano and view the note played**

**The Piano Feature**

- Action: *User navigates to the learn page*

- Expected Result: *The Videos list is dynamically updated with YouTube API and loaded into the videos section*

- Actual Result: *Works as intended*

(Images from play page are visible above)

#### User story 20:

**As a site owner, i would like to be able to be contacted should the user wish to do so, through an emailing service to my private email address**

**Contact Page Feature**

- Action: *User fills in the form on Contact page and clicks send*

- Expected Result: *The form data is sent to the site owner via EmailJS*

- Actual Result: *Works as intended*

![Mail from emailJS](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/emailjs.jpeg)

#### User story 21:

**As a site owner, i would like to have a website that contains validated HTML, CSS and JavaScript**

**ALL PAGES**

- Action: *Have users who care about well written code, validation, etc visiting the site*

- Expected Result: *The website passes all valdation tests*

- Actual Result: *All tests passed without errors*

Validation results can be seen [here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/tree/master/docs/validation)

</details>

## Bugs

<details>
  <summary>View bugs here</summary>

Bug: Error when entering month "oct" in patient booking system
Fix: Correct typo "Okt" in month dictionary, create try and except to catch time format value errors

Bug: Error ``code: 500, APIerror`` when calling the sheets API
Fix: Only happened once, difficult to recreate. Created a "try", "except" to catch API errors when calling the sheets API

Bug: Checking schedule displayed twice
Fix: Change code so things happen in correct order

Bug: Password hiding library import stdiomsk doesn't work on terminal in Heroku and produced ``termios.error: 25, 'Inappropriate ioctl for device'``
Fix: Remove stdiomsk and let password entered be shown

Bug: Datetime parsing not working, returning errors
Fix: Create TimeFConverter class, convert formats with that

Bug: Says date incorrect although it is correct
Fix: Fix while loop and indentation in get date function

Bug: Sheets updating wrong cell when user exists
Fix code at end of sheet.py; use update_cell sheets method

Bug: Schedule displaying wrong weeks when navigating through weeks, out of schedule back in and then showing next week again
Fix: Add initialize method to IncDecWeek class, so when user exits, the weeks count resets

Bug: Some lines appearing without space below
Fix: Add new line to print and input strings where relevant

</details>


## Deployment

### Forking the GitHub Repository

To make a clone, or 'Fork' this repository, follow the steps below.

1. Access your GitHub account and find the relevant repository.
2. Click on 'Fork' on the top right of the page.
3. You will find a copy of the repository in your own Github account.

### Making a Local Clone

1. Access your GitHub account and find the relevant repository.
2. Click the 'Code' button next to 'Add file'.
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Open Git Bash.
5. Access the directory you want the clone to be have.
6. In your IDE's terminal type 'git clone' and the paste the URL you copied.
7. Press Enter.
8. You now have a local clone.

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at [heroku.com](https://.heroku.com/)
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to <Python> and <NodeJS> in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
11. All done!

### Google API

Here's how you can set up your own API:

1. Login or create a Google account and navigate to https://console.cloud.google.com/
2. Create a new Project by clicking on the New Project icon
3. Add Project name and details
4. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
5. IF the API requires, create a credential (service account in this case) for your project
6. Download the credential and upload it to your workspace a a json-file
7. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
8. Search for the needed tasks to be performed in the documentation for the specific API, for example here for the calendar API: [Google Calendar API Reference](https://developers.google.com/calendar/api/v3/reference?hl=en)
9. Add them to your code.


## Credits

Here are links to sites that answered a lot of my questions on coding and the Python language.

### Coding tips and tricks

Overriding false errors when Flake and Pylint validate code:
[StackOverflow, pyflakes](https://stackoverflow.com/questions/8427701/how-to-ignore-pyflakes-errors-imported-but-unused-in-the-init-py-file)
[StackOverflow, pylint](https://stackoverflow.com/questions/26657265/hide-some-maybe-no-member-pylint-errors)

Creating a class to increment and decrement a number free from functions: [Stack Overflow](https://stackoverflow.com/questions/47697945/python-how-to-increment-number-and-store-in-variable-every-time-function-runs/47698278)

Using the dictionary zip function to join two lists: [StackOverflow](https://stackoverflow.com/questions/209840/how-do-i-convert-two-lists-into-a-dictionary)

Creating a user login:[StackExchange](https://codereview.stackexchange.com/questions/164359/python-username-and-password-program)

Using the python datetime library: [docs.python.org](https://docs.python.org/3/library/datetime.html)

Calculating a leap Year with a conditional statement: [geeksforgeeks.org](https://www.geeksforgeeks.org/program-check-given-year-leap-year/)

Regular expression for validating email: [Stack Overflow](https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address)

Using the isnumeric function: [delftstack.com](https://www.delftstack.com/howto/python/user-input-int-python/)

### Acknowledgments

This project was created from a template made by [Code Institute](https://codeinstitute.net/) to recreate the terminal in a regular web browser.

The tutors Scott and Sean and my mentor Mo Shami at Code Institute, have helped me in times of trouble, many thanks to them.
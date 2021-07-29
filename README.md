# FeelGood Physio Booking System

## A Command Line Interface Application

![Screenshot of Home screen](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/screenshot_home.png)
**FeelGood Physio is an application built for a fictional physiotherapy clinic, syncronized with Google Calendar and Google sheets.**

[Click here](https://feelgood-physio.herokuapp.com/) to visit the deployed site.

[Here](https://calendar.google.com/calendar/u/0?cid=dXVlcTNzMnRiZ2RsNTdkdm1tdmNwNW9zZDhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) is the link to view the Google Calendar as it is updated. You will have to log in to Google and add it to your subscribed calendars, but it is just as easy to remove it again.

[Here](https://docs.google.com/spreadsheets/d/1tZfgo8_TkdA9EdJyrj58YbFePcTcciv-zyC2UBqY6-g/edit?usp=sharing) is the link to the Google Spreadsheet, to see the updates made.

## Contents


1. [Project Goals](#project-goals)
2. [User Goals](#user-goals)
3. [Structure](#structure)
    1. [Home Screen](home-screen)
    2. [Booking Process for Patient](#booking-process-for-patient)
    3. [Staff area](#staff-area)
    4. [Staff Schedule](#staff-schedule)
    5. [Patient Log](#patient-log)
4. [User Stories](#user-stories)
    1. [Patient User Stories](#patient-user-stories)
    2. [Staff Member User Stories](#staff-member-user-stories)
    3. [Site Owner Goals](#site-owner-goals)
5. [Technical Design](#technical-design)
    1. [Flow Chart](#flow-chart)
    2. [Data Models](#data-models)
    3. [User Interface](#user-interface)
6. [Features](#features)
    1. [Feature 1: The Patient Booking System](#feature-1-the-patient-booking-system)
    2. [Feature 2: The Schedule](#feature-2-the-schedule)
    3. [Feature 3: The Patient Log](#feature-3-the-patient-log)
    4. [Features to be implemented](#features-to-be-implemented)
7. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Applications, Platforms and Libraries](#applications-platforms-and-libraries)
        1. [Applications and Platforms](#applications-and-platforms)
        2. [Python Libraries](#python-libraries)
        3. [Third Party Libraries](#third-party-libraries)
8. [Validation](#validation)
9. [Testing of Patient User Stories](#testing-of-patient-user-stories)
10. [Testing of Staff Member User Stories](#testing-of-staff-member-user-stories)
11. [Testing of Site Owner Goals](#testing-of-site-owner-goals)
12. [Bugs](#bugs)

13. [Deployment](#deployment)
    1. [Forking the GitHub Repository](#forking-the-github-repository)
    2. [Making a Local Clone](#making-a-local-clone)
    3. [Heroku](#heroku)
    4. [Google API](#google-api)
14. [Credits](#credits)
15. [Coding tips and tricks](#coding-tips-and-tricks)
16. [Acknowledgments](#acknowledgments)

## Project Goals

Project Goals for intended use are:

- Creating a system for managing bookings and patient data for both staff and patients.
- Making this system easy and effective for all users.
- Displaying relevant information so users can easily navigate.

My personal project goals of FeelGood Physio are:

- To build an application that serves the booking needs of both patients and staff
- To explore the possibilities of working with API's
- To gain knowledge of the Python programming language

## User Goals

Patients should find it simple to book appointments, and not be able to book a timeslot that is not available. Patients should also be made aware if their data is being logged.

Staff should find it easy to access and modify their schedule and patient data.

Target Audience

- A Physiotherapist (or their receptionist)
- Patients


## Structure

The FeelGood Physio Booking System relies almost only on user input. There are always options displayed on the screen and users can choose what to do next.
When an input is entered, the application takes the user to the chosen option. All functions are chained together, each depending on the users input.

### 1. Home Screen

<details>
    <summary>Click here to view the home screen</summary>

![Screenshot of Home screen](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/screenshot_home.png)

</details>

This welcomes the user when they first enter the application, when the task at hand is done or when users choose to exit from whereever they are in the application. From the home screen, there are two options:

- Book appointment - takes users to the booking process
- Staff login - takes users to the staff area

### 2. Booking Process for Patient

<details>
    <summary>Click to view image</summary>

![Patient booking, month](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_month.png)

</details>

This is a long chain of functions resulting in a new appointment and an update to the patient log, if completed. Users input their desired appoinment time and details, and get a confirmation message at the end.

### 3. Staff area

To access the staff area, users need the staff password. If entered correctly, users can either view the patient log, or access the schedule.

<details>
    <summary>Click to view image</summary>

![Staff area](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/staff_area/password.png)

</details>

### 4. Staff Schedule

The schedule, which shows 1 week at a time, can be edited, which also updates the linked Google Calendar.

### 5. Patient Log

The log, which is a Google Sheet, updates dynamically as users book appointments.


## User Stories

As this application has such specific target users, I have adapted my user stories to patients and staff.

### Patient User Stories:

1. I would like to be able to book an appointment at a time of my choosing, should the appointement be available
2. I would like to be alerted if my details are saved before I enter them
3. I would like to be well informed from the application throughout the booking process
4. I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again
5. I would like to be able to confirm the booking right before it is made
6. I would like to view a confirmation of the booking when it is made
7. I would like to at any point cancel my booking during the booking process should I wish to do so

### Staff Member User stories:

8. I would like for users to only be able to book appointments on weekdays between 9 and 17, and when the schedule is free
9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
10. I would like the appointments made by patients dynamically update my Google Calendar
11. I would like the changes made in the schedules edit menu to update the events on my Google Calendar
12. I would like to be able to view the patient log
13. I would like to view my schedule for the coming week
14. I would like to navigate between weeks in my schedule
15. I would like to be able to update or remove any appointment viewed in my schedule
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

### Site Owner Goals

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does

## Technical Design

### Flowchart

Below is a flowchart describing the structure of the application, created with [Lucidchart](https://lucid.co/product/lucidchart).

<details>
    <summary>View flowchart here</summary>

![Flowchart](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/flowchart.png)

</details>

### Data models

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

### User interface

I find it important to be clear to the user on displaying information, especially on an interface where styling is limited. As this project focuses solely on the Python language, I decided not to try to implement graphics and focus on funcionality, even though it was tempting.

I have, however, put lots of time in displaying the information to the user as correctly and as clearly as possible. Each message or piece of data displayed to the user has space around it, separating it from the previous one, for optimal readability.

Some simple formatting has also been done, for example when displaying date time, the time format converter converts it into a format that is easier and more pleasing to read.
Also, when displaying the patient log, I have removed curly braces and apostophes before the patient data is printed to the screen, only needed when managing it.

Messages to clarify what has and has not been done, and what the user's choices are have carefully been created to make the user experience as straightforward as possible.

## Features

### Feature 1: The Patient Booking System

This is the main feature of the application, getting patient information to make a booking and make a patient log entry.

The patient booking system consists of several steps after the welcome screen. The user can exit the booking process at any time.

1. The patient is made aware that their details are saved and have to take action to continue

2. The patient is prompted to choose month of the appointment (if the month chosen is june, and it is july at the point of booking, the application will change the year to next year)

3. The patient is informed of the month chosen and get to choose date. The date must corrrespond with the days in that month, made sure by the month_dict dictionary.

4. The patient is notified of the date chosen and can choose the time of the appointment, 9 - 17. The time must be a weekday and between 9 and 17. After validation, the first API request is made. The application gets data through the Google API if the chosen time slot is available in the Google calendar, and, if so, notifies the user. If the slot is not available, the user has to choose another time.

5. If the timeslot is available, the user is prompted to enter their full name. A single name or name with digits is not accepted.

6. The user is, if the name is accepted, prompted to enter their email adress, which is validated with a simple regular expression.

7. If the email input is correct, the patient is prompted to shortly describe their symptoms. This must b at least 8 characters long, so the user cannot enter nothing or a short word.

8. The user is shown the appointment and must confirm the booking.

9. If the booking is confirmed by the user, two requests are made with the users input; one to push the information to FeelGood Physio's Google calendar and one to make an entry in the Google sheets patient log on Google Drive, all with the help of the Google API.

If the user with the same name already exists in the patient log, the patients symptoms are unpdated instead of a row being added. The patient is then notified that the booking has been made and can return to the home screen again.

<details>
  <summary>Click to view images of feature 1</summary>

*Entering month*
![Patient Booking System](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_month.png)

*Booking confirmation*
![Confirm patient booking](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_done.png)

*Google Calendar entry*
![Google calendar entry](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/google_cal/g_cal_new.png)

*Entry in Google Sheets*
![Google sheets](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/g_sheets_new.png)

</details>

**Patient user stories covered:**

1. I would like to be able to book an appointment at a time of my choosing, should the appointement be available
2. I would like to be alerted if my details are saved before I enter them
3. I would like to be well informed from the application throughout the booking process
4. I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again
5. I would like to be able to confirm the booking right before it is made
6. I would like to view a confirmation of the booking when it is made
7. I would like to at any point cancel my booking during the booking process should I wish to do so

**Staff member user stories covered**

8. I would like for users to only be able to book appointments on weekdays between 9 and 17, and when the schedule is free
9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
10. I would like the appointments made by patients dynamically update my Google Calendar
11. I would like the changes made in the application to update the events on my Google Calendar

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does


### Feature 2: The Schedule

The Schedule is accessed via the staff area, which only users with a password can access. Here, users are initially shown the schedule from the current time and 7 days forward. The appointments are retrieved by an API request to FeelGood Physio's Google Calender, and can be edited and removed, by user inputting number displayed within the appointment.

The user can navigate with keys "n" for next and "b" for back, which will respectively retrieve the schedule for the next or previous week. New numbers are displayed for the user to modify specific appointments. If the user enters "e" for edit, the user gets several choices to edit below:

- Time: edit the date and time of the appointment
- Name: Change the name given in the appointment
- Details: Change the patient's email adress or symptoms description

Upon changing these parameters and confirming the changes, the appointments are updated in the Google Calendar. The user is notified of this and can return to the staff menu or exit.


<details>
    <summary>Click to view images of feature 2</summary>

*The schedule*
![The Schedule](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/schedule/schedule.png)

*The edit menu*
![The edit menu](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/schedule/edit_apntmnt.png)

</details>

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

This is where staff can access data from patients that have booked via the booking system. The system lets users know before initiating the booking that their data will be logged, and after a successful booking the datails are logged in the Google Sheet via the API as a new entry. If the user already exists, their symptoms are the only thing that will be updated.

Even though the same details are kept in the Google Calendar, the patient log is a way to consolidate information if staff are looking for a specific patient.

<details>
    <summary>Click to view images of feature 3</summary>

*The patient log*
![Patient Log](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log.png)

*The patient log with an existing patient*
![Old patient books new appointment](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log_old_patient.png)

*The updated details*
![The Google Sheet with the updated details](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/sheet_update_sympt.png)

</details>

**Staff member goals covered:**

9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
12. I would like to be able to view the patient log
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors, whatever the user does


### Features to be implemented

There are endless possibilities with an application like this. If the clinic were to hire more than one therapist, they could each have their own calendar and log. Patients could have the possibility to add a user account with which they log in to the system, and can reschedule or cancel their appointment.

An important feature that the log now lacks is the possibility for staff to edit entries; this will be implemented at a later stage.


## Technologies used

### Languages

- [Python 3](https://www.python.org/) - Was used solely to create this project.


### Applications, Platforms and Libraries


#### Applications and Platforms

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited, pushed and deployed to Github.

- [Gitpod](https://gitpod.com/) - All code was written and tested using the Gitpod web-based IDE.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [Lucidchart](https://lucid.co/product/lucidchart) - Lucidchart was used to create the [flowchart](#flowchart) of the project.

- [Google Calendar](https://calendar.google.com/) - The users input data creates and edits events on Google Calendar

- [Google Sheets](https://calendar.google.com/) - - The users input data creates and edits content on Google Sheets

- [Google Cloud Platform](https://console.cloud.google.com/) - All data send and received with the help of the Google API, through the Google Cloud Platform


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



## Testing of Patient User Stories

User stories are tested with the features that cover them. All user stories passed the tests.


### Testing of user story 1

**"I would like to be able to book an appointment at a time of my choosing, should the appointement be available"**


**Covered by feature 1: The Patient Booking System**

<details>
    <summary>View image of initial steps of the booking</summary>

![User story 1, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_1.png)

</details>

- **Actions**:

    * *User hits "b" to begin*
    * *User enters "1" to agree on the application logging the patient data*
    * *User enters desired month of the appointment (Three letters)*
    * *User enters desired date (one or two figure numbers both work)*
    * *User is notified if the date is bookable*
    * *User enters desired hour of the appointment*
    * *User is notified if the timeslot is free or not*
    * *User enters their name*
    * *User enters their email*
    * *User enters their symptoms*
    * *User confirms by hitting "y"*
    * *User is greeted with their newly made booking*
    * *User can choose to go back to the beginning*

<details>
    <summary>View image of date validation here</summary>

![User story 1, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_2.png)

</details>

<details>
    <summary>View image of booking confirmation here</summary>

![User story 1, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_3.png)

</details>

 - Expected result: *To Make a successful booking at an available time*

 - Actual result: *Works as intended*


### Testing of user story 2

**"I would like to be alerted if my details are saved before I enter them"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *In the welcome screen, user hits "b" to get to the booking screen*

- **Expected Result** - *Application displays message about storing data and user needs to confirm this to carry on*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_2.png)

</details>

### Testing of user story 3

**"I would like to be well informed from the application throughout the booking process"**


This user story is tested in the steps needed to make an appointment.

**Covered by feature 1: The Patient Booking System**

- **Action**: *User initiates a booking by pressing "b"*

- **Expected Result**: *Application displays message about storing data*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image here</summary>

![User story 1, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_1.png)

</details>

___

- **Action** - *User hits "1" to continue*

- **Expected Result** - *Application asks user for the month they would like to come*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters the three first letters of the month that they want to come*

- **Expected Result** - *Application confirms the month entered and asks for the desired appointment date*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters the desired appointment date*

- **Expected Result** - *Application lets user know if the date is unbookable, (weekends for example) or if it is available to book, in which case the app confirms date and asks user for time of appointment*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>


![User story 3, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_2.png)

</details>

___

- **Action** - *User enters hour of desired appointment time*

- **Expected Result** - *Application confirms the time and asks user for name if the desired appoinment time is free and bookable, otherwise lets the user know and user has to choose new time*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters their name*

- **Expected Result** - *Application Confirms the users name and asks for their email*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 3, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_3.png)

</details>

___

- **Action** - *User enters their email*

- **Expected Result** - *Application Confirms the users email address and asks user to enter their symptoms*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters their symptoms*

- **Expected Result** - *Application displays all the patient data retrieved and asks user to confirm appointment*

- **Actual Result** - *Works as intended*

___

- **Action** - *User confirms appointment*

- **Expected Result** - *Application displays confirmation, that patient data is logged and user can return to the main screen*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 3, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_4.png)

</details>

### Testing of user story 4

**"I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again"**


**Covered by feature 1: The Patient Booking System**


- **Action** - *User enters invalid value, or date/time that is not free*

- **Expected Result** - *Application let user know that the entry is invalid, and the user gets to try again*

- **Actual Result** - *Works as intended*

The testing of this user case is best portrayed with the images below. All areas of navigation have passed the tests.

<details>
    <summary>View images of user 4 testing results</summary>

*Invalid choices at home screen:*

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

</details>

### Testing of user story 5

**"I would like to be able to confirm the booking right before it is made"**


**Covered by feature 1: The Patient Booking System**

**Action** - *User completes booking and enters valid information throughout the booking process*

**Expected Result** - *User is asked to confirm the booking*

**Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_3.png)

</details>

### Testing of user story 6

**"I would like to view a confirmation of the booking when it is made"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User confirms the booking made*

- **Expected Result** - *Application displays the details of the booking*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_6.png)

</details>


### Testing of user story 7

**"I would like to at any point cancel my booking during the booking process should I wish to do so"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User follows instructions to exit on screen*

- **Expected Result** - *Booking returns to the home screen or the previous stage*

- **Actual Result** - *Works as intended*

<details>
    <summary>View images here</summary>


![User story 7](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_7_1.png)

![User story 7, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_7_2.png)

</details>

## Testing of Staff Member User Stories


### Testing of user story 8

**"I would like for users to only be able to book appointments on weekdays between 9 and 17, and when the schedule is free"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User tries to make a booking on a weekend, outside the schedule or when a booking is already scheduled*

- **Expected Result** - *Patient is alerted that the time is invalid or unavailable*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 8](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_2.png)

</details>

### Testing of user story 9

**"I would like appointments made by new users add a new row with their information to the Google Sheets patient log"**


**Covered by feature 1: The Patient Booking System and feature 3, the Patient Log**

- **Action** - *User successfully books an appointment*

- **Expected Result** - *Patients information is added on a new row in the patient log on the Google spreadsheet, which is viewable in the application*

- **Actual Result** - *Works as intended*

<details>
    <summary>View images here</summary>

*A completed patient booking*

![User story 9, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_done.png)

*The patient log after booking*

![User story 9, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log.png)

*The Google Sheet after booking is made*
![User story 9, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/g_sheets_new.png)

</details>


### Testing of user story 10

**"I would like the appointments made by patients dynamically update my Google Calendar"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User successfully books an appointment*

- **Expected Result** - *Event on Google Calendar is created from input by user during booking*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image of updated calendar here</summary>

![User story 9, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/google_cal/g_cal_new.png)

</details>


### Testing of user story 11

**"I would like the changes made in the schedules edit menu to update the events on my Google Calendar"**


**Covered by feature 2: The Schedule**

- **Action**: *User edits an appointment from the schedule*

- **Expected Result**: *The appointment is updated on Google Calendar with new data from user*

- **Actual Result**: *Works as intended*

<details>
    <summary>View images here</summary>

![user story 11, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_11_1.png)

![user story 11, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_11_2.png)

![user story 11, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_11_3.png)

</details>


### Testing of user story 12

*"I would like to be able to view the patient log"*

**Covered by feature 3: The Patient Log**

- **Action**: *User hits "l" in the staff area*

- **Expected Result**: *The patient log is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image of the result</summary>

![User story 12](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log.png)

</details>

### Testing of user story 13

*"I would like to view my schedule for the coming week"*

**Covered by feature 2: The Schedule**

- **Action**: *User hits "s" in the staff area*

- **Expected Result**: *The schedule is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image of the result</summary>

![User story 13](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/schedule/schedule.png)

</details>

### Testing of user story 14

*"I would like to navigate between weeks in my schedule"*

**Covered by feature 2: The Schedule**

- **Action**: *User hits "n" or "b" when viewing the schedule*

- **Expected Result**: *The next week is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image of the result</summary>

![User story 14](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_14.png)

</details>

### Testing of user story 15

*"I would like to be able to update or remove any appointment viewed in my schedule"*

**Covered by feature 2: The Schedule**

#### Edit appointment

- **Actions**:

* *User enters number of appoinment when viewing the schedule*
* *User chooses what to edit; time, name or details*
* *User enters new time, name or details for appointment*
* *User confirms changes*


- **Expected Result**: *The event is updated on Google Calendar*

- **Actual Result**: *Works as intended*

<details>
    <summary>View images of editing appointments</summary>

*The edit menu*
![User story 15, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_1.png)

*Editing the date and time*
![User story 15, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_2.png)

*Changes are confirmed*
![User story 15, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_3.png)

*The Google event now has the new time*
![User story 15, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_4.png)

</details>

#### Remove appointment

- **Actions**:

* *User enters number of appoinment when viewing the schedule*
* *User chooses what to edit; time, name or details*
* *User enters new time, name or details for appointment*
* *User confirms changes*


- **Expected Result**: *The event is removed from Google Calendar*

- **Actual Result**: *Works as intended*

<details>
    <summary>View images of removing appointment</summary>

*Choice to remove and confirmation once removed*

![User story 15, 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_5.png)

*The Google event is now nowhere to be seen*

![User story 15, 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_6.png)

</details>

### Testing of user story 16

*"I would like to easily be able to return to the main staff area in the application"*

**Covered by feature 2: The Schedule, and feature 3: The Patient Log**


- **Action**: *User follows the instructions to get to the staff menu*

- **Expected Result**: *Staff main menu is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>Click to view images</summary>

*Returning from patient log to staff menu*

![User story 16, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_16_1.png)

*Returning from schedule to staff menu*

![User story 16, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_16_2.png)

</details>

### Testing of user story 17

*"I would like the staff area to be password protected"*

**Covered by all features**


- **Action**: *User enters "s" to view staff area*

- **Expected Result**: *User must enter password to continue*

- **Actual Result**: *Works as intended*

<details>
    <summary>Click to view image</summary>

*The password being displayed*

![User story 17](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_17.png)

</details>

## Testing of Site Owner Goals

### Testing of user story 18

*"I would like for the application to contain validated Python code without returning any errors, whatever the user does"*

**Covered by all features**


- **Action**: *User enters invalid information*

- **Expected Result**: *Application lets user know and user can enter info again*

- **Actual Result**: *Works as intended*

This was tested by trying all possible entries in all menus in the application. The application passed all validation tests which can be viewed [here](#validation), and user will be displayed with information in all menus if user input is incorrect.

<details>
    <summary>Click to view images</summary>

*Incorrect date entered, staff area*

![User story 18, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_18_1.png)

*Incorrect month entered, patient booking area*

![User story 18, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_18_2.png)

*Incorrect name entered, patient booking area*

![User story 18, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_18_3.png)

</details>

## Bugs

<details>
    <summary>View bugs here</summary>
___

**Bug**: When user tries to delete whole words with option delete on mac, nothing happens, then deleting the input has no effect on the string. Probable error with terminal and not in Python code.

**Fix**: Print message to users not to use this function in the application. No fix for the bug as of yet.
___

**Bug**: User can navigate with arrows anywhere in the terminal window, entering input here renders the printed text in a false manner.

**Fix**: Print message to users not to use this function in the application. No fix for the bug as of yet.
___


**Bug**: Error when entering month "oct" in patient booking system

**Fix**: Correct typo "Okt" in month dictionary, create try and except to catch time format value errors
___

**Bug**: Error ``code: 500, APIerror`` when calling the sheets API

**Fix**: Only happened once, difficult to recreate. Created a "try", "except" to catch API errors when calling the sheets API
___

**Bug**: Checking schedule displayed twice

**Fix**: Change code so things happen in correct order
___

**Bug**: Password hiding library import stdiomsk doesn't work on terminal in Heroku and produced ``termios.error: 25, 'Inappropriate ioctl for device'``

**Fix**: Remove stdiomsk and let password entered be shown
___

**Bug**: Datetime parsing not working, returning errors

**Fix**: Create TimeFConverter class, convert formats with that
___

**Bug**: Says date incorrect although it is correct

**Fix**: Fix while loop and indentation in get date function
___

**Bug**: Sheets updating wrong cell when user exists

**Fix** code at end of sheet.py; use update_cell sheets method
___

**Bug**: Schedule displaying wrong weeks when navigating through weeks, out of schedule back in and then showing next week again

**Fix**: Add initialize method to IncDecWeek class, so when user exits, the weeks count resets
___

**Bug**: Some lines appearing without space below

**Fix**: Add new line to print and input strings where relevant
___

**Bug**: "e" didn't let user exit

**Fix**: Add paretheses to e_to_edit function
___

**Bug**: Error when selecting date in month that has passed

**Fix**: Changed datetime method to year that was wrongly named as variable "yr"

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

The tutors Scott and Sean and my mentor Mo Shami at Code Institute, have helped me in times of trouble. Many thanks to them, and of course to the comprehensive course material from Code Institute.
# FeelGood Physio Booking System

## A Command Line Interface Application

![Screenshot of Home screen](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/screenshot_home.png)
**FeelGood Physio is an application built for a fictional physiotherapy clinic, syncronized with Google Calendar and Google sheets.**

[Click here](https://feelgood-physio.herokuapp.com/) to visit the deployed site.

## Contents

1. [User Experience](#user-experience)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [Future Goals](#future-goals)
        3. [User Goals](#user-goals)

    2. [Structure](#structure)


    3. [Scope](#scope)
        1. [User Stories](#user-stories)
        2. [Site Owner Goals](#site-owner-goals)
    
    4. [Skeleton](#skeleton)

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

The FeelGood Physio Booking System, or FGPBS, relies almost only on user input. There are always options displayed on the screen and users can choose what to do next.

When an input is entered, the application takes the user to the chosen option. All functions are chained together, each depending on the users input.

#### 1. Home Screen

This welcomes the user when they first enter the application, when the task at hand is done or when users choose to exit from whereever they are in the application. From the home screen, there are two options:

- Book appointment - takes users to the booking process
- Staff login - takes users to the staff area

#### 2. Booking process for patient

This is a long chain of functions resulting in a new appointment and an update to the patient log, if completed. Users input their desired appoinment time and details, and get a confirmation message at the end.

#### 3. Staff area

To access the staff area, users need the staff password. If entered correctly, users can either view the patient log, or access the schedule.

#### 4. Staff Schedule

The schedule, which shows 1 week at a time, can be edited, which also updates the linked Google Calendar.

#### 5. Patient Log

The log, which is a Google Sheet, updates dynamically as users book appointments.


### Scope
___

#### User Stories

##### Patient user stories:

1. I would like to be able to book an appointment at a time of my choosing, should the appointement be available
2. I would like to be alerted if my details are saved before I enter them
3. I would like to be well informed from the application throughout the booking process
4. I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again
5. I would like to be able to confirm the booking right before it is made
6. I would like to view a confirmation of the booking when it is made
7. I would like to at any point cancel my booking during the booking process should I wish to do so

##### Staff member user stories:

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

18. I would like for the application to contain validated Python code without returning any errors


### Flowchart
___

Below is a flowchart describing the structure of the application, created with [Lucidchart](https://lucid.co/product/lucidchart).

![Flowchart](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/flowchart.png)

### Technology Design
___

#### Data models

I have chosen to use several data models in this project, but rely mainly on dictionaries for managing data. For variation, I have created two classes for this project, and use lists aswell.

I like the way dictionaries behave, and in this project they are perfect; I could easily pair a patient number with an ID that Google uses for the specific event or 

Here are the most important objects:

- The appointment list(cal_mod.apt_list) that stores dictionaries of appointments, to be read or edited and then passed through the Google API to the Calendar

- The IncDecWeek class, used to increment the the number of days ahead or in the past to display the schedule from.
- The time format converter class (TimeFConverter), created in four instances for each ty p of conversion it makes.

- The appointment dictionary (app_dict), created in the print_appointment function to pair the Google events specific ID together with numbers, that the user can input to edit that appointment. New numbers from 1 upwards are created each time the function is called.
- apntmnt_to_edit, a dictionary of a single event that the edit_appntmnt function gets from Google Calendar, to edit and then push bach to Google with new values.
- The month dictionary (month_dict), used to pair the months three letter abbreviations with their corresponding number of days, accessed when getting date details from user.
- The patient dictionary helps the Google Sheets patient log keep track of patients that have booked appointments, keeping their details as values and assigning (with the help of the get_p_nr function) a unique patient ID. These details can then be displayed to the staff user.

#### User interface

I find it important to be clear to the user on displaying information, especially on an interface where styling is limited. As this project focuses solely on the Python language, I decided not to try to implement graphics and focus on funcionality, even though it was tempting.

I have, however, put lots of time in displaying the information to the user as correctly and as clearly as possible. Each message or piece of data displayed to the user has space around it, separating it from the previous one, for optimal readability.

Some simple formatting has also been done, for example when displaying date time, the time format converter converts it into a format that is easier and more pleasing to read.
Also, when displaying the patient log, I have removed curly braces and apostophes before the patient data is printed to the screen, only needed when managing it.

Messages to clarify what has and has not been done, and what the user's choices are have carefully been created to make the user experience as straightforward as possible.

## Features

### Existing features
___

#### Feature 1 The Patient Booking System

![Patient Booking System](#)

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

- If the booking is confirmed by the user, two requests are made with the users input; one to push the information to FeelGood Physio's Google calendar and one to make an entry in the Google sheets patient log on Google Drive, all with the help of the Google API. If the user with the same name already exists in the patient log, the patients symptoms are unpdated instead of a row being added. The patient is then notified that the booking has been made and can return to the home screen again.

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

18. I would like for the application to contain validated Python code without returning any errors


#### Feature 2: The Schedule

![Schedule](#)

The Schedule is accessed via the staff area, which only users with a password can access. Here, users are initially shown the schedule from the current time and 7 days forward. The appointments are retrieved by an API request to FeelGood Physio's Google Calender, and can be edited and removed, by user inputting number displayed within the appointment.

The user can navigate with keys "n" for next and "b" for back, which will respectively retrieve the schedule for the next or previous week. New numbers are displayed for the user to modify specific appointments. If the user enters "e" for edit, the user gets several choices to edit below:

- Time: edit the date and time of the appointment
- Name: Change the name given in the appointment
- Details: Change the patient's email adress or symptoms description

Upon changing these parameters and confirming the changes, the appointments are updated in the Google Calendar. The user is notified of this and can return to the staff menu or exit.

**Staff member goals covered**

11. I would like the changes made in the application edit menu to update the events on my Google Calendar
13. I would like to view my schedule for the coming week
14. I would like to navigate between weeks in my schedule
15. I would like to be able to update or remove any appointment viewed in my schedule
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors


#### Feature 3: The Patient Log

![Patient Log](#)

This is where staff can access data from patients that have booked via the booking system. The system lets users know before initiating the booking that their data will be logged, and after a successful booking the datails are logged in the Google Sheet via the API as a new entry. If the user already exists, their symptoms are the only thing that will be updated.

Even though the same details are kept in the Google Calendar, the patient log is a way to consolidate information if staff are looking for a specific patient.

**Staff member goals covered:**

9. I would like appointments made by new users add a new row with their information to the Google Sheets patient log
12. I would like to be able to view the patient log
16. I would like to easily be able to return to the main staff area in the application
17. I would like the staff area to be password protected

**Site owner goals covered**

18. I would like for the application to contain validated Python code without returning any errors


### Features to be implemented
___

There are endless possibilities with an application like this. If the clinic were to hire more than one therapist, they could each have their own calendar and log. Patients could have the possibility to add a user account with which they log in to the system, and can reschedule or cancel their appointment. An important feature that the log now lacks is the possibility for staff to edit entries; this will be implemented at a later stage.


## Technologies used

### Languages
___

- [Python 3](https://www.python.org/)


### Applications and Modules


#### Applications

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited, pushed and deployed to Github.

- [Gitpod](https://gitpod.com/) - All code was written and tested using the Gitpod web-based IDE.

- [Heroku](https://www.heroku.com)

- [Lucidchart](https://lucid.co/product/lucidchart) - Lucidchart was used to create the [flowchart](#flowchart) of the project.



## Validation

### HTML Validation

All pages passed the [W3C HTML Validation](https://validator.w3.org/) tests with 0 errors, and can be viewed [here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/tree/master/docs/validation/w3c/html)

### CSS Validation

The CSS on the website passed the [W3C CSS Jigsaw](https://jigsaw.w3.org/css-validator/) validation with 0 errors:

![Results from CSS-validation](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/validation/w3c/css_jigsaw/w3c_css_jigsaw.png)

Warnings were given for using prefix vendors for user-select: none to prevent selecting the piano keys when playing on play page. Removing them made user-select: none not work for me so I decided to keep them.

### JavaScript Validation

The JavaScript on the website was validated with [JSHint](https://jshint.com/). No errors were shown. The results can be viewed [here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/validation/jshint.md)

### Accessibility

Accessibility was tested with the [WAVE Website](https://wave.webaim.org/) and passed all tests. [Here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/tree/master/docs/validation/wave) are the results.

### Performance

[Google Chromes Lighthouse](https://developers.google.com/web/tools/lighthouse) was used for testing the performance of the website, which passed the tests on both desktop and mobile simulator. You can see the results [here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/tree/master/docs/validation/lighthouse)

### Devices

An Apple MacBook Pro 15" was used for testing, running Chrome and Safari. Chrome's DevTools provided simulators for 12 different device sizes, aswell as testing on a custom smallest size (320px x 480px, iPhone 4 size).

Below are linked screenshots of all web pages on five different sizes.

- [Mobile (320 x 568)](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_mobile.md)

- [Mobile, large (411 x 823)](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_mobile_large.md)

- [Tablet (768 x 1024)](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_tablet.md)

- [Laptop (1280 x 802)](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_laptop.md)

- [Desktop (1600 x 992)](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_desktop.md)

Testing was also done on an iPhone XS and an iPad Pro 10.5"

[Here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/tree/master/docs/screenshots/screenshots_iphone) are screenshots from iPhone XS

[Here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/tree/master/docs/screenshots/screenshots_ipad) are screenshots from iPad Pro

**Tests Made on Devices:**

- Nav link works and is displayed as intended
- All buttons and links on all pages work and link to the correct source
- All sizes of elements are appropriate and no elements appear on top of each other
- Width is set accordingly so no sideways scrolling bug is there in portrait mode
- Animations, colors and fonts appear as they should
- Quiz functions as intended, with sounds and functionality
- Modal window 
- Piano plays and displays notes with mouse, screen tap or kwyboard
- Learn page displays videos and videos are viewable
- 404 page

Musical Minds passed all tests made on all devices, with a few minor acceptances noted in [bugs](#bugs)


## Testing of User Stories/Site Owner Goals

User stories are tested with the features that cover them. All user stories passed the tests.

### Testing of user stories

<details>
  <summary>View user story tests</summary>

#### User story 1:

**As a user, i would like to easily navigate the websites pages via the menu or links provided**

**Navmenu Feature**

 - Action: *Click on the links at the top of all pages other than Home on large screens, on mobile, click on the hamburger button*

 - Expected result: *To get to the page clicked on by user*

 - Actual result: *Works as intended*

![Navmenu](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/navmenu_iphone.png)

![Navmenu](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/feature_one_navbar_landscape.png)

 **Home page Feature**

- Action: *Click on any of the buttons or the contact link below | To get to the page clicked on*

- Expected result: *To get to the page clicked on*

- Actual Result: *Works as intended*

![Screenshot of home](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile/mobile_home_landscape.png)


#### User story 2:

**As a user, i would like to be presented with a well designed, user-friendly interface**

**Home page Feature**

- Action: *General navigation, and experience of the home page*

- Expected Result: *Page feels well balanced and attractive to use*

- Actual Result: *Works as intended*

![home](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/feature_two_desktop.png)


**Nav Menu Feature**

- Action: *The clicking and navigating in the nav menu*

- Expected Result: *Animations, positioning and feel of the menu appeal to user
*
- Actual Results: *Works as intended*

![Nav-Desktop](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/desktop/desktop_nav.png)

**The Quiz Feature**

- Action: *Clicking "Let's Play!"*

- Expected Result: *Experience well designed elements with sounds and animation to appeal to user*
- Actual Result: *Works as intended*

![Quiz](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile_large/mobile_large_quiz.png)

**The Piano Feature**

- Action: *Playing keys on the piano by clicking the keys or playing on the keyboard*

- Expected Result: *User is informed by "keys" on screen which keys on computer keyboard to press to play piano. Piano notes played are heard and seen.*

- Actual Result: *Works as intended*

![Play desktop](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/laptop/laptop_play.png)

**The Learn Page Feature**

- Action: *User navigates and clicks on videos to play them*

- Expected Result: *User enjoys the layout and content on the learn page*

- *Works as intended* (for the people I have tested the website on too)

![Learn page](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile/mobile_learn_landscape.png)


#### User story 3:

**As a user, i would like to experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens**

**Nav Menu**

- Action: *The user viewing and navigating in the nav menu on any device*

- Expected Result: *The menu being displayed well, and design appealing*

- Actual Result: *Works as intended*

(The nav menu can be viewed on several devices in the images above)

**Home Page Feature**

- Action: *The user viewing and navigating within the home page on any device*

- Expected Result: *The design of the home page looks good on all devices*

- Actual Result: *Works as intended*

![Home mobile](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile/mobile_home.png)

**The Piano Feature**

- Action: *User plays the piano on any device*

- Expected Result: *The design of the piano and displayed notes is well balanced on all devices*

- Actual Result: *Works as intended*

![Play page](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile_large/mobile_large_play.png)

**The Quiz Feature**

- Action: *User plays the quiz on any device*

- Expected Result: *The quiz elements are displayed well on all devices*

- Actual Result: *Works as intended*

![Quiz](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/tablet/tablet_quiz_landscape.png)

**Learn Page Feature**

- Action: *User navigates and watches videos on any device*

- Expected Result: *The design of the video sections adapt to the screens viewing the page.*

- Actual Result: *Works as intended*

![Learn page](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/tablet/tablet_learn.png)

![Learn page mobile](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile/mobile_learn.png)

**Contact Page Feature**

- Action: *User fills in the form on any device*

- Expected Result: *Form is displayed properly and looks good on all devices.*

- Actual Result: *Works as intended*

![contact](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile/mobile_contact_landscape.png)


#### User story 4:

**As a user, i would like to get responses and confirmation from the website by my interactions with it**

**The Piano Feature**

- Action: *User interacts by playing keys on the piano*

- Expected Result: *Notes are heard and seen from the website, depending on user input*

- Actual Result: *Works as intended*

![](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/desktop/desktop_play.png)

**The Quiz Feature**

- Action: 'User interacts by clicking the buttons in the quiz
'
- Expected Result: *Website confirms and give user feedback in the form of sounds, animations and displaying new questions. This depending on whether the user has answered the question correctly or incorrectly*

- Actual Result: *Works as intended*

![Quiz ipad](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_ipad/quiz_ipad.png)

![Quiz mobile](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/quiz_iphone.png)

**Learn Page Feature**

- Action: *User interacts by navigating the videos section*

- Expected Result: *The main window displays the video with data the user has clicked on*

- Actual Result: *Works as intended*

![Learn mobile](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/learn_iphone_landscape.png)

**Contact Page Feature**

- Action: *User clicks on the "Send" button*

- Expected Result: *The users interaction is confirmed by the website via a message below the send button, letting the user know if the message was sent or if the information in incomplete*

- Actual Result: *Works as intended*

![](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/mobile/mobile_contact_landscape.png)


#### User story 5:

**As a user, i would like to be able to play a quiz on note names, symbols and note lengths**

**The Quiz Feature**

- Action: *User navigates to the Quiz page and clicks on the "Let's Play!" button*

- Expected Result: *The quiz begins and the user answers by clicking one of four buttons*

- Actual Result: *Works as intended*

![Quiz mobile](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/screenshots_iphone/quiz_iphone.png)



#### User story 6:

**As a user, i would like to get points if I answer a question right**

**The Quiz Feature**

- Action: *User answers a question correctly*

- Expected Result: *The score on the quiz page is incremented along with an animation the emphasizes this*

- Actual Result: *Works as intended*

![score](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/score.png)

#### User story 7:

**As a user, i would like to see a timer ticking down from one minute**

**The Quiz Feature**

- Action: *User play quiz*

- Expected Result: *The clock starts ticking down from 60 to 0*

- Actual Result: *Works as intended*

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

 - Bug: iPhone sometimes cuts off the beginning of the sound effects played on the quiz page, and they are sometimes not heard.
 - Fix: Tried to downsize to smaller samples. Still same problem. No fix yet.

- Bug: Contact link appears above other text on 404 page
- Fix: Make link position relative so it is scrollable to see

![Contact link bug](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/errors_bugs/contact_link_error.png)

- Bug: Contact link appearing on top of button on home page.
- Fix: Change dimensions of buttons and button container, home page.

- Bug: Red Shadow barely visible for wrong answer animation.
- Fix: Change so bakcground color and font color are red instead when answer is wrong.

- Bug: Videos not displaying in learn page.
- Fix: Update API key, YouTube API

- Bug: Main video covering whole screen on mobile devices in landscape mode, so navigation is disabled.
- Fix: Style video so it covers half the window in landscape mode, and the videos list in the other half.

- Bug: Quiz not displaying buttons
- Fix: Error in JavaScript was fixed

- Bug: controls not working on main video in learn page when viewed with DevTools on tablet view.
- Fix. Refresh page, cross check with real tablet/mobile, bug is not there

- Bug: Contact details still there after clicking "Send" on contact page
- Fix: Fix error in JavaScript file

- Bug: Video text not showing up in main video on learn page on certain devices/orientations and visible on others where it should not be
- Fix: fix this in several media queries, so portrait doesn't display text under video but landscape does on all devices smaller than tablet

- Bug: CORS error is shown when loading videos from YouTube API.
- Fix: No fix for this; I have spent weeks trying to fix it but the best way is from the back end of which I have no experience yet. Mo, my mentor, explained that it should be ok, due to that the error has nothing to do with my code. Above all, it doesn't affect the functionality of the page.
![CORS-error](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/errors_bugs/cors_error.png)

- Bug: [Cohort warning](https://github.blog/changelog/2021-04-27-github-pages-permissions-policy-interest-cohort-header-added-to-all-pages-sites/) apparently to all GitHub Pages.
- Fix: none.

- Bug: Loading videos in iframes producing warnings about adding non-passive event listeners to scroll blocking 'touchstart' event. These listeners are in a base.js JavaScript file that is linked in the iframe, and I have not found a fix for this.
Fix: none.

</details>


## Deployment

### GitHub Pages

This website has been deployed using GitHub pages.

To deploy a page yourself, do the following:

1. Access your GitHub account and find the relevant repository.
2. Click 'Settings' in the repository.
3. In Settings, click 'Pages' in the left-hand menu.
4. Click 'Source'.
5. In the dropdown menu displaying 'None', select 'Master Branch' or 'Main'6.
6. Allow the page some time to deploy your website.
7. At the top of Github Pages you will see a link to your live website.

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

### YouTube API

Here's how you can set up your own API:

1. Login or create a Google account and navigate to https://console.cloud.google.com/
2. Create a new Project by clicking on the New Project icon
3. Add Project Name
4. Create a credential (API-key) for the project
5. Restrict the API to the websites that will be using them to prevent misuse
6. Navigate to https://developers.google.com/youtube/v3
7. Click on "Search for content" (if it is a search you want to perform")
8. Click the relevant use case (list (by keyword) was my choice)
9. Go to the bottom of the page and enter the search information for your needs.
10. Click "execute" or "show code"
11. copy the URL at the top of the page
12. Perform a GET or Fetch request in JavaScript to the URL, and enter the API key in the space implied.
13. Add code to use results!



### EmailJS

Here's how to make use of EmailjS

1. Create an account at https://www.emailjs.com/
2. Click "add new service" and enter the email provider of your choice
3. Create an email-template
4. Use the example code given on the website or use your own in your JavaScript file
5. Use your Servide ID in services, and template ID the template you want to use.
6. Done!



## Credits

Here are links to sites that answered a lot of my questions on coding and the Python language.

This project was created from a template made by [Code Institute](https://codeinstitute.net/) to recreate the terminal in a regular web browser.

Background Image from [www.123rf.com](https://www.123rf.com/photo_91583290_stock-vector-music-note-seamless-pattern-vector-illustration-hand-drawn-sketched-doodle-music-notes-symbols-.html)

YouTube logos from YouTube, used with the guidelines of YouTube branding:
[YouTube API–Device Partners-logo](https://www.youtube.com/about/brand-resources/#api-device-partners)

[YouTube icon](https://www.youtube.com/about/brand-resources/#logos-icons-colors)

Favicon from [iconsdb.com](https://www.iconsdb.com/green-icons/note-icon.html)

Pdf-compress for smaller PDF-files to upload to GitHub: [smallpdf.com]
(https://smallpdf.com/result#r=a2d783f28bb928fa77b9c573862cdbcf&t=compress)

Tips to use collapse in markdown from [Pierre Joubert](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab) on Github

### Coding tips and tricks

Overriding false errors when Flake and Pylint validate code:
[StackOverflow, pyflakes](https://stackoverflow.com/questions/8427701/how-to-ignore-pyflakes-errors-imported-but-unused-in-the-init-py-file)
[StackOverflow, pylint](https://stackoverflow.com/questions/26657265/hide-some-maybe-no-member-pylint-errors)

Creating a class to increment and decrement a number free from functions: [Stack Overflow](https://stackoverflow.com/questions/47697945/python-how-to-increment-number-and-store-in-variable-every-time-function-runs/47698278)

Two lists into dict:
https://stackoverflow.com/questions/209840/how-do-i-convert-two-lists-into-a-dictionary

Creating a user login:[StackExchange](https://codereview.stackexchange.com/questions/164359/python-username-and-password-program)

Month name from number
https://stackoverflow.com/questions/6557553/get-month-name-from-number

string to attribute datetime
https://stackoverflow.com/questions/19887353/attributeerror-str-object-has-no-attribute-strftime

Guides for converting datetime to string
https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date

Timedelta to years
https://stackoverflow.com/questions/765797/convert-timedelta-to-years

Leap Year:
https://www.geeksforgeeks.org/program-check-given-year-leap-year/

Strin to date:
https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python

Reg ex email:
https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address

Isnumeric:
https://www.delftstack.com/howto/python/user-input-int-python/

Pylint error:


The tutors at Code Institute, especially John and Sean, gave me very good advice.

A great big thanks to my mentor Mo Shami, who has given me so much support during my studies.
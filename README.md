# CSCI 33-a, Athena's Section

Activities and their solutions for Athena Braun's 2025 CSCI 33-a Section.

## Week 6: Testing & CI/CD

Example solutions can be found in the `section6/solution` directory. Note that only the example tests for the Commerce project will be posted (rather than the whole solution to the project).
Section slides can be found [here](https://docs.google.com/presentation/d/1nZF1ZIs16MLEjdcRNeAQnU9RNx6goEWjMgKLDHXiv8g/edit?usp=sharing).

### Activity Goals:

#### Python Testing

You've written a snazzy binary search, but now you need to determine if it actually works. Using Unittest, write a set of tests in `python_testing/tests.py` to root out any bugs.

#### Selenium Testing

Your friends sent you a Javascript based guessing game, but you're a busy individual and don't have time to sit around taking thousands of guesses. Write a Selenium script instead to quickly discover what the number is. You might find these Selenium intro [docs](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/) helpful.

Make sure you have installed both Selenium via `pip install selenium` and the ChromeDriver (or browser of choice driver) via `pip install chromedriver-py`.

#### Django Testing

Download the [staff solution](https://vault.cs50.io/f37ab9cd-9ab5-4ebc-9971-f193defd1037) to the Commerce project. In `auctions/tests.py`, write a set of tests to ensure that the app is working as intended. Solution test code is in `week6/solution/examples/commerce_example/`

## Week 5: UX and React

Example solution will be posted after section in the `section5/quiz` directory. Section slides can be found [here](https://docs.google.com/presentation/d/1TfPTLkD3-kXIlqcFVk1HcclHa1g4KdF6VD-HBJFYkU0/edit?usp=sharing).

### Goal:

Fill in the TODOs in a Quizzlet Lite app and in the process, familiarize yourself a little bit with React.

Already defined in your distro code are the primary paths and template you will need. You will also find some skeleton code for your React components. Start by familiarizing yourself with the template, and then take a look at the existing React components such as the `Card`, `Prompter` and `Quizzlet` components.

When your app is done, your user will be able to click through prompted cards, indicate if they got the answer right or wrong, and view the cards in the corresponding right or wrong sections. As an added bonus, see if you can make the UX a bit better by allowing the user to hide/show cards in a section.

## Week 4: Javascript

Example solution will be posted after section in the `section4/` directory.
Section slides can be found [here](https://docs.google.com/presentation/d/1Ku2BMaRWeKWG_KXdfWgT2pc5K4r5xRFYS4lJw3AK_Hc/edit?usp=sharing).

### Goal:

Create a Javascript based page that queries our app's API for pets available for adoption, and then dynamically displays information about the pets.

Already defined in `adoption/views.py` and `adoption/urls.py` are a couple API endpoints to query data out of the `Pet` model. The data is returned as a JSON, and both endpoints are `GET` endpoints. Also included in the distro are CSS and an index.html file.

#### Where to start:

1. `git pull` to pick up any updates, or clone the repo if you have not already.
2. Familiarize yourself with the `Pet` model and the API endpoints.
3. Start your web server, and from the browser, try getting some data from one of the endpoints.
4. Write some Javascript such that when the page loads, an API call is made, and the data is dynamically added to the existing `<div>`.
5. Implement additional Javascript features, such as displaying additional pet features on click, and additional UX features like highlighting which pet was clicked on.
6. As time allows, add some CSS to make the website look a little nicer.

## Week 3: SQL, Models, & Migrations

Example solution can be found in the `section3/` directory.
Slides from section can be found [here](https://docs.google.com/presentation/d/1mkGWcttUyoWHD94YHvap2hYcQw6wy2cw7TbHtHDBH3A/edit?usp=sharing).

### Goal:

Create a simple website to view students and their enrolled classses. Bonus if you add the ability to enroll a student.

You should define both a Student and a Course model. These models should be related to each other in some way -- consider which of ForeignKey, many-to-many, or One-to-One relationships are most appropriate. (_Tip_: There is an example definition of a Student model in the slides!).

You should also define admin views for each of your models so you can add students and courses.

Finally, try displaying your students in the table in `roster.html` in the templates/ of the students app.

Remember your **migration** workflow:

1. Define models in the app's model.py
2. run `python manage.py makemigrations` from the project directory
3. run `python manage.py migrate` from the project directory

## Section 2: Django

Solutions can be found in the `section2/` directory, as well as another example project.

Slides from section can be found [here](https://docs.google.com/presentation/d/1bmAfoRCbruUtq9lxbmf27HV47h2OxgxS0T_EcDbsxx0/edit?usp=sharing).

### Goal

You're a cadet ready to bond your dragon! Make a Django project with one sub app that prompts for your name and preferred dragon species on one page via a form, and then announces your newly bonded dragon on another!

Your project should be called `dragons` and your app should be called `threshing`.

To make a new Django project, run `django-admin startproject PROJECT_NAME` in the appropriate directory.

To make a new app, run `python manage.py startapp APP_NAME`.

To start your project, run `python manage.py runserver`.

Remember your django checklist! We will be using session variables for this project, so remember to run `python manage.py migrate`.

## Section 1: HTML, CSS + SASS, Python & Git

Covers Lectures 0, 1, and 2

Slides from section can be found [here](https://docs.google.com/presentation/d/12xURyxqRgrcYFNjGEAw8CQbesBINUmB7YIg-N0YWIwc/edit?usp=sharing).

### HTML & DOM Mini Activity: Goal

Familiarize yourself with the structure of a webpage. Take a look at the image in `section1/html_dom_activity/activity/html_activity_screenshot.png` and try to:

1.  Recreate the HTML
2.  Draw out the DOM tree

### About Me Activity: Goal

Starter files are in the `section1/` directory.

Make a simple HTML page about yourself. Your page should include the following:

-   Your name
-   Two fun facts
-   At least 3 pictures (can be of anything)
-   A link to your favorite Google search

You should include but are not limited to the following html tags:

-   \<h1\>
-   \<li\>
-   \<img\>
-   \<a\>

In styles/style.scss, write some styles to make your page look a little nicer. **Bonus points** if you use flexbox or boostrap on top of your own styles. Remember to compile your SCSS (or watch the file) to pick up updates.

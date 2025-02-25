# CSCI 33-a, Athena's Section

Activities and their solutions for Athena Braun's 2025 CSCI 33-a Section.

## Week 3: SQL, Models, & Migrations

Example solution can be found in the `week3/` directory.
Slides from section can be found [here](https://docs.google.com/presentation/d/1mkGWcttUyoWHD94YHvap2hYcQw6wy2cw7TbHtHDBH3A/edit?usp=sharing).

### Goal:

Create a simple website to view students and their enrolled classses. Bonus if you add the ability to enroll a student.

You should define both a Student and a Course model. These models should be related to each other in some way -- consider which of ForeignKey, many-to-many, or One-to-One relationships are most appropriate. (_Tip_: There is an example definition of a Student model in the slides!).

You should also define admin views for each of your models so you can add students and courses.

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

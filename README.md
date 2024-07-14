
# Project Name
## Restaurants Management

# Website Name
## EatSwift  https://eatswift.onrender.com/

# Description
 EatSwift is a comprehensive platform for food ordering, restaurant registration, and order management.

# Installation
Instructions on how to install and set up your Django project locally.
  <ul>
    <li>Clone the Repository: </li>
      git clone https://github.com/chiranjivikeshav/DBMS_Restaurants_management.git
    <li>Create and Activate a Virtual Environment (Optional but Recommended):</li>
      cd your-django-project<br>
      python -m venv venv <br>
      source venv/bin/activate   ( On Windows, use `venv\Scripts\activate`)
    <li>Install Project Dependencies: </li>
      pip install -r requirements.txt
    <li>Set Up the Database:</li>
      If you want to uses a new database, create a new database and run the migrations to set up the database schema<br>
      python manage.py migrate
    <li>Create a Superuser (Optional):</li>
      If you want to uses Django's admin interface, create a superuser<br>
      python manage.py createsuperuser
    <li>Start the Server:</li>
      Start the Django development server to run the project locally<br>
      python manage.py runserver
  </ul>

# Usage
this Django project can use by following above instructions .You can access the admin interface at http://127.0.0.1:8000/admin/. Log in using the superuser credentials to access the admin panel..


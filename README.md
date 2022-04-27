# Revenue and Classroom Requirement Analysis System (RCRAS) <br/>

A web-based application written in Python (Django) to analyze the revenue and classroom data of university students.

- Create a virtual environment using the following command `pip install virtualenv myenv`
- Select that environment's python.exe as the interpreter,'path: `myenv/Scripts/python.exe`'

# Requirments

Install all the list of dependencies with the specified version. You can install it simply using requirements.txt file.

## Instruction:

<b> Step 1: </b> Create a requirements.txt file and add the list given below.<br/>

- Django==4.0.4
- mysqlclient==2.1.0
- numpy==1.22.3
- openpyxl==3.0.9
- pandas==1.4.2
- python-decouple==3.6

<b> Step 2: </b> Run the following command: `pip install requirments.txt`

# Run the project

- Try this command in the terminal [VScode] to run the project `python manage.py runserver`
- The default address [ http://127.0.0.1:8000/ ] will let you login to the web application

## Changing Server Port:

By default, the runserver command starts the development server on the internal IP at port 8000.
<br/> If you want to change the server’s port, pass it as a command-line argument: <br/>
`python manage.py runserver 1234`
<br/> For instance, this command starts the server on port 1234

# Login Credentials

<b> username: </b> admin <br/>
<b> password: </b> 1234

# Alternate Database

- Note that SQLite is used as the default database in this project
- If you choose to use a different database configure it in the Django Settings DATABASE section
- Then migrate to create the tables in the SQL database using the following command `python manage.py makemigrations` followed by `python manage.py migrate`
- Create a user by the following command `python manage.py createsuperuser`
- To populate the database with data run the following script in python shell `populationScript.py` filepath `scripts/populationScript.py`
  - To run the populationScript.py on windows [make sure you have GitBash terminal in VScode]:
    Use the following command `./manage.py shell < scripts/populationScript.py`
  - To run the populationScript.py on Mac:
    Use the following command `python manage.py shell < scripts/populationScript.py`  
    `NOTE:` The population Script will take a very long time to populate data if you are using SQLite Database (60 minutes +)
    - It was lot faster in MySQL like around 4/5 minutes
    - These doesn't apply to Mac users, not sure about Linux users
- You should see that your database has successfully populated

# Let's go! Have some coding! 🙂

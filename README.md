# Hospital-Home
This is a repository containing files related to Hospital@Home website.


1. Install Django 1.10 preferably in a virtual environment using the official Django documentation : https://docs.djangoproject.com/en/1.10/

2. If Django has been installed in a virtual environment, use the following command to activate the virtual environment.
                source <myvirtualenv>/bin/activate	

3. Install MySQL on your system using the official documentation: 
http://dev.mysql.com/downloads/

4. Extract the database from the sqldump file using the following command:
     mysql -u root -p --one-database destdbname < hospitalHome.sql


5. To run the server on localhost, run the following commands: 

cd Hospital-Home/my_proj/src 
python manage.py runserver

6. The website now is ready to use.

# Special Exercise:

- For this exercise you will be asked to create a basic crud application
- You are allowed to use the starter document and django documentation

1. Create a virtual environment for this project and activate it
2. Install django and psycopg2-binary
3. Start a django project named library_project
4. Start an application with name main_app
5. Add main_app to the installed_apps in the settings.py
6. Create the urls.py for the main_app
7. Add the urls.py from your main_app to your library_project
8. Configure your postgres database in the settings.py
9. Create a model for Author with the following fields:
    a. First_name: charField(80)
    b. last_name: charField(80)
    c. Is_best_seller: booleanField
10. Register the model in the admin panel
11. Create the routes, views, and templates for full crud on the author model
12. export the dependancies into a requirements.txt file
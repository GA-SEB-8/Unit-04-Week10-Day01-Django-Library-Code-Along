<h1>
  <span class="headline">Django CRUD App Lab</span>
  <span class="subhead">Exercise</span>
</h1>

## Build Your Own Full Stack Django Application

This lab is an opportunity to apply what you've learned in building the Django CRUD App, Cat_Collector, to a project of your own.

**_Use the structure and techniques from Cat_Collector as a guide to create a custom application._**

### **1. Setup Your Django Application**

#### **Create Your Application**

1. **Start a New App**: Begin by setting up an application within the Django project you created during the setup phase.

   ```bash
   python3 manage.py startapp my_app
   ```

2. **Register Your Application**: Add your new app to the list of `INSTALLED_APPS` in `settings.py`.

3. **Start the Server**: Test your new app connection.
   ```bash
   python3 manage.py runserver
   ```

#### **Configure the Database**

1. **Create Your Database**: Before adjusting the `settings.py`, ensure you create your database.

   ```bash
   createdb mycoolapp
   ```

2. **Database Settings**: Edit the `settings.py` file to include your local database settings.

   ```python
   DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'mycoolapp',
      }
   }
   ```

3. **Migrate Models**: After setting up your model classes in `models.py`, make and apply migrations.
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

#### **Set Up URL Routing**

1. **Create URL Configuration**: Make a new `urls.py` in your app directory to handle app-specific routes.

2. **Include App URLs in Project**: Modify the project’s `urls.py` to include your app’s URL configurations.

   ```python
   from django.urls import path, include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('my_app.urls')), # Mount the app's routes at the root URL
   ]
   ```

### **2. Implement Full CRUD for a Model**

Develop URL patterns, views, and templates to manage a resource fully. Your application should include views for:

- **Home**: The landing page
- **Index**: List all instances of the model
- **Detail**: Show details of a single instance
- **Create**: Form to create a new instance
- **Update**: Form to update an existing instance
- **Delete**: Handle the deletion of an instance

### **3. Introduce a Secondary Model with Associations**

1. **Model Association**: Create a **_one-to-many relationship_** with a second model.
2. **Manage Resources**: Implement full CRUD operations for the secondary model, ensuring resources can be created, read, updated, and deleted.

### **4. Integrate Authentication**

1. **Enable Django Authentication**: Incorporate Django’s built-in authentication system to manage user accounts.
2. **Admin Dashboard**: Utilize Django’s admin to manage user activities.
3. **Protect Resources**: Ensure that routes related to user-owned resources require authentication.

## Level Up

### **5. Introduce a Third Model with Associations**

1. **Model Association**: Create a **_many-to-many relationship_** with a third model.
2. **Manage Resources**: Implement full CRUD operations for the third model, ensuring resources can be created, read, updated, and deleted.

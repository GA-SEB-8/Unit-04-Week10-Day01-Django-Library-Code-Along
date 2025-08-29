<h1>
  <span class="headline">Django CRUD App Lab</span>
  <span class="subhead">Setup</span>
</h1>

## Setup

Open your Terminal application and navigate to your `~/code/ga/lessons` directory:

```bash
cd ~/code/ga/lessons
```

Create a new repository on [GitHub](https://github.com/) named `django-crud-app-lab`.

```bash
git clone https://github.com/<your-username>/django-crud-app-lab.git
```

> 🚨 Do not copy the above command. It will not work. Your GitHub username will replace <github-username> (including the < and >) in the URL above.

Next, `cd` into your new cloned directory, `django-crud-app-lab`:


```bash
cd django-crud-app-lab
```

Initialize a new virtual environment inside your project directory and install Django:

```bash
pipenv install django
```

This command will create a new `Pipfile` and `Pipfile.lock` in your project directory, specifying Django as a dependency.

Activate the virtual environment:

```bash
pipenv shell
```

> 🧠 With your virtual environment activated you should see a slight change in your terminal, with the virtual environment folder name listed to the left of your command line prompt.

## Name your Project

Before you begin your lab you'll need to choose a name for your project, If you already know the model you'll use, consider calling it something related to that resource. ***Ex: finchcollector, nationalparks, bloghub***

Here are some Django guidelines and naming conventions:

1. The project name should reflect its functionality or purpose. 
2. Avoid naming projects after Python or Django internal components, like `django` or `test`. ***Ex: djangoproject, djangomusic, testproject***
3. Python doesn’t allow hyphens in module names because they are interpreted as minus signs. Use underscores if needed, although single-word names are preferred for simplicity.
4. It's a Python convention to name packages all in lowercase to avoid issues with case-sensitive filesystems.

### Got a name? Great.

Start a new Django project within your virtual environment:

```bash
django-admin startproject <mycoolapp>
```

Once the project is created, `cd` into the new `<mycoolapp>` directory:

```bash
cd <mycoolapp>
```

Open the project's folder in your code editor:

```bash
code .
```

To deactivate the virtual environment when you're done, type:

```bash
exit
```

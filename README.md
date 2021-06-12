# Buccshow

The inspiration for this project came when Bucc first announced the skill showcasing during the semester break.
I was thinking about what I should create and wondering where we would have to submit the project once it's complete.
Then it occured to me that why don't I create a platform where Bucc members can easily submit their projects. Other's can view what projects different BUCC members have been working on. 
With that in mind, I created BuccShow. 
The project is build using python(Django) and Bootstrap.

In order to run this project on your computer, follow the steps below. 

### Step 1(Ensure that django is installed) 
Since this project is built using django, django must be installed in your computer. Install django with the following command:

``` 
pip install django
```

### Step 2(clone project)
On an empty directory, clone this project:

```
git clone [url]
```

### Step 4(Run migrations)
Run the following commands to run the migrations:

1) ```python manage.py makemigrations```
2) ```python manage.py migrate```

### Step 5(Create superuser) 

The superuser is needed to access the admin panel. In order to create a superuser, run:
```
python manage.py createsuperuser
```

And enter the details required.

### Step 6(Run the application)
Run the following command to start the development server:

```
python manage.py runserver
```

Then go a browser and enter the localhost at which the server ran.(Usually, it you should find it on `http://localhost:8000/`. But the link can be found in the terminal once the `python manage.py runserver` command is entered.)



The above steps should allow others to run the project. Do let me know if there is an issue while running the project. 

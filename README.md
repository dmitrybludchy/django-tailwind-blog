# Blog(How-to tutorials) using Django and tailwindCSS

### This is a sample project to explore Django and TailwindCSS with using django-allauth.

![](./readme_images/tailwindproject.png)
____________
#### *Getting Started with Django*



### 1. Set up your Django project

If you are ___cloning this repo___ :

create a virtual environment (using Python's venv)

    python3 -m venv venv 

To activate virtual environment (Linux):

    source venv/bin/activate

Install all dependencies:

    pip3 install -r requirements.txt

### 2. Set up your TailwindCSS project

Navigate into folder jstools

    cd jstools

Then, install dependencies:

    npm install

If you need to compile the tailwindcss file

    npm run build

This command will generate two files: styles.css and styles.min.css in __config/static/css__ folder

then, collect static files in STATIC_ROOT (static): 

    python3 manage.py collectstatic

Link style.min.css to your templates and enjoy.

#### When you are developing and using all the capabilities of Tailwind remember to avoid the purge.

![](./readme_images/1.png)





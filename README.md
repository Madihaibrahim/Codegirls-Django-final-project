## Step-by-step: How to run Django Project "Hotel" 
### Create venv (Windows)
python -m venv venv
venv\Scripts\activate
#### 1: Install Django
pip install django python-docx
(python-docx is needed only to generate this Word file programmatically; skip if you don't need it)
#### Step 2: Make migrations & migrate
python manage.py makemigrations
python manage.py migrate

#### Step 3: Create Admin superuser (optional)
python manage.py createsuperuser
Follow prompts to create username, email and password

#### Step4: Run development server
python manage.py runserver
#### Visit http://127.0.0.1:8000/ in your browser




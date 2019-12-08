# Lowbit
It is a web application that creates a website that allows streaming music from youtube.com to mobile devices/computers.
Link to demo: http://lowbit.tk

### Instalation :
```
git clone https://github.com/Kamwebdev/Lowbit
cd Lowbit
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### Application requirements  :
- django-cors-headers
- django
- djangorestframework


### The application requires placing a server that allows you to stream music using ffmpeg
https://github.com/codealchemist/youtube-audio-server

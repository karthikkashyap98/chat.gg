# <img src="https://lh3.googleusercontent.com/2gk4MOJoUf_yqndIXUxiVuVSFhecQBReW1jbZyEvKVU3nslC66_0l1iBFggqPjbkiA" style="vertical-align:middle" width="50" height="50"> CHAT.GG 

## A Web based chat-room-application built with Django and Django Channels 2

### Users can Signup and join chat rooms and chat with multiple users. 

This application can also be integrated with other web-apps. (Base chat application). 

## Installation 

### Clone the repsitory  

  ```git clone https://github.com/karthikkashyap98/Chat-Application.git```
  
### Install and Create virtualenv

  ```pip install virtualenv```
  
  ```cd Chat-Application```
  
  ```virtualenv env```
 
### Install the dependancies 

  ```env\Scripts\activate```
  
  ```pip install -r requirements.txt```

### Start Redis:5

  ```docker run -p 6379:6379 -d redis:5```

### Start the project 

  ```python manage.py runserver```
  
  

# BostonHacks2019

Locate.io is a Web-based application utilizing Kairos Face Recognition API to store information on missing children and refugees.

## Inspiration

While on the bus on our way to the Hackathon, we watched 

## What it does

Web-app that takes a photograph of a user using the computers webcam. It then compares the pictures to current  pictures stored in our database. 

If it finds a match, it will output the known information of the individual in the photo, if not, then it will create a prompt for the user to input information about the person in the picture which will then be stored in the database for future use.

## How it was built

The program uses the computers webcam and KAIROS facial recognition API to train the dataset in the KAIROS database to recognize various faces. It then runs ML algorithms using the KAIROS API to detect similarities in between different photos. 

## Challenges

It is difficult to debug the facial recognition API.

It was a challenge to implement django, rest API, and KAIROS API all in one.

We had difficulty training the dataset originally.

## Future Endeavors

Use of the Facebook Graph API to increase the possible scope of the ML training as well as the overall usefulness of the app.

Use of the Twilio SMS API to send reports and updates over SMS to users of the app.

## Tech

MySQL, Django, Python3, Kairos API, boostrap4

## Running

Download or clone the code
```
git clone https://github.com/NichHarris/BostonHacks2019
```
Move into mysite directory
```
cd path/BostonHacks2019/mysite
```
Make sure a virtual environment is installed before hand
```
$ pip install virtualenv
$ virtualenv mypython'
$ source mypython/bin/activate
```
To deactive virtual environemnt
```
$ deactivate mypython
```
After this is complete, to run the program while in 'BostonHacks2019/mysite'
```
$ python manage.py runserver
```
A webpage landing should open

## API Reference

Reference docs for Kairos Face Recognition API: https://www.kairos.com/docs/api/

KairosDB REST API: https://kairosdb.github.io/docs/build/html/restapi/index.html

Django REST framework: https://www.django-rest-framework.org/ 
 
## Tests

Testing the facial recognition software involves taking a picture with your webcam. 

If it recognizes a face, and does not contain it in its database currently,
the program will generate a user info page which he or she will be prompted to fill out. 

Upon filling out and submitting the information, the users info will be stored in the 
database along with all pictures taken of said person in order for more accurate identification in the future.

## Contributors

Rajat Arora

Arash Manpreet Singh

Suthan Sinnathurai 


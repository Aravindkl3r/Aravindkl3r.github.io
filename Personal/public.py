from flask import *
# from database import *
import uuid
import random
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
public=Blueprint('public',__name__)

@public.route('/')
def index():
	session['uid']="None"
	return render_template("index.html")
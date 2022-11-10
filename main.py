import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


# Get the API key from the '.env' file
load_dotenv()
api_key = os.getenv('API_KEY')



from flask import Flask

app = Flask(__name__)

from app import routes

# IMPORTERAR APP I ROUTES ICH I RUN, KÖR INIT 2 GÅNGER

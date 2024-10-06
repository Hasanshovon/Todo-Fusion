from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from app import routes
#from app import models
#from app import services
# from app import templates   [note : no need to add this line]
from flask import Flask

app = Flask(__name__)

from app import routes
#from app import models
#from app import services
# from app import templates   [note : no need to add this line]
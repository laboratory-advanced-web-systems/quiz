from flask import Flask
from pymongo import MongoClient

app = Flask(__name__);

app.config["SECRET_KEY"] = "secret key"

client = MongoClient('mongodb://localhost:27017/')
db = client.quizservicedb

from quiz_service.controllers import routes
from quiz_service.controllers import CourseController
from quiz_service.controllers import QuestionController
from quiz_service.controllers import TopicController
from quiz_service.controllers import UserController
from quiz_service.controllers import TestController
from quiz_service.controllers import AnswerController

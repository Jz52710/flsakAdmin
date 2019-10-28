from flask import Blueprint,render_template

student = Blueprint("student",__name__,url_prefix="/student",template_folder="templates/student",static_folder="static/student")

@student.route('/')
def index():
    return render_template('student/student.html')
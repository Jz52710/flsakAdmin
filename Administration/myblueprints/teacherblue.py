from flask import Blueprint,render_template

teacher = Blueprint("teacher",__name__,url_prefix="/teacher",template_folder="templates/teacher",static_folder="static/teacher")

@teacher.route('/')
def index():
    return render_template('teacher/teacher.html')